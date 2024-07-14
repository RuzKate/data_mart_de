import os
from dotenv import load_dotenv
from scripts.connect import DatabaseConnect
from scripts.functions import data_mart_calculation_f101, data_mart_calculation_turnover

def main():
    load_dotenv(".env")

    database_name = os.environ.get('DB_NAME')
    user_name = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    host = os.environ.get('DB_HOST')
    port = os.environ.get('DB_PORT')

    connection = DatabaseConnect(database_name, user_name, password, host, port)
    connection.connect_to_db()

    for day in range(1, 32):
        date = f'2018-01-{day:02}'
        data_mart_calculation_turnover(connection.connection, date)
        
    date = '2018-01-01'    
    data_mart_calculation_f101(connection.connection, date)

    connection.disconnect()

if __name__ == '__main__':
    main()    