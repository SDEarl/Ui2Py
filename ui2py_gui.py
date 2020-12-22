# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/ui2py/ui2py_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 300)
        MainWindow.setMinimumSize(QtCore.QSize(740, 300))
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_in_out = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_in_out.sizePolicy().hasHeightForWidth())
        self.frame_in_out.setSizePolicy(sizePolicy)
        self.frame_in_out.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_in_out.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_in_out.setObjectName("frame_in_out")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_in_out)
        self.gridLayout.setObjectName("gridLayout")
        self.button_about = QtWidgets.QPushButton(self.frame_in_out)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_about.sizePolicy().hasHeightForWidth())
        self.button_about.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.button_about.setFont(font)
        self.button_about.setObjectName("button_about")
        self.gridLayout.addWidget(self.button_about, 0, 0, 1, 1)
        self.button_notes = QtWidgets.QPushButton(self.frame_in_out)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_notes.sizePolicy().hasHeightForWidth())
        self.button_notes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.button_notes.setFont(font)
        self.button_notes.setObjectName("button_notes")
        self.gridLayout.addWidget(self.button_notes, 0, 1, 1, 2)
        self.label_input_file = QtWidgets.QLabel(self.frame_in_out)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_input_file.sizePolicy().hasHeightForWidth())
        self.label_input_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_input_file.setFont(font)
        self.label_input_file.setObjectName("label_input_file")
        self.gridLayout.addWidget(self.label_input_file, 1, 0, 1, 1)
        self.text_box_input_file = QtWidgets.QLineEdit(self.frame_in_out)
        self.text_box_input_file.setMinimumSize(QtCore.QSize(520, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.text_box_input_file.setFont(font)
        self.text_box_input_file.setText("")
        self.text_box_input_file.setDragEnabled(True)
        self.text_box_input_file.setObjectName("text_box_input_file")
        self.gridLayout.addWidget(self.text_box_input_file, 1, 2, 1, 1)
        self.button_input_browse = QtWidgets.QPushButton(self.frame_in_out)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_input_browse.sizePolicy().hasHeightForWidth())
        self.button_input_browse.setSizePolicy(sizePolicy)
        self.button_input_browse.setMinimumSize(QtCore.QSize(75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.button_input_browse.setFont(font)
        self.button_input_browse.setObjectName("button_input_browse")
        self.gridLayout.addWidget(self.button_input_browse, 1, 3, 1, 1)
        self.label_output_file = QtWidgets.QLabel(self.frame_in_out)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_output_file.sizePolicy().hasHeightForWidth())
        self.label_output_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_output_file.setFont(font)
        self.label_output_file.setObjectName("label_output_file")
        self.gridLayout.addWidget(self.label_output_file, 2, 0, 1, 2)
        self.text_box_output_file = QtWidgets.QLineEdit(self.frame_in_out)
        self.text_box_output_file.setMinimumSize(QtCore.QSize(520, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.text_box_output_file.setFont(font)
        self.text_box_output_file.setText("")
        self.text_box_output_file.setDragEnabled(True)
        self.text_box_output_file.setClearButtonEnabled(False)
        self.text_box_output_file.setObjectName("text_box_output_file")
        self.gridLayout.addWidget(self.text_box_output_file, 2, 2, 1, 1)
        self.button_output_browse = QtWidgets.QPushButton(self.frame_in_out)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_output_browse.sizePolicy().hasHeightForWidth())
        self.button_output_browse.setSizePolicy(sizePolicy)
        self.button_output_browse.setMinimumSize(QtCore.QSize(75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.button_output_browse.setFont(font)
        self.button_output_browse.setObjectName("button_output_browse")
        self.gridLayout.addWidget(self.button_output_browse, 2, 3, 1, 1)
        self.gridLayout_3.addWidget(self.frame_in_out, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.text_edit_info_box = QtWidgets.QTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_edit_info_box.sizePolicy().hasHeightForWidth())
        self.text_edit_info_box.setSizePolicy(sizePolicy)
        self.text_edit_info_box.setMinimumSize(QtCore.QSize(680, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.text_edit_info_box.setFont(font)
        self.text_edit_info_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_edit_info_box.setAcceptDrops(False)
        self.text_edit_info_box.setToolTip("")
        self.text_edit_info_box.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_edit_info_box.setUndoRedoEnabled(False)
        self.text_edit_info_box.setReadOnly(True)
        self.text_edit_info_box.setObjectName("text_edit_info_box")
        self.gridLayout_2.addWidget(self.text_edit_info_box, 0, 0, 1, 1)
        self.button_convert = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_convert.sizePolicy().hasHeightForWidth())
        self.button_convert.setSizePolicy(sizePolicy)
        self.button_convert.setMinimumSize(QtCore.QSize(75, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.button_convert.setFont(font)
        self.button_convert.setObjectName("button_convert")
        self.gridLayout_2.addWidget(self.button_convert, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.text_box_input_file, self.button_input_browse)
        MainWindow.setTabOrder(self.button_input_browse, self.text_box_output_file)
        MainWindow.setTabOrder(self.text_box_output_file, self.button_convert)
        MainWindow.setTabOrder(self.button_convert, self.button_about)
        MainWindow.setTabOrder(self.button_about, self.text_edit_info_box)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UI2PY - PyUIC Wrapper"))
        self.button_about.setText(_translate("MainWindow", "About"))
        self.button_notes.setText(_translate("MainWindow", "Notes"))
        self.label_input_file.setText(_translate("MainWindow", "Input File(ui):"))
        self.text_box_input_file.setPlaceholderText(_translate("MainWindow", "Drag & drop, type or browse for file you wish to convert"))
        self.button_input_browse.setText(_translate("MainWindow", "Browse"))
        self.label_output_file.setText(_translate("MainWindow", "Output File (py):"))
        self.text_box_output_file.setPlaceholderText(_translate("MainWindow", "Browse for existing file or type in a new file name(See notes)"))
        self.button_output_browse.setText(_translate("MainWindow", "Browse"))
        self.button_convert.setText(_translate("MainWindow", "Convert!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())