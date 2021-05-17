import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

# 창 띄우기
class loginWidget(QWidget):
    def __init__(self, parent=None, ticker="BTC"):
        super().__init__(parent)
        uic.loadUi("source/login.ui", self)
        self.ticker = ticker

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ow = loginWidget()
    ow.show()
    exit(app.exec_())
