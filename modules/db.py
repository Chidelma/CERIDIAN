import sqlite3
from sqlite3 import Connection


class DB:

    CONNECTIONS: dict = {}

    BREEDS_TABLE_NAME: str = 'breeds'

    BREEDS_COUNT_TABLE_NAME: str = 'sub_breeds_count'

    """
    Establishes a connection to the specified database.

    Args:
        database (str): The name of the database to connect to.
    """
    @staticmethod
    def connect_db(database: str):

        try:

            print(f"\nConnecting to {database}\n")

            if DB.CONNECTIONS.get(database) is None:

               DB.CONNECTIONS[database] = sqlite3.connect(f'{database}.db')
        
        except Exception as err:

            raise Exception(f'DB.connect_db(...) -> {str(err)}')
    
    """
    Returns a cursor object for executing SQL queries.

    Args:
        database (str): The name of the database.

    Returns:
        Cursor: The cursor object.
    """
    @staticmethod
    def get_cursor(database: str):

        try:

            if DB.CONNECTIONS.get(database) is None:

                DB.connect_db(database)

            conn: Connection = DB.CONNECTIONS[database]

            return conn.cursor()

        except Exception as err:

            raise Exception(f'DB.get_cursor(...) -> {str(err)}')
        

    """
    Creates the breeds table in the specified database.

    Args:
        database (str): The name of the database.
    """
    @staticmethod
    def create_breads_table(database: str):

        try:

            cur = DB.get_cursor(database)

            print(f"\nCreating {DB.BREEDS_TABLE_NAME} for {database}\n")

            cur.execute(f'''
                CREATE TABLE IF NOT EXISTS {DB.BREEDS_TABLE_NAME} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    breed_name TEXT NOT NULL,
                    sub_breeds TEXT NOT NULL
                )
            ''')

        except Exception as err:

            raise Exception(f'DB.create_breads_table(...) -> {str(err)}')
        

    """
    Creates the sub_breeds_count table in the specified database.

    Args:
        database (str): The name of the database.
    """
    @staticmethod
    def create_breads_count_table(database: str):

        try:

            cur = DB.get_cursor(database)

            print(f"\nCreating {DB.BREEDS_COUNT_TABLE_NAME} for {database}\n")

            cur.execute(f'''
                CREATE TABLE IF NOT EXISTS {DB.BREEDS_COUNT_TABLE_NAME} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    breed_name TEXT NOT NULL,
                    sub_breed_count INTEGER NOT NULL
                )
            ''')

        except Exception as err:

            raise Exception(f'DB.create_breads_count_table(...) -> {str(err)}')
        

    """
    Inserts a record into the breeds table in the specified database.

    Args:
        database (str): The name of the database.
        record (dict): The record to be inserted.
    """
    @staticmethod
    def insert_breeds(database: str, record: dict):

        try:

            cur = DB.get_cursor(database)

            print(f"\nInserting {record} into {DB.BREEDS_TABLE_NAME} table\n")

            placeholders = ', '.join(['?' for _ in range(len(record))])

            sql = f'INSERT INTO {DB.BREEDS_TABLE_NAME} ({", ".join(record.keys())}) VALUES ({placeholders})'

            values = list(record.values())

            cur.execute(sql, values)

        except Exception as err:

            raise Exception(f'DB.insert_breeds(...) -> {str(err)}')
        

    """
    Inserts a record into the sub_breeds_count table in the specified database.

    Args:
        database (str): The name of the database.
        record (dict): The record to be inserted.
    """
    @staticmethod
    def insert_breeds_count(database: str, record: dict):

        try:

            cur = DB.get_cursor(database)

            print(f"\nInserting {record} into {DB.BREEDS_COUNT_TABLE_NAME} table\n")

            placeholders = ', '.join(['?' for _ in range(len(record))])

            sql = f'INSERT INTO {DB.BREEDS_COUNT_TABLE_NAME} ({",".join(record.keys())}) VALUES ({placeholders})'

            values = list(record.values())

            cur.execute(sql, values)

        except Exception as err:

            raise Exception(f'DB.insert_breeds_count(...) -> {str(err)}')
        
    
    """
    Commits and disconnects from the specified database.

    Args:
        database (str): The name of the database.
    """
    @staticmethod
    def commit_and_close(database: str):

        try:

            if DB.CONNECTIONS.get(database) is not None:

                print(f"\nCommitting and Closing connection for {database} database\n")

                conn: Connection = DB.CONNECTIONS[database]

                conn.commit()
                conn.close()

                DB.CONNECTIONS[database] = None

            else:

                print(database)

                raise Exception(f'{database} connect does not exist')

        except Exception as err:

            raise Exception(f'DB.commit_and_close(...) -> {str(err)}')
        

    """
    Fetches breed_name and sub_breed_count from sub_breed_count table in the specified database.

    Args:
        database (str): The name of the database.
    Returns:
        List: list of select query
    """
    @staticmethod
    def fetch_breads_count(database: str) -> list:

        try:

            cur = DB.get_cursor(database)

            print(f"\nFetching Data from {DB.BREEDS_COUNT_TABLE_NAME} table in {database} database\n")

            cur.execute(f'SELECT breed_name, sub_breed_count FROM {DB.BREEDS_COUNT_TABLE_NAME}')

            return cur.fetchall()

        except Exception as err:

            raise Exception(f'DB.fetch_breads_count(...) -> {str(err)}')
