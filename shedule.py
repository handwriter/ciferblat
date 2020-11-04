import sqlite3
# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import datetime
import sys
from PyQt5 import uic


class Mains(QWidget):

    # constructor
    def __init__(self):
        super().__init__()
        uic.loadUi("shedule.ui", self)
        # creating a timer object
        self.conn = sqlite3.connect("sh_db.db")  # или :memory: чтобы сохранить в RAM
        self.cursor = self.conn.cursor()
        result = self.cursor.execute("""SELECT time 
                          FROM shedule;"""
                       ).fetchall()
        self.pushButton.clicked.connect(self.addRow)
        self.pushButton_2.clicked.connect(self.save)
        self.pushButton_3.clicked.connect(self.delete)
        self.keys = {}
        print(result)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        self.tableWidget.itemChanged.connect(self.itemChanged)
        self.setFixedSize(400, 500)

    def addRow(self):
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        self.cursor.execute("INSERT INTO shedule(time) VALUES('')")

    def itemChanged(self, item):
        result = self.cursor.execute("""SELECT * 
                                  FROM shedule;"""
                                     ).fetchall()
        print(result, item.row())
        self.cursor.execute(f"""UPDATE shedule
                                
                                SET time = '{item.text()}'
                                
                                WHERE id = {result[item.row()][1]}""")

    def delete(self):
        result = self.cursor.execute("""SELECT * 
                                          FROM shedule;"""
                                     ).fetchall()
        row = self.tableWidget.currentRow()
        self.tableWidget.removeRow(row)
        print(self.tableWidget.currentRow(), self.tableWidget.currentItem().row(), self.tableWidget.currentItem().text())
        self.cursor.execute(f"""DELETE from shedule
                                
                                where time = {self.tableWidget.currentItem().text()}""")


    def save(self):
        self.conn.commit()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    # creating a clock object
    win1 = Mains()
    # show
    win1.show()

    exit(app.exec_())