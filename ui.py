from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator


class Ui_MainWindow(object):
    only_dec = QDoubleValidator()
    only_dec.setNotation(QDoubleValidator.StandardNotation)
    only_dec.setDecimals(4)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 330)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 413, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowTitle("Communal app")

        self.date = QtWidgets.QDateEdit(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(10, 0, 110, 22))
        self.date.setObjectName("date")
        
        self.koef_label = QtWidgets.QLabel(self.centralwidget)
        self.koef_label.setGeometry(QtCore.QRect(20, 20, 41, 31))
        self.koef_label.setObjectName("koef_label")
        self.koef_label.setText("коэф.")
        
        self.prev_label = QtWidgets.QLabel(self.centralwidget)
        self.prev_label.setGeometry(QtCore.QRect(160, 20, 131, 31))
        self.prev_label.setObjectName("prev_label")
        self.prev_label.setText("предыдущие показания")
        
        self.cur_label = QtWidgets.QLabel(self.centralwidget)
        self.cur_label.setGeometry(QtCore.QRect(300, 20, 101, 31))
        self.cur_label.setObjectName("cur_label")
        self.cur_label.setText("текущие показания")
        
        self.cold_water_coef = QtWidgets.QLineEdit(self.centralwidget)
        self.cold_water_coef.setGeometry(QtCore.QRect(10, 50, 51, 20))
        self.cold_water_coef.setObjectName("cold_water_coef")
        self.cold_water_coef.setValidator(self.only_dec)
        
        
        self.hot_water_coef = QtWidgets.QLineEdit(self.centralwidget)
        self.hot_water_coef.setGeometry(QtCore.QRect(10, 80, 51, 20))
        self.hot_water_coef.setObjectName("hot_water_coef")
        self.hot_water_coef.setValidator(self.only_dec)
        
        self.electricity_coef = QtWidgets.QLineEdit(self.centralwidget)
        self.electricity_coef.setGeometry(QtCore.QRect(10, 110, 51, 20))
        self.electricity_coef.setObjectName("electricity_coef")
        self.electricity_coef.setValidator(self.only_dec)
        
        self.gas_coef = QtWidgets.QLineEdit(self.centralwidget)
        self.gas_coef.setGeometry(QtCore.QRect(10, 140, 51, 20))
        self.gas_coef.setObjectName("gas_coef")
        self.gas_coef.setValidator(self.only_dec)
        
        self.cold_water_prev = QtWidgets.QLineEdit(self.centralwidget)
        self.cold_water_prev.setGeometry(QtCore.QRect(170, 50, 91, 20))
        self.cold_water_prev.setObjectName("cold_water_prev")
        self.cold_water_prev.setReadOnly(True)
        
        self.hot_water_prev = QtWidgets.QLineEdit(self.centralwidget)
        self.hot_water_prev.setGeometry(QtCore.QRect(170, 80, 91, 20))
        self.hot_water_prev.setObjectName("hot_water_prev")
        self.hot_water_prev.setReadOnly(True)
        
        self.electricity_prev = QtWidgets.QLineEdit(self.centralwidget)
        self.electricity_prev.setGeometry(QtCore.QRect(170, 110, 91, 20))
        self.electricity_prev.setObjectName("electricity_prev")
        self.electricity_prev.setReadOnly(True)
        
        self.gas_prev = QtWidgets.QLineEdit(self.centralwidget)
        self.gas_prev.setGeometry(QtCore.QRect(170, 140, 91, 20))
        self.gas_prev.setObjectName("gas_prev")
        self.gas_prev.setReadOnly(True)
        
        self.gas_cur = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.gas_cur.setGeometry(QtCore.QRect(300, 140, 91, 20))
        self.gas_cur.setObjectName("gas_current")
        self.gas_cur.setMaximum(10000)
        
        self.hot_water_cur = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.hot_water_cur.setMaximum(100000)
        self.hot_water_cur.setGeometry(QtCore.QRect(300, 80, 91, 20))
        self.hot_water_cur.setObjectName("hot_water_cur")
        self.hot_water_cur.setMaximum(10000)
        
        self.cold_water_cur = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.cold_water_cur.setGeometry(QtCore.QRect(300, 50, 91, 20))
        self.cold_water_cur.setObjectName("cold_water_cur")
        self.cold_water_cur.setMaximum(10000)
        
        self.electricity_cur = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.electricity_cur.setGeometry(QtCore.QRect(300, 110, 91, 20))
        self.electricity_cur.setObjectName("electrycity_cur")
        self.electricity_cur.setMaximum(100000)
        
        self.label_cw = QtWidgets.QLabel(self.centralwidget)
        self.label_cw.setGeometry(QtCore.QRect(70, 40, 91, 31))
        self.label_cw.setObjectName("label_cw")
        self.label_cw.setText("Холодная вода")

        
        self.label_hw = QtWidgets.QLabel(self.centralwidget)
        self.label_hw.setGeometry(QtCore.QRect(70, 70, 91, 31))
        self.label_hw.setObjectName("label_hw")
        self.label_hw.setText("Горячая вода")
        
        self.label_e = QtWidgets.QLabel(self.centralwidget)
        self.label_e.setGeometry(QtCore.QRect(70, 100, 91, 31))
        self.label_e.setObjectName("label_e")
        self.label_e.setText("Эл. энергия")
        
        self.label_g = QtWidgets.QLabel(self.centralwidget)
        self.label_g.setGeometry(QtCore.QRect(70, 130, 91, 31))
        self.label_g.setObjectName("label_g")
        self.label_g.setText("Газ")
        
        self.result_button = QtWidgets.QPushButton(self.centralwidget)
        self.result_button.setGeometry(QtCore.QRect(10, 170, 75, 23))
        self.result_button.setObjectName("result_button")
        self.result_button.setText("Расчет")

        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(10, 200, 75, 23))
        self.save_button.setObjectName("save_button")
        self.save_button.setText("сохранить")
        self.save_button.setEnabled(False)

        self.save_label = QtWidgets.QLabel(self.centralwidget)
        self.save_label.setGeometry(QtCore.QRect(10, 230, 75, 23))
        self.save_label.setObjectName("save_label")
        self.save_label.setText("")
        self.save_label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(170, 170, 230, 85))
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")
        

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

       
