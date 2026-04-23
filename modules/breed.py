import requests
from .db import DB
import json

class Breed:

    DOGS_BREEDS_URL: str = 'https://dog.ceo/api/breeds/list/all'

    BREEDS_DB_NAME: str = 'breeds'

    """
    Fetches all dog breeds from the given API URL.

    Returns:
        dict: A dictionary containing all the dog breeds.
    """
    @staticmethod
    def fetch_all_breeds() -> dict:

        try:

            print(f"\nFetching all breeds from {Breed.DOGS_BREEDS_URL}\n")

            res = requests.get(Breed.DOGS_BREEDS_URL)

            if res.status_code == 200:

                data: dict = res.json()

                if data['status'] == 'success':

                    return data['message']
                
                else:

                    raise Exception(f'Request Status: {data["status"]}: \n{data["message"]}')
            else:

                raise Exception(f'Request Status Code: {res.status_code}: \n{res.text}')

        except Exception as err:

            raise Exception(f'Dog.fetch_all_breeds -> {str(err)}')


    """
    Saves the retrieved dog breeds and their sub-breeds into the database.
    """
    @staticmethod
    def save_breeds():

        try:

            breeds: dict = Breed.fetch_all_breeds()

            DB.create_breads_table(Breed.BREEDS_DB_NAME)
            DB.create_breads_count_table(Breed.BREEDS_DB_NAME)

            for breed, sub_breads in breeds.items():

                DB.insert_breeds(Breed.BREEDS_DB_NAME, { 'breed_name': breed, 'sub_breeds': json.dumps(sub_breads) })
                DB.insert_breeds_count(Breed.BREEDS_DB_NAME, { 'breed_name': breed, 'sub_breed_count': len(sub_breads) })

        except Exception as err:

            raise Exception(f'Dog.save_breeds -> {str(err)}')
        
        finally:

            DB.commit_and_close(Breed.BREEDS_DB_NAME)
        

    """
    Fetches and displays the count of sub-breeds for each breed.
    """
    @staticmethod
    def view_breeds_count():

        try:

            results: list = DB.fetch_breads_count(Breed.BREEDS_DB_NAME)

            print('\nSub-Bread \tCount')

            print('--------------------------------------')

            for breed, count in results:

                print(f"{breed:<20s} {count:<6d}")

        except Exception as err:

            raise Exception(f'Dog.view_breeds_count -> {str(err)}')
        
        finally:

            DB.commit_and_close(Breed.BREEDS_DB_NAME)