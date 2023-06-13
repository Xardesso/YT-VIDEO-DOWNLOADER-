from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QFileDialog, QPushButton, QHBoxLayout, QLabel
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

import sys
import pytube
import os
import subprocess


def select_directory():
    global path

    folder_path = QFileDialog.getExistingDirectory(None, 'Wybierz folder', '/')
    path = folder_path


def download():
    url = LINE.text()
    file_name = LINE2.text()
    output_filename = file_name + '.mp4'
    destination_folder = path
    video = pytube.YouTube(url)
    video_stream = video.streams.filter(res='720p').first()
    video_stream.download(filename=output_filename, output_path=destination_folder)

    audio_filename = os.path.splitext(output_filename)[0] + '.mp3'
    subprocess.call(['ffmpeg', '-i', os.path.join(destination_folder, output_filename), os.path.join(destination_folder, audio_filename)])

    if video_stream.filesize == os.path.getsize(video.default_filename):
        print("Success")
    else:
        print("FAIL")


app = QApplication(sys.argv)

win = QMainWindow()
icon = QIcon("icon.jpg")
win.setWindowIcon(icon)

win.setGeometry(500, 500, 270, 300)
win.setWindowTitle("VIDEO DOWNLOADER")

label = QtWidgets.QLabel(win)
label.setText("Input url")
label.move(10, 10)

LINE = QLineEdit(win)
LINE.move(10, 40)
LINE.resize(250, 40)

label2 = QtWidgets.QLabel(win)
label2.setText("Choose name")
label2.move(10, 80)

LINE2 = QLineEdit(win)
LINE2.move(10, 120)
LINE2.resize(250, 40)

label3 = QtWidgets.QLabel(win)
label3.setText("Choose directory")
label3.move(10, 170)

button = QPushButton("Select", win)
button.move(10, 200)
button.clicked.connect(select_directory)

label4 = QtWidgets.QLabel(win)
label4.setText("Submit")
label4.move(10, 230)

btn = QPushButton("Enter", win)
btn.setObjectName("Button")
btn.move(10, 260)
btn.clicked.connect(download)

win.show()
sys.exit(app.exec())
