from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def test():
    my_window.lineEdit.setText("Hi Hi")

my_app = QApplication([])

loader = QUiLoader()
my_window = loader.load("mainwindow.ui")
my_window.show()

my_window.pushButton_2.clicked.connect(test)

my_app.exec()