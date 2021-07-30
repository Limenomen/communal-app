from UI import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
import os
import psycopg2
import sys
import numpy as np
import datetime


class database():
    connection = None

    def __init__(self):
        super(database, self).__init__()
        self.create_connection()
        pass

    def create_connection(self):
        try:
            self.connection = psycopg2.connect(
                database="payments",
                user="pc",
                password="1234",
                host="127.0.0.1",
                port="5432"
            )
        except (Exception) as error:
            print('ошибка:', error)

    def insert_payment(self, data):
        pass

    def recieve_coef(self):
        keys = ['electricity', 'hot_water', 'cold_water', 'gas']
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT c_electricity, c_hot_water, c_cold_water, c_gas FROM coefficients ORDER BY id LIMIT 1 "
        )
        values = np.reshape(cursor.fetchall(), len(keys))
        data = dict(list(zip(keys, values)))
        return data

    def recieve_payment(self):
        keys = ['date', 'payment', 'electricity', 'hot_water', 'cold_water', 'gas']
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT date, payment, electricity, hot_water, cold_water, gas FROM payment ORDER BY date LIMIT 1")
        values = np.reshape(cursor.fetchall(), len(keys))
        data = dict(list(zip(keys, values)))
        return data


class main_window(QtWidgets.QMainWindow):
    base: database

    data = None
    coefficients = None
    current_data = None

    def __init__(self):
        super(main_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.base = database()
        self.get_data()
        self.fill_fields()

    def get_data(self):
        self.data = self.base.recieve_payment()
        self.coefficients = self.base.recieve_coef()
        self.current_data = self.data.copy()
        self.current_data['date'] = datetime.date.today()
        print(self.current_data)

    def fill_fields(self):
        self.ui.cold_water_prev.setText(str(self.data['cold_water']))
        self.ui.electricity_prev.setText(str(self.data['electricity']))
        self.ui.hot_water_prev.setText(str(self.data['hot_water']))
        self.ui.gas_prev.setText(str(self.data['gas']))
        self.ui.cold_water_cur.setValue(self.data['cold_water'])
        self.ui.electricity_cur.setValue(self.data['electricity'])
        self.ui.hot_water_cur.setValue(self.data['hot_water'])
        self.ui.gas_cur.setValue(self.data['gas'])
        self.ui.gas_coef.setText(str(self.coefficients['gas']))
        self.ui.electricity_coef.setText(str(self.coefficients['electricity']))
        self.ui.hot_water_coef.setText(str(self.coefficients['hot_water']))
        self.ui.cold_water_coef.setText(str(self.coefficients['cold_water']))
        self.ui.date.setDate(self.current_data['date'])

    def make_current_data(self):
        pass


def main():
    app = QtWidgets.QApplication([])
    view = main_window()
    view.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
