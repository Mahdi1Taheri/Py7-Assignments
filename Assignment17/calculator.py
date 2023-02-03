from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def sum():
    a = main_window.number_1.text()
    b = main_window.number_2.text()
    c = b + a
    main_window.number_result.setText(str(c))

def sub():
    a = main_window.number_1.text()
    b = main_window.number_2.text()
    c = b - a
    main_window.number_result.setText(str(c))


app = QApplication([])

loader = QUiLoader()
main_window = loader.load("main.ui")
main_window.show()

main_window.btn_process.clicked.connect(sum)
main_window.btn_process2.clicked.connect(sub)

app.exec()