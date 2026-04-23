from modules.breed import Breed

def main():

    try:

        Breed.save_breeds()
        Breed.view_breeds_count()

    except Exception as err:

        print(f"Error: {str(err)}")


main()