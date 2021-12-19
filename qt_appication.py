import sys
import os
import PyQt5

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QScrollArea, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

class Window(QMainWindow):

    def __init__(self, photos_paths):
        super().__init__()
        self.title = "Program"
        self.photos_paths = photos_paths
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle(self.title)
        self.scroll = QScrollArea()
        self.vbox = QVBoxLayout() 
        self.widget = QWidget()
            
        shift = 0
        for path in self.photos_paths:
            picture = QLabel(self)
            button = QPushButton("🤍", clicked=self.handle_play_button)
            picture.resize(640, 480)
            pixmap = QPixmap("source/" + path)
            picture.move(0, shift)
            shift += 500
            picture.setPixmap(pixmap)
            self.vbox.addWidget(picture)
            self.vbox.addWidget(button)

        self.widget.setLayout(self.vbox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(False)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)
        self.showMaximized()
        self.show()

    @pyqtSlot()
    def handle_play_button(self):
        btn = PyQt5.QtWidgets.qApp.focusWidget()
        if btn is not None:
            text = btn.text()
            btn.setText("💖" if text == "🤍" else "🤍")


if __name__ == '__main__':
    directory = 'source/'
    files = os.listdir(directory)
    photo_paths = list(filter(lambda x: x.endswith('.jpg'), files))

    app = QApplication(sys.argv)
    w = Window(photo_paths)
    sys.exit(app.exec_())
