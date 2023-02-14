import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def sub():
    global a
    global op
    op = "-"
    a = float(main_window.txtbox.text())
    main_window.txtbox.setText("")

def plus():
    global a
    global op
    op = "+"
    a = float(main_window.txtbox.text())
    main_window.txtbox.setText("")

def multi():
    global a
    global op
    op = "*"
    a = float(main_window.txtbox.text())
    main_window.txtbox.setText("")

def div():
    global a
    global op
    op = "/"
    a = float(main_window.txtbox.text())
    main_window.txtbox.setText("")

def sin():
    a = float(main_window.txtbox.text())
    c = math.sin(a)
    c = round(c,3)
    main_window.txtbox.setText(str(c))

def cos():
    a = float(main_window.txtbox.text())
    c = math.cos(a)
    c = round(c,3)
    main_window.txtbox.setText(str(c))

def tan():
    a = float(main_window.txtbox.text())
    c = math.tan(a)
    c = round(c,3)
    main_window.txtbox.setText(str(c))

def cot():
    a = float(main_window.txtbox.text())
    c = math.cos(a) / math.sin(a)
    c = round(c,3)
    main_window.txtbox.setText(str(c))

def log():
    a = float(main_window.txtbox.text())
    c = math.log(a)
    c = round(c,3)
    main_window.txtbox.setText(str(c))

def sqrt():
    a = float(main_window.txtbox.text())
    c = math.sqrt(a)
    c = round(c,3)
    main_window.txtbox.setText(str(c))

def result():
    if op == "-":
        b = int(main_window.txtbox.text())
        c = a - b
        main_window.txtbox.setText(str(c))
    elif op == "+":
        b = int(main_window.txtbox.text())
        c = a + b
        main_window.txtbox.setText(str(c))
    elif op == "*":
        b = int(main_window.txtbox.text())
        c = a * b
        main_window.txtbox.setText(str(c))
    elif op == "/":
        b = int(main_window.txtbox.text())
        c = a / b
        c = round(c,3)
        main_window.txtbox.setText(str(c))


def nums(n):
    main_window.txtbox.insert(n)
    
def dot():
    main_window.txtbox.insert(".")
def clear():
    main_window.txtbox.clear()

app = QApplication([])
loader = QUiLoader()
main_window = loader.load("Assignment18/MainWin.ui")

main_window.btn_equal1.clicked.connect(result)
main_window.btn_sub.clicked.connect(sub)
main_window.btn_plus.clicked.connect(plus)
main_window.btn_multi.clicked.connect(multi)
main_window.btn_div.clicked.connect(div)
main_window.btn_num0.clicked.connect(partial(nums,"0"))
main_window.btn_num1.clicked.connect(partial(nums,"1"))
main_window.btn_num2.clicked.connect(partial(nums,"2"))
main_window.btn_num3.clicked.connect(partial(nums,"3"))
main_window.btn_num4.clicked.connect(partial(nums,"4"))
main_window.btn_num5.clicked.connect(partial(nums,"5"))
main_window.btn_num6.clicked.connect(partial(nums,"6"))
main_window.btn_num7.clicked.connect(partial(nums,"7"))
main_window.btn_num8.clicked.connect(partial(nums,"8"))
main_window.btn_num9.clicked.connect(partial(nums,"9"))
main_window.btn_sin.clicked.connect(sin)
main_window.btn_cos.clicked.connect(cos)
main_window.btn_tan.clicked.connect(tan)
main_window.btn_cot.clicked.connect(cot)
main_window.btn_log.clicked.connect(log)
main_window.btn_sqrt.clicked.connect(sqrt)
main_window.btn_dot1.clicked.connect(dot)
main_window.btn_clear.clicked.connect(clear)

main_window.show()
app.exec()
