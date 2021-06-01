from PandanArum import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PandanArum import *
import sys
import os

class MenuBar(Ui_ProgramAplikasiToko):
    def __init__(self):
        super(MenuBar, self).__init__()

    def MenuBar(self):
        self.menubar = QtWidgets.QMenuBar(self.programAplikasiToko)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1439, 22))
        self.menubar.setObjectName("menubar")

    def MenuBar_File(self):
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.setTitle('File')

    def MenuBar_File_Keluar(self):
        self.actionKeluar = QtWidgets.QAction(self.programAplikasiToko)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/Tambah/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionKeluar.setIcon(icon22)
        self.actionKeluar.setObjectName("actionKeluar")
        self.actionKeluar.setText("Keluar")
        self.menuFile.addAction(self.actionKeluar)

    def MenuBar_File_ShutDown(self):
        self.actionShutDown = QtWidgets.QAction(self.programAplikasiToko)
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(":/Tambah/error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShutDown.setIcon(icon34)
        self.actionShutDown.setObjectName("actionShutDown")
        self.actionShutDown.setText("Shut Down")
        self.menuFile.addAction(self.actionShutDown)

    def MenuBar_File_Restart(self):
        self.actionRestart = QtWidgets.QAction(self.programAplikasiToko)
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap(":/Tambah/recycle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRestart.setIcon(icon35)
        self.actionRestart.setObjectName("actionRestart")
        self.actionRestart.setText("Restart")
        self.menuFile.addAction(self.actionRestart)

    def MenuBar_User(self):
        self.menuUser = QtWidgets.QMenu(self.menubar)
        self.menuUser.setObjectName("menuUser")
        self.menubar.addAction(self.menuUser.menuAction())
        self.menuUser.setTitle('User')

    def MenuBar_User_Login(self):
        self.actionLogin = QtWidgets.QAction(self.programAplikasiToko)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/Tambah/key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogin.setIcon(icon27)
        self.actionLogin.setObjectName("actionLogin")
        self.actionLogin.setText("Login")
        self.menuUser.addAction(self.actionLogin)

    def MenuBar_User_Logout(self):
        self.actionLogout = QtWidgets.QAction(self.programAplikasiToko)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/Tambah/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogout.setIcon(icon28)
        self.actionLogout.setObjectName("actionLogout")
        self.actionLogout.setText("Logout")
        self.menuUser.addAction(self.actionLogout)

    def MenuBar_User_TambahkanPengguna(self):
        self.actionTambahkanPengguna = QtWidgets.QAction(self.programAplikasiToko)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/Tambah/User group.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTambahkanPengguna.setIcon(icon29)
        self.actionTambahkanPengguna.setObjectName("actionTambahkanPengguna")
        self.actionTambahkanPengguna.setText("Tambahkan Pengguna")
        self.menuUser.addAction(self.actionTambahkanPengguna)

    def MenuBar_User_RequestLupaPassword(self):
        self.actionRequestLupaPassword = QtWidgets.QAction(self.programAplikasiToko)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(":/Tambah/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRequestLupaPassword.setIcon(icon30)
        self.actionRequestLupaPassword.setObjectName("actionRequestLupaPassword")
        self.actionRequestLupaPassword.setText("Request Lupa Password")
        self.menuUser.addAction(self.actionRequestLupaPassword)

    def MenuBar_User_UbahDataPengguna(self):
        self.actionUbahDataPengguna = QtWidgets.QAction(self.programAplikasiToko)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(":/Tambah/file_edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUbahDataPengguna.setIcon(icon31)
        self.actionUbahDataPengguna.setObjectName("actionUbahDataPengguna")
        self.actionUbahDataPengguna.setText("Ubah Data Pengguna")
        self.menuUser.addAction(self.actionUbahDataPengguna)

    def MenuBar_Tampilan(self):
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuView.setTitle("Tampilan")
        self.menubar.addAction(self.menuView.menuAction())

    def MenuBar_Tampilan_TampilkanMenuSamping(self):
        self.actionTampilkanMenuSamping = QtWidgets.QAction(self.programAplikasiToko)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/Tambah/center_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTampilkanMenuSamping.setIcon(icon23)
        self.actionTampilkanMenuSamping.setObjectName("actionTampilkanMenuSamping")
        self.actionTampilkanMenuSamping.setText("Tampilkan Menu Samping")
        self.menuView.addAction(self.actionTampilkanMenuSamping)

    def MenuBar_Tampilan_TampilkanToolbar(self):
        self.actionTampilkanToolBar = QtWidgets.QAction(self.programAplikasiToko)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/Tambah/center_top.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTampilkanToolBar.setIcon(icon24)
        self.actionTampilkanToolBar.setObjectName("actionTampilkanToolBar")
        self.actionTampilkanToolBar.setText("Tampilkan Tool Bar")
        self.menuView.addAction(self.actionTampilkanToolBar)

    def MenuBar_Tampilan_PilihResolusiMonitor(self):
        self.menuPilihResolusiMonitor = QtWidgets.QMenu(self.menuView)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/Tambah/resize diag 1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuPilihResolusiMonitor.setIcon(icon20)
        self.menuPilihResolusiMonitor.setObjectName("menuPilihResolusiMonitor")
        self.menuPilihResolusiMonitor.setTitle("Pilih Resolusi Monitor")
        self.menuView.addAction(self.menuPilihResolusiMonitor.menuAction())
        ###
        self.action400X600 = QtWidgets.QAction(self.programAplikasiToko)
        self.action400X600.setIcon(icon20)
        self.action400X600.setObjectName("action400X600")
        self.action400X600.setText("400 x 600")
        self.menuPilihResolusiMonitor.addAction(self.action400X600)
        ###
        self.action800X600 = QtWidgets.QAction(self.programAplikasiToko)
        self.action800X600.setIcon(icon20)
        self.action800X600.setObjectName("action800X600")
        self.action800X600.setText("800 x 600")
        self.menuPilihResolusiMonitor.addAction(self.action800X600)
        ###
        self.action1024X768 = QtWidgets.QAction(self.programAplikasiToko)
        self.action1024X768.setIcon(icon20)
        self.action1024X768.setObjectName("action1024X768")
        self.action1024X768.setText("1024 x 768")
        self.menuPilihResolusiMonitor.addAction(self.action1024X768)
        ###
        self.action2880X1620 = QtWidgets.QAction(self.programAplikasiToko)
        self.action2880X1620.setIcon(icon20)
        self.action2880X1620.setObjectName("action2880X1620")
        self.action2880X1620.setText("2880 x 1620")
        self.menuPilihResolusiMonitor.addAction(self.action2880X1620)

    def MenuBar_Tampilan_TemaAplikasi(self):
        self.menuTemaAplikasi = QtWidgets.QMenu(self.menuView)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/Tambah/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuTemaAplikasi.setIcon(icon21)
        self.menuTemaAplikasi.setObjectName("menuTemaAplikasi")
        self.menuTemaAplikasi.setTitle("Tema Aplikasi")
        self.menuView.addAction(self.menuTemaAplikasi.menuAction())
        ###
        self.actionGelap = QtWidgets.QAction(self.programAplikasiToko)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(":/Tambah/write.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGelap.setIcon(icon32)
        self.actionGelap.setObjectName("actionGelap")
        self.actionGelap.setText("Gelap")
        self.menuTemaAplikasi.addAction(self.actionGelap)
        ###
        self.actionTerang = QtWidgets.QAction(self.programAplikasiToko)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(":/Tambah/write 1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTerang.setIcon(icon33)
        self.actionTerang.setObjectName("actionTerang")
        self.actionTerang.setText("Terang")
        self.menuTemaAplikasi.addAction(self.actionTerang)

    def MenuBar_Bantuan(self):
        self.menuBantuan = QtWidgets.QMenu(self.menubar)
        self.menuBantuan.setObjectName("menuBantuan")
        self.menuBantuan.setTitle("Bantuan")
        self.menubar.addAction(self.menuBantuan.menuAction())

    def MenuBar_Bantuan_PanduanPenggunaan(self):
        self.actionPanduanPenggunaan = QtWidgets.QAction(self.programAplikasiToko)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/Tambah/mouse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPanduanPenggunaan.setIcon(icon25)
        self.actionPanduanPenggunaan.setObjectName("actionPanduanPenggunaan")
        self.actionPanduanPenggunaan.setText("Panduan Penggunaan")
        self.menuBantuan.addAction(self.actionPanduanPenggunaan)

    def MenuBar_Bantuan_TentangAplikasi(self):
        self.actionTentangAplikasi = QtWidgets.QAction(self.programAplikasiToko)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/Tambah/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTentangAplikasi.setIcon(icon26)
        self.actionTentangAplikasi.setObjectName("actionTentangAplikasi")
        self.actionTentangAplikasi.setText("Tentang Aplikasi")
        self.menuBantuan.addAction(self.actionTentangAplikasi)

    def MenuBar_NamaUser(self):
        self.menuNamaUser = QtWidgets.QMenu(self.menubar)
        self.menuNamaUser.setObjectName("menuNamaUser")
        self.menubar.addAction(self.menuNamaUser.menuAction())
        self.menuNamaUser.setTitle("Nama User")

    def MenuBar_Execution(self):
        self.MenuBar()  # MenuBar
        self.MenuBar_File()  # MenuBar
        self.MenuBar_File_Keluar()  # MenuBar
        self.MenuBar_File_ShutDown()  # MenuBar
        self.MenuBar_File_Restart()  # MenuBar

        self.MenuBar_User()  # MenuBar
        self.MenuBar_User_Login()  # MenuBar
        self.MenuBar_User_Logout()  # MenuBar
        self.menuUser.addSeparator()  # MenuBar
        self.MenuBar_User_TambahkanPengguna()  # MenuBar
        self.MenuBar_User_RequestLupaPassword()  # MenuBar
        self.MenuBar_User_UbahDataPengguna()  # MenuBar

        self.MenuBar_Tampilan()  # MenuBar
        self.MenuBar_Tampilan_TampilkanMenuSamping()  # MenuBar
        self.MenuBar_Tampilan_TampilkanToolbar()  # MenuBar
        self.MenuBar_Tampilan_PilihResolusiMonitor()  # MenuBar
        self.MenuBar_Tampilan_TemaAplikasi()  # MenuBar

        self.MenuBar_Bantuan()  # MenuBar
        self.MenuBar_Bantuan_PanduanPenggunaan()  # MenuBar
        self.MenuBar_Bantuan_TentangAplikasi()  # MenuBar

        self.MenuBar_NamaUser()  # MenuBar
        self.MenuBar_PERINTAH()

        self.programAplikasiToko.setMenuBar(self.menubar)  # MenuBar

    '''Definition'''
    def MenuBar_DialogShutdown(self):
        ShutdownMessege = QtWidgets.QDialog()
        ShutdownMessege.setWindowFlags(Qt.WindowTitleHint | Qt.WindowStaysOnTopHint)
        ShutdownMessege.setWindowTitle('Konfirmasi Shutdown')
        ShutdownMessege.setModal(True)

        Layout = QtWidgets.QVBoxLayout(ShutdownMessege)

        LabelKonfirmasi = QtWidgets.QLabel('Apakah anda yakin akan mematikan komputer?')
        LabelKonfirmasi.setMinimumSize(0, 100)
        Layout.addWidget(LabelKonfirmasi)

        LayoutTombolKonfirmasi = QtWidgets.QHBoxLayout()
        Layout.addLayout(LayoutTombolKonfirmasi)

        PushButton_Ya = QtWidgets.QPushButton('Ya')
        PushButton_Ya.setMinimumSize(150, 40)
        PushButton_Ya.setMaximumSize(150, 40)
        LayoutTombolKonfirmasi.addWidget(PushButton_Ya)

        PushButton_Tidak = QtWidgets.QPushButton('Tidak')
        PushButton_Tidak.setMinimumSize(150, 40)
        PushButton_Tidak.setMaximumSize(150, 40)
        LayoutTombolKonfirmasi.addWidget(PushButton_Tidak)

        PushButton_Ya.clicked.connect(self.MenuBar_Shutdown)
        PushButton_Tidak.clicked.connect(ShutdownMessege.close)

        ShutdownMessege.show()
        ShutdownMessege.exec_()

    def MenuBar_Shutdown(self):
        os.system("shutdown /s /t 1")

    def MenuBar_DialogRestart(self):
        RestartMessege = QtWidgets.QDialog()
        RestartMessege.setWindowFlags(Qt.WindowTitleHint | Qt.WindowStaysOnTopHint)
        RestartMessege.setObjectName('RestartMessege')
        RestartMessege.setWindowTitle('Konfirmasi Restart')
        RestartMessege.setModal(True)

        Layout = QtWidgets.QVBoxLayout(RestartMessege)

        LabelKonfirmasi = QtWidgets.QLabel('Apakah anda yakin akan merestart komputer?')
        LabelKonfirmasi.setMinimumSize(0, 100)
        Layout.addWidget(LabelKonfirmasi)

        LayoutTombolKonfirmasi = QtWidgets.QHBoxLayout()
        Layout.addLayout(LayoutTombolKonfirmasi)

        PushButton_Ya = QtWidgets.QPushButton('Ya')
        PushButton_Ya.setMinimumSize(150, 40)
        PushButton_Ya.setMaximumSize(150, 40)
        LayoutTombolKonfirmasi.addWidget(PushButton_Ya)

        PushButton_Tidak = QtWidgets.QPushButton('Tidak')
        PushButton_Tidak.setMinimumSize(150, 40)
        PushButton_Tidak.setMaximumSize(150, 40)
        LayoutTombolKonfirmasi.addWidget(PushButton_Tidak)

        PushButton_Ya.clicked.connect(self.MenuBar_Restart)
        PushButton_Tidak.clicked.connect(RestartMessege.close)

        RestartMessege.show()
        RestartMessege.exec_()

    def MenuBar_PERINTAH(self):
        self.actionKeluar.triggered.connect(self.programAplikasiToko.close)
        self.actionShutDown.triggered.connect(self.MenuBar_DialogShutdown)
        self.actionRestart.triggered.connect(self.MenuBar_DialogRestart)

    def MenuBar_Restart(self):
        os.system("shutdown /r /t 1")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = MenuBar()
    objek.MenuBar_Execution()
    objek.programAplikasiToko.show()
    sys.exit(app.exec_())

