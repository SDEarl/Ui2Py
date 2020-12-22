"""
ui2py_main.pyw
Author = Steve Earl
Converts PYQT5 Designer UI file to Python PY file

Copyright 2020 Steve Earl

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

# Imports
import sys
import os
import subprocess
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QObject
from ui2py_gui import Ui_MainWindow


class MainUI:

    version = 1.0

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.widget_actions()

        self.input_file = ""
        self.output_file = ""

        self.convert = Convert(input_file=self.input_file, output_file=self.output_file)
        self.thread = QThread()
        # Move the worker object to the thread object.
        self.convert.moveToThread(self.thread)

        self.MainWindow.show()
        sys.exit(app.exec_())

    def start_convert_thread(self):
        # Start the thread.
        self.thread.start()
        print('Converter thread started.\n')

    def widget_actions(self):
        self.ui.button_about.clicked.connect(self.show_about)
        self.ui.button_notes.clicked.connect(self.show_notes)
        self.ui.button_convert.clicked.connect(self.send_convert)
        self.ui.button_input_browse.clicked.connect(self.input_file_browse)
        self.ui.button_output_browse.clicked.connect(self.output_file_browse)

    def show_about(self):
        QMessageBox.about(self.MainWindow, 'About', 'UI2PY - A PyQt5 Uic Wrapper\nCreated by Steve Earl \n' +
                          f'Version: {self.version}')

    def input_file_browse(self):
        self.input_file = QtWidgets.QFileDialog.getOpenFileName(filter='PyQt5 Designer UI Files (*.ui)')
        self.input_file = self.input_file[0]
        self.ui.text_box_input_file.clear()
        self.ui.text_box_input_file.setText(self.input_file)

    def output_file_browse(self):
        output_file = QtWidgets.QFileDialog.getOpenFileName(filter='Python File (*.py)')
        self.output_file = output_file[0]
        self.ui.text_box_output_file.clear()
        self.ui.text_box_output_file.setText(self.output_file)

    def clear_text_box(self):
        self.ui.text_edit_info_box.clear()

    def update_text_box(self, text):
        self.ui.text_edit_info_box.append(text)

    def send_convert(self):
        input_file = self.ui.text_box_input_file.text()
        output_file = self.ui.text_box_output_file.text()
        print(f'Input file: {input_file}\nOutput file: {output_file}')
        self.input_file = input_file
        self.output_file = output_file
        print(f'Input file: {self.input_file}\nOutput file: {self.output_file}')
        self.clear_text_box()

        self.convert = Convert(input_file=self.input_file, output_file=self.output_file)
        # Connect worker`s signals to Main class method slots to update data.
        self.convert.conversion_status.connect(self.update_text_box)

        # Connect thread started signal to worker operational slot method.
        # Following line is needed because Python has an issue with the .connect below.
        # noinspection PyUnresolvedReferences
        self.thread.started.connect(self.convert.convert)
        # Connect worker signals to the thread slots.
        self.convert.finished.connect(self.thread.quit)

        self.start_convert_thread()

    def show_notes(self):
        """
        Displays a window with containing informational notes about the program.

        :return: None
        """
        msg = QMessageBox(self.MainWindow)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Notes")
        msg.setText('1. If you do not specify an existing or new \".py\" file one will be created with the same name '
                    ' as the input file.\n\n2. Existing files with the same name will be overwritten without asking'
                    ' permission.\n\n3. If it says the conversion was completed yet your new file is nowhere to be'
                    ' found, run the program from a command window as there may be background errors.')
        msg.setStyleSheet('font: 10 pt "Arial";')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()


class Convert(QObject):

    conversion_status = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, input_file, output_file):
        super().__init__()
        self.in_file = input_file
        self.out_file = output_file

    @pyqtSlot()
    def update_conversion_status(self, text):
        self.conversion_status.emit(text)

    def convert(self):
        print('Entered convert method.')  # Print statements were left in this method for troubleshooting
        file_path = self.in_file.rsplit('/', 1)[0]  # Index[0] returns the first half of the split
        print(f'File Path: {file_path}')
        in_file = self.in_file.rsplit('/', 1)[-1]  # Index[-1] returns the last half of the split
        print(f'File: {in_file}')
        if self.out_file == "":
            out_file = in_file.rsplit('.', 1)[0]  # Grab the file name less extension from the input file
            self.out_file = str(f'{out_file}.py')  # Add the file extension
        else:
            out_file = self.out_file.rsplit('/', 1)[-1]
            self.out_file = out_file
        print(f'File: {self.out_file}')

        self.conversion_status.emit("Setting file names and path...")
        print("Setting file names and path...")
        os.chdir(file_path)
        self.conversion_status.emit("Converting....")
        print("Converting....")

        try:
            subprocess.run(f'pyuic5 -x -o %s %s' % (self.out_file, self.in_file))
            print("Ran Subprocess")
        except subprocess.CalledProcessError as error:
            self.conversion_status.emit(error.returncode, error.output)
            # The above exception does not always work.  I believe it's due to the way PyQt5 emits the error(s).

        self.conversion_status.emit("Conversion complete!")
        self.conversion_status.emit(f"See {os.getcwd()}\\ for converted file.")
        self.finished.emit()
        print("Finished emitted")


if __name__ == '__main__':
    MainUI()
