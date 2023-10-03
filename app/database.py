import psycopg2
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

params = {
    'database': DB_NAME,
    'user': DB_USER,
    'password': DB_PASS,
    'host': DB_HOST,
    'port': DB_PORT
}


def connection():
    try:
        con = psycopg2.connect(**params)
        print('database connected')
        return con
    except:
        print("Cannot connect db.")
        print()
        return 0


conn = connection()
