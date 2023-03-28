import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)

        self.timeLabel = QLabel('00:00:00')
        self.timeLabel.setStyleSheet('font-size: 50px;')

        startButton = QPushButton('Start')
        startButton.clicked.connect(self.startTimer)

        stopButton = QPushButton('Stop')
        stopButton.clicked.connect(self.stopTimer)

        resetButton = QPushButton('Reset')
        resetButton.clicked.connect(self.resetTimer)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(startButton)
        buttonLayout.addWidget(stopButton)
        buttonLayout.addWidget(resetButton)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.timeLabel)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        
    def updateTime(self):
        time = self.timer.remainingTime() // 1000
        hours = time // 3600
        minutes = (time % 3600) // 60
        seconds = time % 60
        self.timeLabel.setText(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

    def startTimer(self):
         if not self.timer.isActive():
             self.timer.start(1000) # update every second

    def stopTimer(self):
         if self.timer.isActive():
             self.timer.stop()

    def resetTimer(self):
         if not self.timer.isActive():
             self.timeLabel.setText('00:00:00')

if __name__ == '__main__':
     app = QApplication(sys.argv)
     timer = Timer()
     timer.show()
     sys.exit(app.exec_())