import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox 
from PySide6.QtCore import QFile
from pytube import YouTube
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_download.clicked.connect(self.download)
    
    def download(self):
        self.link = self.ui.line_edit1.text()
        yt = YouTube(self.link)
        self.ui.textEdit.setText(f"Title: {yt.title}\n views: {yt.views}\n Description: {yt.description}")
        video = yt.streams.get_by_resolution("480p")
        video.download()

app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()