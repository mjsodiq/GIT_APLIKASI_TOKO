from PyQt5 import QtCore, QtGui, QtWidgets
from win32api import GetSystemMetrics
from PyQt5.QtCore import QDate, QTime, QTimer
from StyleSheets import *
import Resource_rc
import sys
import os
import pandas as pd
import sqlite3
import math
import sqlite3
import pathlib


def GetParentPath(filePath=os.getcwd):
    path = '{}'.format(os.path.dirname(filePath)).replace('\\','/')
    return path

# Main Directory for Application
MainDir = GetParentPath(GetParentPath(__file__))

def PesanError(tittle, messege):
    App = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMessageBox()
    Dialog.setIcon(QtWidgets.QMessageBox.Warning)
    Dialog.setModal(True)
    Dialog.setWindowTitle(tittle)
    Dialog.setText(messege)
    Dialog.show()
    Dialog.exec_()


def CekResolusi():
    resolution = '{}x{}'.format(GetSystemMetrics(0), GetSystemMetrics(1))
    return resolution


def Font(PixelSize, BoldorNot):
    myFont = QtGui.QFont()
    myFont.setPointSize(PixelSize)
    myFont.setBold(BoldorNot)
    return myFont


def Icon(Icon, Size):
    path = r'{}/Source/Pictures/'.format(MainDir)
    myIcon = QtGui.QIcon(str(path) + str(Icon))
    return myIcon


def IntegerValidator():
    integerValidator = QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]*'))
    return integerValidator


def FloatValidator():
    floatValidator = QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]?([0-9]*[.])?[0-9]+'))  # Jika ada kendala gunakan di bawah
    # floatValidator = QtGui.QDoubleValidator(0, 1000, 2)
    # floatValidator.setNotation(QtGui.QDoubleValidator.StandardNotation)
    return floatValidator


def RoundUp100(price):
    return int(math.ceil(price / 100.0)) * 100


def RoundDown100(price):
    return int(-math.ceil(price / (-100.0))) * 100


def RoundUpAny(Pembulatan, Angka=0):
    Hasil = (Angka % Pembulatan)
    if Hasil > 0:
        Pembulatan2 = Pembulatan - Hasil
        Hasil2 = Angka + Pembulatan2
    else:
        Hasil2 = Angka
    return int(Hasil2)


def RoundDownAny(Pembulatan, Angka=0):
    Hasil = (Angka % Pembulatan)
    if Hasil > 0:
        Hasil2 = Angka - Hasil
    else:
        Hasil2 = Angka
    return int(Hasil2)


def RoundTerdekat(Pembulatan, Angka=0):
    BatasTengah = Pembulatan / 2
    Hasil = (Angka % Pembulatan)

    if Hasil < BatasTengah:
        Hasil2 = RoundDownAny(Pembulatan, Angka)
    else:
        Hasil2 = RoundUpAny(Pembulatan, Angka)
    return int(Hasil2)


def RoundAll(Angka=0):
    Batas1 = 50000
    Pembulatan1 = 500

    Batas2 = 10000
    Pembulatan2 = 200

    Batas3 = 1000
    Pembulatan3 = 100

    Batas4 = 200
    Pembulatan4 = 50

    Batas5 = 0
    Pembulatan5 = 25

    if Angka > Batas1:
        Hasil = RoundTerdekat(Pembulatan1, Angka)
        if Hasil < Angka:
            Hasil2 = RoundUpAny(Pembulatan1, Angka)
        else:
            Hasil2 = Hasil
    elif Angka > Batas2:
        Hasil = RoundTerdekat(Pembulatan2, Angka)
        if Hasil < Angka:
            Hasil2 = RoundUpAny(Pembulatan2, Angka)
        else:
            Hasil2 = Hasil
    elif Angka > Batas3:
        Hasil = RoundTerdekat(Pembulatan3, Angka)
        if Hasil < Angka:
            Hasil2 = RoundUpAny(Pembulatan3, Angka)
        else:
            Hasil2 = Hasil
    elif Angka > Batas4:
        Hasil = RoundTerdekat(Pembulatan4, Angka)
        if Hasil < Angka:
            Hasil2 = RoundUpAny(Pembulatan4, Angka)
        else:
            Hasil2 = Hasil
    elif Angka > Batas5:
        Hasil = RoundTerdekat(Pembulatan5, Angka)
        if Hasil < Angka:
            Hasil2 = RoundUpAny(Pembulatan5, Angka)
        else:
            Hasil2 = Hasil

    return Hasil2


def GetKeyFromDictionariesItem(val, ListOfDictItems):
    for key, value in ListOfDictItems:
        if val == value:
            return key


def DatabaseProduk():
    Produk_Path = r"{}/Data/Produk/Data_Produk_Master.db".format(MainDir)
    return Produk_Path


def DatabaseShopee():
    Produk_Path = r"{}/Data/Produk/DataUploadShopee.db".format(MainDir)
    return Produk_Path


def ExcellDanaToko():
    Path = r'{}/Data/Analisa/Uang_Cash_Di_Toko.xlsx'.format(MainDir)
    return Path


def DatabaseBlacklistProduk():
    BlackListProduk_Path = r"{}/Data/Produk/BlackListOrder.db".format(MainDir)
    return BlackListProduk_Path


def DatabaseKatalogProdukDanDistributor():
    KatalogProdukDanDistributor_Path = r"{}/Data/Produk/Katalog_Produk_Distributor.db".format(MainDir)
    return KatalogProdukDanDistributor_Path


class CommunicationSignal(QtCore.QObject):
    signalLoginSukses = QtCore.pyqtSignal(str, str)
    def __init__(self):
        super(CommunicationSignal, self).__init__()

    def SignalLoginSukses(self):
        self.signalLoginSukses.emit('', '')


class Ui_ProgramAplikasiToko(object):
    def __init__(self):
        super(Ui_ProgramAplikasiToko, self).__init__()
        self.Communication = CommunicationSignal()
        self.Execution()
        self.File_SystemLog()
        self.File_TransactionLog()
        self.File_TransaksiTokoTerkonfirmasiLog()

    def Resources(self):
        # DATA UMUM
        self.PathPictures = r'{}/Source/Pictures/'.format(MainDir)

        # DATABASE USER
        self.UserDatabase = r'{}/Data/User/toko_username.sqlite'.format(MainDir)

        # DATA LOG Untuk Editing
        self.LOG = r'{}/Data/LOG/LOGSystem'.format(MainDir)
        self.systemLOG = self.LOG + r'/SystemLOG'
        self.TransactionLOG = self.LOG + r'/TransactionLOG'
        self.TransaksiTokoTerkonfirmasiLOG = self.LOG + r'/TransaksiTokoTerkonfirmasiLOG'
        self.column_SystemLog = ['Tanggal', 'Waktu', 'Nama Pengguna', 'Event']
        self.column_TransactionLog = ['Tanggal', 'Waktu', 'Nama Pengguna', 'Event', 'Jenis Transaki', 'Nilai']
        self.column_TransaksiTokoTerkonfirmasi = ['Tanggal', 'Waktu', 'Nomor Transaksi', 'Nama Kasir', 'Event', 'Nilai', 'Lokasi Penyimpanan Bukti Transaksi']

        # DATA LOG Untuk Dibuka
        self.LOG_User = r'{}/Data/LOG/LOGUser'.format(MainDir)

        # DATA LOGIN
        self.username = []
        self.kelas = []

        # DATA WAKTU
        self.dateNow = QDate.currentDate().toString('dd')
        self.monthNow1 = QDate.currentDate().toString('MM')
        self.monthNow2 = QDate.currentDate().toString('MMMM')
        self.yearNow = QDate.currentDate().toString('yyyy')
        self.clockNow = QTime.currentTime().toString('hh')
        self.minuteNow = QTime.currentTime().toString('mm')
        self.secondNow = QTime.currentTime().toString('ss')

    def File_SystemLog(self):
        folderTahun = self.systemLOG + r'/{}'.format(self.yearNow)
        folderBulan = folderTahun + r'/{}. {}'.format(self.monthNow1, self.monthNow2)
        folderTanggal = folderBulan + r'/{}-{}-{}'.format(self.dateNow, self.monthNow2, self.yearNow)
        self.file_SystemLOG = folderTanggal + r'/{}-{}-{} (system Log).csv'.format(self.dateNow, self.monthNow2, self.yearNow)

        # Buat File SystemLog
        try:
            os.mkdir(self.LOG)
            # Buat Folder 'LOG'
            os.mkdir(self.systemLOG)
            # Buat Folder 'Tahun'
            os.mkdir(folderTahun)
            # Buat Folder 'Bulan'
            os.mkdir(folderBulan)
            # Buat Folder 'Tanggal'
            os.mkdir(folderTanggal)
            # Buat File CSV
            self.Buat_File_SystemLOG()
        except:
            try:
                # Buat Folder 'LOG'
                os.mkdir(self.systemLOG)
                # Buat Folder 'Tahun'
                os.mkdir(folderTahun)
                # Buat Folder 'Bulan'
                os.mkdir(folderBulan)
                # Buat Folder 'Tanggal'
                os.mkdir(folderTanggal)
                # Buat File CSV
                self.Buat_File_SystemLOG()
            except:
                try:
                    # Buat Folder 'Tahun'
                    os.mkdir(folderTahun)
                    # Buat Folder 'Bulan'
                    os.mkdir(folderBulan)
                    # Buat Folder 'Tanggal'
                    os.mkdir(folderTanggal)
                    # Buat File CSV
                    self.Buat_File_SystemLOG()
                except:
                    try:
                        # Buat Folder 'Bulan'
                        os.mkdir(folderBulan)
                        # Buat Folder 'Tanggal'
                        os.mkdir(folderTanggal)
                        # Buat File CSV
                        self.Buat_File_SystemLOG()
                    except:
                        try:
                            # Buat Folder 'Tanggal'
                            os.mkdir(folderTanggal)
                            # Buat File CSV
                            self.Buat_File_SystemLOG()
                        except:
                            try:
                                # Buat File CSV
                                self.Buat_File_SystemLOG()
                            except:
                                pass
            return self.file_SystemLOG

    def Buat_File_SystemLOG(self):
        cekExistingFile = os.path.isfile(self.file_SystemLOG)
        if cekExistingFile:
            pass
        else:
            Tanggal = '{}-{}-{}'.format(self.dateNow, self.monthNow2, self.yearNow)
            Waktu = '{}:{}:{}'.format(self.clockNow, self.minuteNow, self.secondNow)
            Username = 'Admin Pandan Arum'
            Event = 'File System LOG dibuat'
            self.data_SystemLog = [Tanggal, Waktu, Username, Event]
            df = pd.DataFrame([self.data_SystemLog], index=None, columns=self.column_SystemLog).to_csv(self.file_SystemLOG, index=0)

    def CreateEventSystemLOG(self, username, event):
        # Inisiasi
        self.Resources()
        username = username
        event = event
        folderTahun = self.systemLOG + r'/{}'.format(self.yearNow)
        folderBulan = folderTahun + r'/{}. {}'.format(self.monthNow1, self.monthNow2)
        folderTanggal = folderBulan + r'/{}-{}-{}'.format(self.dateNow, self.monthNow2, self.yearNow)
        self.file_SystemLOG = folderTanggal + r'/{}-{}-{} (system Log).csv'.format(self.dateNow, self.monthNow2, self.yearNow)
        Tanggal = '{}-{}-{}'.format(self.dateNow, self.monthNow2, self.yearNow)
        Waktu = '{}:{}:{}'.format(self.clockNow, self.minuteNow, self.secondNow)

        # Tambahkan ke Excell
        try:
            data = [[Tanggal, Waktu, username, event]]
            df = pd.DataFrame(data, columns=self.column_SystemLog)
            df.to_csv(self.file_SystemLOG, header=None, mode='a', index=0)
        except:
            pass

    def File_TransactionLog(self):
        folderTahun = self.TransactionLOG + r'/{}'.format(self.yearNow)
        folderBulan = folderTahun + r'/{}. {}'.format(self.monthNow1, self.monthNow2)
        folderTanggal = folderBulan + r'/{}-{}-{}'.format(self.dateNow, self.monthNow2, self.yearNow)
        self.file_TransactionLOG = folderTanggal + r'/{}-{}-{} (Transaction Log).csv'.format(self.dateNow, self.monthNow2, self.yearNow)

        # Buat File SystemLog
        try:
            os.mkdir(self.LOG)
            # Buat Folder 'LOG'
            os.mkdir(self.TransactionLOG)
            # Buat Folder 'Tahun'
            os.mkdir(folderTahun)
            # Buat Folder 'Bulan'
            os.mkdir(folderBulan)
            # Buat Folder 'Tanggal'
            os.mkdir(folderTanggal)
            # Buat File CSV
            self.Buat_File_TransactionLOG()
        except:
            try:
                # Buat Folder 'LOG'
                os.mkdir(self.TransactionLOG)
                # Buat Folder 'Tahun'
                os.mkdir(folderTahun)
                # Buat Folder 'Bulan'
                os.mkdir(folderBulan)
                # Buat Folder 'Tanggal'
                os.mkdir(folderTanggal)
                # Buat File CSV
                self.Buat_File_TransactionLOG()
            except:
                try:
                    # Buat Folder 'Tahun'
                    os.mkdir(folderTahun)
                    # Buat Folder 'Bulan'
                    os.mkdir(folderBulan)
                    # Buat Folder 'Tanggal'
                    os.mkdir(folderTanggal)
                    # Buat File CSV
                    self.Buat_File_TransactionLOG()
                except:
                    try:
                        # Buat Folder 'Bulan'
                        os.mkdir(folderBulan)
                        # Buat Folder 'Tanggal'
                        os.mkdir(folderTanggal)
                        # Buat File CSV
                        self.Buat_File_TransactionLOG()
                    except:
                        try:
                            # Buat Folder 'Tanggal'
                            os.mkdir(folderTanggal)
                            # Buat File CSV
                            self.Buat_File_TransactionLOG()
                        except:
                            try:
                                # Buat File CSV
                                self.Buat_File_TransactionLOG()
                            except:
                                pass
            return self.file_SystemLOG

    def Buat_File_TransactionLOG(self):
        cekExistingFile = os.path.isfile(self.file_TransactionLOG)
        if cekExistingFile:
            pass
        else:
            Tanggal = '{}-{}-{}'.format(self.dateNow, self.monthNow2, self.yearNow)
            Waktu = '{}:{}:{}'.format(self.clockNow, self.minuteNow, self.secondNow)
            NamaPengguna = 'Admin Pandan Arum'
            Event = 'File Transaction LOG dibuat'
            JenisTransaksi = ''
            Nilai = ''
            self.data_TransactionLog = [Tanggal, Waktu, NamaPengguna, Event, JenisTransaksi, Nilai]
            df = pd.DataFrame([self.data_TransactionLog], index=None, columns=self.column_TransactionLog).to_csv(self.file_TransactionLOG, index=0)

    def CreateEventTransactionLOG(self, username, event, jenisTransaksi, nilai):
        # Inisiasi
        self.Resources()
        username = username
        event = event
        jenisTransaksi = jenisTransaksi
        nilai = nilai
        folderTahun = self.TransactionLOG + r'/{}'.format(self.yearNow)
        folderBulan = folderTahun + r'/{}. {}'.format(self.monthNow1, self.monthNow2)
        folderTanggal = folderBulan + r'/{}-{}-{}'.format(self.dateNow, self.monthNow2, self.yearNow)
        self.file_TransactionLOG = folderTanggal + r'/{}-{}-{} (Transaction Log).csv'.format(self.dateNow, self.monthNow2, self.yearNow)
        Tanggal = '{}-{}-{}'.format(self.dateNow, self.monthNow2, self.yearNow)
        Waktu = '{}:{}:{}'.format(self.clockNow, self.minuteNow, self.secondNow)

        # Tambahkan ke EXCELL
        try:
            data = [[Tanggal, Waktu, username, event, jenisTransaksi, nilai]]
            df = pd.DataFrame(data, columns=self.column_TransactionLog)
            df.to_csv(self.file_TransactionLOG, header=None, mode='a', index=0)
        except:
            pass

    def File_TransaksiTokoTerkonfirmasiLog(self):
        folderTahun = self.TransaksiTokoTerkonfirmasiLOG + r'/{}'.format(self.yearNow)
        folderBulan = folderTahun + r'/{}. {}'.format(self.monthNow1, self.monthNow2)
        folderTanggal = folderBulan + r'/{}-{}-{}'.format(self.dateNow, self.monthNow2, self.yearNow)
        self.file_TransaksiTokoTerkonfirmasiLOG = folderTanggal + r'/{}-{}-{} (TransaksiTokoTerkonfirmasiLOG).csv'.format(self.dateNow, self.monthNow2, self.yearNow)

        # Buat File SystemLog
        try:
            os.mkdir(self.LOG)
            # Buat Folder 'LOG'
            os.mkdir(self.TransaksiTokoTerkonfirmasiLOG)
            # Buat Folder 'Tahun'
            os.mkdir(folderTahun)
            # Buat Folder 'Bulan'
            os.mkdir(folderBulan)
            # Buat Folder 'Tanggal'
            os.mkdir(folderTanggal)
            # Buat File CSV
            self.Buat_File_TransaksiTokoTerkonfirmasiLOG()
        except:
            try:
                # Buat Folder 'LOG'
                os.mkdir(self.TransaksiTokoTerkonfirmasiLOG)
                # Buat Folder 'Tahun'
                os.mkdir(folderTahun)
                # Buat Folder 'Bulan'
                os.mkdir(folderBulan)
                # Buat Folder 'Tanggal'
                os.mkdir(folderTanggal)
                # Buat File CSV
                self.Buat_File_TransaksiTokoTerkonfirmasiLOG()
            except:
                try:
                    # Buat Folder 'Tahun'
                    os.mkdir(folderTahun)
                    # Buat Folder 'Bulan'
                    os.mkdir(folderBulan)
                    # Buat Folder 'Tanggal'
                    os.mkdir(folderTanggal)
                    # Buat File CSV
                    self.Buat_File_TransaksiTokoTerkonfirmasiLOG()
                except:
                    try:
                        # Buat Folder 'Bulan'
                        os.mkdir(folderBulan)
                        # Buat Folder 'Tanggal'
                        os.mkdir(folderTanggal)
                        # Buat File CSV
                        self.Buat_File_TransaksiTokoTerkonfirmasiLOG()
                    except:
                        try:
                            # Buat Folder 'Tanggal'
                            os.mkdir(folderTanggal)
                            # Buat File CSV
                            self.Buat_File_TransaksiTokoTerkonfirmasiLOG()
                        except:
                            try:
                                # Buat File CSV
                                self.Buat_File_TransaksiTokoTerkonfirmasiLOG()
                            except:
                                pass
            return self.file_TransaksiTokoTerkonfirmasiLOG

    def Buat_File_TransaksiTokoTerkonfirmasiLOG(self):
        cekExistingFile = os.path.isfile(self.file_TransaksiTokoTerkonfirmasiLOG)
        if cekExistingFile:
            pass
        else:
            Tanggal = '{}-{}-{}'.format(self.dateNow, self.monthNow2, self.yearNow)
            Waktu = '{}:{}:{}'.format(self.clockNow, self.minuteNow, self.secondNow)
            NomorTransaksi = ''
            NamaKasir = 'Admin Pandan Arum'
            Event = 'File TransaksiTokoTerkonfirmasiLOG dibuat'
            Nilai = ''
            LokasiPenyimpananBuktiTransaksi = ''
            self.data_TransaksiTokoTerkonfirmasiLog = [Tanggal, Waktu, NomorTransaksi, NamaKasir, Event, Nilai, LokasiPenyimpananBuktiTransaksi]
            df = pd.DataFrame([self.data_TransaksiTokoTerkonfirmasiLog], index=None, columns=self.column_TransaksiTokoTerkonfirmasi).to_csv(self.file_TransaksiTokoTerkonfirmasiLOG, index=0)

    def CreateEventTransaksiTokoTerkonfirmasiLOG(self, nomorTransaksi, username, event, nilai):
        # Inisiasi
        self.Resources()
        nomorTransaksi = nomorTransaksi
        username = username
        event = event
        nilai = nilai

        folderTahun = self.TransaksiTokoTerkonfirmasiLOG + r'/{}'.format(self.yearNow)
        folderBulan = folderTahun + r'/{}. {}'.format(self.monthNow1, self.monthNow2)
        folderTanggal = folderBulan + r'/{}-{}-{}'.format(self.dateNow, self.monthNow2, self.yearNow)
        folderLokasiPenyimpanan = folderTanggal + r'/{}'.format(nomorTransaksi)
        self.lokasiPenyimpananBuktiTransaksi = folderLokasiPenyimpanan
        self.file_TransaksiTokoTerkonfirmasiLOG = folderTanggal + r'/{}-{}-{} (TransaksiTokoTerkonfirmasiLOG).csv'.format(self.dateNow, self.monthNow2, self.yearNow)
        Tanggal = '{}-{}-{}'.format(self.dateNow, self.monthNow2, self.yearNow)
        Waktu = '{}:{}:{}'.format(self.clockNow, self.minuteNow, self.secondNow)

        # Tambahkan ke EXCELL
        try:
            data = [[Tanggal, Waktu, nomorTransaksi, username, event, nilai, self.lokasiPenyimpananBuktiTransaksi]]
            df = pd.DataFrame(data, columns=self.column_TransaksiTokoTerkonfirmasi)
            df.to_csv(self.file_TransaksiTokoTerkonfirmasiLOG, header=None, mode='a', index=0)
        except:
            pass

    def ProgramAplikasiToko(self):
        self.programAplikasiToko = QtWidgets.QMainWindow()
        self.programAplikasiToko.setObjectName("ProgramAplikasiToko")
        self.programAplikasiToko.setWindowModality(QtCore.Qt.NonModal)
        self.programAplikasiToko.resize(1439, 758)
        self.programAplikasiToko.setWindowTitle("Produseno Aplikasi Toko")

    def Centralwidget(self):
        self.centralwidget = QtWidgets.QWidget(self.programAplikasiToko)
        self.centralwidget.setObjectName("centralwidget")
        self.programAplikasiToko.setCentralWidget(self.centralwidget)

    def GridLayout_2(self):
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

    def Utama_GridLayout(self):
        self.utama_GridLayout = QtWidgets.QGridLayout()
        self.utama_GridLayout.setObjectName("UTAMA_GridLayout")
        self.gridLayout_2.addLayout(self.utama_GridLayout, 0, 0, 1, 1)

    def Utama_VerticalLayout(self):
        self.utama_VerticalLayout = QtWidgets.QVBoxLayout()
        self.utama_VerticalLayout.setObjectName("UTAMA_VerticalLayout")
        self.utama_GridLayout.addLayout(self.utama_VerticalLayout, 0, 0, 1, 1)

    def Tab_UTAMA(self):
        self.tab_UTAMA = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_UTAMA.setFont(Font(8, True))
        self.tab_UTAMA.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_UTAMA.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_UTAMA.setElideMode(QtCore.Qt.ElideNone)
        self.tab_UTAMA.setDocumentMode(False)
        self.tab_UTAMA.setTabsClosable(False)
        self.tab_UTAMA.setMovable(False)
        self.tab_UTAMA.setTabBarAutoHide(False)
        self.tab_UTAMA.setObjectName("TAB_UTAMA")
        self.utama_VerticalLayout.addWidget(self.tab_UTAMA)
        self.tab_UTAMA.setStyleSheet(TabStyleSheet4(CekResolusi()))
        self.tab_UTAMA.setCurrentIndex(0)

    def endOfSetup(self):
        QtCore.QMetaObject.connectSlotsByName(self.programAplikasiToko)

    def Execution(self):
        self.Resources()
        self.ProgramAplikasiToko()

        # TAB UTAMA
        self.Centralwidget()  #                             TAB Utama
        self.GridLayout_2()  #                              TAB Utama
        self.Utama_GridLayout()  #                          TAB Utama
        self.Utama_VerticalLayout()  #                      TAB Utama
        self.Tab_UTAMA()  #                                 TAB Utama
        self.endOfSetup()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    ui = Ui_ProgramAplikasiToko()
    ui.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())

