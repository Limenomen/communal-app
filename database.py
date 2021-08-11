import psycopg2
import numpy as np


class DataBase():
    """
    Класс, содержащий методы для работы с базой данных
    """
    connection = None

    def __init__(self):
        super(DataBase, self).__init__()
        self.create_connection()
        pass

    def create_connection(self):
        """
        Метод для подключения к бд
        """
        self.connection = psycopg2.connect(
            database="payments",
            user="pc",
            password="1234",
            host="127.0.0.1",
            port="5432"
        )

    def insert_payment(self, data):
        """
        Вставка новой записи в таблицу payment
        """
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO payment (cold_water, hot_water, gas, electricity, date, payment) VALUES ({data['cold_water']}, {data['hot_water']}, {data['gas']}, {data['electricity']}, '{(data['date'])}', {data['payment']})")
        self.connection.commit()
        cursor.close()

    def recieve_coef(self):
        """
        Получение актуальных коэффициентов из бд
        """
        keys = ['electricity', 'hot_water', 'cold_water', 'gas']
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT c_electricity, c_hot_water, c_cold_water, c_gas FROM coefficients ORDER BY id LIMIT 1 "
        )
        values = np.reshape(cursor.fetchall(), len(keys))
        data = dict(list(zip(keys, values)))
        cursor.close()
        return data

    def recieve_payment(self):
        """
        получение данных последнего платежа
        """
        keys = ['date', 'payment', 'electricity',
                'hot_water', 'cold_water', 'gas']
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT date, payment, electricity, hot_water, cold_water, gas FROM payment ORDER BY id DESC LIMIT 1")
        values = np.reshape(cursor.fetchall(), len(keys))
        data = dict(list(zip(keys, values)))
        cursor.close()
        return data

    def close_connection(self):
        """
        Закрытие соединения с бд
        """
        self.connection.close()
