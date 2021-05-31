from PyQt5 import QtCore, QtWidgets, QtGui
from MenuBar import *
from StyleSheets import *
from PandanArum import *


class Page0(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super().__init__()

    def Tab0(self):
        self.tab0 = QtWidgets.QWidget()
        self.tab0.setObjectName("Tab0")
        self.tab_UTAMA.addTab(self.tab0, '')
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab0), "Login")

    def Page0_GridLayout(self):
        self.page0_GridLayout = QtWidgets.QGridLayout(self.tab0)
        self.page0_GridLayout.setObjectName("gridLayout_29")

    def Page0_GridLayout_1(self):
        self.page0_GridLayout_1 = QtWidgets.QGridLayout()
        self.page0_GridLayout_1.setObjectName("TAB_PAGE3_GridLayout")
        self.page0_GridLayout.addLayout(self.page0_GridLayout_1, 0, 0, 1, 1)

    def Page0_TabWidget(self):
        self.page0_TabWidget = QtWidgets.QTabWidget(self.tab0)
        self.page0_TabWidget.setFont(Font(8, False))
        self.page0_TabWidget.setObjectName("TAB_PAGE3_TAB")
        self.page0_TabWidget.setStyleSheet(TabStyleSheet5(CekResolusi()))
        self.page0_GridLayout_1.addWidget(self.page0_TabWidget, 0, 0, 1, 1)
        self.page0_TabWidget.setCurrentIndex(0)

    def Page0_Widget(self):
        self.page0_Widget = QtWidgets.QWidget()
        self.page0_Widget.setObjectName("page0_Widget")
        self.page0_TabWidget.addTab(self.page0_Widget, "")
        self.page0_TabWidget.setTabText(self.page0_TabWidget.indexOf(self.page0_Widget), "Silakan Login")

    def Page0_GridLayout_2(self):
        self.page0_GridLayout_2 = QtWidgets.QGridLayout()
        self.page0_GridLayout_2.setObjectName('page0_GridLayout_2')
        self.page0_Widget.setLayout(self.page0_GridLayout_2)

    def Page0_SpacerItem(self):
        # Sebelah Kanan
        self.page0_SpacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        self.page0_GridLayout_2.addItem(self.page0_SpacerItem, 1, 0)

    def Page0_SpacerItem_1(self):
        # Sebelah Atas
        self.page0_SpacerItem_1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        self.page0_GridLayout_2.addItem(self.page0_SpacerItem_1, 0, 1)

    def Page0_Label(self):
        # Logo
        self.page0_label = QtWidgets.QLabel('Logo/Gambar')
        self.page0_label.setObjectName('page0_label')
        Gambar = self.PathPictures + '\\Logo5.png'
        Pixmap = QtGui.QPixmap(Gambar)
        self.page0_label.setScaledContents(True)
        self.page0_label.setPixmap(Pixmap)
        self.page0_label.setAlignment(QtCore.Qt.AlignHCenter)
        self.page0_GridLayout_2.addWidget(self.page0_label, 1, 1, 1, 3)

    def Page0_Label_1(self):
        # Ucapan Selamat Datang
        self.page0_label_1 = QtWidgets.QLabel('Selamat Datang di PandanArum Store. \nSilakan masukkan nama pengguna dan kata sandi\n \n')
        self.page0_label_1.setObjectName('page0_label_1')
        self.page0_label_1.setFont(Font(9, False))
        self.page0_label_1.setAlignment(QtCore.Qt.AlignHCenter)
        self.page0_GridLayout_2.addWidget(self.page0_label_1, 3, 1, 1, 3)

    def Page0_SpacerItem_2(self):
        # Tengah antara (Logo, Ucapan Selamat Datang) dan (Masukkan Nama Pengguna)
        self.page0_SpacerItem_2 = QtWidgets.QSpacerItem(50, 50, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.page0_GridLayout_2.addItem(self.page0_SpacerItem_2, 2, 1)

    def Page0_Label_2(self):
        self.page0_label_2 = QtWidgets.QLabel('Nama Pengguna : ')
        self.page0_label_2.setObjectName('page0_label_2')
        self.page0_label_2.setFont(Font(9, False))
        self.page0_GridLayout_2.addWidget(self.page0_label_2, 4, 1, 1, 1)

    def Page0_LineEdit(self):
        self.page0_lineEdit = QtWidgets.QLineEdit()
        self.page0_lineEdit.setObjectName('page0_lineEdit : ')
        self.page0_lineEdit.setFont(Font(9, False))
        self.page0_lineEdit.setMinimumHeight(50)
        self.page0_lineEdit.setFocus()
        self.page0_GridLayout_2.addWidget(self.page0_lineEdit, 4, 2, 1, 2)

    def Page0_Label_3(self):
        self.page0_label_3 = QtWidgets.QLabel('Kata Sandi : ')
        self.page0_label_3.setObjectName('page0_label_3')
        self.page0_label_3.setFont(Font(9, False))
        self.page0_GridLayout_2.addWidget(self.page0_label_3, 5, 1, 1, 1)

    def Page0_LineEdit_1(self):
        self.page0_lineEdit_1 = QtWidgets.QLineEdit()
        self.page0_lineEdit_1.setObjectName('page0_lineEdit_1')
        self.page0_lineEdit_1.setFont(Font(9, False))
        self.page0_lineEdit_1.setMinimumHeight(50)
        self.page0_lineEdit_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.page0_GridLayout_2.addWidget(self.page0_lineEdit_1, 5, 2, 1, 2)

    def Page0_SpacerItem_3(self):
        # Tengah antara (label Nama Pengguna, Kata Sandi) dan (pushButton login, keluar)
        self.page0_SpacerItem_3 = QtWidgets.QSpacerItem(50, 50, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.page0_GridLayout_2.addItem(self.page0_SpacerItem_3, 6, 1)

    def Page0_PushButton(self):
        self.page0_pushButton = QtWidgets.QPushButton('Login')
        self.page0_pushButton.setObjectName('page0_pushButton')
        self.page0_pushButton.setFont(Font(9, False))
        self.page0_pushButton.setMinimumHeight(70)
        self.page0_pushButton.setStyleSheet(ButtonStyleSheets1(CekResolusi()))
        self.page0_pushButton.setShortcut(QtGui.QKeySequence('Return'))
        self.page0_GridLayout_2.addWidget(self.page0_pushButton, 7, 2)

    def Page0_PushButton_1(self):
        self.page0_pushButton_1 = QtWidgets.QPushButton('Keluar')
        self.page0_pushButton_1.setObjectName('page0_pushButton_1')
        self.page0_pushButton_1.setFont(Font(9, False))
        self.page0_pushButton_1.setMinimumHeight(70)
        self.page0_pushButton_1.setStyleSheet(ButtonStyleSheets1(CekResolusi()))
        self.page0_pushButton_1.setShortcut(QtGui.QKeySequence('Esc'))
        self.page0_GridLayout_2.addWidget(self.page0_pushButton_1, 7, 3)

    def Page0_SpacerItem_4(self):
        # Tengah antara (pushButton Login, Keluar) dan (label produseno.com)
        self.page0_SpacerItem_4 = QtWidgets.QSpacerItem(50, 150, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.page0_GridLayout_2.addItem(self.page0_SpacerItem_4, 8, 1)

    def Page0_Label_4(self):
        self.page0_label_4 = QtWidgets.QLabel('\nCopyright 2020, Aplikasi Toko PandanArum\nBy PandanArum.com')
        self.page0_label_4.setObjectName('page0_label_4')
        self.page0_label_4.setFont(Font(9, False))
        self.page0_label_4.setAlignment(QtCore.Qt.AlignHCenter)
        self.page0_GridLayout_2.addWidget(self.page0_label_4, 9, 1, 1, 3)

    def Page0_SpacerItem_5(self):
        # Bawah
        self.page0_SpacerItem_5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        self.page0_GridLayout_2.addItem(self.page0_SpacerItem_5, 10, 1)

    def Page0_SpacerItem_6(self):
        # Kanan
        self.page0_SpacerItem_6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        self.page0_GridLayout_2.addItem(self.page0_SpacerItem_6, 11, 4)

    def Page0_ResolutionManager(self):
        Resolusi = CekResolusi()
        if Resolusi == '1280x720':
            self.page0_label.setFixedSize(300, 125)
            self.page0_SpacerItem_2.changeSize(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            self.page0_lineEdit.setMinimumHeight(25)
            self.page0_lineEdit_1.setMinimumHeight(25)
            self.page0_SpacerItem_3.changeSize(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            self.page0_pushButton.setMinimumHeight(30)
            self.page0_pushButton_1.setMinimumHeight(30)
            self.page0_SpacerItem_4.changeSize(50, 75, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        else:
            pass

    def Page0_Execution(self):
        # TAB 0
        self.Tab0()  # Page 0
        self.Page0_GridLayout()  # Page 0
        self.Page0_GridLayout_1()  # Page 0
        self.Page0_TabWidget()  # Page 0
        self.Page0_Widget()  # Page 0
        self.Page0_GridLayout_2()
        self.Page0_SpacerItem()
        self.Page0_SpacerItem_1()
        self.Page0_Label()
        self.Page0_SpacerItem_2()
        self.Page0_Label_1()
        self.Page0_Label_2()
        self.Page0_LineEdit()
        self.page0_lineEdit.setText('mjsodiq')
        self.Page0_Label_3()
        self.Page0_LineEdit_1()
        self.page0_lineEdit_1.setText('mjsodiq1')
        self.Page0_SpacerItem_3()
        self.Page0_PushButton()
        self.Page0_PushButton_1()
        self.Page0_SpacerItem_4()
        self.Page0_Label_4()
        self.Page0_SpacerItem_5()
        self.Page0_SpacerItem_6()
        self.Page0_PERINTAH()
        self.Page0_ResolutionManager()

    ########################################################################################################################
    def Page0_PERINTAH(self):
        self.page0_pushButton.clicked.connect(self.KlikTombolLogin)
        self.page0_pushButton_1.clicked.connect(self.programAplikasiToko.close)

    def KlikTombolLogin(self):
        # connect to Database
        user = []
        InputedData = str(self.page0_lineEdit.text())+str(self.page0_lineEdit_1.text())
        self.page0_UserDatabase_connection = sqlite3.connect(self.UserDatabase)
        self.page0_UserDatabase_cursor = self.page0_UserDatabase_connection.cursor()
        data = self.page0_UserDatabase_cursor.execute('SELECT username,password,kelas FROM user').fetchall()
        jumlahUser = len(data)
        for item in range(jumlahUser):
            user.append(str(data[item][0])+str(data[item][1]))

        if InputedData in user:
            self.username = []
            self.kelas = []
            self.username.clear()
            username = str(self.page0_lineEdit.text())
            self.username.append(username)

            self.kelas.clear()
            try:
                kelas = self.page0_UserDatabase_cursor.execute('SELECT kelas FROM user WHERE "username"="{}"'.format(username)).fetchone()[0]
            except:
                kelas = ''
                pass
            self.kelas.append(kelas)
            self.CreateEventSystemLOG('{}, {}'.format(username, kelas), '{} {} berhasil login'.format(kelas, username))

            self.Communication.SignalLoginSukses()
            return username

        else:
            username = str(self.page0_lineEdit.text())
            try:
                kelas = self.page0_UserDatabase_cursor.execute('SELECT kelas FROM user WHERE "username"="{}"'.format(username)).fetchone()[0]
            except:
                kelas = ''
            pesanError = QtWidgets.QMessageBox()
            pesanError.setWindowTitle('Login Error')
            pesanError.setText('NAMA PENGGUNA atau KATA SANDI yang anda masukkan salah')
            pesanError.setIcon(QtWidgets.QMessageBox.Warning)
            pesanError.exec_()
            self.CreateEventSystemLOG('{}, {}'.format(username, kelas), 'User {} mencoba untuk login namun gagal. Username yang diinput "{}", pasword yang diinput "{}"'.format(self.page0_lineEdit.text(), self.page0_lineEdit.text(), self.page0_lineEdit_1.text()))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page0()
    objek.Page0_Execution()
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
