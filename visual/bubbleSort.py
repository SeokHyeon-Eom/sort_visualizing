import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MY APP")
        self.move(300, 10)
        self.resize(1290, 900)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        
        arr = [4, 7, 9, 0, 1, 6, 2, 8, 3, 5]
        for i in range(0, 9):
            for j in range(1, 10 - i):
                self.painting(qp, arr, j, j - 1)
                if(arr[j] < arr[j - 1]):
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]

        qp.end()

    def painting(self, qp, arr, com, com2):
        for i in range(0, 10):
            self.draw_rect(qp, i, arr[i], com, com2)

    def draw_rect(self, qp, idx, value, com, com2):
        if(idx == com or idx == com2):
            qp.drawRect(100 * (idx + 1) + idx * 10, 120, 100, value * 60 + 10)
            qp.setBrush(QColor(180, 100, 160))
            qp.setPen(QPen(QColor(60, 60, 60), 3))
        else:
            qp.drawRect(100 * (idx + 1) + idx * 10, 100, 100, value * 60 + 10)
            qp.setBrush(QColor(0, 100, 160))
            qp.setPen(QPen(QColor(60, 60, 60), 3))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
