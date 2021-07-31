from UI import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
import os
import psycopg2
import sys
import numpy as np
import datetime


class database():
    """
    Класс, содержащий методы для работы с базой данных
    """
    connection = None

    def __init__(self):
        super(database, self).__init__()
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


class main_window(QtWidgets.QMainWindow):

    base: database
    prev_data = None
    coefficients = None
    current_data = None
    current_sums = None

    def __init__(self):
        super(main_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_to_database()
        if self.base is not None:
            self.get_data()
            self.fill_fields()
        self.ui.cold_water_cur.valueChanged.connect(
            self.cold_water_cur_valueChanged)
        self.ui.hot_water_cur.valueChanged.connect(
            self.hot_water_cur_valueChanged)
        self.ui.gas_cur.valueChanged.connect(
            self.gas_cur_valueChanged)
        self.ui.electricity_cur.valueChanged.connect(
            self.electricity_cur_valueChanged)
        self.ui.result_button.clicked.connect(
            self.result_button_clicked)
        self.ui.save_button.clicked.connect(self.save_button_clicked)

    def connect_to_database(self):
        """
        Создание соединения с бд
        """
        try:
            self.base = database()
            return self.base
        except psycopg2.Error as e:
            print(e)
            self.base = None
            return self.base

    def cold_water_cur_valueChanged(self):
        if self.current_data is not None:
            self.current_data['cold_water'] = self.ui.cold_water_cur.value()

    def hot_water_cur_valueChanged(self):
        if self.current_data is not None:
            self.current_data['hot_water'] = self.ui.hot_water_cur.value()

    def gas_cur_valueChanged(self):
        if self.current_data is not None:
            self.current_data['gas'] = self.ui.gas_cur.value()

    def electricity_cur_valueChanged(self):
        if self.current_data is not None:
            self.current_data['electricity'] = self.ui.electricity_cur.value()

    def get_data(self):
        """
        Получение данных из бд и запись актуальной даты
        """
        self.prev_data = self.base.recieve_payment()
        self.coefficients = self.base.recieve_coef()
        self.current_data = self.prev_data.copy()
        self.current_data['date'] = datetime.date.today()

    def fill_fields(self):
        """
        Заполнение колонок коэффициентов и предыдущих показаний
        """
        self.ui.cold_water_prev.setText(str(self.prev_data['cold_water']))
        self.ui.electricity_prev.setText(str(self.prev_data['electricity']))
        self.ui.hot_water_prev.setText(str(self.prev_data['hot_water']))
        self.ui.gas_prev.setText(str(self.prev_data['gas']))
        self.ui.cold_water_cur.setValue(self.prev_data['cold_water'])
        self.ui.electricity_cur.setValue(self.prev_data['electricity'])
        self.ui.hot_water_cur.setValue(self.prev_data['hot_water'])
        self.ui.gas_cur.setValue(self.prev_data['gas'])
        self.ui.gas_coef.setText(str(self.coefficients['gas']))
        self.ui.electricity_coef.setText(str(self.coefficients['electricity']))
        self.ui.hot_water_coef.setText(str(self.coefficients['hot_water']))
        self.ui.cold_water_coef.setText(str(self.coefficients['cold_water']))
        self.ui.date.setDate(self.current_data['date'])

    def make_current_payment(self):
        """
        Расчет платежа
        """
        sums = {}
        sums.update({'cold_water': (self.current_data['cold_water'] -
                                    self.prev_data['cold_water']) * self.coefficients['cold_water']})
        sums.update({'hot_water': (self.current_data['hot_water'] -
                                   self.prev_data['hot_water']) * self.coefficients['hot_water']})
        sums.update({'electricity': (self.current_data['electricity'] -
                                     self.prev_data['electricity']) * self.coefficients['electricity']})
        sums.update({
            'gas': (self.current_data['gas'] - self.prev_data['gas']) * self.coefficients['gas']})
        payment = sum(sums.values())
        self.current_data['payment'] = payment
        self.current_sums = sums.copy()

    def save_button_clicked(self):
        """
        Обработчик кнопки "сохранить"
        """
        self.base.insert_payment(self.current_data)
        self.ui.save_label.setText('сохранено!')
        self.ui.save_button.setEnabled(False)

    def result_button_clicked(self):
        """
        Обработчик кнопки "расчет"
        """
        self.make_current_payment()
        self.ui.save_button.setEnabled(True)
        self.ui.result_label.setText(
            f"Холодная вода: {self.current_sums['cold_water']}, \nГорячая вода: {self.current_sums['hot_water']}, \nЭл.энергия: {self.current_sums['electricity']},\nГаз: {self.current_sums['gas']},\n\nИтого: {self.current_data['payment']}")

    def closeEvent(self, event):
        """
        Закрытие окна
        """
        self.base.close_connection()


def main():
    app = QtWidgets.QApplication([])
    view = main_window()
    view.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
