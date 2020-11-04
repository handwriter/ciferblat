# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import datetime
import sys


# creating a clock class
class Clock(QMainWindow):

    # constructor
    def __init__(self):
        super().__init__()

        # creating a timer object
        timer = QTimer(self)
        spacer = QSpacerItem(30, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.comboBox = QComboBox(self)
        for i in range(-11, 13):
            self.comboBox.addItem(f"UTC {i}")
        self.comboBox.currentTextChanged.connect(self.on_combobox_changed)
        # adding action to the timer
        # update the whole code
        timer.timeout.connect(self.update)

        # setting start time of timer i.e 1 second
        timer.start(1000)

        # setting window title
        self.setWindowTitle('Clock')
        # setting window geometry
        self.comboBox.setGeometry(155, 460, 90, 30)
        self.setFixedSize(400, 500)

        # setting background color to the window

        # creating hour hand
        self.hPointer = QtGui.QPolygon([QPoint(6, 7),
                                        QPoint(-6, 7),
                                        QPoint(0, -50)])

        # creating minute hand
        self.mPointer = QPolygon([QPoint(6, 7),
                                  QPoint(-6, 7),
                                  QPoint(0, -70)])

        # creating second hand
        self.sPointer = QPolygon([QPoint(1, 1),
                                  QPoint(-1, 1),
                                  QPoint(0, -90)])
        # colors
        # color for minute and hour hand
        self.bColor = Qt.black

        # color for second hand
        self.sColor = Qt.red

        # method for paint event

    def on_combobox_changed(self, value):
        print()
        # do your code

    def paintEvent(self, event):

        # getting minimum of width and height
        # so that clock remain square
        rec = min(self.width(), self.height())

        # getting current time
        tik = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=int(self.comboBox.currentText().split()[1]), minutes=0)
        # creating a painter object
        painter = QPainter(self)

        # method to draw the hands
        # argument : color rotation and which hand should be pointed
        def drawPointer(color, rotation, pointer):

            # setting brush
            painter.setBrush(QBrush(color))

            # saving painter
            painter.save()

            # rotating painter
            painter.rotate(rotation)

            # draw the polygon i.e hand
            painter.drawConvexPolygon(pointer)

            # restore the painter
            painter.restore()

            # tune up painter

        painter.setRenderHint(QPainter.Antialiasing)

        # translating the painter
        painter.translate(self.width() / 2, self.height() / 2)

        # scale the painter
        painter.scale(rec / 200, rec / 200)

        # set current pen as no pen
        painter.setPen(QtCore.Qt.NoPen)

        # draw each hand
        drawPointer(self.bColor, (30 * (tik.hour + tik.minute / 60)), self.hPointer)
        drawPointer(self.bColor, (6 * (tik.minute + tik.second / 60)), self.mPointer)
        drawPointer(self.sColor, (6 * tik.second), self.sPointer)
        # drawing background
        painter.setPen(QPen(self.bColor))

        # for loop
        for i in range(0, 60):

            # drawing background lines
            if (i % 5) == 0:
                painter.drawLine(87, 0, 97, 0)

                # rotating the painter
            painter.rotate(6)

            # ending the painter
        painter.end()

    # Driver code
class Mains(QMainWindow):

    # constructor
    def __init__(self):
        super().__init__()

        # creating a timer object
        button1 = QPushButton("1")
        button2 = QPushButton("2")
        self.setFixedSize(400, 500)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # creating a clock object
    win = Clock()
    win1 = Mains()
    # show
    win1.show()

    exit(app.exec_())