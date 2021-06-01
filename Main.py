import os
import sys


# 1. Masukkan Paket yang berisi modul yang kita ingin import ke dalam path, agar mudah diimport
[print("item syspath 1 : ", item) for item in sys.path]
Directory = []
Directory_to_Ignore = ["__pycache__", ".git", "Temp"]
DirectoryItem = os.listdir(os.getcwd())
for item in DirectoryItem:
    if item in Directory_to_Ignore:
        pass
    elif os.path.isdir(r'{}\{}'.format(os.getcwd(), item)):
        Directory.append(item)
        sys.path.append(r'{}\{}'.format(os.getcwd(), item))
    else:
        pass
[print("item syspath 2 : ", item) for item in sys.path]
# .1 Akhir dari 1

from Module import *

class PageExecution(Page0, Page1, Page2, Page3, Page4, Page5, Page6, Page7, Page8, Page9, Page10, Page11, Page12, Page13, Page14, Page15, Page16, Page17, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(PageExecution, self).__init__()

        self.PageExecution_Execution()
        # self.programAplikasiToko.setWindowFlags(Qt.WindowTitleHint | Qt.WindowMaximizeButtonHint)
        self.programAplikasiToko.showMaximized()
        sys.exit(app.exec_())

    def Page0_Execution_PERINTAH(self):
        self.pushButton_13.clicked.connect(self.KlikTombolLogout)
        self.tab_UTAMA.currentChanged.connect(self.EventTabUtamaTabChange)
        pass

    def PageExecution_Execution(self):
        # PERINTAH DI TAB 0
        Page0.Page0_Execution(self)
        self.Communication.signalLoginSukses.connect(self.SetelahLoginSukses)
        self.page0_pushButton.click()

    def KlikTombolLogout(self):
        # Tombol Logout
        try:
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab1))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab2))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab3))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab4))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab5))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab6))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab7))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab8))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab9))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab10))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab11))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab12))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab13))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab14))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab15))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab16))
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab17))
            self.tab_UTAMA.addTab(self.tab0, QtGui.QIcon(), 'Login')
        except:
            print("PageExecution.py said : def KlikTombolLogout(self): Gagal")
            pass

    QtCore.pyqtSlot()
    def SetelahLoginSukses(self):
        username = self.page0_lineEdit.text()
        nama = self.page0_UserDatabase_cursor.execute('SELECT Nama FROM USER WHERE "username"="{}"'.format(username)).fetchone()[0]
        kelas = self.page0_UserDatabase_cursor.execute('SELECT kelas FROM USER WHERE "username"="{}"'.format(username)).fetchone()[0]

        if kelas == 'super':
            # Page0 Widget = self.tab0 (Login)
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab0))
            # Page1 Widget = self.tab1 (Aplikasi Kasir)
            Page1.Page1_Execution(self, nama, kelas)
            # Page2 Widget = self.tab2 (Atur Pengguna)
            Page2.Page2_Execution(self, nama, kelas)
            # Page3 Widget = self.tab3 (Atur Stok)
            Page3.Page3_Execution(self, nama, kelas)
            # Page4 Widget = self.tab4 (Marketplace)
            Page4.Page4_Execution(self, nama, kelas)
            # Page5 Widget = self.tab5 (LOG)
            Page5.Page5_Execution(self, nama, kelas)
            # Page6 Widget = self.tab6 (Analisis)
            Page6.Page6_Execution(self, nama, kelas)
            # Page7 Widget = self.tab7 (Pengaturan)
            Page7.Page7_Execution(self, nama, kelas)
            # Page8 Widget = self.tab8 (Page 1)
            Page8.Page8_Execution(self, nama, kelas)
            # Page9 Widget = self.tab9 (Page 2)
            Page9.Page9_Execution(self, nama, kelas)
            # Page10 Widget = self.tab10 (Page 3)
            Page10.Page10_Execution(self, nama, kelas)
            # Page11 Widget = self.tab11 (Page 4)
            Page11.Page11_Execution(self, nama, kelas)
            # Page12 Widget = self.tab12 (Page 5)
            Page12.Page12_Execution(self, nama, kelas)
            # Page13 Widget = self.tab13 (Page 6)
            Page13.Page13_Execution(self, nama, kelas)
            # Page14 Widget = self.tab14 (Page 7)
            Page14.Page14_Execution(self, nama, kelas)
            # Page15 Widget = self.tab15 (Page 8)
            Page15.Page15_Execution(self, nama, kelas)
            # Page16 Widget = self.tab16 (Page 9)
            Page16.Page16_Execution(self, nama, kelas)
            # Page17 Widget = self.tab17 (Page 10)
            Page17.Page17_Execution(self, nama, kelas)

        elif kelas == 'admin':
            # Page0 Widget = self.tab0 (Login)
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab0))
            # Page1 Widget = self.tab1 (Aplikasi Kasir)
            Page1.Page1_Execution(self, nama, kelas)
            # Page3 Widget = self.tab3 (Atur Stok)
            Page3.Page3_Execution(self, nama, kelas)
            # Page5 Widget = self.tab5 (LOG)
            Page5.Page5_Execution(self, nama, kelas)

        elif kelas == 'karyawan':
            # Page0 Widget = self.tab0 (Login)
            self.tab_UTAMA.removeTab(self.tab_UTAMA.indexOf(self.tab0))
            # Page1 Widget = self.tab1 (Aplikasi Kasir)
            Page1.Page1_Execution(self, nama, kelas)

        else:
            pass
        self.Page0_Execution_PERINTAH()
        #self.programAplikasiToko.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTitleHint)
        self.programAplikasiToko.showNormal()
        self.programAplikasiToko.showMaximized()

    def EventTabUtamaTabChange(self):
        try:
            self.page3_pushButton_3.click() # tombol reload database di page 3, tab semua item
        except:
            print("PageExecution.py said: def EventTabUtamaTabChange(self): Gagal")
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = PageExecution()
