import sqlite3
import shutil
import time
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate, QTime, QTimer
from escpos.printer import Usb
from escpos import *
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from openpyxl import load_workbook
from PIL import Image, ImageDraw, ImageFont

# 1. Masukkan Paket yang berisi modul yang kita ingin import ke dalam path, agar mudah diimport
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
# .1 Akhir dari 1

from Module import *


class Page1(MenuBar, Ui_ProgramAplikasiToko):
    pelanggan = 0
    def __init__(self):
        super(Page1, self).__init__()
        # self.programAplikasiToko.resize(2100, 800)
        self.Bayar = []
        self.Kembalian = []
        self.MetodePembayaran = ["Tunai"]
        self.RekeningBankDimiliki = ["BCA", "Mandiri", "Bank Jatim"]
        self.MesinEDCDimiliki = ["BCA"]
        self.QRIZ = ["Mandiri"]

    # Buka koneksi database
    def Page1_Database(self):
        self.page1_DBConnection = sqlite3.connect(DatabaseProduk())
        self.page1_DBConnection.row_factory = sqlite3.Row
        self.page1_DBCursor = self.page1_DBConnection.cursor()

    def Page1_Update_ExpiredDate(self):
        conn = sqlite3.connect(DatabaseProduk())
        conn.row_factory = sqlite3.Row
        curr = conn.cursor()
        perintahTable = curr.execute("select name from sqlite_master where type='table' order by name").fetchall()
        table = [perintahTable[item][0] for item in range(len(perintahTable)) if perintahTable[item][0] != "Data_Produk_Master"]

        for tableItem in table:
            ExpiredDate_to_No = {}
            ExpiredDate_to_Barcode = {}
            Barcode_to_ExpiredDate = {}
            Barcode_to_No = {}
            ExpiredDate_List = []
            ED = curr.execute("select No,Expired_Date from '{}' where Total_Stok_Sekarang > 0".format(tableItem)).fetchall()
            if len(ED) < 1:
                pass
            else:
                for item2 in range(len(ED)):
                    kode = tableItem
                    No = ED[item2]["No"]
                    Exp = ED[item2]["Expired_Date"]
                    ExpiredDate_List.append(Exp)
                    ExpiredDate_List.sort()
                    ED_to_No = {Exp: No}
                    ExpiredDate_to_No.update(ED_to_No)
                    ED_to_Barcode = {Exp: kode}
                    ExpiredDate_to_Barcode.update(ED_to_Barcode)
                Barcode_to_ED = {tableItem: ExpiredDate_List[0]}
                Barcode_to_ExpiredDate.update(Barcode_to_ED)
                Barcode_to_no = {tableItem: ExpiredDate_to_No[ExpiredDate_List[0]]}
                Barcode_to_No.update(Barcode_to_no)
        conn.close()

    def Page1_PrinterConnection(self):
        try:
            self.MyPrinter = Usb(0x0483, 0x5840, 0, 0x58, 0x03)
        except:
            Dialog = QtWidgets.QMessageBox()
            Dialog.setWindowFlags(Qt.WindowTitleHint | Qt.WindowStaysOnTopHint)
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setWindowTitle('Printer')
            Dialog.setText('Printer tidak terdeteksi, nyalakan printer dan pastikan '
                           'semua kabel telah terpasang dengan benar')
            Dialog.setModal(True)
            Dialog.show()
            Dialog.exec_()
            pass

    def Tab1(self):
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("Tab1")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Tambah/116-1169669_png-shopping-cart-free-icon.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.tab_UTAMA.addTab(self.tab1, icon7, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab1), "Aplikasi Kasir")

    def Page1_GridLayout_5(self):
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout_5.setObjectName("gridLayout_5")

    def Page1_Tab1_GridLayout(self):
        self.tab1_GridLayout = QtWidgets.QGridLayout()
        self.tab1_GridLayout.setObjectName("Tab1_GridLayout")
        self.gridLayout_5.addLayout(self.tab1_GridLayout, 0, 0, 1, 1)

    def Page1_Tab1_TabAnak1(self):
        self.tab1_TabAnak1 = QtWidgets.QTabWidget(self.tab1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab1_TabAnak1.setFont(font)
        self.tab1_TabAnak1.setUsesScrollButtons(True)
        self.tab1_TabAnak1.setDocumentMode(False)
        self.tab1_TabAnak1.setTabsClosable(False)
        self.tab1_TabAnak1.setMovable(False)
        self.tab1_TabAnak1.setTabBarAutoHide(False)
        self.tab1_TabAnak1.setObjectName("Tab1_TabAnak1")
        self.tab1_GridLayout.addWidget(self.tab1_TabAnak1, 0, 0, 1, 1)
        self.tab1_TabAnak1.setStyleSheet(TabStyleSheet3(CekResolusi()))
        self.tab1_TabAnak1.setCurrentIndex(0)

    def Page1_Tab1_TabAnak1_Tab1(self):
        self.tab1_TabAnak1_Tab1 = QtWidgets.QWidget()
        self.tab1_TabAnak1_Tab1.setObjectName("Tab1_TabAnak1_Tab1")
        self.tab1_TabAnak1.addTab(self.tab1_TabAnak1_Tab1, "")
        self.tab1_TabAnak1.setTabText(self.tab1_TabAnak1.indexOf(self.tab1_TabAnak1_Tab1), "Transaksi")

    def Page1_GridLayout_3(self):
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab1_TabAnak1_Tab1)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")

    def Page1_Frame(self):
        self.frame = QtWidgets.QFrame()
        self.frame.setFont(Font(9, True))
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet('background-color: black; color: white;')
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 3)

    def Page1_GridLayout_9(self):
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_9.setObjectName("gridLayout_9")

    def Page1_Label_35(self):
        # Label Pengguna, atas
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setText('Pengguna : ')
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.gridLayout_9.addWidget(self.label_35, 0, 4, 1, 1)

    def Page1_Label_36(self):
        self.label_36 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.gridLayout_9.addWidget(self.label_36, 0, 5, 1, 1)
        self.label_36.setText('Muhammad Ja\'far Sodiq')
        self.label_36.setText('Nama Kasir')

    def Page1_Label_34(self):
        self.label_34 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout_9.addWidget(self.label_34, 0, 2, 1, 1)
        self.label_34.setText('00:00')

    def Page1_Label_33(self):
        self.label_33 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout_9.addWidget(self.label_33, 0, 1, 1, 1)
        self.label_33.setText('-')

    def Page1_Label_32(self):
        # Label Tanggal
        self.label_32 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gridLayout_9.addWidget(self.label_32, 0, 0, 1, 1)
        self.label_32.setText(
            '{}, {} {} {}'.format(self.page1_HariSekarang, self.page1_TanggalSekarang, self.page1_BulanSekarang,
                                  self.page1_TahunSekarang))

    def Page1_SpacerItem(self):
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem, 0, 3, 1, 1)

    def Page1_PushButton_13(self):
        # Tombol Logout
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setFont(Font(9, False))
        self.pushButton_13.setStyleSheet("background-color: rgb(0, 85, 0);\ncolor: rgb(211, 211, 211);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.setText("Logout")
        self.pushButton_13.setMinimumSize(150, 50)
        self.pushButton_13.setStyleSheet(ButtonStyleSheets1(CekResolusi()))
        self.gridLayout_9.addWidget(self.pushButton_13, 0, 6, 1, 1)

    def Page1_HorizontalLayout_1(self):
        self.page1_horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.gridLayout_3.addLayout(self.page1_horizontalLayout_1, 1, 0, 1, 3)

    def Page1_Frame_3(self):
        self.frame_3 = QtWidgets.QFrame(self.tab1_TabAnak1_Tab1)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setStyleSheet(FrameStyleSheets1(CekResolusi()))
        self.page1_horizontalLayout_1.addWidget(self.frame_3, 2)

    def Page1_FormLayout_6(self):
        self.formLayout_6 = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout_6.setObjectName("formLayout_6")

    def Page1_FormLayout_4(self):
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.formLayout_6.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.formLayout_4)

    def Page1_Label_41(self):
        self.label_41 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label_41.setText('Transaksi : ')
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_41)

    def Page1_Label_43(self):
        self.label_43 = QtWidgets.QLabel(self.frame_3)
        self.label_43.setFont(Font(9, False))
        self.label_43.setObjectName("label_43")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_43)
        self.label_43.setText('Diskon Khusus : ')

    def Page1_Label_45(self):
        self.label_45 = QtWidgets.QLabel(self.frame_3)
        self.label_45.setFont(Font(9, False))
        self.label_45.setObjectName("label_45")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_45)
        self.label_45.setText('TOTAL : ')

    def Page1_HorizontalLayout_8(self):
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.formLayout_4.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)

    def Page1_SpacerItem1(self):
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)

    def Page1_Label_49(self):
        self.label_49 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_49.setObjectName("label_49")
        self.horizontalLayout_8.addWidget(self.label_49)
        self.label_49.setText('Rp. ')

    def Page1_Label_50(self):
        self.label_50 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_50.setObjectName("label_50")
        self.horizontalLayout_8.addWidget(self.label_50)
        self.label_50.setText('000.000.000')

    def Page1_Label_51(self):
        self.label_51 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_8.addWidget(self.label_51)
        self.label_51.setText(',-')

    def Page1_Label_37(self):
        self.label_37 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_37)
        self.label_37.setText('TOTAL TRANSAKSI')

    def Page1_LineEdit_25(self):
        self.page1_ComboBox = QtWidgets.QComboBox(self.frame_3)
        self.MesinEDCDimiliki = ["BCA"]
        self.QRIZ = ["Mandiri"]
        if len(self.RekeningBankDimiliki) > 0:
            for rekeningBank in self.RekeningBankDimiliki:
                text1 = "Transfer Bank Sesama {}".format(rekeningBank)
                text2 = "Transfer Bank Lain ke rekening {} toko".format(rekeningBank)
                self.MetodePembayaran.append(text1)
                self.MetodePembayaran.append(text2)
        else:
            pass

        if len(self.MesinEDCDimiliki) > 0:
            for mesinEDC in self.MesinEDCDimiliki:
                text1 = "Transaksi kartu {} dengan EDC-{}".format(mesinEDC, mesinEDC)
                text2 = "Transaksi kartu selain {} dengan EDC-{}".format(mesinEDC, mesinEDC)
                self.MetodePembayaran.append(text1)
                self.MetodePembayaran.append(text2)
        else:
            pass

        if len(self.QRIZ) > 0:
            for qriz in self.QRIZ:
                text1 = "Transaksi QRIZ-{} dari Bank {}".format(qriz, qriz)
                text2 = "Transaksi QRIZ-{} dari selain Bank {}".format(qriz, qriz)
                self.MetodePembayaran.append(text1)
                self.MetodePembayaran.append(text2)
        else:
            pass
        for item in self.MetodePembayaran:
            self.page1_ComboBox.addItem(str(item))
        self.page1_ComboBox.setEditable(False)
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.page1_ComboBox)


        # self.lineEdit_25 = QtWidgets.QLineEdit(self.frame_3)
        # font = QtGui.QFont()
        # font.setPointSize(9)
        # self.lineEdit_25.setFont(font)
        # self.lineEdit_25.setReadOnly(True)
        # self.lineEdit_25.setObjectName("lineEdit_25")
        # self.lineEdit_25.setText("Default")
        # self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_25)

    def Page1_HorizontalLayout_14(self):
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.formLayout_4.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_14)

    def Page1_LineEdit_24(self):
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_24.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_24.setText('0')
        self.lineEdit_24.setReadOnly(True)
        self.horizontalLayout_14.addWidget(self.lineEdit_24)

    def Page1_LineEdit_26(self):
        self.lineEdit_26 = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_26.setFont(font)
        self.lineEdit_26.setText("")
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_26.setPlaceholderText("Tulis Event")
        self.lineEdit_26.setText("Tidak ada event")
        self.lineEdit_26.setReadOnly(True)
        self.horizontalLayout_14.addWidget(self.lineEdit_26)

    def Page1_Frame_2(self):
        self.frame_2 = QtWidgets.QFrame(self.tab1_TabAnak1_Tab1)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setStyleSheet(FrameStyleSheets1(CekResolusi()))
        self.page1_horizontalLayout_1.addWidget(self.frame_2, 2)

    def Page1_FormLayout_5(self):
        self.formLayout_5 = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout_5.setObjectName("formLayout_5")

    def Page1_FormLayout_3(self):
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout_5.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.formLayout_3)

    def Page1_Label_28(self):
        self.label_28 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_28)
        self.label_28.setText('RINCIAN PESANAN')

    def Page1_Label_40(self):
        self.label_40 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_40)
        self.label_40.setText('Nomor Transaksi : ')

    def Page1_HorizontalLayout_11(self):
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_11)

    def Page1_LineEdit_5(self):
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_11.addWidget(self.lineEdit_5)

    def Page1_HorizontalLayout_19(self):
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.formLayout_3.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_19)

    def Page1_Label_42(self):
        self.label_42 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_19.addWidget(self.label_42)
        self.label_42.setText('Waktu Transaksi : ')

    def Page1_SpacerItem2(self):
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem2)

    def Page1_HorizontalLayout_12(self):
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.formLayout_3.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_12)

    def Page1_LineEdit_21(self):
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.horizontalLayout_12.addWidget(self.lineEdit_21)

    def Page1_Label_44(self):
        self.label_44 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.label_44.setText('Kasir : ')
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_44)

    def Page1_HorizontalLayout_13(self):
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.formLayout_3.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_13)

    def Page1_LineEdit_23(self):
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.horizontalLayout_13.addWidget(self.lineEdit_23)

    def Page1_HorizontalLayout(self):
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSpacing(10)
        self.gridLayout_3.addLayout(self.horizontalLayout, 4, 0, 1, 2)

    def Page1_TableWidget_2(self):
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab1_TabAnak1_Tab1)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setAlternatingRowColors(False)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2_Kolom = ['No', 'Kode', 'Barcode', 'Nama Item', 'Qty', 'Harga Satuan', 'SubTotal', 'Diskon',
                                    'TOTAL']
        self.tableWidget_2.setColumnCount(len(self.tableWidget_2_Kolom))
        for NomorKolom in range(len(self.tableWidget_2_Kolom)):
            self.tableWidget_2.setHorizontalHeaderItem(NomorKolom,
                                                       QtWidgets.QTableWidgetItem(self.tableWidget_2_Kolom[NomorKolom]))
        self.tableWidget_2.setColumnWidth(0, 100)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setFont(Font(9, True))
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.tableWidget_2)

    def Page1_Frame_4(self):
        self.frame_4 = QtWidgets.QFrame(self.tab1_TabAnak1_Tab1)
        self.frame_4.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_4.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.setStyleSheet(FrameStyleSheets3(CekResolusi()))
        self.gridLayout_3.addWidget(self.frame_4, 3, 2, 2, 1)

    def Page1_HorizontalLayout_9(self):
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_9.setContentsMargins(3, 1, 3, 1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")

    def Page1_VerticalLayout(self):
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9.addLayout(self.verticalLayout)

    def Page1_PushButton_7(self):
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(250, 100))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_7.setStyleSheet("text-align: left;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Tambah/shopcartadd.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setToolTip("Tambah Item (Tombol T)")
        self.pushButton_7.setText("Tambah Item")
        self.pushButton_7.setStyleSheet(ButtonStyleSheets3(CekResolusi()))
        self.verticalLayout.addWidget(self.pushButton_7)

    def Page1_PushButton_8(self):
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(250, 100))
        self.pushButton_8.setStyleSheet("text-align: left;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Tambah/shopcartexclude.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setToolTip("Hapus Item (Tombol H)")
        self.pushButton_8.setText("Hapus Item")
        self.pushButton_8.setStyleSheet(ButtonStyleSheets3(CekResolusi()))
        self.verticalLayout.addWidget(self.pushButton_8)

    def Page1_PushButton_9(self):
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_9.setMinimumSize(QtCore.QSize(250, 100))
        self.pushButton_9.setStyleSheet("text-align: left;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Tambah/shopcart.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setToolTip("Batalkan Transaksi (Tombol L)")
        self.pushButton_9.setText("Batalkan")
        self.pushButton_9.setStyleSheet(ButtonStyleSheets3(CekResolusi()))
        self.verticalLayout.addWidget(self.pushButton_9)

    def Page1_PushButton_11(self):
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_11.setMinimumSize(QtCore.QSize(250, 100))
        self.pushButton_11.setStyleSheet("text-align: left;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Tambah/shopcartapply.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon3)
        self.pushButton_11.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setToolTip("Bayar (Tombol B)")
        self.pushButton_11.setText("Bayar")
        self.pushButton_11.setStyleSheet(ButtonStyleSheets3(CekResolusi()))
        self.verticalLayout.addWidget(self.pushButton_11)

    def Page1_PushButton_6(self):
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setMinimumSize(QtCore.QSize(250, 100))
        self.pushButton_6.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Tambah/icon-printer02-black-icon-print-data-11553457644zutfcky9ex.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setToolTip("Cetak Struk Belanja (Tombol Enter)")
        self.pushButton_6.setText("  Cetak Struk")
        self.pushButton_6.setStyleSheet(ButtonStyleSheets3(CekResolusi()))
        self.verticalLayout.addWidget(self.pushButton_6)

    def Page1_PushButton_10(self):
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_10.setMinimumSize(QtCore.QSize(250, 100))
        self.pushButton_10.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Tambah/Next_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon5)
        self.pushButton_10.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setToolTip("Transaksi Baru (Tombol Spasi)")
        self.pushButton_10.setText("   Baru")
        self.pushButton_10.setStyleSheet(ButtonStyleSheets3(CekResolusi()))
        self.verticalLayout.addWidget(self.pushButton_10)

    def Page1_PushButton11(self):
        self.page1_PushButton11 = QtWidgets.QPushButton("self.page1_PushButton11")
        self.verticalLayout.addWidget(self.page1_PushButton11)

    def Page1_HorizontalLayout_4(self):
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 3, 0, 1, 2)

    def Page1_LineEdit_2(self):
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab1_TabAnak1_Tab1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Cari item")
        self.horizontalLayout_4.addWidget(self.lineEdit_2, 1)

    def Page1_PushButton_24(self):
        self.pushButton_24 = QtWidgets.QPushButton(self.tab1_TabAnak1_Tab1)
        self.pushButton_24.setText("")
        self.pushButton_24.setIcon(Icon('Tambah.png', 0))
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_4.addWidget(self.pushButton_24)

    def Page1_SpacerItem4(self):
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 2, 0, 1, 1)

    def Page1_Tab_lsi(self):
        self.Page1_dsi = Page1_dsi(self)
        self.Page1_dsi.Page1_TambahTransaksiBaru()
        self.Page1_ht = Page1_ht(self)

    def Page1_HorizontalLayout_15(self):
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.gridLayout_5.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)

    def Page1_Label_39(self):
        self.label_39 = QtWidgets.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_15.addWidget(self.label_39)
        self.label_39.setText('Aplikasi Toko by PandanArum, Produseno.com')

    def Page1_Label_38(self):
        self.label_38 = QtWidgets.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(0, 85, 0);")
        self.label_38.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_15.addWidget(self.label_38)
        self.label_38.setText('Kota Batu, Jawa Timur, INDONESIA (2020)')

    '''
    ATUR TAMPILAN GUI DISINI :
    '''

    def Page1_Waktu(self):
        # Hari
        self.page1_DayNow = QDate.currentDate().toString('dddd').lower()
        if self.page1_DayNow == 'sunday':
            self.page1_HariSekarang = 'Minggu'
        elif self.page1_DayNow == 'monday':
            self.page1_HariSekarang = 'Senin'
        elif self.page1_DayNow == 'tuesday':
            self.page1_HariSekarang = 'Selasa'
        elif self.page1_DayNow == 'wednesday':
            self.page1_HariSekarang = 'Rabu'
        elif self.page1_DayNow == 'thursday':
            self.page1_HariSekarang = 'Kamis'
        elif self.page1_DayNow == 'friday':
            self.page1_HariSekarang = "Jum'at"
        elif self.page1_DayNow == 'saturday':
            self.page1_HariSekarang = 'Sabtu'
        else:
            self.page1_HariSekarang = 'Hari Tidak Terdeteksi'

        # Tanggal
        self.page1_TanggalSekarang = QDate.currentDate().toString('dd')

        # Bulan
        self.page1_MonthNow = QDate.currentDate().toString('MMMM').lower()
        if self.page1_MonthNow == 'january':
            self.page1_BulanSekarang = 'Januari'
        elif self.page1_MonthNow == 'february':
            self.page1_BulanSekarang = 'Februari'
        elif self.page1_MonthNow == 'march':
            self.page1_BulanSekarang = 'Maret'
        elif self.page1_MonthNow == 'april':
            self.page1_BulanSekarang = 'April'
        elif self.page1_MonthNow == 'may':
            self.page1_BulanSekarang = 'Mei'
        elif self.page1_MonthNow == 'june':
            self.page1_BulanSekarang = "Juni"
        elif self.page1_MonthNow == 'july':
            self.page1_BulanSekarang = 'Juli'
        elif self.page1_MonthNow == 'august':
            self.page1_BulanSekarang = 'Agustus'
        elif self.page1_MonthNow == 'september':
            self.page1_BulanSekarang = 'September'
        elif self.page1_MonthNow == 'october':
            self.page1_BulanSekarang = 'Oktober'
        elif self.page1_MonthNow == 'november':
            self.page1_BulanSekarang = 'November'
        elif self.page1_MonthNow == 'december':
            self.page1_BulanSekarang = "Desember"
        else:
            self.page1_HariSekarang = 'Bulan Tidak Terdeteksi'

        # Bulan Sekarang Angka
        self.page1_BulanSekarangAngka = QDate.currentDate().toString('MM')

        # Tahun Sekarang
        self.page1_TahunSekarang = QDate.currentDate().toString('yyyy')

        # Jam Sekarang
        self.page1_JamSekarang = QTime.currentTime().toString('HH')

        # Menit Sekarang
        self.page1_MenitSekarang = QTime.currentTime().toString('mm')

        # Detik Sekarang
        self.page1_DetikSekarang = QTime.currentTime().toString('ss')

    def Page1_DigitalClock1(self):
        # Untuk menjalankan Digital Clock
        self.timer = QTimer()
        self.timer.timeout.connect(self.Page1_label_32_label_34_lineEdit_21_DigitalClock2)
        self.timer.start(1000)

        # Fungsi timeout untuk mencopy Folder LOG ke LOG User agar tidak mempengaruhi writing file excell log
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.Page1_DataAkhir3)
        self.timer2.start(60000)

        # Fungsi timeout untuk refresh tablewidget_2
        self.timer3 = QTimer()
        self.timer3.start(0)

    def Page1_label_36_labelKaryawan(self):
        self.label_36.setText(self.username)

    def Page1_NomorTransaksiGenerator(self):
        FileExcell = self.file_TransaksiTokoTerkonfirmasiLOG
        Df1 = pd.read_csv(FileExcell)

        self.page1_NomorTransaksiTerpakaiHariIni = []
        dataTransaksiHariIni = Df1.loc[:, 'Nomor Transaksi']
        for item in dataTransaksiHariIni:
            self.page1_NomorTransaksiTerpakaiHariIni.append(item)

        # Generate Nomor Transaksi Baru
        No = 1
        if No < 10:
            prefix = '0000'
        elif No < 100:
            prefix = '000'
        elif No < 1000:
            prefix = '00'
        elif No < 1000000:
            prefix = '0'
        else:
            prefix = ''
        PrefixNo = prefix + str(No)
        NomorTransaksi = '{}{}{}-{}'.format(self.page1_TahunSekarang,
                                            self.page1_BulanSekarangAngka,
                                            self.page1_TanggalSekarang,
                                            PrefixNo)
        while NomorTransaksi in self.page1_NomorTransaksiTerpakaiHariIni:
            No += 1
            if No < 10:
                prefix = '000'
            elif No < 100:
                prefix = '00'
            elif No < 1000:
                prefix = '0'
            else:
                prefix = ''
            PrefixNo = prefix + str(No)
            NomorTransaksi = '{}{}{}-{}'.format(self.page1_TahunSekarang,
                                                self.page1_BulanSekarangAngka,
                                                self.page1_TanggalSekarang,
                                                PrefixNo)
        else:
            pass
        return NomorTransaksi

    def Page1_lineEdit5_setNomorTransaksi(self):
        self.lineEdit_5.setText(self.Page1_NomorTransaksiGenerator())

    def Page1_label_32_label_34_lineEdit_21_DigitalClock2(self):
        self.Page1_Waktu()
        self.label_32.setText(
            '{}, {} {} {}'.format(self.page1_HariSekarang, self.page1_TanggalSekarang, self.page1_BulanSekarang,
                                  self.page1_TahunSekarang))
        self.label_34.setText(
            '{}:{}:{}'.format(self.page1_JamSekarang, self.page1_MenitSekarang, self.page1_DetikSekarang))
        self.lineEdit_21.setText('{}/{}/{} - {}:{}:{}'.format(self.page1_TanggalSekarang, self.page1_BulanSekarangAngka,
                                                              self.page1_TahunSekarang, self.page1_JamSekarang,
                                                              self.page1_MenitSekarang, self.page1_DetikSekarang))

    def Page1_lineEdit_23_namaKasir(self):
        self.lineEdit_23.setText(self.username)

    def Page1_OperasiTableWidget1(self):
        # Load Database
        self.Page1_StokListBarcode = []
        self.Page1_StokListKodeToko = []
        self.Page1_StokListNamaItem = []
        self.Page1_StokDatabaseConnection = sqlite3.connect(DatabaseProduk())
        self.Page1_StokDatabaseCursor = self.Page1_StokDatabaseConnection.cursor()
        self.Page1_StokListBarcodeData = self.Page1_StokDatabaseCursor.execute(
            'select Barcode_Produk from Data_Produk_Master').fetchall()
        for item in self.Page1_StokListBarcodeData:
            self.Page1_StokListBarcode.append(item[0])

    def Page1_DataAkhir3(self):
        # Untuk mencopy Folder LOG ke LOG User agar tidak mempengaruhi writing file excell log
        try:
            shutil.copytree(self.LOG, self.LOG_User, dirs_exist_ok=True)
        except:
            pass

    '''
    OPERASI TRANSAKSI DISINI :
    '''

    def Page1_KumpulkanData(self):
        self.page1_NomorTransaksi = self.lineEdit_5.text()
        self.page1_WaktuTransaksi = self.lineEdit_21.text()
        self.page1_Kasir = self.lineEdit_23.text()
        self.page1_Transaksi = self.lineEdit_25.text()
        self.page1_DiskonKhusus = self.lineEdit_24.text()
        self.page1_DiskonKhusus_Event = self.lineEdit_26.text()
        self.page1_TotalBelanjaan = self.label_50.text()
        pass

    def Page1_pushButton_10_clicked(self):
        pass

    def Page1_PushButton11_clicked(self):
        objek = Page1_TambahPembeli(self)
        pass

    def Page1_CariItem_Completer(self):
        self.page1_ListKode = []
        self.page1_ListBarcode = []
        self.page1_ListNamaItem = []
        Data = []

        rows = self.page1_DBCursor.execute('select * from Data_Produk_Master').fetchall()
        for row in range(len(rows)):
            if str(rows[row]['Kode_Toko']) not in self.page1_ListKode:
                self.page1_ListKode.append(str(rows[row]['Kode_Toko']))
            else:
                pass
            if str(rows[row]['Barcode_Produk']) not in self.page1_ListBarcode:
                self.page1_ListBarcode.append(str(rows[row]['Barcode_Produk']))
            else:
                pass
            if str(rows[row]['Nama_Produk_Di_Toko']) not in self.page1_ListNamaItem:
                self.page1_ListNamaItem.append(str(rows[row]['Nama_Produk_Di_Toko']))
            else:
                pass

        for row in range(len(rows)):
            if str(rows[row]['Kode_Toko']) not in Data:
                Data.append(str(rows[row]['Kode_Toko']))
            else:
                pass
            if str(rows[row]['Barcode_Produk']) not in Data:
                Data.append(str(rows[row]['Barcode_Produk']))
            else:
                pass
            if str(rows[row]['Nama_Produk_Di_Toko']) not in Data:
                Data.append(str(rows[row]['Nama_Produk_Di_Toko']))
            else:
                pass

        self.page1_completer = QtWidgets.QCompleter(Data)
        self.page1_completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.page1_completer.setFilterMode(QtCore.Qt.MatchContains)
        self.lineEdit_2.setCompleter(self.page1_completer)
        self.page1_completer.activated.connect(self.pushButton_7.click)

    def Page1_CariItem_SetFocus(self):
        self.lineEdit_2.setFocus()

    def Page1_PERINTAH(self):
        self.pushButton_10.clicked.connect(self.Page1_pushButton_10_clicked)
        self.page1_PushButton11.clicked.connect(self.Page1_PushButton11_clicked)
        # self.tableWidget_2..connect(self.Page1_CariItem_SetFocus)
        pass

    def Page1_ResolutionManager(self):
        Resolusi = CekResolusi()
        if Resolusi == '1280x720':
            self.frame.setFixedHeight(40)
            self.pushButton_13.setMinimumSize(100, 25)
            self.frame_4.setMaximumWidth(150)
            self.pushButton_6.setMinimumSize(QtCore.QSize(130, 40))
            self.pushButton_6.setIconSize(QtCore.QSize(25, 25))
            self.pushButton_7.setMinimumSize(QtCore.QSize(130, 40))
            self.pushButton_7.setIconSize(QtCore.QSize(25, 25))
            self.pushButton_8.setMinimumSize(QtCore.QSize(130, 40))
            self.pushButton_8.setIconSize(QtCore.QSize(25, 25))
            self.pushButton_9.setMinimumSize(QtCore.QSize(130, 40))
            self.pushButton_9.setIconSize(QtCore.QSize(25, 25))
            self.pushButton_10.setMinimumSize(QtCore.QSize(130, 40))
            self.pushButton_10.setIconSize(QtCore.QSize(25, 25))
            self.pushButton_11.setMinimumSize(QtCore.QSize(130, 40))
            self.pushButton_11.setIconSize(QtCore.QSize(25, 25))
        elif Resolusi == '2880x1620':
            pass
        else:
            pass

    def Page1_Editing_Mode(self):
        self.label_35.setText("self.label_35")
        self.label_36.setText("self.label_36")
        self.label_34.setText("self.label_34")
        self.label_33.setText("self.label_33")
        self.label_32.setText("self.label_32")
        self.pushButton_13.setText("self.pushButton_13")
        self.label_41.setText("self.label_41")
        self.label_43.setText("self.label_43")
        self.label_45.setText("self.label_45")
        self.label_49.setText("self.label_49")
        self.label_50.setText("self.label_50")
        self.label_51.setText("self.label_51")
        self.label_37.setText("self.label_37")
        # self.lineEdit_25.setText("self.lineEdit_25")
        self.lineEdit_24.setText("self.lineEdit_24")
        self.lineEdit_26.setText("self.lineEdit_26")
        self.label_28.setText("self.label_28")
        self.label_40.setText("self.label_40")
        self.lineEdit_5.setText("self.lineEdit_5")
        self.label_42.setText("self.label_42")
        self.lineEdit_21.setText("self.lineEdit_21")
        self.label_44.setText("self.label_44")
        self.lineEdit_23.setText("self.lineEdit_23")
        self.pushButton_7.setText("self.pushButton_7")
        self.pushButton_8.setText("self.pushButton_8")
        self.pushButton_9.setText("self.pushButton_9")
        self.pushButton_11.setText("self.pushButton_11")
        self.pushButton_6.setText("self.pushButton_6")
        self.pushButton_10.setText("self.pushButton_10")
        self.lineEdit_2.setText("self.lineEdit_2")
        # self.pushButton_24.setText("self.pushButton_24")
        self.label_39.setText("self.label_39")
        self.label_38.setText("self.label_38")
        pass

    def Page1_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        self.Page1_Waktu()
        self.Page1_DigitalClock1()
        self.Page1_OperasiTableWidget1()

        '''LOAD GUI : ___________________________________'''
        # TAB 1
        MenuBar.MenuBar_Execution(self)
        self.Page1_Database()
        self.Page1_Update_ExpiredDate()
        self.Tab1()  # Page 1
        self.Page1_GridLayout_5()  # Page 1
        self.Page1_Tab1_GridLayout()  # Page 1
        self.Page1_Tab1_TabAnak1()  # Page 1
        self.Page1_Tab1_TabAnak1_Tab1()  # Page 1
        self.Page1_GridLayout_3()  # Page 1
        self.Page1_Frame()  # Page 1
        self.Page1_GridLayout_9()  # Page 1
        self.Page1_Label_35()  # Page 1
        self.Page1_Label_36()  # Page 1
        self.Page1_Label_34()  # Page 1
        self.Page1_Label_33()  # Page 1
        self.Page1_Label_32()  # Page 1
        self.Page1_SpacerItem()  # Page 1
        self.Page1_PushButton_13()  # Page 1
        self.Page1_HorizontalLayout_1()
        self.Page1_Frame_2()  # Page 1
        self.Page1_Frame_3()  # Page 1
        self.Page1_FormLayout_6()  # Page 1
        self.Page1_FormLayout_4()  # Page 1
        self.Page1_Label_41()  # Page 1
        self.Page1_Label_43()  # Page 1
        self.Page1_Label_45()  # Page 1
        self.Page1_HorizontalLayout_8()  # Page 1
        self.Page1_SpacerItem1()  # Page 1
        self.Page1_Label_49()  # Page 1
        self.Page1_Label_50()  # Page 1
        self.Page1_Label_51()  # Page 1
        self.Page1_Label_37()  # Page 1
        self.Page1_LineEdit_25()  # Page 1
        self.Page1_HorizontalLayout_14()  # Page 1
        self.Page1_LineEdit_24()  # Page 1
        self.Page1_LineEdit_26()  # Page 1
        self.Page1_FormLayout_5()  # Page 1
        self.Page1_FormLayout_3()  # Page 1
        self.Page1_Label_28()  # Page 1
        self.Page1_Label_40()  # Page 1
        self.Page1_HorizontalLayout_11()  # Page 1
        self.Page1_LineEdit_5()  # Page 1
        self.Page1_HorizontalLayout_19()  # Page 1
        self.Page1_Label_42()  # Page 1
        self.Page1_SpacerItem2()  # Page 1
        self.Page1_HorizontalLayout_12()  # Page 1
        self.Page1_LineEdit_21()  # Page 1
        self.Page1_Label_44()  # Page 1
        self.Page1_HorizontalLayout_13()  # Page 1
        self.Page1_LineEdit_23()  # Page 1
        self.Page1_HorizontalLayout()  # Page 1
        self.Page1_TableWidget_2()  # Page 1
        self.Page1_Frame_4()  # Page 1
        self.Page1_HorizontalLayout_9()  # Page 1
        self.Page1_VerticalLayout()  # Page 1
        self.Page1_PushButton_7()  # Page 1
        self.Page1_PushButton_8()  # Page 1
        self.Page1_PushButton_9()  # Page 1
        self.Page1_PushButton_11()  # Page 1
        self.Page1_PushButton_6()  # Page 1
        self.Page1_PushButton_10()  # Page 1
        self.Page1_PushButton11()
        self.Page1_HorizontalLayout_4()  # Page 1
        # self.Page1_PushButton_24()  # Page 1
        self.Page1_LineEdit_2()  # Page 1
        self.Page1_SpacerItem4()  # Page 1
        self.Page1_HorizontalLayout_15()  # Page 1
        self.Page1_Label_39()  # Page 1
        self.Page1_Label_38()  # Page 1

        '''SETELAH GUI TERLOAD : _____________________________________'''
        self.Page1_PrinterConnection()
        self.Page1_label_36_labelKaryawan()
        self.Page1_lineEdit5_setNomorTransaksi()
        self.Page1_lineEdit_23_namaKasir()
        self.Page1_CariItem_Completer()
        self.Page1_Tab_lsi()  # Page 1
        self.Page1_PERINTAH()
        self.lineEdit_2.setFocus()
        # self.Page1_Editing_Mode()
        self.Page1_ResolutionManager()


class Page1_dsi(Page1):
    # Page1_lsi = Page1_ListSemuaItem
    def __init__(self, data):
        self.Data = data
        super(Page1_dsi, self).__init__()

        '''INISIALISASI DATA'''
        self.Page1_dsi_LoadDataBase()

        '''BUAT GUI'''
        self.Page1_dsi_INISIALISASI()
        self.Page1_dsi_GridLayout()
        self.Page1_dsi_Frame()
        self.Page1_dsi_HBoxLayout()
        self.Page1_dsi_Label()
        self.Page1_dsi_Label_2()
        self.Page1_dsi_SpacerItem()
        self.Page1_dsi_Label_3()
        self.Page1_dsi_Label_4()
        self.Page1_dsi_PushButton()
        self.Page1_dsi_Frame_2()
        self.Page1_dsi_GridLayout_2()
        self.Page1_dsi_Label_5()
        self.Page1_dsi_Label_7()
        self.Page1_dsi_LineEdit_2()
        self.Page1_dsi_Label_8()
        self.Page1_dsi_LineEdit_3()
        self.Page1_dsi_SpacerItem_4()

        self.Page1_dsi_HBoxLayout_2()
        self.Page1_dsi_Label_6()
        self.Page1_dsi_LineEdit()
        self.Page1_dsi_PushButton_2()
        self.Page1_dsi_TableWidget()
        self.Page1_dsi_HBoxLayout_3()
        self.Page1_dsi_SpacerItem_2()
        self.Page1_dsi_PushButton_3()
        self.Page1_dsi_SpacerItem_3()
        # self.Page1_dsi_SpacerItem_40()
        '''GUI SELESAI'''

        '''EDIT GUI'''
        self.Page1_dsi_Frame_Edited()
        self.Page1_dsi_Frame_2_Edited()
        self.Page1_dsi_Label_Edited()
        self.Page1_dsi_Label_2_Edited()
        self.Page1_dsi_Label_3_Edited()
        self.Page1_dsi_Label_4_Edited()
        self.Page1_dsi_PushButton_Edited()
        self.Page1_dsi_TableWidget_Edited()
        self.Page1_dsi_LineEdit_AutoComplete()

        '''PERINTAH'''
        self.page1_dsi_PushButton_3.clicked.connect(self.Page1_dsi_PushButton_3_Edited)
        self.Data.timer.timeout.connect(self.Page1_dsi_Label_Edited)
        self.Data.timer.timeout.connect(self.Page1_dsi_Label_2_Edited)
        self.Data.timer3.timeout.connect(self.Page1_lineEdit_2_Edited)
        # self.Data.pushButton_24.clicked.connect(self.Page1_pushButton_24_Edited)
        self.Data.pushButton_7.clicked.connect(self.Page1_pushButton_7_Edited)
        self.Data.timer3.timeout.connect(self.Page1_Kolom_Qty_Diskon_Harga_Berubah)
        self.Data.timer3.timeout.connect(self.Page1_SetEditableItemTable)
        self.Data.timer3.timeout.connect(self.Page1_SetTypeDataTable)
        self.page1_dsi_PushButton.clicked.connect(self.Page1_dsi_PushButton_Clicked)
        self.Data.pushButton_8.clicked.connect(self.Page1_HapusItem)
        self.Data.pushButton_9.clicked.connect(self.Page1_BatalkanTransaksi)
        self.Data.pushButton_11.clicked.connect(self.Page1_Bayar)



        self.Data.pushButton_6.clicked.connect(self.Page1_CetakStruk2)
        self.Data.pushButton_6.clicked.connect(self.Page1_UpdateExcellSetelahTransaksi)



        self.Data.pushButton_10.clicked.connect(self.Page1_TambahTransaksiBaru)
        self.Data.tab1_TabAnak1.currentChanged.connect(self.Page1_Event_Tab1TabAnak1_Changed)
        self.page1_dsi_PushButton_2.clicked.connect(self.Page1_dsi_LineEdit_AutoComplete_Completed)
        self.Page1_dsi_ResolutionManager()
        # self.Data.pushButton_10.clicked.connect(self.Page1_UpdateDatabaseSetelahTransaksi)
        # self.Data.pushButton_10.clicked.connect(self.Page1_LokasiSimpanStruk)

        '''Nomor Terakhir Digunakan:
        Frame: self.page1_dsi_Frame_2
        Label: self.page1_dsi_Label_8
        LineEdit: self.page1_dsi_LineEdit_3
        PushButton: self.page1_dsi_PushButton_3
        GidLayout: self.page1_dsi_GridLayout_2
        HBoxLayout: self.page1_dsi_.HBoxLayout_3
        VBoxLayout: -
        SpacerItem: self.page1_dsi_SpacerItem_4
        '''

        # self.Data.tab1_TabAnak1.setCurrentWidget(self.page1_dsi)
        self.page1_dsi_DBConnection.close()

    def Page1_dsi_LoadDataBase(self):
        self.page1_dsi_DBConnection = sqlite3.connect(DatabaseProduk())
        self.page1_dsi_DBCursor = self.page1_dsi_DBConnection.cursor()
        # self.page1_dsi_DBData = self.page1_dsi_DBCursor.execute('select No, KodeToko, Barcode, Nama_Item, Stok, Satuan, Harga_Jual_Per_Satuan_Terkecil, Quantity_Jual_Terkecil, Satuan_Jual_Terkecil, Diskon1, Diskon2, Diskon3, Posisi_Barang from Data_Produk_Master').fetchall()
        pass

    def Page1_dsi_INISIALISASI(self):
        self.page1_dsi = QtWidgets.QWidget()
        self.page1_dsi.setObjectName("lsi")
        self.Data.tab1_TabAnak1.addTab(self.page1_dsi, "")
        self.Data.tab1_TabAnak1.setTabText(self.Data.tab1_TabAnak1.indexOf(self.page1_dsi), "Daftar Semua Item")

    def Page1_dsi_GridLayout(self):
        self.page1_dsi_GridLayout = QtWidgets.QGridLayout(self.page1_dsi)
        self.page1_dsi_GridLayout.setObjectName('page1_dsi_GridLayout')

    def Page1_dsi_Frame(self):
        self.page1_dsi_Frame = QtWidgets.QFrame()
        self.page1_dsi_GridLayout.addWidget(self.page1_dsi_Frame, 0, 0)

    def Page1_dsi_HBoxLayout(self):
        self.page1_dsi_HBoxLayout = QtWidgets.QHBoxLayout(self.page1_dsi_Frame)

    def Page1_dsi_Label(self):
        self.page1_dsi_Label = QtWidgets.QLabel('Jum\'at, 13 November 2020')
        self.page1_dsi_HBoxLayout.addWidget(self.page1_dsi_Label)

    def Page1_dsi_Label_2(self):
        self.page1_dsi_Label_2 = QtWidgets.QLabel(' - 13:21:00')
        self.page1_dsi_HBoxLayout.addWidget(self.page1_dsi_Label_2)

    def Page1_dsi_SpacerItem(self):
        self.page1_dsi_SpacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                                          QtWidgets.QSizePolicy.Fixed)
        self.page1_dsi_HBoxLayout.addItem(self.page1_dsi_SpacerItem)

    def Page1_dsi_Label_3(self):
        self.page1_dsi_Label_3 = QtWidgets.QLabel('Pengguna : ')
        self.page1_dsi_HBoxLayout.addWidget(self.page1_dsi_Label_3)

    def Page1_dsi_Label_4(self):
        self.page1_dsi_Label_4 = QtWidgets.QLabel('Nama Pengguna')
        self.page1_dsi_HBoxLayout.addWidget(self.page1_dsi_Label_4)

    def Page1_dsi_PushButton(self):
        self.page1_dsi_PushButton = QtWidgets.QPushButton('Logout')
        self.page1_dsi_PushButton.setMinimumSize(150, 50)
        self.page1_dsi_HBoxLayout.addWidget(self.page1_dsi_PushButton)

    def Page1_dsi_Frame_2(self):
        self.page1_dsi_Frame_2 = QtWidgets.QFrame()
        self.page1_dsi_Frame_2.setObjectName('page1_dsi_Frame_2')
        self.page1_dsi_GridLayout.addWidget(self.page1_dsi_Frame_2, 1, 0)

    def Page1_dsi_GridLayout_2(self):
        self.page1_dsi_GridLayout_2 = QtWidgets.QGridLayout(self.page1_dsi_Frame_2)

    def Page1_dsi_Label_5(self):
        self.page1_dsi_Label_5 = QtWidgets.QLabel('DAFTAR SEMUA ITEM')
        self.page1_dsi_Label_5.setMinimumSize(0, 100)
        self.page1_dsi_Label_5.setFont(Font(14, True))
        self.page1_dsi_Label_5.setAlignment(QtCore.Qt.AlignHCenter)
        self.page1_dsi_GridLayout_2.addWidget(self.page1_dsi_Label_5, 0, 0, 1, 2)

    def Page1_dsi_Label_7(self):
        self.page1_dsi_Label_7 = QtWidgets.QLabel('Total Item Saat ini : ')
        self.page1_dsi_GridLayout_2.addWidget(self.page1_dsi_Label_7, 1, 0)

    def Page1_dsi_LineEdit_2(self):
        self.page1_dsi_LineEdit_2 = QtWidgets.QLineEdit()
        self.page1_dsi_LineEdit_2.setText("page1_dsi_LineEdit_2")
        self.page1_dsi_GridLayout_2.addWidget(self.page1_dsi_LineEdit_2, 1, 1)

    def Page1_dsi_Label_8(self):
        self.page1_dsi_Label_8 = QtWidgets.QLabel('Jumlah Item Kosong : ')
        self.page1_dsi_GridLayout_2.addWidget(self.page1_dsi_Label_8, 2, 0)

    def Page1_dsi_LineEdit_3(self):
        self.page1_dsi_LineEdit_3 = QtWidgets.QLineEdit()
        self.page1_dsi_LineEdit_3.setText('page1_dsi_LineEdit_3')
        self.page1_dsi_GridLayout_2.addWidget(self.page1_dsi_LineEdit_3, 2, 1)

    def Page1_dsi_SpacerItem_4(self):
        self.page1_dsi_SpacerItem_4 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Fixed,
                                                            QtWidgets.QSizePolicy.Fixed)
        self.page1_dsi_GridLayout.addItem(self.page1_dsi_SpacerItem_4, 2, 0)

    def Page1_dsi_HBoxLayout_2(self):
        self.page1_dsi_HBoxLayout_2 = QtWidgets.QHBoxLayout()
        self.page1_dsi_GridLayout.addLayout(self.page1_dsi_HBoxLayout_2, 3, 0)

    def Page1_dsi_Label_6(self):
        self.page1_dsi_Label_6 = QtWidgets.QLabel('Cari Item : ')
        self.page1_dsi_HBoxLayout_2.addWidget(self.page1_dsi_Label_6)

    def Page1_dsi_LineEdit(self):
        self.page1_dsi_LineEdit = QtWidgets.QLineEdit()
        self.page1_dsi_LineEdit.setPlaceholderText('Isikan dengan Kode Toko, Barcode Produk, Atau Nama Produk')
        self.page1_dsi_LineEdit.setMinimumSize(0, 50)
        self.page1_dsi_HBoxLayout_2.addWidget(self.page1_dsi_LineEdit)

    def Page1_dsi_PushButton_2(self):
        self.page1_dsi_PushButton_2 = QtWidgets.QPushButton('Cari')
        self.page1_dsi_PushButton_2.setMinimumSize(150, 50)
        self.page1_dsi_HBoxLayout_2.addWidget(self.page1_dsi_PushButton_2)

    def Page1_dsi_TableWidget(self):
        self.page1_dsi_TableWidget = QtWidgets.QTableWidget()
        self.page1_dsi_GridLayout.addWidget(self.page1_dsi_TableWidget, 4, 0)

    def Page1_dsi_HBoxLayout_3(self):
        self.page1_dsi_HBoxLayout_3 = QtWidgets.QHBoxLayout()
        self.page1_dsi_GridLayout.addLayout(self.page1_dsi_HBoxLayout_3, 5, 0)

    def Page1_dsi_SpacerItem_2(self):
        self.page1_dsi_SpacerItem_2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                                            QtWidgets.QSizePolicy.Fixed)
        self.page1_dsi_HBoxLayout_3.addItem(self.page1_dsi_SpacerItem_2)

    def Page1_dsi_PushButton_3(self):
        self.page1_dsi_PushButton_3 = QtWidgets.QPushButton('  Reload Tabel')
        self.page1_dsi_PushButton_3.setMinimumSize(250, 70)
        self.page1_dsi_PushButton_3.setIcon(Icon('Refresh.png', 50))
        self.page1_dsi_PushButton_3.setStyleSheet(ButtonStyleSheets3(CekResolusi()))
        self.page1_dsi_HBoxLayout_3.addWidget(self.page1_dsi_PushButton_3)

    def Page1_dsi_SpacerItem_3(self):
        self.page1_dsi_SpacerItem_3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                                            QtWidgets.QSizePolicy.Fixed)
        self.page1_dsi_HBoxLayout_3.addItem(self.page1_dsi_SpacerItem_3)

    def Page1_dsi_SpacerItem_40(self):
        self.page1_dsi_SpacerItem_40 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                             QtWidgets.QSizePolicy.Expanding)
        self.page1_dsi_GridLayout.addItem(self.page1_dsi_SpacerItem_40, 40, 0)

    '''Edit : '''

    def Page1_dsi_LineEdit_AutoComplete(self):
        barcode =self.page1_dsi_DBCursor.execute("select name from sqlite_master where type='table' order by name").fetchall()
        Barcode = [barcode[item][0] for item in range(len(barcode)) if barcode[item][0] != "Data_Produk_Master"]
        kodeToko = self.page1_dsi_DBCursor.execute("select name from sqlite_master where type='table' order by name").fetchall()
        KodeToko = [kodeToko[item][0] for item in range(len(kodeToko)) if kodeToko[item][0]!="Data_Produk_Master"]
        Nama_Item = [str(self.page1_dsi_DBCursor.execute("select Nama_Produk from '{}'".format(item2)).fetchone()[0]) for item2 in Barcode if item2 != "Data_Produk_Master"]

        self.Page1_dsi_Completer = QtWidgets.QCompleter(KodeToko + Barcode + Nama_Item)
        self.Page1_dsi_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.Page1_dsi_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page1_dsi_LineEdit.setCompleter(self.Page1_dsi_Completer)

    def Page1_dsi_LineEdit_AutoComplete_Completed(self):
        barcode = self.page1_dsi_DBCursor.execute("select name from sqlite_master where type='table' order by name").fetchall()
        Barcode = [barcode[item][0] for item in range(len(barcode)) if barcode[item][0] != "Data_Produk_Master"]
        KodeToko = {self.page1_dsi_DBCursor.execute("select Kode_Toko from '{}'".format(str(item2))).fetchone()[0]:str(item2) for item2 in Barcode}
        Nama_Item = {self.page1_dsi_DBCursor.execute("select Nama_Produk from '{}'".format(str(item2))).fetchone()[0]:str(item2) for item2 in Barcode}
        print(KodeToko)
        Text = self.page1_dsi_LineEdit.text()

        if Text in KodeToko:
            KodeToko_No = 1
            KodeToko_KodeToko = Text
            KodeToko_Barcode = KodeToko[Text]
            KodeToko_NamaItem = self.page1_dsi_DBCursor.execute("select Nama_Produk from '{}'".format(KodeToko_Barcode)).fetchone()[0]
            KodeToko_Stok = int(self.page1_dsi_DBCursor.execute("select TOTAL(Total_Stok_Sekarang) from '{}'".format(KodeToko_Barcode)).fetchone()[0])
            KodeToko_Satuan = self.page1_dsi_DBCursor.execute("select Total_Stok_Sekarang_Satuan from '{}'".format(KodeToko_Barcode)).fetchone()[0]
            KodeToko_PosisiBarang = self.page1_dsi_DBCursor.execute('select Posisi_Barang from Data_Produk_Master where "Kode_Toko"="{}"'.format(Text)).fetchall()[0][0]
            # KodeToko_Qty = self.page1_dsi_DBCursor.execute('select Quantity_Jual_Terkecil from Data_Produk_Master where "Kode_Toko"="{}"'.format(Text)).fetchall()[0][0]
            # KodeToko_SatuanJual = self.page1_dsi_DBCursor.execute('select Satuan_Jual_Terkecil from Data_Produk_Master where "Kode_Toko"="{}"'.format(Text)).fetchall()[0][0]
            KodeToko_HargaJual = self.page1_dsi_DBCursor.execute('select Harga_Jual_Saat_Diskon from Data_Produk_Master where "Kode_Toko"="{}"'.format(Text)).fetchall()[0][0]
            KodeToko_Grosir1 = self.page1_dsi_DBCursor.execute('select Harga_Jual_Saat_Diskon from Data_Produk_Master where "Kode_Toko"="{}"'.format(Text)).fetchall()[0][0]
            KodeToko_Grosir2 = self.page1_dsi_DBCursor.execute('select Harga_Jual_Saat_Diskon from Data_Produk_Master where "Kode_Toko"="{}"'.format(Text)).fetchall()[0][0]
            KodeToko_Grosir3 = self.page1_dsi_DBCursor.execute('select Harga_Jual_Saat_Diskon from Data_Produk_Master where "Kode_Toko"="{}"'.format(Text)).fetchall()[0][0]
            while self.page1_dsi_TableWidget.rowCount() >= 2:
                self.page1_dsi_TableWidget.removeRow(1)
            else:
                self.page1_dsi_TableWidget.item(0, 0).setText(str(KodeToko_No))
                self.page1_dsi_TableWidget.item(0, 1).setText(str(KodeToko_KodeToko))
                self.page1_dsi_TableWidget.item(0, 2).setText(str(KodeToko_Barcode))
                self.page1_dsi_TableWidget.item(0, 3).setText(str(KodeToko_NamaItem))
                self.page1_dsi_TableWidget.item(0, 4).setText(str(KodeToko_Stok))
                self.page1_dsi_TableWidget.item(0, 5).setText(str(KodeToko_Satuan))
                self.page1_dsi_TableWidget.item(0, 6).setText(str(KodeToko_PosisiBarang))
                # self.page1_dsi_TableWidget.item(0, 7).setText(str(KodeToko_Qty))
                # self.page1_dsi_TableWidget.item(0, 8).setText(str(KodeToko_SatuanJual))
                self.page1_dsi_TableWidget.item(0, 9).setText(str(KodeToko_HargaJual))
                self.page1_dsi_TableWidget.item(0, 10).setText(str(KodeToko_Grosir1))
                self.page1_dsi_TableWidget.item(0, 11).setText(str(KodeToko_Grosir2))
                self.page1_dsi_TableWidget.item(0, 12).setText(str(KodeToko_Grosir3))

        elif Text in Barcode:
            Barcode_No = 1
            Barcode_Barcode = Text
            Barcode_KodeToko = self.page1_dsi_DBCursor.execute("select Kode_Toko from '{}'".format(Text)).fetchone()[0]
            Barcode_NamaItem = self.page1_dsi_DBCursor.execute("select Nama_Produk from '{}'".format(Text)).fetchone()[0]
            Barcode_Stok = int(self.page1_dsi_DBCursor.execute("select sum(Total_Stok_Sekarang) from '{}'".format(Text)).fetchone()[0])
            Barcode_Satuan = self.page1_dsi_DBCursor.execute("select Total_Stok_Sekarang_Satuan from '{}'".format(Text)).fetchone()[0]
            Barcode_PosisiBarang = self.page1_dsi_DBCursor.execute('select Posisi_Barang from Data_Produk_Master where "Barcode_Produk"="{}"'.format(Text)).fetchall()[0][0]
            # Barcode_Qty = self.page1_dsi_DBCursor.execute('select Quantity_Jual_Terkecil from Data_Produk_Master where "Barcode_Produk"="{}"'.format(Text)).fetchall()[0][0]
            # Barcode_SatuanJual = self.page1_dsi_DBCursor.execute('select Satuan_Jual_Terkecil from Data_Produk_Master where "Barcode_Produk"="{}"'.format(Text)).fetchall()[0][0]
            Barcode_HargaJual = self.page1_dsi_DBCursor.execute('select Harga_Jual_Saat_Diskon from Data_Produk_Master where "Barcode_Produk"="{}"'.format(Text)).fetchall()[0][0]
            Barcode_Grosir1 = self.page1_dsi_DBCursor.execute('select Harga_Jual_Saat_Diskon from Data_Produk_Master where "Barcode_Produk"="{}"'.format(Text)).fetchall()[0][0]
            Barcode_Grosir2 = self.page1_dsi_DBCursor.execute('select Harga_Jual_Saat_Diskon from Data_Produk_Master where "Barcode_Produk"="{}"'.format(Text)).fetchall()[0][0]
            Barcode_Grosir3 = self.page1_dsi_DBCursor.execute('select Harga_Jual_Saat_Diskon from Data_Produk_Master where "Barcode_Produk"="{}"'.format(Text)).fetchall()[0][0]
            while self.page1_dsi_TableWidget.rowCount() >= 2:
                self.page1_dsi_TableWidget.removeRow(1)
            else:
                self.page1_dsi_TableWidget.item(0, 0).setText(str(Barcode_No))
                self.page1_dsi_TableWidget.item(0, 1).setText(str(Barcode_KodeToko))
                self.page1_dsi_TableWidget.item(0, 2).setText(str(Barcode_Barcode))
                self.page1_dsi_TableWidget.item(0, 3).setText(str(Barcode_NamaItem))
                self.page1_dsi_TableWidget.item(0, 4).setText(str(Barcode_Stok))
                self.page1_dsi_TableWidget.item(0, 5).setText(str(Barcode_Satuan))
                self.page1_dsi_TableWidget.item(0, 6).setText(str(Barcode_PosisiBarang))
                # self.page1_dsi_TableWidget.item(0, 7).setText(str(Barcode_Qty))
                # self.page1_dsi_TableWidget.item(0, 8).setText(str(Barcode_SatuanJual))
                self.page1_dsi_TableWidget.item(0, 9).setText(str(Barcode_HargaJual))
                self.page1_dsi_TableWidget.item(0, 10).setText(str(Barcode_Grosir1))
                self.page1_dsi_TableWidget.item(0, 11).setText(str(Barcode_Grosir2))
                self.page1_dsi_TableWidget.item(0, 12).setText(str(Barcode_Grosir3))
        elif Text in Nama_Item:
            Nama_Item_No = 1
            Nama_Item_Barcode = Nama_Item[Text]
            Nama_Item_KodeToko = self.page1_dsi_DBCursor.execute("select Kode_Toko from '{}'".format(Nama_Item_Barcode)).fetchone()[0]
            Nama_Item_NamaItem = Text
            Nama_Item_Stok = int(self.page1_dsi_DBCursor.execute("select sum(Total_Stok_Sekarang) from '{}'".format(Nama_Item_Barcode)).fetchone()[0])
            Nama_Item_Satuan = self.page1_dsi_DBCursor.execute("select Total_Stok_Sekarang_Satuan from '{}'".format(Nama_Item_Barcode)).fetchone()[0]
            Nama_Item_PosisiBarang = self.page1_dsi_DBCursor.execute('select Posisi_Barang from Data_Produk_Master where "Nama_Produk_Di_Toko"="{}"'.format(Text)).fetchall()[0][0]
            # Nama_Item_Qty = self.page1_dsi_DBCursor.execute('select Quantity_Jual_Terkecil from Data_Produk_Master where "Nama_Produk_Di_Toko"="{}"'.format(Text)).fetchall()[0][0]
            # Nama_Item_SatuanJual = self.page1_dsi_DBCursor.execute('select Satuan_Jual_Terkecil from Data_Produk_Master where "Nama_Produk_Di_Toko"="{}"'.format(Text)).fetchall()[0][0]
            Nama_Item_HargaJual = self.page1_dsi_DBCursor.execute('select Harga_Jual_Saat_Diskon from Data_Produk_Master where "Nama_Produk_Di_Toko"="{}"'.format(Text)).fetchall()[0][0]
            Nama_Item_Grosir1 = self.page1_dsi_DBCursor.execute('select Harga_Jual_Saat_Diskon from Data_Produk_Master where "Nama_Produk_Di_Toko"="{}"'.format(Text)).fetchall()[0][0]
            Nama_Item_Grosir2 = self.page1_dsi_DBCursor.execute('select Harga_Jual_Saat_Diskon from Data_Produk_Master where "Nama_Produk_Di_Toko"="{}"'.format(Text)).fetchall()[0][0]
            Nama_Item_Grosir3 = self.page1_dsi_DBCursor.execute('select Harga_Jual_Saat_Diskon from Data_Produk_Master where "Nama_Produk_Di_Toko"="{}"'.format(Text)).fetchall()[0][0]
            while self.page1_dsi_TableWidget.rowCount() >= 2:
                self.page1_dsi_TableWidget.removeRow(1)
            else:
                self.page1_dsi_TableWidget.item(0, 0).setText(str(Nama_Item_No))
                self.page1_dsi_TableWidget.item(0, 1).setText(str(Nama_Item_KodeToko))
                self.page1_dsi_TableWidget.item(0, 2).setText(str(Nama_Item_Barcode))
                self.page1_dsi_TableWidget.item(0, 3).setText(str(Nama_Item_NamaItem))
                self.page1_dsi_TableWidget.item(0, 4).setText(str(Nama_Item_Stok))
                self.page1_dsi_TableWidget.item(0, 5).setText(str(Nama_Item_Satuan))
                self.page1_dsi_TableWidget.item(0, 6).setText(str(Nama_Item_PosisiBarang))
                # self.page1_dsi_TableWidget.item(0, 7).setText(str(Nama_Item_Qty))
                # self.page1_dsi_TableWidget.item(0, 8).setText(str(Nama_Item_SatuanJual))
                self.page1_dsi_TableWidget.item(0, 9).setText(str(Nama_Item_HargaJual))
                self.page1_dsi_TableWidget.item(0, 10).setText(str(Nama_Item_Grosir1))
                self.page1_dsi_TableWidget.item(0, 11).setText(str(Nama_Item_Grosir2))
                self.page1_dsi_TableWidget.item(0, 12).setText(str(Nama_Item_Grosir3))
        else:
            Dialog = QtWidgets.QMessageBox()
            Dialog.setWindowFlags(Qt.WindowTitleHint | Qt.WindowStaysOnTopHint)
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setWindowTitle('Peringatan')
            Dialog.setText('Item tidak ditemukan')
            Dialog.setModal(True)
            Dialog.show()
            Dialog.exec_()
            pass

    def Page1_dsi_Frame_Edited(self):
        self.page1_dsi_Frame.setStyleSheet('background-color: black; color: white;')

    def Page1_dsi_Label_Edited(self):
        self.page1_dsi_Label.setFont(Font(9, True))
        self.page1_dsi_Label.setText('{}, {} {} {}'.format(self.Data.page1_HariSekarang, self.Data.page1_TanggalSekarang, self.Data.page1_BulanSekarang, self.Data.page1_TahunSekarang))

    def Page1_dsi_Label_2_Edited(self):
        self.page1_dsi_Label_2.setFont(Font(9, True))
        self.page1_dsi_Label_2.setText('- {}:{}:{}'.format(self.Data.page1_JamSekarang, self.Data.page1_MenitSekarang,
                                                           self.Data.page1_DetikSekarang))

    def Page1_dsi_Label_3_Edited(self):
        self.page1_dsi_Label_3.setFont(Font(9, True))

    def Page1_dsi_Label_4_Edited(self):
        self.page1_dsi_Label_4.setFont(Font(9, True))
        self.page1_dsi_Label_4.setText(self.Data.username)

    def Page1_dsi_PushButton_Edited(self):
        self.page1_dsi_PushButton.setStyleSheet(ButtonStyleSheets1(CekResolusi()))

    def Page1_dsi_PushButton_Clicked(self):
        self.Data.pushButton_13.click()

    def Page1_dsi_TableWidget_Edited(self):
        DataNo = []
        Kolom = ['No', 'Kode_Toko', 'Barcode_Produk', 'NamaItem', 'Total_Stok', 'Satuan', 'PosisiBarang', 'Qty',
                 'Satuan_Jual', 'Harga_Jual', 'Harga_Diskon', 'Grosir_1', 'Grosir_2']
        self.page1_dsi_TableWidget.setSelectionBehavior(1)
        self.page1_dsi_TableWidget.setColumnCount(len(Kolom))
        self.page1_dsi_TableWidget.setHorizontalHeaderLabels(Kolom)
        self.page1_dsi_TableWidget.verticalHeader().setVisible(False)
        self.page1_dsi_TableWidget.horizontalHeader().setDefaultAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.page1_dsi_TableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.page1_dsi_TableWidget.horizontalHeader().setFont(Font(9, True))
        No = self.page1_dsi_DBCursor.execute('SELECT No FROM Data_Produk_Master').fetchall()
        for no in No:
            DataNo.append(no[0])

        for row in range(len(DataNo)):
            no = str(DataNo[row])
            self.page1_dsi_TableWidget.insertRow(row)
            self.page1_dsi_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(no))
            self.page1_dsi_TableWidget.item(row, 0).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

            KodeToko = self.page1_dsi_DBCursor.execute('select Kode_Toko from Data_Produk_Master where "No"="{}"'.format(no)).fetchall()[0][0]
            self.page1_dsi_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(KodeToko))

            Barcode = \
                self.page1_dsi_DBCursor.execute('select Barcode_Produk from Data_Produk_Master where "No"="{}"'.format(no)).fetchall()[
                    0][0]
            self.page1_dsi_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(Barcode))

            Nama_Item = self.page1_dsi_DBCursor.execute(
                'select Nama_Produk_Di_Toko from Data_Produk_Master where "No"="{}"'.format(no)).fetchall()[0][0]
            self.page1_dsi_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(Nama_Item))

            Stok = \
                self.page1_dsi_DBCursor.execute(
                    'select Total_Stok from Data_Produk_Master where "No"="{}"'.format(no)).fetchall()[0][
                    0]
            self.page1_dsi_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(Stok))
            self.page1_dsi_TableWidget.item(row, 4).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

            Satuan = \
                self.page1_dsi_DBCursor.execute(
                    'select Total_Stok_Satuan from Data_Produk_Master where "No"="{}"'.format(no)).fetchall()[
                    0][0]
            self.page1_dsi_TableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(Satuan))

            Posisi_Barang = self.page1_dsi_DBCursor.execute(
                'select Posisi_Barang from Data_Produk_Master where "No"="{}"'.format(no)).fetchall()[0][0]
            self.page1_dsi_TableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(Posisi_Barang))

            # Qty = self.page1_dsi_DBCursor.execute(
            #     'select Quantity_Jual_Terkecil from Data_Produk_Master where "No"="{}"'.format(no)).fetchall()[0][0]
            # self.page1_dsi_TableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(Qty))
            # self.page1_dsi_TableWidget.item(row, 7).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            #
            # Satuan_Jual_Terkecil = self.page1_dsi_DBCursor.execute(
            #     'select Satuan_Jual_Terkecil from Data_Produk_Master where "No"="{}"'.format(no)).fetchall()[0][0]
            # self.page1_dsi_TableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(Satuan_Jual_Terkecil))

            HargaJual = self.page1_dsi_DBCursor.execute(
                'select Harga_Jual_Saat_Diskon from Data_Produk_Master where "No"="{}"'.format(no)).fetchall()[0][0]
            self.page1_dsi_TableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(HargaJual))
            self.page1_dsi_TableWidget.item(row, 9).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

            Diskon1 = \
                self.page1_dsi_DBCursor.execute(
                    'select Harga_Jual_Saat_Grosir_1 from Data_Produk_Master where "No"="{}"'.format(no)).fetchall()[
                    0][0]
            self.page1_dsi_TableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(Diskon1))
            self.page1_dsi_TableWidget.item(row, 10).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

            Diskon2 = \
                self.page1_dsi_DBCursor.execute(
                    'select Harga_Jual_Saat_Grosir_2 from Data_Produk_Master where "No"="{}"'.format(no)).fetchall()[
                    0][0]
            self.page1_dsi_TableWidget.setItem(row, 11, QtWidgets.QTableWidgetItem(Diskon2))
            self.page1_dsi_TableWidget.item(row, 11).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

            Diskon3 = \
                self.page1_dsi_DBCursor.execute(
                    'select Harga_Jual_Saat_Grosir_3 from Data_Produk_Master where "No"="{}"'.format(no)).fetchall()[
                    0][0]
            self.page1_dsi_TableWidget.setItem(row, 12, QtWidgets.QTableWidgetItem(Diskon3))
            self.page1_dsi_TableWidget.item(row, 12).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.page1_dsi_DBConnection.commit()

    def Page1_dsi_PushButton_3_Edited(self):
        self.page1_dsi_LineEdit.clear()
        self.page1_dsi_TableWidget.setRowCount(0)
        self.Page1_dsi_TableWidget_Edited()
        self.page1_dsi_TableWidget.scrollToTop()

    def Page1_dsi_Frame_2_Edited(self):
        self.page1_dsi_Frame_2.setStyleSheet(FrameStyleSheets3(CekResolusi()))

    def Page1_lineEdit_2_Edited(self):
        text = self.Data.lineEdit_2.text()
        Rows = self.page1_dsi_TableWidget.rowCount()
        ListBarcode = []
        for row in range(Rows):
            ListBarcode.append(self.page1_dsi_TableWidget.item(row, 2).text())
        if text in ListBarcode:
            pass
        else:
            pass

    def Page1_pushButton_7_Edited(self):
        text = self.Data.lineEdit_2.text()
        Rows = self.page1_dsi_TableWidget.rowCount()
        Page1_Rows = self.Data.tableWidget_2.rowCount()

        Page1_ListKodeToko = []
        Page1_ListBarcode = []
        Page1_ListNamaItem = []
        for Page1_row in range(Page1_Rows):
            if self.Data.tableWidget_2.item(Page1_row, 1).text() not in Page1_ListKodeToko:
                Page1_ListKodeToko.append(self.Data.tableWidget_2.item(Page1_row, 1).text())
            else:
                pass
            if self.Data.tableWidget_2.item(Page1_row, 2).text() not in Page1_ListBarcode:
                Page1_ListBarcode.append(self.Data.tableWidget_2.item(Page1_row, 2).text())
            else:
                pass
            if self.Data.tableWidget_2.item(Page1_row, 3).text() not in Page1_ListNamaItem:
                Page1_ListNamaItem.append(self.Data.tableWidget_2.item(Page1_row, 3).text())
            else:
                pass

        ListKodeToko = []
        ListBarcode = []
        ListNamaItem = []
        for row in range(Rows):
            ListKodeToko.append(self.page1_dsi_TableWidget.item(row, 1).text())
            ListBarcode.append(self.page1_dsi_TableWidget.item(row, 2).text())
            ListNamaItem.append(self.page1_dsi_TableWidget.item(row, 3).text())

        if text == '':
            pass
        elif text in Page1_ListKodeToko:
            BarisItem_diPage1 = Page1_ListKodeToko.index(text)
            BarisItem_diPage1_dsi = ListKodeToko.index(text)
            Qtyawal = int(self.Data.tableWidget_2.item(BarisItem_diPage1, 4).text())
            Qtytambah = 1
            QtyAkhir = Qtyawal + Qtytambah
            self.Data.tableWidget_2.item(BarisItem_diPage1, 4).setText(str(QtyAkhir))
            self.Data.tableWidget_2.setCurrentCell(BarisItem_diPage1, 4)
        elif text in Page1_ListBarcode:
            BarisItem_diPage1 = Page1_ListBarcode.index(text)
            BarisItem_diPage1_dsi = ListBarcode.index(text)
            Qtyawal = int(self.Data.tableWidget_2.item(BarisItem_diPage1, 4).text())
            Qtytambah = 1
            QtyAkhir = Qtyawal + Qtytambah
            self.Data.tableWidget_2.item(BarisItem_diPage1, 4).setText(str(QtyAkhir))
            self.Data.tableWidget_2.setCurrentCell(BarisItem_diPage1, 4)
        elif text in Page1_ListNamaItem:
            BarisItem_diPage1 = Page1_ListNamaItem.index(text)
            BarisItem_diPage1_dsi = ListNamaItem.index(text)
            Qtyawal = int(self.Data.tableWidget_2.item(BarisItem_diPage1, 4).text())
            try:
                Qtytambah = int(self.page1_dsi_TableWidget.item(BarisItem_diPage1_dsi, 7).text())
            except Exception as e:
                print("EXCEPTION ERROR in 'def Page1_pushButton_7_Edited(self)' Function : ", e)
                Qtytambah = 1
                print("EXCEPTION ERROR PASSED")
            QtyAkhir = Qtyawal + Qtytambah
            self.Data.tableWidget_2.item(BarisItem_diPage1, 4).setText(str(QtyAkhir))
            self.Data.tableWidget_2.setCurrentCell(BarisItem_diPage1, 4)
        else:
            if text in ListBarcode:
                indexRow = ListBarcode.index(text)
                pass
            elif text in ListKodeToko:
                indexRow = ListKodeToko.index(text)
            elif text in ListNamaItem:
                indexRow = ListNamaItem.index(text)
            else:
                indexRow = '000'

            if indexRow != '000':
                Baris = self.Data.tableWidget_2.rowCount()
                No = Baris + 1
                Kode = self.page1_dsi_TableWidget.item(indexRow, 1).text()
                Barcode = self.page1_dsi_TableWidget.item(indexRow, 2).text()
                NamaItem = self.page1_dsi_TableWidget.item(indexRow, 3).text()
                Qty = '1'
                HargaSatuan = self.page1_dsi_TableWidget.item(indexRow, 9).text()
                SubTotal = int(Qty) * int(HargaSatuan)
                Diskon = '0'
                Total = (int(Qty) * int(HargaSatuan)) - ((int(Qty) * int(Diskon)))
                self.Data.tableWidget_2.insertRow(Baris)
                self.Data.tableWidget_2.setItem(Baris, 0, QtWidgets.QTableWidgetItem(str(No)))
                self.Data.tableWidget_2.setItem(Baris, 1, QtWidgets.QTableWidgetItem(str(Kode)))
                self.Data.tableWidget_2.setItem(Baris, 2, QtWidgets.QTableWidgetItem(str(Barcode)))
                self.Data.tableWidget_2.setItem(Baris, 3, QtWidgets.QTableWidgetItem(str(NamaItem)))
                self.Data.tableWidget_2.setItem(Baris, 4, QtWidgets.QTableWidgetItem(str(Qty)))
                self.Data.tableWidget_2.setItem(Baris, 5, QtWidgets.QTableWidgetItem(str(HargaSatuan)))
                self.Data.tableWidget_2.setItem(Baris, 6, QtWidgets.QTableWidgetItem(str(SubTotal)))
                self.Data.tableWidget_2.setItem(Baris, 7, QtWidgets.QTableWidgetItem(str(Diskon)))
                self.Data.tableWidget_2.setItem(Baris, 8, QtWidgets.QTableWidgetItem(str(Total)))
                self.Data.tableWidget_2.setCurrentCell(Baris, 4)
            else:
                pass

        self.Data.lineEdit_2.clear()
        self.Data.tableWidget_2.setFocus()
        self.Data.lineEdit_2.setFocus()

    def Page1_CekDiskon(self):
        BarisSekarang = self.Data.tableWidget_2.currentRow()
        KodeSekarang = self.Data.tableWidget_2.item(BarisSekarang, 1).text()
        QtySekarang = self.Data.tableWidget_2.item(BarisSekarang, 4).text()
        KodeDatabase = []
        Diskon1Database = []
        Diskon2Database = []
        Diskon3Database = []
        BanyakDataDalamDatabase = self.page1_dsi_TableWidget.rowCount()
        for kode in range(BanyakDataDalamDatabase):
            KodeDatabase.append(self.page1_dsi_TableWidget.item(kode, 1).text())
            Diskon1Database.append(self.page1_dsi_TableWidget.item(kode, 10).text())
            Diskon2Database.append(self.page1_dsi_TableWidget.item(kode, 11).text())
            Diskon3Database.append(self.page1_dsi_TableWidget.item(kode, 12).text())
        DiskonSekarang = 0
        # if int(QtySekarang) < 3:
        #     DiskonSekarang = 0
        # elif int(QtySekarang) < 6:
        #     index = KodeDatabase.index(KodeSekarang)
        #     DiskonSekarang = Diskon1Database[index]
        # elif int(QtySekarang) < 9:
        #     index = KodeDatabase.index(KodeSekarang)
        #     DiskonSekarang = Diskon2Database[index]
        # elif int(QtySekarang) >= 9:
        #     index = KodeDatabase.index(KodeSekarang)
        #     DiskonSekarang = Diskon3Database[index]
        # else:
        #     DiskonSekarang = 0
        self.Data.tableWidget_2.item(BarisSekarang, 7).setText(str(DiskonSekarang))

    def Page1_Kolom_Qty_Diskon_Harga_Berubah(self):
        try:
            TotalTransaksi = 0
            BarisSekarang = self.Data.tableWidget_2.currentRow()
            if BarisSekarang >= 0:
                QtySekarang = self.Data.tableWidget_2.item(BarisSekarang, 4).text()
                HargaJualSekarang = self.Data.tableWidget_2.item(BarisSekarang, 5).text()
                self.Page1_CekDiskon()
                HargaSubTotal = int(QtySekarang) * int(HargaJualSekarang)
                DiskonSekarang = self.Data.tableWidget_2.item(BarisSekarang, 7).text()
                HargaTotal = (int(QtySekarang) * int(HargaJualSekarang)) - (int(QtySekarang) * int(DiskonSekarang))
                self.Data.tableWidget_2.item(BarisSekarang, 6).setText(str(HargaSubTotal))
                self.Data.tableWidget_2.item(BarisSekarang, 8).setText(str(HargaTotal))
                for data in range(self.Data.tableWidget_2.rowCount()):
                    TotalTransaksi += int(self.Data.tableWidget_2.item(data, 8).text())
            else:
                pass
            self.Data.label_50.setText(str(TotalTransaksi))
        except:
            MessegeBox = QtWidgets.QMessageBox()
            MessegeBox.setText('Salah satu dari Kolom Qty atau Diskon ada yang salah input, silakan benarkan kembali')
            MessegeBox.isModal()
            MessegeBox.show()
            MessegeBox.exec_()
            pass

    def Page1_HapusItem(self):
        BarisSekarang = self.Data.tableWidget_2.currentRow()
        self.Data.tableWidget_2.removeRow(BarisSekarang)
        self.Data.lineEdit_2.setFocus()

    def Page1_BatalkanTransaksi(self):
        JumlahBaris = self.Data.tableWidget_2.rowCount()
        while JumlahBaris != 0:
            for Baris in range(JumlahBaris):
                self.Data.tableWidget_2.removeRow(Baris)
            JumlahBaris = self.Data.tableWidget_2.rowCount()
        else:
            pass
        self.Data.lineEdit_2.setFocus()

    def Page1_Bayar(self):
        BanyakBaris = self.Data.tableWidget_2.rowCount()
        if BanyakBaris <= 0:
            self.Data.lineEdit_2.setFocus()
            pass
        else:
            Dialog = QtWidgets.QDialog()
            Dialog.setWindowFlags(Qt.WindowTitleHint | Qt.WindowStaysOnTopHint)
            Dialog.setModal(True)
            Dialog.setWindowTitle('Pembayaran')
            GridLayout = QtWidgets.QGridLayout(Dialog)

            Label1 = QtWidgets.QLabel('Total Transaksi : ')
            GridLayout.addWidget(Label1, 0, 0)

            LineEdit1 = QtWidgets.QLineEdit()
            LineEdit1.setText(self.Data.label_50.text())
            LineEdit1.setStyleSheet('background-color: #F0F0F0')
            LineEdit1.setFrame(False)
            LineEdit1.setReadOnly(True)
            GridLayout.addWidget(LineEdit1, 0, 1)

            Label2 = QtWidgets.QLabel('Bayar : ')
            GridLayout.addWidget(Label2, 1, 0)

            LineEdit2 = QtWidgets.QLineEdit()
            LineEdit2.setText('0')
            LineEdit2.setPlaceholderText('0')
            LineEdit2.setValidator(IntegerValidator())
            GridLayout.addWidget(LineEdit2, 1, 1)

            Label3 = QtWidgets.QLabel('Kembalian : ')
            GridLayout.addWidget(Label3, 2, 0)

            LineEdit3 = QtWidgets.QLineEdit()
            LineEdit3.setStyleSheet('background-color: #F0F0F0')
            LineEdit3.setFrame(False)
            LineEdit3.setReadOnly(True)
            LineEdit3.setText('0')
            GridLayout.addWidget(LineEdit3, 2, 1)

            HorizontalLayout = QtWidgets.QHBoxLayout()
            GridLayout.addLayout(HorizontalLayout, 3, 1)

            PushButton1 = QtWidgets.QPushButton('OK')
            HorizontalLayout.addWidget(PushButton1)

            PushButton2 = QtWidgets.QPushButton('Batalkan')
            HorizontalLayout.addWidget(PushButton2)

            '''PERINTAH : '''
            LineEdit2.setFocus()

            def HitunganKembalian():
                if LineEdit2.text() == '':
                    Bayar = 0
                else:
                    Bayar = int(LineEdit2.text())
                Tagihan = int(LineEdit1.text())
                Kembalian = str(Bayar - Tagihan)
                LineEdit3.setText(Kembalian)
                return Kembalian

            def Simpan():
                if int(LineEdit2.text()) < int(LineEdit1.text()):
                    Dialog2 = QtWidgets.QMessageBox()
                    Dialog2.setWindowFlags(Qt.WindowTitleHint | Qt.WindowStaysOnTopHint)
                    Dialog2.setWindowTitle('Peringatan')
                    Dialog2.setText('Uang yang dibayarkan kurang dari harga belanjaan')
                    Dialog2.setModal(True)
                    Dialog2.show()
                    Dialog2.exec_()
                else:
                    Dialog.close()
                    self.Data.Bayar.append(LineEdit2.text())
                    self.Data.Kembalian.append(LineEdit3.text())
                    self.Page1_UpdateDatabaseSetelahTransaksi()
                    self.Page1_UpdateExcellSetelahTransaksi()
                    self.Page1_CetakStruk2()
                pass

            Dialog.show()
            # HitunganKembalian()
            LineEdit1.textChanged.connect(HitunganKembalian)
            LineEdit2.textChanged.connect(HitunganKembalian)
            PushButton1.clicked.connect(Simpan)
            PushButton2.clicked.connect(Dialog.close)
            Dialog.exec_()

            self.Data.lineEdit_2.setFocus()
            return HitunganKembalian()

    def Page1_HitungDiskonUntukStruk(self):
        TotalDiskon = 0
        BanyakBaris = self.Data.tableWidget_2.rowCount()
        for item in range(BanyakBaris):
            Qty = self.Data.tableWidget_2.item(item, 4).text()
            DiskonPerQty = self.Data.tableWidget_2.item(item, 7).text()
            Diskon = int(Qty) * int(DiskonPerQty)
            TotalDiskon += Diskon
        return str(TotalDiskon)

    def Page1_CetakStruk2(self):
        if len(self.Data.Bayar) < 1:
            self.Data.lineEdit_2.setFocus()
            pass
        else:
            CekData = self.Data.tableWidget_2.rowCount()
            if CekData <= 0:
                self.Data.lineEdit_2.setFocus()
                pass
            else:
                # Image Nomor Transaksi (Lebar Kertas : 383 px, tinggi per baris kelipatan 30px)
                NomorTransaksi = self.Data.lineEdit_5.text()
                WaktuTransaksi = self.Data.lineEdit_21.text()
                fnt0 = ImageFont.truetype(r'D:\PYTHON\PROJECT\AllProject\APLIKASI_TOKO\SOURCE\Oswald-Regular.ttf', 22)
                img0 = Image.new('RGB', (383, 120), color=(255, 255, 255))
                d0 = ImageDraw.Draw(img0)
                d0.text((0, 0), '', font=fnt0, fill=(0, 0, 0), )
                d0.text((63, 30), 'No.Transaksi : {}'.format(NomorTransaksi), font=fnt0, fill=(0, 0, 0))
                d0.text((93, 60), '{}'.format(WaktuTransaksi), font=fnt0, fill=(0, 0, 0))
                d0.text((0, 90), '', font=fnt0, fill=(0, 0, 0))
                img0.save('NomorTransaksi.png')

                # Image Isi Transaksi
                JumlahRows = self.Data.tableWidget_2.rowCount()
                fnt1 = ImageFont.truetype(r'D:\PYTHON\PROJECT\AllProject\APLIKASI_TOKO\SOURCE\Oswald-Regular.ttf', 22)
                PerTransactionImage = []
                for row in range(JumlahRows):
                    No = self.Data.tableWidget_2.item(row, 0).text()
                    NamaItem = self.Data.tableWidget_2.item(row, 3).text()
                    Kuantitas = self.Data.tableWidget_2.item(row, 4).text()
                    HargaSubTotal = self.Data.tableWidget_2.item(row, 6).text()
                    Diskon = self.Data.tableWidget_2.item(row, 7).text()
                    HargaTotal = self.Data.tableWidget_2.item(row, 8).text()

                    TextJudul = '{}. {}'.format(No, NamaItem)
                    TextQty = ' (Qty : {}, Disc : @Rp {},-)'.format(Kuantitas, Diskon) + str(
                        (30 - len(' (Qty : {}, Diskon : {} x Rp {},-)'.format(Kuantitas, Kuantitas, Diskon))) * '..')
                    TextHarga = 'Rp {},-'.format(HargaSubTotal)
                    TextHarga = ((15 - len(TextHarga)) * '  ') + TextHarga
                    pembagi1 = 38

                    # Parsing baris
                    TextJudulFix = TextJudul
                    JumlahKarakter_TextJudulFix = len(TextJudulFix)

                    # Cek apakah text judul fix habis dibagi 23:
                    Text1 = JumlahKarakter_TextJudulFix % pembagi1

                    if Text1 != 0:
                        JumlahBaris = int(JumlahKarakter_TextJudulFix / pembagi1) + 1
                        img = Image.new('RGB', (383, int((JumlahBaris * 30) + 45)), color=(255, 255, 255))
                        d = ImageDraw.Draw(img)
                        for Baris in range(int(JumlahBaris)):
                            if (Baris + 1) == int(JumlahBaris):
                                Text2 = TextJudulFix[(Baris * pembagi1):((Baris + 1) * pembagi1)]
                                d.text((0, (Baris * 30)), Text2, font=fnt1, fill=(0, 0, 0))
                                d.text((0, ((Baris + 1) * 30)), TextQty, font=fnt1, fill=(0, 0, 0))
                                d.text((240, ((Baris + 1) * 30)), TextHarga, font=fnt1, fill=(0, 0, 0))
                                # d.text((0, ((Baris+1)*30)), '', font=fnt1, fill=(0, 0, 0))
                            elif Baris == 0:
                                Text2 = TextJudulFix[(Baris * pembagi1):((Baris + 1) * pembagi1)] + '-'
                                d.text((0, (Baris * 30)), Text2, font=fnt1, fill=(0, 0, 0))
                            else:
                                Text2 = TextJudulFix[(Baris * pembagi1):((Baris + 1) * pembagi1)] + '-'
                                d.text((0, (Baris * 30)), Text2, font=fnt1, fill=(0, 0, 0))
                    else:
                        JumlahBaris = int(JumlahKarakter_TextJudulFix / pembagi1)
                        img = Image.new('RGB', (383, (int((JumlahBaris + 1) * 30) + 15)), color=(255, 255, 255))
                        d = ImageDraw.Draw(img)
                        for Baris in range(int(JumlahBaris)):
                            if (Baris + 1) == int(JumlahBaris):
                                Text2 = TextJudulFix[(Baris * pembagi1):((Baris + 1) * pembagi1)]
                                d.text((0, (Baris * 30)), Text2, font=fnt1, fill=(0, 0, 0))
                                d.text((0, ((Baris + 1) * 30)), TextQty, font=fnt1, fill=(0, 0, 0))
                                d.text((240, ((Baris + 1) * 30)), TextHarga, font=fnt1, fill=(0, 0, 0))
                            elif Baris == 0:
                                Text2 = TextJudulFix[(Baris * pembagi1):((Baris + 1) * pembagi1)] + '-'
                                d.text((0, (Baris * 30)), Text2, font=fnt1, fill=(0, 0, 0))
                            else:
                                Text2 = TextJudulFix[(Baris * pembagi1):((Baris + 1) * pembagi1)] + '-'
                                d.text((0, (Baris * 30)), Text2, font=fnt1, fill=(0, 0, 0))
                    img.save('Transaksi{}.png'.format(row))
                    PerTransactionImage.append('Transaksi{}.png'.format(row))
                TransactionImage = [Image.open(y) for y in PerTransactionImage]
                TransactionImage_widths, TransactionImage_heights = zip(*(i.size for i in TransactionImage))
                TransactionImage_max_width = max(TransactionImage_widths)
                TransactionImage_total_height = sum(TransactionImage_heights)
                new_TransactionImage = Image.new('RGB', (TransactionImage_max_width, TransactionImage_total_height),
                                                 color=(255, 255, 255))
                y_offset = 0
                for im in TransactionImage:
                    new_TransactionImage.paste(im, (0, y_offset))
                    y_offset += im.size[1]
                new_TransactionImage.save('TransaksiTotal.png')

                # Image Total Transaksi (Lebar Kertas : 383 px, tinggi per baris kelipatan 40px)
                TotalTransaksi = self.Data.label_50.text()
                fnt2 = ImageFont.truetype(r'D:\PYTHON\PROJECT\AllProject\APLIKASI_TOKO\SOURCE\Oswald-Bold.ttf', 26)
                img2 = Image.new('RGB', (383, 240), color=(255, 255, 255))
                d2 = ImageDraw.Draw(img2)
                d2.text((10, 0), '', font=fnt2, fill=(0, 0, 0))
                d2.text((10, 40), 'Diskon : Rp {},-'.format(self.Page1_HitungDiskonUntukStruk()), font=fnt2,
                        fill=(0, 0, 0))
                d2.text((10, 80), 'TOTAL : Rp {},-'.format(TotalTransaksi), font=fnt2, fill=(0, 0, 0))
                d2.text((10, 120), 'Bayar : Rp {},-'.format(self.Data.Bayar[0]), font=fnt2, fill=(0, 0, 0))
                d2.text((10, 160), 'Kembalian : Rp {},-'.format(self.Data.Kembalian[0]), font=fnt2, fill=(0, 0, 0))
                d2.text((10, 200), '', font=fnt2, fill=(0, 0, 0))
                img2.save('TotalTransaksi.png')

                # DaftarImage Buat Struk:
                header = r'D:\PYTHON\PROJECT\AllProject\APLIKASI_TOKO\SOURCE\0PrinterHeader.png'
                nomorTransaksi = 'NomorTransaksi.png'
                detailTransaksi = 'TransaksiTotal.png'
                totalTransaksi = 'TotalTransaksi.png'
                footer = r'D:\PYTHON\PROJECT\AllProject\APLIKASI_TOKO\SOURCE\0PrinterFooter.png'

                IsiStruk = [header, nomorTransaksi, detailTransaksi, totalTransaksi, footer]
                StrukItemImage = [Image.open(y) for y in IsiStruk]
                StrukItem_widths, StrukItem_heights = zip(*(i.size for i in StrukItemImage))
                Struk_max_width = max(StrukItem_widths)
                Struk_total_height = sum(StrukItem_heights)
                StrukImage = Image.new('RGB', (Struk_max_width, Struk_total_height), color=(255, 255, 255))
                y_offset = 0
                for im in StrukItemImage:
                    StrukImage.paste(im, (0, y_offset))
                    y_offset += im.size[1]
                StrukName = '{}/{}.png'.format(self.Page1_FolderPenyimpananStruk, self.Data.lineEdit_5.text())
                StrukImage.save(StrukName)
                self.Data.lineEdit_2.setDisabled(True)

                # PRINT STRUK
                try:
                    try:
                        self.Data.MyPrinter = Usb(0x0483, 0x5840, 0, 0x58, 0x03)
                        try:
                            self.Data.MyPrinter.image(StrukName)
                        except:
                            pass
                        self.Data.MyPrinter.close()
                    except:
                        try:
                            self.Data.MyPrinter.image(StrukName)
                        except:
                            pass
                        self.Data.MyPrinter.close()
                except:
                    Dialog = QtWidgets.QMessageBox()
                    Dialog.setWindowFlags(Qt.WindowTitleHint | Qt.WindowStaysOnTopHint)
                    Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                    Dialog.setWindowTitle('Printer')
                    Dialog.setText('Printer tidak terdeteksi, nyalakan printer dan pastikan '
                                   'semua kabel telah terpasang dengan benar')
                    Dialog.setModal(True)
                    Dialog.show()
                    Dialog.exec_()
                    pass

                # DisableEditing
                Rows = self.Data.tableWidget_2.rowCount()
                for row in range(Rows):
                    cell_item4 = self.Data.tableWidget_2.item(row, 4)
                    cell_item4.setFlags(cell_item4.flags() ^ QtCore.Qt.ItemIsEditable)
                self.Data.pushButton_7.setDisabled(True)
                self.Data.pushButton_8.setDisabled(True)
                self.Data.pushButton_9.setDisabled(True)
                self.Data.pushButton_11.setDisabled(True)
                self.Data.pushButton_10.setEnabled(True)

    def Page1_SetEditableItemTable(self):
        Rows = self.Data.tableWidget_2.rowCount()
        for row in range(Rows):
            cell_item0 = self.Data.tableWidget_2.item(row, 0)
            cell_item0.setFlags(cell_item0.flags() ^ QtCore.Qt.ItemIsEditable)
            cell_item1 = self.Data.tableWidget_2.item(row, 1)
            cell_item1.setFlags(cell_item1.flags() ^ QtCore.Qt.ItemIsEditable)
            cell_item2 = self.Data.tableWidget_2.item(row, 2)
            cell_item2.setFlags(cell_item2.flags() ^ QtCore.Qt.ItemIsEditable)
            cell_item3 = self.Data.tableWidget_2.item(row, 3)
            cell_item3.setFlags(cell_item3.flags() ^ QtCore.Qt.ItemIsEditable)
            cell_item5 = self.Data.tableWidget_2.item(row, 5)
            cell_item5.setFlags(cell_item5.flags() ^ QtCore.Qt.ItemIsEditable)
            cell_item6 = self.Data.tableWidget_2.item(row, 6)
            cell_item6.setFlags(cell_item6.flags() ^ QtCore.Qt.ItemIsEditable)
            cell_item7 = self.Data.tableWidget_2.item(row, 7)
            cell_item7.setFlags(cell_item7.flags() ^ QtCore.Qt.ItemIsEditable)
            cell_item8 = self.Data.tableWidget_2.item(row, 8)
            cell_item8.setFlags(cell_item8.flags() ^ QtCore.Qt.ItemIsEditable)

    def Page1_SetTypeDataTable(self):
        Rows = self.Data.tableWidget_2.rowCount()
        for row in range(Rows):
            cell_Qty = self.Data.tableWidget_2.item(row, 4).text()
            cell_Diskon = self.Data.tableWidget_2.item(row, 7).text()
            try:
                int(cell_Qty) * 1
                pass
            except:
                self.Data.tableWidget_2.item(row, 4).setText('0')

            try:
                int(cell_Diskon) * 1
                pass
            except:
                self.Data.tableWidget_2.item(row, 7).setText('0')

    def Page1_TambahTransaksiBaru(self):
        folderTahun = self.TransaksiTokoTerkonfirmasiLOG + r'/{}'.format(self.yearNow)
        folderBulan = folderTahun + r'/{}. {}'.format(self.monthNow1, self.monthNow2)
        folderTanggal = folderBulan + r'/{}-{}-{}'.format(self.dateNow, self.monthNow2, self.yearNow)
        Lokasi = folderTanggal
        Lokasi2 = os.listdir(Lokasi)
        ListFolder = []
        for item in Lokasi2:
            Folder = str(Lokasi) + '/' + str(item)
            ListFolder.append(Folder)

        self.Data.Bayar.clear()
        self.Data.Kembalian.clear()
        self.Data.lineEdit_2.setEnabled(True)
        self.Data.pushButton_7.setEnabled(True)
        self.Data.pushButton_8.setEnabled(True)
        self.Data.pushButton_9.setEnabled(True)
        self.Data.pushButton_11.setEnabled(True)
        self.Data.pushButton_10.setDisabled(True)
        while self.Data.tableWidget_2.rowCount() > 0:
            self.Data.tableWidget_2.removeRow(0)
        else:
            pass
        self.Data.lineEdit_2.setFocus()

        NomorTransaksi = self.Data.lineEdit_5.text()
        CekFolder = Lokasi + str('/') + NomorTransaksi
        TransaksiHariIni = 0
        while CekFolder in ListFolder:
            TransaksiHariIni += 1
            if TransaksiHariIni < 10:
                Awalan = str(self.Data.page1_TahunSekarang) + str(self.Data.page1_BulanSekarangAngka) + str(
                    self.Data.page1_TanggalSekarang) + '-0000'
                NomorTransaksi = Awalan + str(TransaksiHariIni)
            elif TransaksiHariIni < 100:
                Awalan = str(self.Data.page1_TahunSekarang) + str(self.Data.page1_BulanSekarangAngka) + str(
                    self.Data.page1_TanggalSekarang) + '-000'
                NomorTransaksi = Awalan + str(TransaksiHariIni)
            elif TransaksiHariIni < 1000:
                Awalan = str(self.Data.page1_TahunSekarang) + str(self.Data.page1_BulanSekarangAngka) + str(
                    self.Data.page1_TanggalSekarang) + '-00'
                NomorTransaksi = Awalan + str(TransaksiHariIni)
            elif TransaksiHariIni < 1000000:
                Awalan = str(self.Data.page1_TahunSekarang) + str(self.Data.page1_BulanSekarangAngka) + str(
                    self.Data.page1_TanggalSekarang) + '-0'
                NomorTransaksi = Awalan + str(TransaksiHariIni)
            else:
                Awalan = str(self.Data.page1_TahunSekarang) + str(self.Data.page1_BulanSekarangAngka) + str(
                    self.Data.page1_TanggalSekarang) + ''
                NomorTransaksi = Awalan + str(TransaksiHariIni)
            CekFolder = Lokasi + str('/') + NomorTransaksi
            self.Data.lineEdit_5.setText(NomorTransaksi)
        else:
            CekFolder = Lokasi + str('/') + NomorTransaksi

        try:
            os.mkdir(CekFolder)
        except:
            print('tidak dapat membuat folder karena folder sudah ada')
            pass
        self.Page1_FolderPenyimpananStruk = CekFolder

    def Page1_UpdateDatabaseSetelahTransaksi(self):
        # Inisiasi Database
        DBconnection = sqlite3.connect(DatabaseProduk())
        DBcursor = DBconnection.cursor()

        # Inisiasi Data Penjualan
        ItemTerjual = []
        BanyakBaris = self.Data.tableWidget_2.rowCount()
        if BanyakBaris >= 1:
            for Baris in range(BanyakBaris):
                kodeToko = self.Data.tableWidget_2.item(Baris, 1).text()
                barcode = self.Data.tableWidget_2.item(Baris, 2).text()
                Qty = int(self.Data.tableWidget_2.item(Baris, 4).text())
                ItemTerjual.append(kodeToko)
                StokSebelumTransaksi = DBcursor.execute("select sum(Total_Stok_Sekarang) from '{}'".format(barcode)).fetchone()[0]
                ProsesTransaksi = int(StokSebelumTransaksi) - int(Qty)
                DBcursor.execute('UPDATE Data_Produk_Master SET `Total_Stok`="{}" WHERE "Kode_Toko"="{}"'.format(str(ProsesTransaksi), kodeToko))

                JumlahTransaksidiDatabase = DBcursor.execute("select * from '{}'".format(barcode)).fetchall()
                for item in range(len(JumlahTransaksidiDatabase)):
                    rowid_item = DBcursor.execute("select rowid from '{}'".format(barcode)).fetchall()[item][0]
                    stok_awal_tiap_transaksi = DBcursor.execute("select Total_Stok_Sekarang from '{}' where rowid='{}'".format(barcode, (item+1))).fetchone()[0]
                    if int(stok_awal_tiap_transaksi) - Qty > 0:
                        stok_akhir_tiap_transaksi = int(stok_awal_tiap_transaksi) - Qty
                        terjual = int(stok_awal_tiap_transaksi) - int(stok_akhir_tiap_transaksi)
                        Qty = 0
                    else:
                        if (item+1) < len(JumlahTransaksidiDatabase):
                            Qty = Qty - int(stok_awal_tiap_transaksi)
                            stok_akhir_tiap_transaksi = 0
                            terjual = int(stok_awal_tiap_transaksi) - int(stok_akhir_tiap_transaksi)
                        else:
                            stok_akhir_tiap_transaksi = int(stok_awal_tiap_transaksi) - Qty
                            terjual = int(stok_awal_tiap_transaksi) - int(stok_akhir_tiap_transaksi)
                    try:
                        try:
                            terjual_awal = int(DBcursor.execute("select Terjual from '{}' where No='{}'".format(barcode, item + 1)).fetchone()[0])
                        except:
                            terjual_awal = 0
                        if terjual_awal == None:
                            terjual_awal = 0
                        else:
                            pass
                    except:
                        terjual_awal = 0
                    terjual_total = int(terjual_awal) + int(terjual)

                    DBcursor.execute("UPDATE '{}' SET `Total_Stok_Sekarang`='{}' where No='{}'".format(barcode, stok_akhir_tiap_transaksi, str(item+1)))
                    DBcursor.execute("UPDATE '{}' SET `Terjual`='{}' where No='{}'".format(barcode, terjual_total, str(item+1)))
                    print("baris ke : {}, awal : {}, terjual : {}, stok akhir : {}, terjual akhir : {}".format(item, stok_awal_tiap_transaksi, terjual, stok_akhir_tiap_transaksi, terjual_total))




                DBcursor.execute("UPDATE '{}' SET Total_Stok_Sekarang='{}' WHERE 'Kode_Toko'='{}'".format(str(barcode), str(ProsesTransaksi), kodeToko))
                StokSetelahTransaksi = DBcursor.execute('select Kode_Toko,Total_Stok from Data_Produk_Master where "Kode_Toko"="{}"'.format(kodeToko)).fetchall()[0][1]

                print('Stok setelah transaksi : ', StokSetelahTransaksi)
        else:
            pass
        DBconnection.commit()
        DBconnection.close()

    def Page1_UpdateExcellSetelahTransaksi(self):
        dataframe = pd.read_excel(ExcellDanaToko(), sheet_name="Sheet1", index_col=False)
        row = len(dataframe)
        # wb = load_workbook(ExcellDanaToko())
        # sheet_names = wb.get_sheet_names()
        # name = sheet_names[0]
        # sheet_ranges = wb[name]
        # df = pd.DataFrame(sheet_ranges.values)
        print(dataframe)
        print(row)
        pass

    def Page1_Event_Tab1TabAnak1_Changed(self):
        pass
        # self.page1_dsi_PushButton_3.click()

    def Page1_dsi_ResolutionManager(self):
        Resolusi = CekResolusi()
        if Resolusi == '1280x720':
            self.page1_dsi_Frame.setFixedHeight(40)
            self.page1_dsi_PushButton.setMinimumSize(100, 25)
            self.page1_dsi_Frame_2.setMaximumHeight(110)
            self.page1_dsi_SpacerItem_4.changeSize(20, 25, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            self.page1_dsi_LineEdit.setMinimumSize(0, 20)
            self.page1_dsi_PushButton_2.setMinimumSize(100, 25)
            self.page1_dsi_TableWidget.horizontalHeader().setFixedHeight(35)
            self.page1_dsi_TableWidget.setColumnWidth(0, 25)
            self.page1_dsi_TableWidget.setColumnWidth(1, 125)
            self.page1_dsi_TableWidget.setColumnWidth(2, 100)
            self.page1_dsi_TableWidget.setColumnWidth(3, 150)
            self.page1_dsi_TableWidget.setColumnWidth(4, 50)
            self.page1_dsi_TableWidget.setColumnWidth(5, 75)
            self.page1_dsi_TableWidget.setColumnWidth(6, 150)
            self.page1_dsi_TableWidget.setColumnWidth(7, 50)
            self.page1_dsi_TableWidget.setColumnWidth(8, 125)
            self.page1_dsi_TableWidget.setColumnWidth(9, 100)
            self.page1_dsi_TableWidget.setColumnWidth(10, 75)
            self.page1_dsi_TableWidget.setColumnWidth(11, 75)
            self.page1_dsi_TableWidget.setColumnWidth(12, 75)
            self.page1_dsi_SpacerItem_2.changeSize(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            self.page1_dsi_PushButton_3.setMinimumSize(125, 35)

        else:

            self.page1_dsi_TableWidget.horizontalHeader().setFixedHeight(70)
            self.page1_dsi_TableWidget.setColumnWidth(0, 50)
            self.page1_dsi_TableWidget.setColumnWidth(1, 250)
            self.page1_dsi_TableWidget.setColumnWidth(2, 200)
            self.page1_dsi_TableWidget.setColumnWidth(3, 300)
            self.page1_dsi_TableWidget.setColumnWidth(4, 100)
            self.page1_dsi_TableWidget.setColumnWidth(5, 150)
            self.page1_dsi_TableWidget.setColumnWidth(6, 300)
            self.page1_dsi_TableWidget.setColumnWidth(7, 100)
            self.page1_dsi_TableWidget.setColumnWidth(8, 250)
            self.page1_dsi_TableWidget.setColumnWidth(9, 200)
            self.page1_dsi_TableWidget.setColumnWidth(10, 150)
            self.page1_dsi_TableWidget.setColumnWidth(11, 150)
            self.page1_dsi_TableWidget.setColumnWidth(12, 150)
            pass


class Page1_ht(Page1):
    # Page1_ht = Page1_HistoryTransaksi
    def __init__(self, data):
        self.Data = data
        super(Page1_ht, self).__init__()
        self.Page1_ht_InisiasiTab()
        self.Page1_ht_Frame()
        self.Page1_ht_HorizontalLayout()
        self.Page1_ht_Label()
        self.Page1_ht_SpacerItem()
        self.Page1_ht_Label_2()
        self.Page1_ht_Label_3()
        self.Page1_ht_pushButton()
        self.Page1_ht_Frame_2()
        self.Page1_ht_GridLayout_2()
        self.Page1_ht_Label_4()
        self.Page1_ht_Frame_4()
        self.Page1_ht_GridLayout_4()
        self.Page1_ht_Label_5()
        self.Page1_ht_LineEdit()
        self.Page1_ht_PushButton_2()
        self.Page1_ht_SpacerItem_2()
        self.Page1_ht_Label_6()
        self.Page1_ht_CalendarWiget()
        self.Page1_ht_HorizontalLayout_3()
        self.Page1_ht_PushButton_5()
        self.Page1_ht_PushButton_3()
        self.Page1_ht_Frame_3()
        self.Page1_ht_GridLayout_3()
        self.Page1_ht_Label_7()
        self.Page1_ht_TableWidget()
        self.Page1_ht_HorizontalLayout_2()
        self.Page1_ht_SpacerItem_3()
        self.Page1_ht_Frame_5()
        self.Page1_ht_GridLayout_5()
        self.Page1_ht_Label_8()
        self.Page1_ht_Label_9()
        self.Page1_ht_PushButton_4()
        self.Page1_ht_TableWidget_Edited()

        '''PERINTAH : '''
        self.Data.timer.timeout.connect(self.Page1_ht_Label_Edited)
        self.Data.tab1_TabAnak1.currentChanged.connect(self.Page1_ht_TableWidget_Edited)
        self.page1_ht_PushButton_4.clicked.connect(self.Page1_ht_PrintStruk)
        self.page1_ht_pushButton.clicked.connect(self.Page1_ht_PushButton_Edited)
        self.page1_ht_PushButton_2.clicked.connect(self.Page1_ht_PushButton_2_Edited)
        self.page1_ht_PushButton_3.clicked.connect(self.Page1_ht_PushButton_3_Edited)
        self.page1_ht_PushButton_5.clicked.connect(self.Page1_ht_PushButton_5_Edited)
        self.Page1_ht_ResolutionManager()

    def Page1_ht_InisiasiTab(self):
        self.page1_ht = QtWidgets.QWidget()
        self.page1_ht.setObjectName('ht')
        self.Data.tab1_TabAnak1.addTab(self.page1_ht, '')
        self.Data.tab1_TabAnak1.setTabText(self.Data.tab1_TabAnak1.indexOf(self.page1_ht), 'History Transaksi')

        # Layout for Tab History Transaksi :
        self.page1_ht_Layout = QtWidgets.QGridLayout(self.page1_ht)

    def Page1_ht_Frame(self):
        self.page1_ht_Frame = QtWidgets.QFrame()
        self.page1_ht_Frame.setStyleSheet('background-color: black; color: white;')
        self.page1_ht_Layout.addWidget(self.page1_ht_Frame, 0, 0, 1, 4)

    def Page1_ht_HorizontalLayout(self):
        self.page1_ht_HorizontalLayout = QtWidgets.QHBoxLayout(self.page1_ht_Frame)

    def Page1_ht_Label(self):
        self.page1_ht_label = QtWidgets.QLabel('Tanggal, Bulan, Tahun, Jam, Menit, Detik')
        self.page1_ht_label.setFont(Font(9, True))
        self.page1_ht_HorizontalLayout.addWidget(self.page1_ht_label)

    def Page1_ht_SpacerItem(self):
        self.page1_ht_separator = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Fixed)
        self.page1_ht_HorizontalLayout.addItem(self.page1_ht_separator)

    def Page1_ht_Label_2(self):
        self.page1_ht_label_2 = QtWidgets.QLabel('Pengguna : ')
        self.page1_ht_label_2.setFont(Font(9, True))
        self.page1_ht_HorizontalLayout.addWidget(self.page1_ht_label_2)

    def Page1_ht_Label_3(self):
        self.page1_ht_label_3 = QtWidgets.QLabel('Nama Pengguna')
        self.page1_ht_label_3.setText(self.Data.username)
        self.page1_ht_label_3.setFont(Font(9, True))
        self.page1_ht_HorizontalLayout.addWidget(self.page1_ht_label_3)

    def Page1_ht_pushButton(self):
        self.page1_ht_pushButton = QtWidgets.QPushButton('Logout')
        self.page1_ht_pushButton.setStyleSheet(ButtonStyleSheets1(CekResolusi()))
        self.page1_ht_pushButton.setMinimumSize(150, 50)
        self.page1_ht_HorizontalLayout.addWidget(self.page1_ht_pushButton)

    def Page1_ht_Frame_2(self):
        self.page1_ht_frame_2 = QtWidgets.QFrame()
        self.page1_ht_frame_2.setObjectName('page1_ht_frame_2')
        self.page1_ht_frame_2.setStyleSheet(FrameStyleSheets3(CekResolusi()))
        self.page1_ht_Layout.addWidget(self.page1_ht_frame_2, 1, 0, 1, 4)

    def Page1_ht_GridLayout_2(self):
        self.page1_ht_GridLayout_2 = QtWidgets.QGridLayout(self.page1_ht_frame_2)

    def Page1_ht_Label_4(self):
        self.page1_ht_label_4 = QtWidgets.QLabel('HISTORY TRANSAKSI')
        self.page1_ht_label_4.setMinimumSize(0, 100)
        self.page1_ht_label_4.setFont(Font(14, True))
        self.page1_ht_label_4.setAlignment(QtCore.Qt.AlignHCenter)
        self.page1_ht_GridLayout_2.addWidget(self.page1_ht_label_4, 0, 0)

    def Page1_ht_Frame_4(self):
        self.page1_ht_Frame_4 = QtWidgets.QFrame()
        self.page1_ht_Frame_4.setObjectName('page1_ht_Frame_4')
        self.page1_ht_Frame_4.setMaximumSize(800, 160000)
        self.page1_ht_Frame_4.setStyleSheet(FrameStyleSheets2(CekResolusi()))
        self.page1_ht_Layout.addWidget(self.page1_ht_Frame_4, 2, 0)

    def Page1_ht_GridLayout_4(self):
        self.page1_ht_GridLayout_4 = QtWidgets.QGridLayout(self.page1_ht_Frame_4)

    def Page1_ht_Label_5(self):
        self.page1_ht_label_5 = QtWidgets.QLabel('Masukkan Nomor Transaksi : ')
        self.page1_ht_GridLayout_4.addWidget(self.page1_ht_label_5, 0, 0)

    def Page1_ht_LineEdit(self):
        self.page1_ht_LineEdit = QtWidgets.QLineEdit()
        self.page1_ht_LineEdit.setMaximumSize(400, 50)
        self.page1_ht_GridLayout_4.addWidget(self.page1_ht_LineEdit, 0, 1)

    def Page1_ht_PushButton_2(self):
        self.page1_ht_PushButton_2 = QtWidgets.QPushButton('Tampilkan')
        self.page1_ht_GridLayout_4.addWidget(self.page1_ht_PushButton_2, 0, 2)

    def Page1_ht_SpacerItem_2(self):
        self.page1_ht_SpacerItem_2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Fixed)
        self.page1_ht_GridLayout_4.addItem(self.page1_ht_SpacerItem_2, 1, 0, 1, 3)

    def Page1_ht_Label_6(self):
        self.page1_ht_Label_6 = QtWidgets.QLabel('Atau pilih berdasarkan tanggal : ')
        self.page1_ht_GridLayout_4.addWidget(self.page1_ht_Label_6, 2, 0, 1, 3)

    def Page1_ht_CalendarWiget(self):
        self.page1_ht_CalendarWidget = QtWidgets.QCalendarWidget()
        self.page1_ht_GridLayout_4.addWidget(self.page1_ht_CalendarWidget, 3, 0, 1, 3)

    def Page1_ht_HorizontalLayout_3(self):
        self.page1_ht_HorizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.page1_ht_GridLayout_4.addLayout(self.page1_ht_HorizontalLayout_3, 4, 0, 1, 3)

    def Page1_ht_PushButton_3(self):
        self.page1_ht_PushButton_3 = QtWidgets.QPushButton('Tampilkan')
        self.page1_ht_PushButton_3.setMinimumSize(0, 60)
        self.page1_ht_PushButton_3.setStyleSheet(ButtonStyleSheets3(CekResolusi()))
        self.page1_ht_HorizontalLayout_3.addWidget(self.page1_ht_PushButton_3)

    def Page1_ht_PushButton_5(self):
        self.page1_ht_PushButton_5 = QtWidgets.QPushButton('Hari Ini')
        self.page1_ht_PushButton_5.setMinimumSize(0, 60)
        self.page1_ht_PushButton_5.setStyleSheet(ButtonStyleSheets3(CekResolusi()))
        self.page1_ht_HorizontalLayout_3.addWidget(self.page1_ht_PushButton_5)

    def Page1_ht_Frame_3(self):
        self.page1_ht_Frame_3 = QtWidgets.QFrame()
        self.page1_ht_Frame_3.setObjectName('page1_ht_Frame_3')
        self.page1_ht_Frame_3.setStyleSheet(FrameStyleSheets2(CekResolusi()))
        self.page1_ht_Layout.addWidget(self.page1_ht_Frame_3, 2, 1, 1, 1)

    def Page1_ht_GridLayout_3(self):
        self.page1_ht_GridLayout_3 = QtWidgets.QGridLayout(self.page1_ht_Frame_3)

    def Page1_ht_Label_7(self):
        self.page1_ht_Label_7 = QtWidgets.QLabel('Transaksi : ')
        self.page1_ht_GridLayout_3.addWidget(self.page1_ht_Label_7, 1, 0)

    def Page1_ht_TableWidget(self):
        self.page1_ht_TableWidget = QtWidgets.QTableWidget()
        self.page1_ht_TableWidget.horizontalHeader().setFont(Font(9, True))
        self.page1_ht_GridLayout_3.addWidget(self.page1_ht_TableWidget, 2, 0)

    def Page1_ht_HorizontalLayout_2(self):
        self.page1_ht_HorizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.page1_ht_GridLayout_3.addLayout(self.page1_ht_HorizontalLayout_2, 3, 0)

    def Page1_ht_SpacerItem_3(self):
        self.page1_ht_SpacerItem_3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed,
                                                           QtWidgets.QSizePolicy.Expanding)
        self.page1_ht_Layout.addItem(self.page1_ht_SpacerItem_3, 2, 2)

    def Page1_ht_Frame_5(self):
        self.page1_ht_Frame_5 = QtWidgets.QFrame()
        self.page1_ht_Frame_5.setObjectName('page1_ht_Frame_5')
        self.page1_ht_Frame_5.setMaximumSize(400, 160000)
        self.page1_ht_Frame_5.setStyleSheet(FrameStyleSheets2(CekResolusi()))
        self.page1_ht_Layout.addWidget(self.page1_ht_Frame_5, 2, 3)

    def Page1_ht_GridLayout_5(self):
        self.page1_ht_GridLayout_5 = QtWidgets.QGridLayout(self.page1_ht_Frame_5)

    def Page1_ht_Label_8(self):
        self.page1_ht_Label_8 = QtWidgets.QLabel('Struk : ')
        self.page1_ht_GridLayout_5.addWidget(self.page1_ht_Label_8, 0, 0)

    def Page1_ht_Label_9(self):
        self.page1_ht_ScrollArea = QtWidgets.QScrollArea()
        self.page1_ht_ScrollArea.setBackgroundRole(QtGui.QPalette.Light)
        self.page1_ht_ScrollArea.setAlignment(QtCore.Qt.AlignHCenter)
        self.page1_ht_Label_9 = QtWidgets.QLabel('')
        self.page1_ht_Label_9.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.page1_ht_Label_9.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.page1_ht_Label_9.setBackgroundRole(QtGui.QPalette.Base)
        self.page1_ht_GridLayout_5.addWidget(self.page1_ht_ScrollArea, 1, 0)

    def Page1_ht_PushButton_4(self):
        self.page1_ht_PushButton_4 = QtWidgets.QPushButton('Cetak Struk')
        self.page1_ht_PushButton_4.setMinimumHeight(70)
        self.page1_ht_PushButton_4.setStyleSheet(ButtonStyleSheets3(CekResolusi()))
        self.page1_ht_GridLayout_5.addWidget(self.page1_ht_PushButton_4, 2, 0)

    def Page1_ht_TableWidget_Edited(self):
        self.page1_ht_KodeTransaksi = {}
        File = []
        self.page1_ht_Pathfile = []
        direktori0 = self.TransaksiTokoTerkonfirmasiLOG
        direktori0_itemList = os.listdir(direktori0)
        for item0 in direktori0_itemList:
            direktori1 = '{}/{}'.format(direktori0, item0)
            direktori1_itemList = os.listdir(direktori1)
            for item1 in direktori1_itemList:
                direktori2 = '{}/{}'.format(direktori1, item1)
                direktori2_itemList = os.listdir(direktori2)
                for item2 in direktori2_itemList:
                    direktori3 = '{}/{}'.format(direktori2, item2)
                    direktori3_itemList = os.listdir(direktori3)
                    for item3 in direktori3_itemList:
                        direktori4 = '{}/{}'.format(direktori3, item3)
                        try:
                            direktori4_itemList = os.listdir(direktori4)[0]
                            kodeTransaksi = direktori4_itemList[:-4]
                            bulan = direktori4_itemList[4:6]
                            tanggal = direktori4_itemList[6:8]
                            tahun = direktori4_itemList[:4]
                            self.page1_ht_KodeTransaksi[kodeTransaksi] = [tahun, bulan, tanggal, direktori4_itemList,
                                                                          (direktori4 + '/' + direktori4_itemList)]

                        except:
                            pass

        kolom = ['Tahun', 'Bulan', 'Tanggal', 'KodeTransaksi']
        self.page1_ht_TableWidget.setSelectionBehavior(1)
        self.page1_ht_TableWidget.setColumnCount(len(kolom))
        self.page1_ht_TableWidget.setHorizontalHeaderLabels(kolom)
        self.page1_ht_TableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.page1_ht_TableWidget.setRowCount(len(File))
        self.page1_ht_TableWidget.verticalHeader().setVisible(False)

        for key in self.page1_ht_KodeTransaksi.keys():
            jumlahBaris = self.page1_ht_TableWidget.rowCount()
            self.page1_ht_TableWidget.insertRow(jumlahBaris)
            self.page1_ht_TableWidget.setItem(jumlahBaris, 3, QtWidgets.QTableWidgetItem(key))
            self.page1_ht_TableWidget.item(jumlahBaris, 3).setTextAlignment(
                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.page1_ht_TableWidget.setItem(jumlahBaris, 0,
                                              QtWidgets.QTableWidgetItem(str(self.page1_ht_KodeTransaksi[key][0])))
            self.page1_ht_TableWidget.item(jumlahBaris, 0).setTextAlignment(
                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.page1_ht_TableWidget.setItem(jumlahBaris, 1,
                                              QtWidgets.QTableWidgetItem(str(self.page1_ht_KodeTransaksi[key][1])))
            self.page1_ht_TableWidget.item(jumlahBaris, 1).setTextAlignment(
                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.page1_ht_TableWidget.setItem(jumlahBaris, 2,
                                              QtWidgets.QTableWidgetItem(str(self.page1_ht_KodeTransaksi[key][2])))
            self.page1_ht_TableWidget.item(jumlahBaris, 2).setTextAlignment(
                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.page1_ht_TableWidget.sortItems(3, QtCore.Qt.DescendingOrder)
        self.page1_ht_TableWidget.cellClicked.connect(self.Page1_ht_ViewStrukFromTableWidget)

    def Page1_ht_ViewStrukFromTableWidget(self):
        currentRow = self.page1_ht_TableWidget.currentRow()
        if currentRow >= 0:
            currentFile = self.page1_ht_TableWidget.item(currentRow, 3).text()
            File = self.page1_ht_KodeTransaksi[currentFile][3]
            Path = self.page1_ht_KodeTransaksi[currentFile][4]
            image = Path
            self.page1_ht_pixmapStruk = QtGui.QPixmap(image).scaledToWidth(210, 1)
            self.page1_ht_Label_9.setPixmap(self.page1_ht_pixmapStruk)
            self.page1_ht_ScrollArea.setWidget(self.page1_ht_Label_9)
            self.page1_ht_ScrollArea.setWidgetResizable(True)
            self.page1_ht_TableWidget.itemSelectionChanged.connect(self.page1_ht_ScrollAreatoTop)
            self.page1_ht_Label_8.setText('Struk : {}'.format(currentFile))
        else:
            Path = ''

        return Path

    def page1_ht_ScrollAreatoTop(self):
        self.page1_ht_ScrollArea.verticalScrollBar().setValue(0)

    def Page1_ht_Label_Edited(self):
        self.page1_ht_label.setText(
            '{}, {} {} {}  - {}:{}:{}'.format(self.Data.page1_HariSekarang, self.Data.page1_TanggalSekarang,
                                              self.Data.page1_BulanSekarang, self.Data.page1_TahunSekarang,
                                              self.Data.page1_JamSekarang, self.Data.page1_MenitSekarang,
                                              self.Data.page1_DetikSekarang))

    def Page1_ht_PushButton_Edited(self):
        self.Data.pushButton_13.click()

    def Page1_ht_PushButton_2_Edited(self):
        Text = self.page1_ht_LineEdit.text()
        if len(Text) == 0:
            self.Page1_ht_TableWidget_Edited()
        else:
            if Text in self.page1_ht_KodeTransaksi:
                rowCount = self.page1_ht_TableWidget.rowCount()
                while rowCount >= 0:
                    self.page1_ht_TableWidget.removeRow(rowCount)
                    rowCount -= 1
                else:
                    pass
                self.page1_ht_TableWidget.setRowCount(1)
                self.page1_ht_TableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(Text))
                self.page1_ht_TableWidget.item(0, 3).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.page1_ht_TableWidget.setItem(0, 0,
                                                  QtWidgets.QTableWidgetItem(self.page1_ht_KodeTransaksi[Text][0]))
                self.page1_ht_TableWidget.item(0, 0).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.page1_ht_TableWidget.setItem(0, 1,
                                                  QtWidgets.QTableWidgetItem(self.page1_ht_KodeTransaksi[Text][1]))
                self.page1_ht_TableWidget.item(0, 1).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.page1_ht_TableWidget.setItem(0, 2,
                                                  QtWidgets.QTableWidgetItem(self.page1_ht_KodeTransaksi[Text][2]))
                self.page1_ht_TableWidget.item(0, 2).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            else:
                Dialog = QtWidgets.QMessageBox()
                Dialog.setWindowFlags(Qt.WindowTitleHint | Qt.WindowStaysOnTopHint)
                Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                Dialog.setWindowTitle('File Tidak Ditemukan')
                Dialog.setText(
                    'Nomor Transaksi tidak ditemukan, silakan periksa kembali nomor transaksi yang anda masukkan')
                Dialog.setModal(True)
                Dialog.show()
                Dialog.exec_()
                pass

    def Page1_ht_PushButton_3_Edited(self):
        KodeTransaksi = {}
        TahunDipilih = str(self.page1_ht_CalendarWidget.yearShown())
        BulanDipilih = str(self.page1_ht_CalendarWidget.monthShown())
        print("Bulan dipilih : ", BulanDipilih)
        if BulanDipilih == '1':
            Bulan = '01. January'
            BulanSaja = 'January'
        elif BulanDipilih == '2':
            Bulan = '02. February'
            BulanSaja = 'February'
        elif BulanDipilih == '3':
            Bulan = '03. March'
            BulanSaja = 'March'
        elif BulanDipilih == '4':
            Bulan = '04. April'
            BulanSaja = 'April'
        elif BulanDipilih == '5':
            Bulan = '05. May'
            BulanSaja = 'May'
        elif BulanDipilih == '6':
            Bulan = '06. June'
            BulanSaja = 'June'
        elif BulanDipilih == '7':
            Bulan = '07. July'
            BulanSaja = 'July'
        elif BulanDipilih == '8':
            Bulan = '08. August'
            BulanSaja = 'August'
        elif BulanDipilih == '9':
            Bulan = '09. September'
            BulanSaja = 'September'
        elif BulanDipilih == '10':
            Bulan = '10. October'
            BulanSaja = 'October'
        elif BulanDipilih == '11':
            Bulan = '11. November'
            BulanSaja = 'November'
        elif BulanDipilih == '12':
            Bulan = '12. December'
            BulanSaja = 'December'
        else:
            Bulan = ''
            BulanSaja = ''
            print('Bulan tidak ditemukan')
            print('BulanSaja tidak ditemukan')
            pass

        TanggalDipilih = self.page1_ht_CalendarWidget.selectedDate().toString('dd')

        direktori0 = self.TransaksiTokoTerkonfirmasiLOG
        direktori0_itemList = os.listdir(direktori0)
        if str(TahunDipilih) in direktori0_itemList:
            direktori1 = '{}/{}'.format(direktori0, TahunDipilih)
            direktori1_itemList = os.listdir(direktori1)
            print(direktori1_itemList)
            if str(Bulan) in direktori1_itemList:
                direktori2 = '{}/{}'.format(direktori1, Bulan)
                print(direktori2)
                direktori2_itemList = os.listdir(direktori2)
                print(direktori2_itemList)
                if str('{}-{}-{}'.format(TanggalDipilih, BulanSaja, TahunDipilih)) in direktori2_itemList:
                    direktori3 = '{}/{}'.format(direktori2,
                                                str('{}-{}-{}'.format(TanggalDipilih, BulanSaja, TahunDipilih)))
                    direktori3_itemList = os.listdir(direktori3)
                    for item in direktori3_itemList:
                        direktori4 = '{}/{}'.format(direktori3, item)
                        try:
                            direktori4_itemList = os.listdir(direktori4)[0]
                            kodeTransaksi = direktori4_itemList[:-4]
                            bulan = direktori4_itemList[4:6]
                            tanggal = direktori4_itemList[6:8]
                            tahun = direktori4_itemList[:4]
                            KodeTransaksi[kodeTransaksi] = [tahun, bulan, tanggal, direktori4_itemList,
                                                            (direktori4 + '/' + direktori4_itemList)]
                        except:
                            pass

                    if len(KodeTransaksi) == 0:
                        Dialog = QtWidgets.QMessageBox()
                        Dialog.setWindowFlags(Qt.WindowTitleHint | Qt.WindowStaysOnTopHint)
                        Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                        Dialog.setWindowTitle('File Tidak Ditemukan')
                        Dialog.setText(
                            'Nomor Transaksi tidak ditemukan atau tidak ada transaksi pada tanggal yang dipilih, silakan periksa kembali tanggal yang anda masukkan')
                        Dialog.setModal(True)
                        Dialog.show()
                        Dialog.exec_()
                        pass
                    else:
                        rowCount = self.page1_ht_TableWidget.rowCount()
                        while rowCount > 0:
                            self.page1_ht_TableWidget.removeRow(rowCount - 1)
                            rowCount = self.page1_ht_TableWidget.rowCount()
                        else:
                            pass
                        rowCount2 = self.page1_ht_TableWidget.rowCount()
                        for item in KodeTransaksi.keys():
                            self.page1_ht_TableWidget.setRowCount(rowCount2 + 1)
                            self.page1_ht_TableWidget.setItem(rowCount2, 3, QtWidgets.QTableWidgetItem(str(item)))
                            self.page1_ht_TableWidget.item(rowCount2, 3).setTextAlignment(
                                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                            self.page1_ht_TableWidget.setItem(rowCount2, 0,
                                                              QtWidgets.QTableWidgetItem(str(KodeTransaksi[item][0])))
                            self.page1_ht_TableWidget.item(rowCount2, 0).setTextAlignment(
                                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                            self.page1_ht_TableWidget.setItem(rowCount2, 1,
                                                              QtWidgets.QTableWidgetItem(str(KodeTransaksi[item][1])))
                            self.page1_ht_TableWidget.item(rowCount2, 1).setTextAlignment(
                                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                            self.page1_ht_TableWidget.setItem(rowCount2, 2,
                                                              QtWidgets.QTableWidgetItem(str(KodeTransaksi[item][2])))
                            self.page1_ht_TableWidget.item(rowCount2, 2).setTextAlignment(
                                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                            rowCount2 = self.page1_ht_TableWidget.rowCount()
                        self.page1_ht_TableWidget.sortItems(3, QtCore.Qt.DescendingOrder)
                else:
                    direktori3_itemList = ''
                    Dialog = QtWidgets.QMessageBox()
                    Dialog.setWindowFlags(Qt.WindowTitleHint | Qt.WindowStaysOnTopHint)
                    Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                    Dialog.setWindowTitle('File Tidak Ditemukan')
                    Dialog.setText(
                        'Nomor Transaksi tidak ditemukan atau tidak ada transaksi pada tanggal yang dipilih, silakan periksa kembali tanggal yang anda masukkan')
                    Dialog.setModal(True)
                    Dialog.show()
                    Dialog.exec_()
                    pass
            else:
                direktori2_itemList = ''
                Dialog = QtWidgets.QMessageBox()
                Dialog.setWindowFlags(Qt.WindowTitleHint | Qt.WindowStaysOnTopHint)
                Dialog.setIcon(QtWidgets.QMessageBox.Warning)
                Dialog.setWindowTitle('File Tidak Ditemukan')
                Dialog.setText(
                    'Nomor Transaksi tidak ditemukan atau tidak ada transaksi pada tanggal yang dipilih, silakan periksa kembali tanggal yang anda masukkan')
                Dialog.setModal(True)
                Dialog.show()
                Dialog.exec_()
                pass
        else:
            direktori1_itemList = ''
            Dialog = QtWidgets.QMessageBox()
            Dialog.setWindowFlags(Qt.WindowTitleHint | Qt.WindowStaysOnTopHint)
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setWindowTitle('File Tidak Ditemukan')
            Dialog.setText(
                'Nomor Transaksi tidak ditemukan atau tidak ada transaksi pada tanggal yang dipilih, silakan periksa kembali tanggal yang anda masukkan')
            Dialog.setModal(True)
            Dialog.show()
            Dialog.exec_()
            pass

        rowCount = self.page1_ht_TableWidget.rowCount()

    def Page1_ht_PushButton_5_Edited(self):
        self.page1_ht_CalendarWidget.setCurrentPage(int(self.yearNow), int(self.monthNow1))
        self.page1_ht_CalendarWidget.setSelectedDate(QtCore.QDate.currentDate())

    def Page1_ht_PrintStruk(self):
        try:
            try:
                self.Data.MyPrinter = Usb(0x0483, 0x5840, 0, 0x58, 0x03)
                try:
                    self.Data.MyPrinter.image(self.Page1_ht_ViewStrukFromTableWidget())
                except:
                    pass
                self.Data.MyPrinter.close()
            except:
                try:
                    self.Data.MyPrinter.image(self.Page1_ht_ViewStrukFromTableWidget())
                except:
                    pass
                self.Data.MyPrinter.close()
        except:
            Dialog = QtWidgets.QMessageBox()
            Dialog.setWindowFlags(Qt.WindowTitleHint | Qt.WindowStaysOnTopHint)
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setWindowTitle('Printer')
            Dialog.setText('Printer tidak terdeteksi, nyalakan printer dan pastikan '
                           'semua kabel telah terpasang dengan benar')
            Dialog.setModal(True)
            Dialog.show()
            Dialog.exec_()
            pass

    def Page1_ht_ResolutionManager(self):
        Resolusi = CekResolusi()
        if Resolusi == '1280x720':
            self.page1_ht_Frame.setFixedHeight(40)
            self.page1_ht_pushButton.setFixedSize(100, 25)
            self.page1_ht_label_4.setMinimumSize(0, 10)
            self.page1_ht_Frame_4.setMaximumSize(370, 160000)
            self.page1_ht_SpacerItem_2.changeSize(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            self.page1_ht_PushButton_3.setMinimumSize(0, 30)
            self.page1_ht_PushButton_5.setMinimumSize(0, 30)
            self.page1_ht_SpacerItem_3.changeSize(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
            self.page1_ht_Frame_5.setMaximumSize(250, 160000)
            self.page1_ht_PushButton_4.setMinimumHeight(30)
            self.page1_ht_TableWidget.horizontalHeader().setFixedHeight(35)
            self.page1_ht_TableWidget.verticalHeader().setDefaultSectionSize(30)
        else:
            self.page1_ht_TableWidget.horizontalHeader().setFixedHeight(70)
            self.page1_ht_TableWidget.verticalHeader().setDefaultSectionSize(45)
            pass


class Page1_TambahPembeli(Page1):
    pelanggan = 0
    def __init__(self, Data):
        super(Page1_TambahPembeli, self).__init__()
        self.Data = Data
        self.Data.pelanggan +=1
        self.Pelanggan = self.Data.pelanggan
        self.Page1_TambahPembeli_DialogBox = QtWidgets.QDialog()
        self.Page1_TambahPembeli_Layout = QtWidgets.QGridLayout(self.Page1_TambahPembeli_DialogBox)
        self.Page1_TambahPembeli_DialogBox.setWindowTitle("Pelanggan Tambahan " + str(self.Pelanggan))

        self.Page1_TambahPembeli_Label()
        self.Page1_TambahPembeli_Frame1()
        self.Page1_TambahPembeli_Layout1()
        self.Page1_TambahPembeli_Label1()
        self.Page1_TambahPembeli_Label2()
        self.Page1_TambahPembeli_LineEdit1()
        self.Page1_TambahPembeli_Label3()
        self.Page1_TambahPembeli_LineEdit2()
        self.Page1_TambahPembeli_Label4()
        self.Page1_TambahPembeli_LineEdit3()
        self.Page1_TambahPembeli_Frame2()
        self.Page1_TambahPembeli_Layout2()
        self.Page1_TambahPembeli_Label5()
        self.Page1_TambahPembeli_Label6()
        self.Page1_TambahPembeli_ComboBox1()
        self.Page1_TambahPembeli_Label7()
        self.Page1_TambahPembeli_HBoxLayout1()
        self.Page1_TambahPembeli_LineEdit4()
        self.Page1_TambahPembeli_LineEdit5()
        self.Page1_TambahPembeli_Label8()

        self.Page1_TambahPembeli_DialogBox.showMaximized()
        self.Page1_TambahPembeli_DialogBox.exec_()
        self.Data.pelanggan -= 1
        self.Pelanggan = self.Data.pelanggan

    def Page1_TambahPembeli_Label(self):
        self.page1_TambahPembeli_Label = QtWidgets.QLabel("Pelanggan Tambahan {}".format(self.Pelanggan))
        self.page1_TambahPembeli_Label.setFont(Font(14, True))
        self.page1_TambahPembeli_Label.setAlignment(Qt.AlignHCenter)
        self.Page1_TambahPembeli_Layout.addWidget(self.page1_TambahPembeli_Label, 0, 0, 1, 2)

    def Page1_TambahPembeli_Frame1(self):
        self.page1_TambahPembeli_Frame1 = QtWidgets.QFrame()
        self.page1_TambahPembeli_Frame1.setFrameShape(1)
        self.Page1_TambahPembeli_Layout.addWidget(self.page1_TambahPembeli_Frame1, 1, 0)

    def Page1_TambahPembeli_Layout1(self):
        self.page1_TambahPembeli_Layout1 = QtWidgets.QGridLayout(self.page1_TambahPembeli_Frame1)

    def Page1_TambahPembeli_Label1(self):
        self.page1_TambahPembeli_Label1 = QtWidgets.QLabel("RINCIAN PESANAN")
        self.page1_TambahPembeli_Label1.setFont(Font(11, True))
        self.page1_TambahPembeli_Layout1.addWidget(self.page1_TambahPembeli_Label1, 0, 0)

    def Page1_TambahPembeli_Label2(self):
        self.page1_TambahPembeli_Label2 = QtWidgets.QLabel("Nomor Transaksi :")
        self.page1_TambahPembeli_Label2.setFont(Font(9, False))
        self.page1_TambahPembeli_Layout1.addWidget(self.page1_TambahPembeli_Label2, 1, 0)

    def Page1_TambahPembeli_LineEdit1(self):
        self.page1_TambahPembeli_LineEdit1 = QtWidgets.QLineEdit()
        self.page1_TambahPembeli_Layout1.addWidget(self.page1_TambahPembeli_LineEdit1, 1, 1)

    def Page1_TambahPembeli_Label3(self):
        self.page1_TambahPembeli_Label3 = QtWidgets.QLabel("Waktu Transaksi :")
        self.page1_TambahPembeli_Label3.setFont(Font(9, False))
        self.page1_TambahPembeli_Layout1.addWidget(self.page1_TambahPembeli_Label3, 2, 0)

    def Page1_TambahPembeli_LineEdit2(self):
        self.page1_TambahPembeli_LineEdit2 = QtWidgets.QLineEdit()
        self.page1_TambahPembeli_Layout1.addWidget(self.page1_TambahPembeli_LineEdit2, 2, 1)

    def Page1_TambahPembeli_Label4(self):
        self.page1_TambahPembeli_Label4 = QtWidgets.QLabel("Kasir :")
        self.page1_TambahPembeli_Label4.setFont(Font(9, False))
        self.page1_TambahPembeli_Layout1.addWidget(self.page1_TambahPembeli_Label4, 3, 0)

    def Page1_TambahPembeli_LineEdit3(self):
        self.page1_TambahPembeli_LineEdit3 = QtWidgets.QLineEdit()
        self.page1_TambahPembeli_Layout1.addWidget(self.page1_TambahPembeli_LineEdit3, 3, 1)

    def Page1_TambahPembeli_Frame2(self):
        self.page1_TambahPembeli_Frame2 = QtWidgets.QFrame()
        self.page1_TambahPembeli_Frame2.setFrameShape(1)
        self.Page1_TambahPembeli_Layout.addWidget(self.page1_TambahPembeli_Frame2, 1, 1)

    def Page1_TambahPembeli_Layout2(self):
        self.page1_TambahPembeli_Layout2 = QtWidgets.QGridLayout(self.page1_TambahPembeli_Frame2)

    def Page1_TambahPembeli_Label5(self):
        self.page1_TambahPembeli_Label5 = QtWidgets.QLabel("TOTAL TRANSAKSI")
        self.page1_TambahPembeli_Label5.setFont(Font(12, True))
        self.page1_TambahPembeli_Layout2.addWidget(self.page1_TambahPembeli_Label5, 0, 0)

    def Page1_TambahPembeli_Label6(self):
        self.page1_TambahPembeli_Label6 = QtWidgets.QLabel("Transaksi : ")
        self.page1_TambahPembeli_Label6.setFont(Font(9, False))
        self.page1_TambahPembeli_Layout2.addWidget(self.page1_TambahPembeli_Label6, 1, 0)

    def Page1_TambahPembeli_ComboBox1(self):
        self.page1_TambahPembeli_ComboBox1 = QtWidgets.QComboBox()
        self.page1_TambahPembeli_Layout2.addWidget(self.page1_TambahPembeli_ComboBox1, 1, 1)

    def Page1_TambahPembeli_Label7(self):
        self.page1_TambahPembeli_Label7 = QtWidgets.QLabel("Diskon Khusus : ")
        self.page1_TambahPembeli_Label7.setFont(Font(9, False))
        self.page1_TambahPembeli_Layout2.addWidget(self.page1_TambahPembeli_Label7, 2, 0)

    def Page1_TambahPembeli_HBoxLayout1(self):
        self.page1_TambahPembeli_HBoxLayout1 = QtWidgets.QHBoxLayout()
        self.page1_TambahPembeli_Layout2.addLayout(self.page1_TambahPembeli_HBoxLayout1, 2, 1)

    def Page1_TambahPembeli_LineEdit4(self):
        self.page1_TambahPembeli_LineEdit4 = QtWidgets.QLineEdit()
        self.page1_TambahPembeli_HBoxLayout1.addWidget(self.page1_TambahPembeli_LineEdit4)

    def Page1_TambahPembeli_LineEdit5(self):
        self.page1_TambahPembeli_LineEdit5 = QtWidgets.QLineEdit()
        self.page1_TambahPembeli_HBoxLayout1.addWidget(self.page1_TambahPembeli_LineEdit5)

    def Page1_TambahPembeli_Label8(self):
        self.page1_TambahPembeli_Label8 = QtWidgets.QLabel("TOTAL : ")
        self.page1_TambahPembeli_Label8.setFont(Font(9, False))
        self.page1_TambahPembeli_Layout2.addWidget(self.page1_TambahPembeli_Label8, 3, 0)






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page1()
    objek.Page1_Execution('Admin Page 1', 'super')
    objek.Page1_Editing_Mode()
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
