import sys
import os
from PyQt5.QtWidgets import QWidget, QPushButton, QDesktopWidget, QApplication, QLabel, QFileDialog
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QColor, QPainter
import hashlib


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.save_file = ''
        self.initUI()
        self.center()

    def initUI(self):
        dir_lbl = QLabel(self)
        dir_lbl.setText('Выберите путь до файла')
        dir_lbl.setGeometry(20, 20, 200, 20)

        self.path_lbl = QLabel(self)
        self.path_lbl.setText('')
        self.path_lbl.setGeometry(20, 40, 300, 20)

        file_btn = QPushButton('Обзор', self)
        file_btn.clicked.connect(self.open_dir)
        file_btn.resize(file_btn.sizeHint())
        file_btn.move(325, 40)

        self.look_btn = QPushButton('Посмотреть/изменить файл', self)
        self.look_btn.clicked.connect(self.open_file)
        self.look_btn.resize(200,30)
        self.look_btn.move(20, 70)
        self.look_btn.setVisible(False)

        self.decode_btn = QPushButton('Закодировать сообщение', self)
        self.decode_btn.clicked.connect(self.decoding)
        self.decode_btn.resize(200, 30)
        self.decode_btn.move(230, 70)
        self.decode_btn.setVisible(False)

        qbtn = QPushButton('Завершить работу', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(140,30)
        qbtn.move(300, 120)

        self.setGeometry(400, 400, 460, 160)
        self.setWindowTitle('SHA-256')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(18, 40, 300, 20)
        qp.end()

    def open_dir(self):
        self.filename = QFileDialog.getOpenFileName(self, "Выберите файл с сообщением", "C:/","Text files (*.txt)")[0]
        if self.filename:
            self.path_lbl.setText(self.filename)
            self.look_btn.setVisible(True)
            self.decode_btn.setVisible(True)

    def open_file(self):
        os.startfile(self.filename)

    def decoding(self):
        if self.save_file == '':
            self.save_file = QFileDialog.getSaveFileName(self, "Выберите файл для шифрования", "","Text Files (*.txt)")[0]
        if self.save_file:
            save_file = open(self.save_file, 'w')
            from_file = open(self.filename, 'r')
            for line in from_file:
                decoded_line = hashlib.sha256(line.encode('utf-8')).hexdigest()
                save_file.write(decoded_line+'\n')
            os.startfile(self.save_file)


app = QApplication(sys.argv)
ex = Window()
sys.exit(app.exec_())