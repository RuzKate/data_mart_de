import psycopg2

class DatabaseConnect:
    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        """Инициализатор класса

            :param db_name: название базы данных
            :type db_name: str

            :param db_user: имя пользователя для подключения к бд
            :type db_user: str

            :param db_password: пароль пользователя для подключения к бд
            :type db_password: str

            :param db_host: адрес сервера базы данных
            :type db_host: str

            :param db_port: порт для подключения
            :type db_port: str
        """
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.connection = None


    def connect_to_db(self):
        """Подключение к серверу PostgreSQL"""
        try:
            self.connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port
            )
        except ConnectionError as error:
            print(f'Unable to connect to the server: {error}')

    def disconnect(self):
        """Закрытие подключения"""
        if self.connection:
            self.connection.close()
