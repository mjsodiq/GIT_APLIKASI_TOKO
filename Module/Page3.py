import sqlite3
from PandanArum import *
from StyleSheets import *
from MenuBar import *
from PyQt5 import QtCore, QtGui, QtWidgets
import code128
from PIL import Image
import code128
import locale
from escpos.printer import Usb

try:
    printer = Usb(0x0483, 0x5840, 0, 0x58, 0x03)
except:
    PesanError("Printer", "Printer tidak terdeteksi.\nPastikan printer dalam kondisi normal dan semua kabel terhubung dengan benar.")


# Mencetak Label Produk terutama untuk produk los-losan
def Cetak_Barcode_Label_Produk(nama_produk, kode_produk, expired=''):
    NamaProduk = nama_produk
    Expired = expired
    Barcode = kode_produk

    lebar_cetak = 402
    tinggi = 100

    code128.image(Barcode, tinggi).save("{}.png".format(Barcode))
    img = Image.open('{}.png'.format(Barcode))
    wpercent = (lebar_cetak / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((lebar_cetak, hsize), Image.ANTIALIAS)
    img.save("{}.png".format(Barcode))

    printer.text("\n--------------------------------")
    printer.text(NamaProduk)
    printer.text("\n("+Barcode+")")
    printer.text("\n")
    printer.image("{}.png".format(Barcode))
    printer.text("\n")
    printer.text("Expired : "+Expired)
    printer.text("\n--------------------------------")
    printer.text("\n\n\n")


# Mencetak Label harga untuk tiap produk
def Cetak_Barcode_Label_Harga(nama_produk, kode_produk, harga):
    NamaProduk = nama_produk
    Barcode = kode_produk
    Harga = harga

    lebar_cetak = 402
    tinggi_barcode = 100

    code128.image(Barcode, tinggi_barcode).save("{}.png".format(Barcode))
    img = Image.open('{}.png'.format(Barcode))
    wpercent = (lebar_cetak / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((lebar_cetak, hsize), Image.ANTIALIAS)
    img.save("{}.png".format(Barcode))

    printer.text("\n--------------------------------")
    printer.text("{} \n({})".format(NamaProduk, Barcode))
    printer.text("\n")
    printer.image("{}.png".format(Barcode))
    printer.text("\n")
    printer.text("Harga : Rp. " + str(Harga) + ",-")
    printer.text("\n--------------------------------")
    printer.text("\n\n\n")


# Class Atur Stok
class Page3(MenuBar, Ui_ProgramAplikasiToko):
    signal1 = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Page3, self).__init__()
        MenuBar.MenuBar_Execution(self)
        self.page3_databasePath1 = DatabaseProduk()

        # Nama Tab
        self.Page3_NamaTab_Tab1 = ""
        self.Page3_NamaTab_Tab2 = ""
        self.Page3_NamaTab_Tab3 = ""
        self.Page3_NamaTab_Tab4 = "Katalog Produk dan Distributor"
        self.Page3_KolomtoIndex = {}
        self.Page3_IndextoKolom = {}

    def Page3_PesanError(self, judul, pesanError):
        MessegeBox = QtWidgets.QMessageBox()
        MessegeBox.setWindowTitle(str(judul))
        MessegeBox.setText(str(pesanError))
        MessegeBox.Warning
        MessegeBox.show()
        MessegeBox.exec_()

    def Tab3(self):
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("Tab3")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/Tambah/Refresh_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_UTAMA.addTab(self.tab3, icon14, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab3), "Atur Stok")

    def Page3_GridLayout_7(self):
        self.page3_gridLayout_7 = QtWidgets.QGridLayout(self.tab3)
        self.page3_gridLayout_7.setObjectName("page3_gridLayout_7")

    def Page3_Tab_ATUR_STOK_GridLayout(self):
        self.page3_tab_ATUR_STOK_GridLayout = QtWidgets.QGridLayout()
        self.page3_tab_ATUR_STOK_GridLayout.setObjectName("page3_TAB_ATUR_STOK_GridLayout")
        self.page3_gridLayout_7.addLayout(self.page3_tab_ATUR_STOK_GridLayout, 0, 0, 1, 1)

    def Page3_Tab_ATUR_STOK_TAB(self):
        self.page3_tab_ATUR_STOK_TAB = QtWidgets.QTabWidget(self.tab3)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.page3_tab_ATUR_STOK_TAB.setFont(font)
        self.page3_tab_ATUR_STOK_TAB.setTabBarAutoHide(False)
        self.page3_tab_ATUR_STOK_TAB.setObjectName("page3_TAB_ATUR_STOK_TAB")
        self.page3_tab_ATUR_STOK_GridLayout.addWidget(self.page3_tab_ATUR_STOK_TAB, 0, 0, 1, 1)
        self.page3_tab_ATUR_STOK_TAB.setStyleSheet(TabStyleSheet3(CekResolusi()))
        self.page3_tab_ATUR_STOK_TAB.setCurrentIndex(0)

    def Page3_Tab3_Tab1(self):
        self.page3_tab3_Tab1 = QtWidgets.QWidget()
        self.page3_tab3_Tab1.setObjectName("page3_Tab3_Tab1")
        self.page3_tab_ATUR_STOK_TAB.addTab(self.page3_tab3_Tab1, "")
        self.page3_tab_ATUR_STOK_TAB.setTabText(self.page3_tab_ATUR_STOK_TAB.indexOf(self.page3_tab3_Tab1), "SemuaItem")

    def Page3_Tab3_Tab2(self):
        self.page3_tab3_Tab2 = QtWidgets.QWidget()
        self.page3_tab3_Tab2.setObjectName("page3_Tab3_Tab1")
        self.page3_tab_ATUR_STOK_TAB.addTab(self.page3_tab3_Tab2, "")
        self.page3_tab_ATUR_STOK_TAB.setTabText(self.page3_tab_ATUR_STOK_TAB.indexOf(self.page3_tab3_Tab2), "Transaksi Per Item")
        objek = Page3_t2(self)

    def Page3_Tab3_Tab3(self):
        self.page3_tab3_Tab3 = QtWidgets.QWidget()
        self.page3_tab3_Tab3.setObjectName("page3_tab3_Tab3")
        self.page3_tab_ATUR_STOK_TAB.addTab(self.page3_tab3_Tab3, "")
        self.page3_tab_ATUR_STOK_TAB.setTabText(self.page3_tab_ATUR_STOK_TAB.indexOf(self.page3_tab3_Tab3), "BlackList Product")
        objek = Page3_t3(self)

    def Page3_Tab3_Tab4(self):
        self.page3_tab3_tab4 = QtWidgets.QWidget()
        self.page3_tab3_tab4.setObjectName("page3_tab3_tab4")
        self.page3_tab_ATUR_STOK_TAB.addTab(self.page3_tab3_tab4, "")
        self.page3_tab_ATUR_STOK_TAB.setTabText(self.page3_tab_ATUR_STOK_TAB.indexOf(self.page3_tab3_tab4), self.Page3_NamaTab_Tab4)
        objek = Page3_t4(self)

    def Page3_GridLayout(self):
        self.page3_gridLayout = QtWidgets.QGridLayout(self.page3_tab3_Tab1)
        self.page3_gridLayout.setObjectName("page3_gridLayout")

    def Page3_Tab_ATUR_STOK_TAB_SemuaItem_gridLayout(self):
        self.page3_tab_ATUR_STOK_TAB_SemuaItem_gridLayout = QtWidgets.QGridLayout()
        self.page3_tab_ATUR_STOK_TAB_SemuaItem_gridLayout.setObjectName("page3_TAB_ATUR_STOK_TAB_SemuaItem_gridLayout")
        self.page3_gridLayout.addLayout(self.page3_tab_ATUR_STOK_TAB_SemuaItem_gridLayout, 0, 1, 1, 1)

    def Page3_GridLayout_4(self):
        self.page3_gridLayout_4 = QtWidgets.QGridLayout()
        self.page3_gridLayout_4.setObjectName("page3_gridLayout_4")
        self.page3_tab_ATUR_STOK_TAB_SemuaItem_gridLayout.addLayout(self.page3_gridLayout_4, 0, 0, 1, 1)

    def Page3_HorizontalLayout_20(self):
        self.page3_horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.page3_horizontalLayout_20.setObjectName("page3_horizontalLayout_20")
        self.page3_gridLayout_4.addLayout(self.page3_horizontalLayout_20, 3, 1, 1, 1)

    def Page3_ComboBox_3(self):
        self.page3_comboBox_3 = QtWidgets.QComboBox(self.page3_tab3_Tab1)
        self.page3_comboBox_3.setObjectName("page3_comboBox_3")
        self.page3_comboBox_3.addItem("")
        self.page3_comboBox_3.addItem("")
        self.page3_comboBox_3.addItem("")
        self.page3_comboBox_3.setItemText(0, "Kategori")
        self.page3_comboBox_3.setItemText(1, "Lokasi")
        self.page3_comboBox_3.setItemText(2, "Kode")
        self.page3_horizontalLayout_20.addWidget(self.page3_comboBox_3)

    def Page3_LineEdit_7(self):
        self.page3_lineEdit_7 = QtWidgets.QLineEdit(self.page3_tab3_Tab1)
        self.page3_lineEdit_7.setObjectName("page3_lineEdit_7")
        self.page3_lineEdit_7.setPlaceholderText("Masukkan Nilai")
        self.page3_horizontalLayout_20.addWidget(self.page3_lineEdit_7)

    def Page3_PushButton_29(self):
        self.page3_pushButton_29 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        self.page3_pushButton_29.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Tambah/Add_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_29.setIcon(icon11)
        self.page3_pushButton_29.setObjectName("page3_pushButton_29")
        self.page3_horizontalLayout_20.addWidget(self.page3_pushButton_29)

    def Page3_PushButton_36(self):
        self.page3_pushButton_36 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        self.page3_pushButton_36.setText("")
        self.page3_pushButton_36.setObjectName("page3_pushButton_36")
        self.page3_horizontalLayout_20.addWidget(self.page3_pushButton_36)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Tambah/Delete_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_36.setIcon(icon13)

    def Page3_PushButton_26(self):
        self.page3_pushButton_26 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Tambah/Search_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_26.setIcon(icon6)
        self.page3_pushButton_26.setObjectName("page3_pushButton_26")
        self.page3_pushButton_26.setText("Cari")
        self.page3_gridLayout_4.addWidget(self.page3_pushButton_26, 5, 2, 1, 1)

    def Page3_Label_4(self):
        self.page3_label_4 = QtWidgets.QLabel(self.page3_tab3_Tab1)
        self.page3_label_4.setObjectName("page3_label_4")
        self.page3_gridLayout_4.addWidget(self.page3_label_4, 1, 0, 1, 1)
        self.page3_label_4.setText('Filter Pencarian Berdasarkan :')

    def Page3_Label(self):
        self.page3_label = QtWidgets.QLabel(self.page3_tab3_Tab1)
        self.page3_label.setObjectName("page3_label")
        self.page3_gridLayout_4.addWidget(self.page3_label, 0, 0, 1, 1)
        self.page3_label.setText('Cari Item : ')

    def Page3_PushButton(self):
        self.page3_pushButton = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Tambah/Search_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton.setIcon(icon6)
        self.page3_pushButton.setObjectName("page3_pushButton")
        self.page3_pushButton.setText(" Cari")
        self.page3_gridLayout_4.addWidget(self.page3_pushButton, 0, 2, 1, 1)

    def Page3_LineEdit(self):
        # LineEdit Cari, baris pertama
        # Parent page3_gridLayout_4
        self.page3_lineEdit = QtWidgets.QLineEdit(self.page3_tab3_Tab1)
        self.page3_lineEdit.setObjectName("page3_lineEdit")
        self.page3_lineEdit.setPlaceholderText("Masukkan kode produk, kode barcode atau nama produk")
        self.page3_gridLayout_4.addWidget(self.page3_lineEdit, 0, 1, 1, 1)

    def Page3_HorizontalLayout_10(self):
        self.page3_horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.page3_horizontalLayout_10.setObjectName("page3_horizontalLayout_10")
        self.page3_gridLayout_4.addLayout(self.page3_horizontalLayout_10, 5, 1, 1, 1)

    def Page3_ComboBox(self):
        self.page3_comboBox = QtWidgets.QComboBox(self.page3_tab3_Tab1)
        self.page3_comboBox.setObjectName("page3_comboBox")
        self.page3_comboBox.addItem("")
        self.page3_comboBox.addItem("")
        self.page3_comboBox.addItem("")
        self.page3_comboBox.setItemText(0, "Kategori")
        self.page3_comboBox.setItemText(1, "Lokasi")
        self.page3_comboBox.setItemText(2, "Kode")
        self.page3_horizontalLayout_10.addWidget(self.page3_comboBox)

    def Page3_LineEdit_4(self):
        self.page3_lineEdit_4 = QtWidgets.QLineEdit(self.page3_tab3_Tab1)
        self.page3_lineEdit_4.setObjectName("page3_lineEdit_4")
        self.page3_lineEdit_4.setPlaceholderText("Masukkan Nilai")
        self.page3_horizontalLayout_10.addWidget(self.page3_lineEdit_4)

    def Page3_PushButton_25(self):
        self.page3_pushButton_25 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        self.page3_pushButton_25.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Tambah/Delete_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_25.setIcon(icon13)
        self.page3_pushButton_25.setObjectName("page3_pushButton_25")
        self.page3_pushButton_25.setToolTip("Tambahkan Filter")
        self.page3_horizontalLayout_10.addWidget(self.page3_pushButton_25)

    def Page3_HorizontalLayout_18(self):
        self.page3_horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.page3_horizontalLayout_18.setObjectName("page3_horizontalLayout_18")
        self.page3_gridLayout_4.addLayout(self.page3_horizontalLayout_18, 1, 1, 1, 1)

    def Page3_ComboBox_2(self):
        self.page3_comboBox_2 = QtWidgets.QComboBox(self.page3_tab3_Tab1)
        self.page3_comboBox_2.setObjectName("page3_comboBox_2")
        self.page3_comboBox_2.addItem("")
        self.page3_comboBox_2.addItem("")
        self.page3_comboBox_2.addItem("")
        self.page3_comboBox_2.setItemText(0, "Kategori")
        self.page3_comboBox_2.setItemText(1, "Lokasi")
        self.page3_comboBox_2.setItemText(2, "Kode")
        self.page3_horizontalLayout_18.addWidget(self.page3_comboBox_2)

    def Page3_LineEdit_3(self):
        self.page3_lineEdit_3 = QtWidgets.QLineEdit(self.page3_tab3_Tab1)
        self.page3_lineEdit_3.setObjectName("page3_lineEdit_3")
        self.page3_lineEdit_3.setPlaceholderText("Masukkan Nilai")
        self.page3_horizontalLayout_18.addWidget(self.page3_lineEdit_3)

    def Page3_PushButton_27(self):
        self.page3_pushButton_27 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        self.page3_pushButton_27.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Tambah/Add_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_27.setIcon(icon11)
        self.page3_pushButton_27.setObjectName("page3_pushButton_27")
        self.page3_horizontalLayout_18.addWidget(self.page3_pushButton_27)

    def Page3_HorizontalLayout_21(self):
        self.page3_horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.page3_horizontalLayout_21.setObjectName("page3_horizontalLayout_21")
        self.page3_gridLayout_4.addLayout(self.page3_horizontalLayout_21, 2, 1, 1, 1)

    def Page3_ComboBox_4(self):
        self.page3_comboBox_4 = QtWidgets.QComboBox(self.page3_tab3_Tab1)
        self.page3_comboBox_4.setObjectName("page3_comboBox_4")
        self.page3_comboBox_4.addItem("")
        self.page3_comboBox_4.addItem("")
        self.page3_comboBox_4.addItem("")
        self.page3_comboBox_4.setItemText(0, "Kategori")
        self.page3_comboBox_4.setItemText(1, "Lokasi")
        self.page3_comboBox_4.setItemText(2, "Kode")
        self.page3_horizontalLayout_21.addWidget(self.page3_comboBox_4)

    def Page3_LineEdit_6(self):
        self.page3_lineEdit_6 = QtWidgets.QLineEdit(self.page3_tab3_Tab1)
        self.page3_lineEdit_6.setObjectName("page3_lineEdit_6")
        self.page3_lineEdit_6.setPlaceholderText("Masukkan Nilai")
        self.page3_horizontalLayout_21.addWidget(self.page3_lineEdit_6)

    def Page3_PushButton_28(self):
        self.page3_pushButton_28 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        self.page3_pushButton_28.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Tambah/Add_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_28.setIcon(icon11)
        self.page3_pushButton_28.setObjectName("page3_pushButton_28")
        self.page3_horizontalLayout_21.addWidget(self.page3_pushButton_28)

    def Page3_PushButton_35(self):
        self.page3_pushButton_35 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        self.page3_pushButton_35.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Tambah/Delete_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_35.setIcon(icon13)
        self.page3_pushButton_35.setObjectName("page3_pushButton_35")
        self.page3_horizontalLayout_21.addWidget(self.page3_pushButton_35)

    def Page3_HorizontalLayout_22(self):
        self.page3_horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.page3_horizontalLayout_22.setObjectName("page3_horizontalLayout_22")
        self.page3_gridLayout_4.addLayout(self.page3_horizontalLayout_22, 4, 1, 1, 1)

    def Page3_ComboBox_5(self):
        self.page3_comboBox_5 = QtWidgets.QComboBox(self.page3_tab3_Tab1)
        self.page3_comboBox_5.setObjectName("page3_comboBox_5")
        self.page3_comboBox_5.addItem("")
        self.page3_comboBox_5.addItem("")
        self.page3_comboBox_5.addItem("")
        self.page3_comboBox_5.setItemText(0, "Kategori")
        self.page3_comboBox_5.setItemText(1, "Lokasi")
        self.page3_comboBox_5.setItemText(2, "Kode")
        self.page3_horizontalLayout_22.addWidget(self.page3_comboBox_5)

    def Page3_LineEdit_8(self):
        self.page3_lineEdit_8 = QtWidgets.QLineEdit(self.page3_tab3_Tab1)
        self.page3_lineEdit_8.setObjectName("page3_lineEdit_8")
        self.page3_lineEdit_8.setPlaceholderText("Masukkan Nilai")
        self.page3_horizontalLayout_22.addWidget(self.page3_lineEdit_8)

    def Page3_PushButton_30(self):
        self.page3_pushButton_30 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        self.page3_pushButton_30.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Tambah/Add_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_30.setIcon(icon11)
        self.page3_pushButton_30.setObjectName("page3_pushButton_30")
        self.page3_horizontalLayout_22.addWidget(self.page3_pushButton_30)

    def Page3_PushButton_37(self):
        self.page3_pushButton_37 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        self.page3_pushButton_37.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Tambah/Delete_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_37.setIcon(icon13)
        self.page3_pushButton_37.setObjectName("page3_pushButton_37")
        self.page3_horizontalLayout_22.addWidget(self.page3_pushButton_37)

    def Page3_PushButton_31(self):
        self.page3_pushButton_31 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Tambah/Search_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_31.setIcon(icon6)
        self.page3_pushButton_31.setObjectName("page3_pushButton_31")
        self.page3_pushButton_31.setText("Cari")
        self.page3_gridLayout_4.addWidget(self.page3_pushButton_31, 1, 2, 1, 1)

    def Page3_PushButton_32(self):
        self.page3_pushButton_32 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Tambah/Search_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_32.setIcon(icon6)
        self.page3_pushButton_32.setObjectName("page3_pushButton_32")
        self.page3_pushButton_32.setText("Cari")
        self.page3_gridLayout_4.addWidget(self.page3_pushButton_32, 2, 2, 1, 1)

    def Page3_PushButton_33(self):
        self.page3_pushButton_33 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Tambah/Search_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_33.setIcon(icon6)
        self.page3_pushButton_33.setObjectName("page3_pushButton_33")
        self.page3_pushButton_33.setText("Cari")
        self.page3_gridLayout_4.addWidget(self.page3_pushButton_33, 3, 2, 1, 1)

    def Page3_PushButton_34(self):
        self.page3_pushButton_34 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Tambah/Search_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_34.setIcon(icon6)
        self.page3_pushButton_34.setObjectName("page3_pushButton_34")
        self.page3_pushButton_34.setText("Cari")
        self.page3_gridLayout_4.addWidget(self.page3_pushButton_34, 4, 2, 1, 1)

    def Page3_HorizontalLayout_2(self):
        self.page3_horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.page3_horizontalLayout_2.setObjectName("page3_horizontalLayout_2")
        self.page3_tab_ATUR_STOK_TAB_SemuaItem_gridLayout.addLayout(self.page3_horizontalLayout_2, 2, 0, 1, 1)

    def Page3_SpacerItem7(self):
        page3_spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.page3_horizontalLayout_2.addItem(page3_spacerItem7)

    def Page3_PushButton_3(self):
        # Tombol Load Item, bawah
        self.page3_pushButton_3 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        self.page3_pushButton_3.setMinimumSize(QtCore.QSize(100, 30))
        self.page3_pushButton_3.setMaximumSize(QtCore.QSize(150, 16777215))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/Tambah/Refresh_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_3.setIcon(icon14)
        self.page3_pushButton_3.setObjectName("page3_pushButton_3")
        self.page3_pushButton_3.setText("  Load Item ")
        self.page3_horizontalLayout_2.addWidget(self.page3_pushButton_3)

    def Page3_PushButton_2(self):
        # Tombol Hapus Item, bawah
        self.page3_pushButton_2 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        self.page3_pushButton_2.setMinimumSize(QtCore.QSize(100, 30))
        self.page3_pushButton_2.setMaximumSize(QtCore.QSize(150, 16777215))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Tambah/Remove_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_2.setIcon(icon8)
        self.page3_pushButton_2.setObjectName("page3_pushButton_2")
        self.page3_pushButton_2.setText("  Hapus Item ")
        self.page3_horizontalLayout_2.addWidget(self.page3_pushButton_2)

    def Page3_PushButton_5(self):
        # Tombol Ubah Item, bawah
        self.page3_pushButton_5 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        self.page3_pushButton_5.setMinimumSize(QtCore.QSize(100, 30))
        self.page3_pushButton_5.setMaximumSize(QtCore.QSize(150, 16777215))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Tambah/Edit_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_5.setIcon(icon10)
        self.page3_pushButton_5.setObjectName("page3_pushButton_5")
        self.page3_pushButton_5.setText("  Ubah Item ")
        self.page3_horizontalLayout_2.addWidget(self.page3_pushButton_5)

    def Page3_PushButton_4(self):
        # Tombol Tambah Item, bawah
        self.page3_pushButton_4 = QtWidgets.QPushButton(self.page3_tab3_Tab1)
        self.page3_pushButton_4.setMinimumSize(QtCore.QSize(100, 30))
        self.page3_pushButton_4.setMaximumSize(QtCore.QSize(150, 16777215))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Tambah/Add_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page3_pushButton_4.setIcon(icon11)
        self.page3_pushButton_4.setObjectName("page3_pushButton_4")
        self.page3_pushButton_4.setText("  Tambah Item ")
        self.page3_horizontalLayout_2.addWidget(self.page3_pushButton_4)

    def Page3_PushButton_6(self):
        self.page3_pushButton_6 = QtWidgets.QPushButton("Cetak Label")
        self.page3_horizontalLayout_2.addWidget(self.page3_pushButton_6)
        self.page3_pushButton_6.setMinimumSize(100, 30)
        self.page3_pushButton_6.setMaximumSize(150, 150000)

    def Page3_SpacerItem8(self):
        page3_spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.page3_horizontalLayout_2.addItem(page3_spacerItem8)

    def Page3_TableWidget(self):
        self.page3_tableWidget = QtWidgets.QTableWidget(self.page3_tab3_Tab1)
        self.page3_tableWidget.setObjectName("page3_tableWidget")
        self.page3_tableWidget.setStyleSheet('selection-background-color: #0F82DC; selection-color: white')
        self.page3_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        # self.page3_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.page3_tableWidget.setDragEnabled(False)
        self.page3_tableWidget.setAlternatingRowColors(True)
        self.page3_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.page3_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.page3_tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.page3_tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.page3_tableWidget.setRowCount(0)
        self.page3_tableWidget.setColumnCount(0)
        self.page3_tableWidget.verticalHeader().setVisible(False)
        self.page3_tableWidget.horizontalHeader().setFont(Font(10, True))
        self.page3_tab_ATUR_STOK_TAB_SemuaItem_gridLayout.addWidget(self.page3_tableWidget, 1, 0, 1, 1)

    def Page3_Tab_3(self):
        self.page3_tab_3 = QtWidgets.QWidget()
        self.page3_tab_3.setObjectName("page3_tab_3")
        self.page3_tab_ATUR_STOK_TAB.addTab(self.page3_tab_3, "")
        self.page3_tab_ATUR_STOK_TAB.setTabText(self.page3_tab_ATUR_STOK_TAB.indexOf(self.page3_tab_3), "Page")

    def Page3_Execution(self, username, kelas):
        self.page3_username = username
        self.page3_kelas = kelas
        self.CreateEventSystemLOG(username, 'membuka Page 3 (Atur Stok)')
        # TAB 3
        self.Tab3()  # Page 3
        self.Page3_GridLayout_7()  # Page 3
        self.Page3_Tab_ATUR_STOK_GridLayout()  # Page 3
        self.Page3_Tab_ATUR_STOK_TAB()  # Page 3
        self.Page3_Tab3_Tab1()  # Page 3
        self.Page3_Tab3_Tab2()
        self.Page3_Tab3_Tab3()
        self.Page3_Tab3_Tab4()
        self.Page3_GridLayout()  # Page 3
        self.Page3_Tab_ATUR_STOK_TAB_SemuaItem_gridLayout()  # Page 3
        self.Page3_GridLayout_4()  # Page 3
        self.Page3_HorizontalLayout_20()  # Page 3
        # self.Page3_ComboBox_3()  # Page 3
        # self.Page3_LineEdit_7()  # Page 3
        # self.Page3_PushButton_29()  # Page 3
        # self.Page3_PushButton_36()  # Page 3
        # self.Page3_PushButton_26()  # Page 3
        # self.Page3_Label_4()  # Page 3
        self.Page3_Label()  # Page 3
        self.Page3_PushButton()  # Tombol Cari, baris pertama
        self.Page3_LineEdit()  # LineEdit Cari, baris pertama
        self.Page3_HorizontalLayout_10()  # Page 3
        # self.Page3_ComboBox()  # Page 3
        # self.Page3_LineEdit_4()  # Page 3
        # self.Page3_PushButton_25()  # Page 3
        self.Page3_HorizontalLayout_18()  # Page 3
        # self.Page3_ComboBox_2()  # Page 3
        # self.Page3_LineEdit_3()  # Page 3
        # self.Page3_PushButton_27()  # Page 3
        self.Page3_HorizontalLayout_21()  # Page 3
        # self.Page3_ComboBox_4()  # Page 3
        # self.Page3_LineEdit_6()  # Page 3
        # self.Page3_PushButton_28()  # Page 3
        # self.Page3_PushButton_35()  # Page 3
        self.Page3_HorizontalLayout_22()  # Page 3
        # self.Page3_ComboBox_5()  # Page 3
        # self.Page3_LineEdit_8()  # Page 3
        # self.Page3_PushButton_30()  # Page 3
        # self.Page3_PushButton_37()  # Page 3
        # self.Page3_PushButton_31()  # Page 3
        # self.Page3_PushButton_32()  # Page 3
        # self.Page3_PushButton_33()  # Page 3
        # self.Page3_PushButton_34()  # Page 3
        self.Page3_HorizontalLayout_2()  # Page 3
        self.Page3_SpacerItem7()  # Page 3
        self.Page3_PushButton_3()  # Tombol Load Item, bawah
        self.Page3_PushButton_2()  # Tombol Hapus Item, bawah
        self.Page3_PushButton_5()  # Tombol Ubah Item, bawah
        self.Page3_PushButton_4()  # Tombol Tambah Item, bawah
        self.Page3_PushButton_6()
        self.Page3_SpacerItem8()  # Page 3
        self.Page3_TableWidget()  # Page 3
        #self.Page3_Tab_3()  # Page 3
        self.Page3_UBAH_TAMPILAN_GUI()
        self.Page3_Database()
        self.Page3_TableWidgetView()
        self.Page3_CariItem_Completer()
        self.Page3_PERINTAH()
        self.Page3_ResolutionManager()

    '''
    RUBAH GUI DISINI :
    '''

    def Page3_UBAH_TAMPILAN_GUI(self):
        self.page3_lineEdit.setMinimumSize(0, 50)
        self.page3_lineEdit.setFont(Font(10, False))

        self.page3_pushButton.setMinimumSize(250, 50)
        self.page3_pushButton.setFont(Font(10, True))

        self.page3_pushButton_3.setMinimumSize(250, 70)
        self.page3_pushButton_3.setFont(Font(10, True))

        self.page3_pushButton_2.setMinimumSize(250, 70)
        self.page3_pushButton_2.setFont(Font(10, True))

        self.page3_pushButton_5.setMinimumSize(250, 70)
        self.page3_pushButton_5.setFont(Font(10, True))

        self.page3_pushButton_4.setMinimumSize(250, 70)
        self.page3_pushButton_4.setFont(Font(10, True))
        pass

    def Page3_Database(self):
        self.page3_database_connection = sqlite3.connect(self.page3_databasePath1)
        self.page3_database_cursor = self.page3_database_connection.cursor()

    def Page3_TableWidgetView(self):
        self.page3_pushButton_3.setDisabled(True)
        # LineEdit Pencarian Operation
        self.page3_lineEdit.clear()

        # Column Operation
        self.page3_database_connection = sqlite3.connect(self.page3_databasePath1)
        self.page3_database_connection.row_factory = sqlite3.Row
        self.page3_database_cursor = self.page3_database_connection.cursor()
        column = self.page3_database_cursor.execute('select * from Data_Produk_Master')
        column2 = column.fetchone()
        self.column3 = column2.keys()
        self.page3_tableWidget.setColumnCount(len(self.column3))
        for columnIndex in range(len(self.column3)):
            self.page3_tableWidget.setHorizontalHeaderItem(columnIndex, QtWidgets.QTableWidgetItem(self.column3[columnIndex]))
            columntoIndexdict = {self.column3[columnIndex]: columnIndex}
            IndexToColumndict = {columnIndex: self.column3[columnIndex]}
            self.Page3_KolomtoIndex.update(columntoIndexdict)
            self.Page3_IndextoKolom.update(IndexToColumndict)
        self.page3_tableWidget.setColumnWidth(0, 30)  # No
        self.page3_tableWidget.setColumnWidth(1, 80)  # SKU_Induk
        self.page3_tableWidget.setColumnWidth(2, 100)  # SKU_Varian_1
        self.page3_tableWidget.setColumnWidth(3, 100)  # SKU_Varian_2
        self.page3_tableWidget.setColumnWidth(4, 120)  # Kode_Toko
        self.page3_tableWidget.setColumnWidth(5, 150)  # Barcode_Produk
        self.page3_tableWidget.setColumnWidth(6, 500)  # Nama_Produk_Di_Distributor
        self.page3_tableWidget.setColumnWidth(7, 500)  # Nama_Produk_Di_Toko
        self.page3_tableWidget.setColumnWidth(8, 80)  # Repack
        self.page3_tableWidget.setColumnWidth(9, 240)  # Produk_Umum_Khusus
        self.page3_tableWidget.setColumnWidth(10, 500)  # Deskripsi_Produk
        self.page3_tableWidget.setColumnWidth(11, 100)  # Total_Stok
        self.page3_tableWidget.setColumnWidth(12, 150)  # Total_Stok_Satuan
        self.page3_tableWidget.setColumnWidth(13, 200)  # Berat_atau_Volume_Bersih
        self.page3_tableWidget.setColumnWidth(14, 150)  # Satuan_Berat_Bersih
        self.page3_tableWidget.setColumnWidth(15, 300)  # Berat_Untuk_Pengiriman_Dalam_Gram
        self.page3_tableWidget.setColumnWidth(16, 150)  # Kemasan
        self.page3_tableWidget.setColumnWidth(17, 100)  # Perizinan
        self.page3_tableWidget.setColumnWidth(18, 150)  # Kode_BPOM_atau_PIRT
        self.page3_tableWidget.setColumnWidth(19, 100)  # Label_Halal
        self.page3_tableWidget.setColumnWidth(20, 400)  # Produsen
        self.page3_tableWidget.setColumnWidth(21, 400)  # Distributor
        self.page3_tableWidget.setColumnWidth(22, 250)  # Nama_Sales
        self.page3_tableWidget.setColumnWidth(23, 200)  # No_Telepon_Sales
        self.page3_tableWidget.setColumnWidth(24, 150)  # Harga_Beli_Terakhir
        self.page3_tableWidget.setColumnWidth(25, 150)  # Biaya_Penanganan
        self.page3_tableWidget.setColumnWidth(26, 200)  # Laba_Dasar_Dalam_Persen
        self.page3_tableWidget.setColumnWidth(27, 200)  # Laba_Dasar_Dalam_Rupiah
        self.page3_tableWidget.setColumnWidth(28, 150)  # Harga_Jual_Dasar
        self.page3_tableWidget.setColumnWidth(29, 250)  # Laba_Saat_Diskon_Dalam_Persen
        self.page3_tableWidget.setColumnWidth(30, 250)  # Laba_Saat_Diskon_Dalam_Rupiah
        self.page3_tableWidget.setColumnWidth(31, 200)  # Harga_Jual_Saat_Diskon
        self.page3_tableWidget.setColumnWidth(32, 250)  # Minimal_Pembelian_Grosir_1
        self.page3_tableWidget.setColumnWidth(33, 250)  # Laba_Saat_Grosir_1_Dalam_Persen
        self.page3_tableWidget.setColumnWidth(34, 250)  # Laba_Saat_Grosir_1_Dalam_Rupiah
        self.page3_tableWidget.setColumnWidth(35, 250)  # Harga_Jual_Saat_Grosir_1
        self.page3_tableWidget.setColumnWidth(36, 250)  # Minimal_Pembelian_Grosir_2
        self.page3_tableWidget.setColumnWidth(37, 250)  # Laba_Saat_Grosir_2_Dalam_Persen
        self.page3_tableWidget.setColumnWidth(38, 250)  # Laba_Saat_Grosir_2_Dalam_Rupiah
        self.page3_tableWidget.setColumnWidth(39, 250)  # Harga_Jual_Saat_Grosir_2
        self.page3_tableWidget.setColumnWidth(40, 250)  # Minimal_Pembelian_Grosir_3
        self.page3_tableWidget.setColumnWidth(41, 250)  # Laba_Saat_Grosir_3_Dalam_Persen
        self.page3_tableWidget.setColumnWidth(42, 250)  # Laba_Saat_Grosir_3_Dalam_Rupiah
        self.page3_tableWidget.setColumnWidth(43, 250)  # Harga_Jual_Saat_Grosir_3
        self.page3_tableWidget.setColumnWidth(44, 400)  # Catatan
        self.page3_tableWidget.setColumnWidth(45, 150)  # Foto_Produk_1
        self.page3_tableWidget.setColumnWidth(46, 150)  # Foto_Produk_2
        self.page3_tableWidget.setColumnWidth(47, 150)  # Foto_Produk_3
        self.page3_tableWidget.setColumnWidth(48, 150)  # Foto_Produk_4
        self.page3_tableWidget.setColumnWidth(49, 150)  # Foto_Produk_5
        self.page3_tableWidget.setColumnWidth(50, 150)  # Foto_Produk_6
        self.page3_tableWidget.setColumnWidth(51, 150)  # Foto_Produk_7
        self.page3_tableWidget.setColumnWidth(52, 150)  # Foto_Produk_8
        self.page3_tableWidget.setColumnWidth(53, 150)  # Foto_Produk_9
        self.page3_tableWidget.setColumnWidth(54, 150)  # Foto_Video
        self.page3_tableWidget.setColumnWidth(55, 150)  # Posisi_Barang

        # Row Operation
        rows = self.page3_database_cursor.execute('select * from Data_Produk_Master order by "No" asc').fetchall()
        self.page3_tableWidget.setRowCount(len(rows))
        for row in range(len(rows)):
            for indexKolom in range(len(self.column3)):
                self.page3_tableWidget.setItem(row, indexKolom, QtWidgets.QTableWidgetItem(str(rows[row][(self.column3[indexKolom])])))
        self.page3_tableWidget.setFont(Font(10, False))

        self.page3_pushButton_3.setEnabled(True)

    def Page3_TableWidget_ClickOnCell_Action(self):
        try:
            columnName = self.page3_tableWidget.horizontalHeaderItem(self.page3_tableWidget.currentColumn()).text()
            rowName_ByItem = self.page3_tableWidget.item(self.page3_tableWidget.currentRow(), self.page3_tableWidget.currentColumn()).text()
            rowName_ByKode = self.page3_tableWidget.item(self.page3_tableWidget.currentRow(), 4).text()
            rowName_ByBarcode = self.page3_tableWidget.item(self.page3_tableWidget.currentRow(), 5).text()
        except:
            columnName = ''
            rowName_ByItem = ''
            rowName_ByKode = ''
            rowName_ByBarcode = ''
        # print('Nama Kolom : ', columnName)
        # print('Nama Item : ', rowName_ByItem)
        # print('Kode Produk : ', rowName_ByKode)
        # print('Barcode : ', rowName_ByBarcode, '\n')

    def Page3_CariItem_Completer(self):
        self.List_Kode = []
        self.List_Barcode = []
        self.List_Nama_Item = []
        Completer_Gabungan = []
        rows = self.page3_database_cursor.execute('select * from Data_Produk_Master').fetchall()
        for row in range(len(rows)):
            self.List_Kode.append(str(rows[row]['Kode_Toko']))
            self.List_Barcode.append(str(rows[row]['Barcode_Produk']))
            self.List_Nama_Item.append(str(rows[row]['Nama_Produk_Di_Toko']))
            if str(rows[row]['Kode_Toko']) not in Completer_Gabungan:
                Completer_Gabungan.append(str(rows[row]['Kode_Toko']))
            else:
                pass
            if str(rows[row]['Barcode_Produk']) not in Completer_Gabungan:
                Completer_Gabungan.append(str(rows[row]['Barcode_Produk']))
            else:
                pass
            if str(rows[row]['Nama_Produk_Di_Toko']) not in Completer_Gabungan:
                Completer_Gabungan.append(str(rows[row]['Nama_Produk_Di_Toko']))
            else:
                pass

        Completer = Completer_Gabungan
        Completer.sort()
        self.page3_completer = QtWidgets.QCompleter(Completer)
        self.page3_completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.page3_completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_lineEdit.setCompleter(self.page3_completer)
        self.page3_completer.activated.connect(self.Page3_CariItem_Completer_Completed)

    def Page3_CariItem_Completer_Completed(self):
        text = self.page3_lineEdit.text().upper()
        BanyakData = self.page3_tableWidget.rowCount()
        Barcode_to_Row_dict = {}
        KodeToko_to_Row_dict = {}
        NamaProduk_to_Row_dict = {}
        KodeToko_to_Barcode_dict = {}
        Barcode_to_KodeToko_dict = {}
        NamaProduk_to_Barcode_dict = {}
        Barcode_to_NamaProduk_dict = {}

        BarcodeDitampilkan = []
        BarisDitampilkan = []

        for item in range(BanyakData):
            barcode = self.page3_tableWidget.item(item, self.Page3_KolomtoIndex['Barcode_Produk']).text()
            barcode_to_Row = {barcode: item}
            Barcode_to_Row_dict.update(barcode_to_Row)

            kodeToko = self.page3_tableWidget.item(item, self.Page3_KolomtoIndex['Kode_Toko']).text()
            kodeToko_to_Row = {kodeToko: item}
            kodeToko_to_Barcode = {kodeToko: barcode}
            Barcode_to_KodeToko = {barcode: kodeToko}
            KodeToko_to_Row_dict.update(kodeToko_to_Row)
            KodeToko_to_Barcode_dict.update(kodeToko_to_Barcode)
            Barcode_to_KodeToko_dict.update(Barcode_to_KodeToko)

            namaProduk = self.page3_tableWidget.item(item, self.Page3_KolomtoIndex['Nama_Produk_Di_Toko']).text()
            namaProduk_to_Row = {namaProduk: item}
            NamaProduk_to_Row_dict.update(namaProduk_to_Row)
            namaProduk_to_Barcode = {namaProduk: barcode}
            Barcode_to_namaProduk = {barcode: namaProduk}
            NamaProduk_to_Barcode_dict.update(namaProduk_to_Barcode)
            Barcode_to_NamaProduk_dict.update(Barcode_to_namaProduk)



        for item in self.List_Barcode:
            if text in item.upper():
                Barcode = item
                if Barcode not in BarcodeDitampilkan:
                    BarcodeDitampilkan.append(Barcode)
                else:
                    pass

        for item in self.List_Kode:
            if text in item.upper():
                Barcode = KodeToko_to_Barcode_dict[item]
                if Barcode not in BarcodeDitampilkan:
                    BarcodeDitampilkan.append(Barcode)
                else:
                    pass

        for item in self.List_Nama_Item:
            if text in item.upper():
                Barcode = NamaProduk_to_Barcode_dict[item]
                if Barcode not in BarcodeDitampilkan:
                    BarcodeDitampilkan.append(Barcode)
                else:
                    pass

        for item in BarcodeDitampilkan:
            Baris = Barcode_to_Row_dict[item]
            BarisDitampilkan.append(Baris)

        for item in range(BanyakData):
            self.page3_tableWidget.hideRow(item)
            for item2 in BarisDitampilkan:
                if item2 == item:
                    self.page3_tableWidget.showRow(item)
                else:
                    pass
        self.page3_tableWidget.scrollToTop()

    def Page3_PushButton_2_clicked(self):
        Page3_chi(self)

    def Page3_PushButton_3_clicked(self):
        self.Page3_TableWidgetView()
        BanyakData = self.page3_tableWidget.rowCount()
        for item in range(BanyakData):
            self.page3_tableWidget.showRow(item)

    def Page3_PushButton_5_clicked(self):
        def SimpanData():
            conn = sqlite3.connect(DatabaseProduk())
            DBColumn = conn.execute('select * from Data_Produk_Master')
            DBColumnNames = list(map(lambda x: x[0], DBColumn.description))
            DBColumnNames.remove('Barcode_Produk')
            curr = conn.cursor()

            # Hapus Isi Database
            curr.execute('delete from Data_Produk_Master')


            BanyakData = self.page3_tableWidget.rowCount()
            for item in range(BanyakData):
                self.page3_tableWidget.showRow(item)

            for item in range(BanyakData):
                Barcode = self.page3_tableWidget.item(item, self.Page3_KolomtoIndex['Barcode_Produk']).text()

                curr.execute("INSERT INTO Data_Produk_Master ('Barcode_Produk') VALUES ('{}')".format(str(Barcode)))
                for item2 in DBColumnNames:
                    Data = self.page3_tableWidget.item(item, self.Page3_KolomtoIndex[str(item2)]).text()
                    curr.execute("update Data_Produk_Master set '{}'='{}' where Barcode_Produk='{}'".format(item2, Data, Barcode))
            conn.commit()
            conn.close()

            DialogSimpanData()

        def DialogSimpanData():
            self.Page3_PesanError("Sukses", "Data berhasil disimpan !!")

        SimpanData()
        self.Page3_CariItem_Completer()
        baris_terakhir = self.page3_tableWidget.currentRow()
        self.page3_tableWidget.scrollToItem(self.page3_tableWidget.item(baris_terakhir, 0))

    def Page3_PushButton_4_clicked(self):
        Page3_cti(self)

    def Page3_PushButton_6_clicked(self):
        def Gagal_Cetak(tittle, messege):
            Dialog = QtWidgets.QMessageBox()
            Dialog.setIcon(QtWidgets.QMessageBox.Warning)
            Dialog.setModal(True)
            Dialog.setWindowTitle(tittle)
            Dialog.setText(messege)
            Dialog.show()
            Dialog.exec_()
        printer = Usb(0x0483, 0x5840, 0, 0x58, 0x03)
        try:
            Barcode = self.page3_tableWidget.item(self.page3_tableWidget.currentRow(), 5).text()
            NamaProduk = self.page3_tableWidget.item(self.page3_tableWidget.currentRow(), 7).text()
            harga = self.page3_tableWidget.item(self.page3_tableWidget.currentRow(), 32).text()
        except:
            Barcode = ''
            NamaProduk = ""
            harga = ""

        if Barcode == "":
            Gagal_Cetak("Gagal Cetak", "Anda belum memilih produk yang akan dicetak")
            pass
        elif NamaProduk == "":
            Gagal_Cetak("Gagal Cetak", "Anda belum memilih produk yang akan dicetak")
            pass
        elif harga == "":
            Gagal_Cetak("Gagal Cetak", "Anda belum memilih produk yang akan dicetak")
            pass
        else:
            # Label Harga di Rak
            def Barcode_Label_Harga_Rak():
                printer.set("center", "a", False, 0, width=1, height=1, custom_size=False)
                try:
                    locale.setlocale(locale.LC_ALL, "en_ID")
                    Harga = locale.format_string("%d", val=int(harga), grouping=True)

                    lebar_cetak = 402
                    tinggi_barcode = 100

                    code128.image(Barcode, tinggi_barcode).save("{}.png".format(Barcode))
                    img = Image.open('{}.png'.format(Barcode))
                    wpercent = (lebar_cetak / float(img.size[0]))
                    hsize = int((float(img.size[1]) * float(wpercent)))
                    img = img.resize((lebar_cetak, hsize), Image.ANTIALIAS)
                    img.save("{}.png".format(Barcode))

                    printer.text("--------------------------------")
                    printer.text("\n{}".format(NamaProduk))
                    printer.text("\n")
                    printer.set("center", "a", True, 0, width=8, height=8, custom_size=True)
                    printer.text("\nRp. " + str(Harga) + ",-")
                    printer.set("center", "a", False, 0, width=1, height=1, custom_size=False)
                    printer.text("\n")
                    printer.text("\n({})".format(Barcode))
                    printer.text("\n--------------------------------")
                    printer.text("\n\n")
                    Dialog.close()
                except:
                    print("Error : Cetak Barcode Label Harga Rak Error")
                    pass

            # Label Harga di Showcase
            def Barcode_Label_Harga_Showcase():
                printer.set("center", "b", False, 0, width=1, height=1, custom_size=False)
                try:
                    locale.setlocale(locale.LC_ALL, "en_ID")
                    Harga = locale.format_string("%d", val=int(harga), grouping=True)

                    lebar_cetak = 402
                    tinggi_barcode = 100

                    code128.image(Barcode, tinggi_barcode).save("{}.png".format(Barcode))
                    img = Image.open('{}.png'.format(Barcode))
                    wpercent = (lebar_cetak / float(img.size[0]))
                    hsize = int((float(img.size[1]) * float(wpercent)))
                    img = img.resize((lebar_cetak, hsize), Image.ANTIALIAS)
                    img.save("{}.png".format(Barcode))

                    printer.text("\n------------------------------------------")
                    printer.text("\n{}".format(NamaProduk))
                    printer.set("center", "a", True, 0, width=8, height=8, custom_size=True)
                    printer.text("\nRp. " + str(Harga) + ",-")
                    printer.set("center", "b", False, 0, width=1, height=1, custom_size=False)
                    printer.text("\n({})".format(Barcode))
                    printer.text("\n------------------------------------------")
                    printer.text("\n\n")
                    Dialog.close()
                except:
                    print("Error : Cetak Barcode Label Harga Rak Error")
                    pass

            Dialog = QtWidgets.QDialog()
            Dialog.resize(250, 75)
            Dialog.setWindowTitle("Cetak Label Harga")
            Dialog.setModal(True)
            Layout = QtWidgets.QGridLayout(Dialog)

            Text = QtWidgets.QLabel("Pilih Ukuran Cetak : ")
            Text.setAlignment(QtCore.Qt.AlignHCenter)
            Layout.addWidget(Text, 0, 1, 1, 2)

            PushButton_Showcase = QtWidgets.QPushButton("Showcase")
            PushButton_Showcase.setMinimumHeight(30)
            PushButton_Showcase.clicked.connect(Barcode_Label_Harga_Showcase)
            Layout.addWidget(PushButton_Showcase, 1, 1)

            PushButton_Rak_Gondola = QtWidgets.QPushButton("Rak Gondola")
            PushButton_Rak_Gondola.setMinimumHeight(30)
            PushButton_Rak_Gondola.clicked.connect(Barcode_Label_Harga_Rak)
            Layout.addWidget(PushButton_Rak_Gondola, 1, 2)

            Dialog.show()
            PushButton_Rak_Gondola.setFocus()
            Dialog.exec_()
            printer.close()

    def Page3_PERINTAH(self):
        self.page3_tableWidget.currentCellChanged.connect(self.Page3_TableWidget_ClickOnCell_Action)
        self.page3_pushButton.clicked.connect(self.Page3_CariItem_Completer_Completed)
        self.page3_pushButton_2.clicked.connect(self.Page3_PushButton_2_clicked)
        self.page3_pushButton_3.clicked.connect(self.Page3_PushButton_3_clicked)
        self.page3_pushButton_4.clicked.connect(self.Page3_PushButton_4_clicked)
        self.page3_pushButton_5.clicked.connect(self.Page3_PushButton_5_clicked)
        self.page3_pushButton_6.clicked.connect(self.Page3_PushButton_6_clicked)
        self.page3_lineEdit.editingFinished.connect(self.Page3_CariItem_Completer_Completed)
        pass

    def Page3_ResolutionManager(self):
        Resolusi = CekResolusi()
        if Resolusi == '1280x720':
            self.page3_lineEdit.setFixedHeight(25)
            self.page3_pushButton.setFixedSize(100, 27)
            self.page3_pushButton.setFont(Font(8, True))
            self.page3_pushButton_2.setFixedSize(150, 30)
            self.page3_pushButton_3.setFixedSize(150, 30)
            self.page3_pushButton_4.setFixedSize(150, 30)
            self.page3_pushButton_5.setFixedSize(150, 30)
        elif Resolusi == '2880x1620':
            pass
        else:
            pass


# Page3_cti = Page3_ClassTambahItem (untuk menambahkan item baru ke dalam database)
class Page3_cti(Page3):
    def __init__(self, data, parent=None):
        super(Page3_cti, self).__init__()
        self.Data = data
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setModal(True)
        self.Dialog.setMinimumSize(500, 600)
        self.Dialog.setWindowTitle("Tambah Produk")
        self.page3_cti_layout = QtWidgets.QVBoxLayout(self.Dialog)
        self.Page3_cti_Label()  # Label pembuka
        self.page3_cti_scrollArea = QtWidgets.QScrollArea()
        self.page3_cti_scrollArea.setWidgetResizable(True)
        self.page3_cti_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.page3_cti_GridLayout_2 = QtWidgets.QGridLayout(self.page3_cti_scrollAreaWidgetContents)
        self.page3_cti_scrollArea.setWidget(self.page3_cti_scrollAreaWidgetContents)
        self.page3_cti_layout.addWidget(self.page3_cti_scrollArea)

        self.Page3_cti_Label_2()        # Label Nomor
        self.Page3_cti_LineEdit()       # LineEdit Nomor
        self.Page3_cti_Label_65()       # Label SKU Induk
        self.Page3_cti_LineEdit_34()    # LineEdit SKU Induk
        self.Page3_cti_Label_66()       # Label SKU Varian 1
        self.Page3_cti_LineEdit_35()    # LineEdit SKU Varian 1
        self.Page3_cti_Label_67()       # Label SKU Varian 2
        self.Page3_cti_LineEdit_36()    # LineEdit SKU Varian 2
        self.Page3_cti_Label_3()        # Label Kode_Toko
        self.Page3_cti_LineEdit_2()     # LineEdit Kode_Toko
        self.Page3_cti_Label_5()        # Label Barcode_Produk
        self.Page3_cti_LineEdit_4()     # LineEdit Barcode_Produk
        self.Page3_cti_Label_6()        # Label Nama Produk di Distributor
        self.Page3_cti_LineEdit_5()     # LineEdit Nama Produk di Distributor
        self.Page3_cti_Label_4()        # Label Nama_Produk
        self.Page3_cti_LineEdit_3()     # LineEdit Nama_Produk
        self.Page3_cti_Label_7()        # Label Deskripsi_Produk
        self.Page3_cti_TextEdit()       # TextEdit Deskripsi_Produk
        self.Page3_cti_Label_68()       # Label Total Stok
        self.Page3_cti_HBoxLayout_19()  # HBoxLayout Total Stok
        self.Page3_cti_LineEdit_37()    # LineEdit Total Stok
        self.Page3_cti_ComboBox_4()     # ComboBox Total Stok Satuan
        self.Page3_cti_Label_73()       # Label Warning Stok
        self.Page3_cti_HBoxLayout_23()  # HBoxLayout Warning Stok
        self.Page3_cti_LineEdit_40()    # LineEdit Warning Stok
        self.Page3_cti_ComboBox_7()     # ComboBox Warning Stok

        self.Page3_cti_Label_69()       # Label Berat/Volume di Kemasan
        self.Page3_cti_HBoxLayout_20()  # HBoxLayout Berat/Volume di Kemasan
        self.Page3_cti_LineEdit_38()    # LineEdit Berat/Volume di Kemasan
        self.Page3_cti_ComboBox_5()     # ComboBox Berat/Volume di Kemasan Satuan
        self.Page3_cti_Label_8()        # Label Berat_Untuk_Pengiriman
        self.Page3_cti_HBoxLayout()     # HBoxLayout Berat_Untuk_Pengiriman
        self.Page3_cti_LineEdit_6()     # LineEdit Berat_Untuk_Pengiriman
        self.Page3_cti_Label_9()        # Label Gram untuk Berat_Untuk_Pengiriman
        self.Page3_cti_Label_10()       # Label Kemasan
        self.Page3_cti_ComboBox()       # ComboBox Kemasan
        self.Page3_cti_Label_11()       # Label Perizinan
        self.Page3_cti_ComboBox_2()     # ComboBox Perizinan
        self.Page3_cti_Label_12()       # Label Kode_BPOM_atau_PIRT
        self.Page3_cti_LineEdit_7()     # LineEdit Kode_BPOM_atau_PIRT
        self.Page3_cti_Label_13()       # Label Label_Halal
        self.Page3_cti_ComboBox_3()     # ComboBox Label_Halal
        self.Page3_cti_Label_14()       # Label Produsen
        self.Page3_cti_LineEdit_8()     # LineEdit Produsen
        self.Page3_cti_Label_15()       # Label Distributor
        self.Page3_cti_LineEdit_9()     # LineEdit Distributor
        self.Page3_cti_Label_16()       # Label Nama_Sales
        self.Page3_cti_LineEdit_10()    # LineEdit Nama_Sales
        self.Page3_cti_Label_17()       # Label Nomor_Telepon_Sales
        self.Page3_cti_LineEdit_11()    # LineEdit Nomor_Telepon_Sales
        self.Page3_cti_Label_18()       # Label Barang Umum / Khusus
        self.Page3_cti_HBoxLayout_21()  # HBoxLayout Barang Umum atau Khusus
        self.Page3_cti_ComboBox_6()     # ComboBox Barang Umum atau Khusus
        self.Page3_cti_SpacerItem()     # SpacerItem
        self.Page3_cti_Label_19()       # Label PENJUALAN
        self.Page3_cti_Label_20()       # Label Harga_Beli_Terakhir_Per_Satuan_Terkecil
        self.Page3_cti_LineEdit_13()    # LineEdit Harga_Beli_Terakhir_Per_Satuan_Terkecil
        self.Page3_cti_Label_70()       # Label_Biaya Penanganan
        self.Page3_cti_HBoxLayout_22()  # HBoxLayout Biaya Penanganan
        self.Page3_cti_Label_71()       # Label "Rp. " Biaya Penanganan
        self.Page3_cti_LineEdit_12()    # LineEdit Biaya Penanganan
        self.Page3_cti_Label_72()       # Label ",-" Biaya Penanganan
        self.Page3_cti_Label_21()       # Label Laba_Dasar (dalam persen dan rupiah)
        self.Page3_cti_HBoxLayout_2()   # HBoxLayout Laba_Dasar (dalam persen dan rupiah)
        self.Page3_cti_LineEdit_14()    # LineEdit % Laba_Dasar (dalam persen dan rupiah)
        self.Page3_cti_Label_22()       # Label % Laba_Dasar (dalam persen dan rupiah)
        self.Page3_cti_Label_23()       # Label "-->" Laba_Dasar (dalam persen dan rupiah)
        self.Page3_cti_Label_24()       # Label " rupiah" Laba_Dasar (dalam persen dan rupiah)
        self.Page3_cti_LineEdit_15()    # LineEdit rupiah Laba_Dasar (dalam persen dan rupiah)
        self.Page3_cti_Label_25()       # Label Harga_Jual_Dasar
        self.Page3_cti_HBoxLayout_3()   # HBoxLayout Harga_Jual_Dasar
        self.Page3_cti_Label_26()       # Label Rupiah Harga_Jual_Dasar
        self.Page3_cti_LineEdit_16()    # LineEdit Harga_Jual_Dasar
        self.Page3_cti_Label_27()       # Label Laba_Saat_Diskon
        self.Page3_cti_HBoxLayout_4()   # HBoxLayout Laba_Saat_Diskon
        self.Page3_cti_LineEdit_17()    # LineEdit Laba_Saat_Diskon (Persen)
        self.Page3_cti_Label_28()       # Label % Laba_Saat_Diskon
        self.Page3_cti_Label_29()       # Label --> Laba_Saat_Diskon
        self.Page3_cti_Label_30()       # Label Rupiah Laba_Saat_Diskon
        self.Page3_cti_LineEdit_18()    # LineEdit Laba_Saat_Diskon (Rupiah)
        self.Page3_cti_Label_31()       # Label Harga_Jual_Saat_Diskon
        self.Page3_cti_HBoxLayout_5()   # HBoxLayout Harga_Jual_Saat_Diskon
        self.Page3_cti_Label_32()       # Label Rupiah Harga_Jual_Saat_Diskon
        self.Page3_cti_LineEdit_19()    # LineEdit Rupiah Harga_Jual_Saat_Diskon
        self.Page3_cti_Label_33()       # Label Grosir_1
        self.Page3_cti_Label_34()       # Label Minimal_Pembelian_Grosir_1
        self.Page3_cti_HBoxLayout_6()   # HBoxLayout Minimal_Pembelian_Grosir_1
        self.Page3_cti_LineEdit_20()    # LineEdit Minimal_Pembelian_Grosir_1
        self.Page3_cti_Label_35()       # Label Satuan Minimal_Pembelian_Grosir_1
        self.Page3_cti_Label_36()       # Label Laba_Saat_Grosir_1
        self.Page3_cti_HBoxLayout_7()   # HBoxLayout Laba_Saat_Grosir_1
        self.Page3_cti_LineEdit_21()    # LineEdit % Laba_Saat_Grosir_1
        self.Page3_cti_Label_37()       # Label % Laba_Saat_Grosir_1
        self.Page3_cti_Label_38()       # Label --> Laba_Saat_Grosir_1
        self.Page3_cti_Label_39()       # Label Rupiah Laba_Saat_Grosir_1
        self.Page3_cti_LineEdit_22()    # LineEdit Rupiah Laba_Saat_Grosir_1
        self.Page3_cti_Label_40()       # Label Harga_Jual_Saat_Grosir_1
        self.Page3_cti_HBoxLayout_8()   # HBoxLayout Harga_Jual_Saat_Grosir_1
        self.Page3_cti_Label_41()       # Label Rupiah Harga_Jual_Saat_Grosir_1
        self.Page3_cti_LineEdit_23()    # LineEdit Rupiah Harga_Jual_Saat_Grosir_1
        self.Page3_cti_Label_42()       # Label Grosir_2
        self.Page3_cti_Label_43()       # Label Minimal_Pembelian_Grosir_2
        self.Page3_cti_HBoxLayout_9()   # HBoxLayout Minimal_Pembelian_Grosir_2
        self.Page3_cti_LineEdit_24()    # LineEdit Minimal_Pembelian_Grosir_2
        self.Page3_cti_Label_44()       # Label Satuan Minimal_Pembelian_Grosir_2
        self.Page3_cti_Label_45()       # Label Laba_Saat_Grosir_2
        self.Page3_cti_HBoxLayout_10()  # HBoxLayout Laba_Saat_Grosir_2
        self.Page3_cti_LineEdit_25()    # LineEdit % Laba_Saat_Grosir_2
        self.Page3_cti_Label_46()       # Label % Laba_Saat_Grosir_2
        self.Page3_cti_Label_47()       # Label --> Laba_Saat_Grosir_2
        self.Page3_cti_Label_48()       # Label Rupiah Laba_Saat_Grosir_2
        self.Page3_cti_LineEdit_26()    # LineEdit Rupiah Laba_Saat_Grosir_2
        self.Page3_cti_Label_49()       # Label Harga_Jual_Saat_Grosir_2
        self.Page3_cti_HBoxLayout_11()  # HBoxLayout Harga_Jual_Saat_Grosir_2
        self.Page3_cti_Label_50()       # Label Rupiah Harga_Jual_Saat_Grosir_2
        self.Page3_cti_LineEdit_27()    # LineEdit Harga_Jual_Saat_Grosir_2
        self.Page3_cti_Label_51()       # Label Grosir_3
        self.Page3_cti_Label_52()       # Label Minimal_Pembelian_Saat_Grosir_3
        self.Page3_cti_HBoxLayout_12()  # HBoxLayout Minimal_Pembelian_Saat_Grosir_3
        self.Page3_cti_LineEdit_28()    # LineEdit Minimal_Pembelian_Saat_Grosir_3
        self.Page3_cti_Label_53()       # Label Pcs Minimal_Pembelian_Saat_Grosir_3
        self.Page3_cti_Label_54()       # Label Laba_Saat_Grosir_3
        self.Page3_cti_HBoxLayout_13()  # HBoxLayout Laba_Saat_Grosir_3
        self.Page3_cti_LineEdit_29()    # LineEdit % Laba_Saat_Grosir_3
        self.Page3_cti_Label_55()       # Label% Laba_Saat_Grosir_3
        self.Page3_cti_Label_56()       # Label --> Laba_Saat_Grosir_3
        self.Page3_cti_Label_57()       # Label Rupiah Laba_Saat_Grosir_3
        self.Page3_cti_LineEdit_30()    # LineEdit Rupiah Laba_Saat_Grosir_3
        self.Page3_cti_Label_58()       # Label Harga_Jual_Saat_Grosir_3
        self.Page3_cti_HBoxLayout_14()  # HBoxLayout Harga_Jual_Saat_Grosir_3
        self.Page3_cti_Label_59()       # Label Rupiah Harga_Jual_Saat_Grosir_3
        self.Page3_cti_LineEdit_31()    # LineEdit Harga_Jual_Saat_Grosir_3
        self.Page3_cti_SpacerItem_2()   # SpacerItem INFORMASI TAMBAHAN
        self.Page3_cti_Label_60()       # Label INFORMASI TAMBAHAN
        self.Page3_cti_Label_61()       # Label Catatan
        self.Page3_cti_TextEdit_2()     # TextEdit Catatan
        self.Page3_cti_Label_63()       # Label Foto_Produk
        self.Page3_cti_HBoxLayout_16()  # HBoxLayout Foto_Produk
        self.Page3_cti_LineEdit_33()    # LineEdit Foto_Produk
        self.Page3_cti_PushButton_3()   # PushButton Tambah Foto_Produk
        self.Page3_cti_PushButton_9()   # PushButton Hapus Foto_Produk
        self.Page3_cti_Label_64()       # Label Gambar Foto_Produk
        self.Page3_cti_HBoxLayout_17()  # HBoxLayout Gambar Foto_Produk
        self.Page3_cti_PushButton_4()   # PushButton Gambar1 Foto_Produk
        self.Page3_cti_PushButton_5()   # PushButton Gambar2 Foto_Produk
        self.Page3_cti_PushButton_6()   # PushButton Gambar3 Foto_Produk
        self.Page3_cti_PushButton_7()   # PushButton Gambar4 Foto_Produk
        self.Page3_cti_PushButton_8()   # PushButton Gambar5 Foto_Produk
        self.Page3_cti_HBoxLayout_18()  # HBoxLayout Gambar5 Foto_Produk Baris Kedua
        self.Page3_cti_PushButton_10()  # PushButton Gambar6 Foto_Produk
        self.Page3_cti_PushButton_11()  # PushButton Gambar7 Foto_Produk
        self.Page3_cti_PushButton_12()  # PushButton Gambar8 Foto_Produk
        self.Page3_cti_PushButton_13()  # PushButton Gambar9 Foto_Produk
        self.Page3_cti_PushButton_14()  # PushButton GambarVid Foto_Produk
        self.Page3_cti_Label_62()       # Label Posisi_Barang
        self.Page3_cti_LineEdit_32()    # LineEdit Posisi_Barang
        self.Page3_cti_HBoxLayout_15()  # HBoxLayout untuk PushButton Batalkan dan Simpan
        self.Page3_cti_Spacer_3()       # Spacer di HBoxLayout (agar tombol rata kanan)
        self.Page3_cti_PushButton()     # PushButton Batalkan
        self.Page3_cti_PushButton_2()   # PushButton Simpan
        self.Page3_cti_PushButton_15()  # PushButton Cetak Label Harga

        # INISIASI
        self.Page3_cti_Mode_Editing() # Aktifkan untuk mode editing script
        self.Page3_cti_Definisikan_Data()
        self.Page3_cti_Database_Load()  # Database_Load
        self.Page3_cti_Nomor_Urut()
        self.Page3_cti_SKU_Induk_Completer()  # Database_Kumpulkan Data Awal SKU_Induk
        self.Page3_cti_Produsen_Completer()
        self.Page3_cti_Distributor_Completer()
        self.Page3_cti_Nama_Sales_Completer()
        self.Page3_cti_No_Telepon_Sales_Completer()
        self.Page3_cti_Keuntungan()
        self.Page3_cti_Hitungan_Biaya_Penanganan()
        self.Page3_cti_Hitungan_Laba_Dasar_Dalam_Persen()
        self.Page3_cti_Hitungan_Laba_Saat_Diskon_Dalam_Persen()
        self.Page3_cti_Hitungan_Laba_Saat_Diskon_Dalam_Rupiah()
        self.Page3_cti_Hitungan_Grosir_1_Minimal_Pembelian()
        self.Page3_cti_Hitungan_Grosir_2_Minimal_Pembelian()
        self.Page3_cti_Hitungan_Grosir_3_Minimal_Pembelian()

        # PERINTAH
        self.page3_cti_LineEdit_34.textChanged.connect(self.Page3_cti_Kode_Produk_Di_Toko)
        self.page3_cti_LineEdit_35.textChanged.connect(self.Page3_cti_Kode_Produk_Di_Toko)
        self.page3_cti_LineEdit_36.textChanged.connect(self.Page3_cti_Kode_Produk_Di_Toko)
        self.page3_cti_LineEdit_2.textChanged.connect(self.Page3_cti_Nama_Produk_Di_Distributor_Completer)
        self.page3_cti_LineEdit_38.textChanged.connect(self.Page3_cti_Berat_Untuk_Pengiriman)
        self.page3_cti_ComboBox_5.currentTextChanged.connect(self.Page3_cti_Berat_Untuk_Pengiriman)
        self.page3_cti_PushButton.clicked.connect(self.Page3_cti_Konfirmasi_Tombol_Batal_klik)
        self.page3_cti_PushButton_2.clicked.connect(self.Page3_cti_PushButton_2_klik)
        self.page3_cti_PushButton_15.clicked.connect(self.Page3_cti_Cetak_Label_Harga1)
        self.page3_cti_PushButton_3.clicked.connect(self.Page3_cti_Tambah_Gambar)
        self.page3_cti_ComboBox_2.currentTextChanged.connect(self.Page3_cti_KodeBPOM_atau_PIRT)
        self.page3_cti_LineEdit_8.textChanged.connect(self.Page3_cti_Distributor_Completer)
        self.page3_cti_LineEdit_8.textChanged.connect(self.Page3_cti_Nama_Sales_Completer)
        self.page3_cti_LineEdit_8.textChanged.connect(self.Page3_cti_No_Telepon_Sales_Completer)
        self.page3_cti_LineEdit_9.textChanged.connect(self.Page3_cti_Nama_Sales_Completer)
        self.page3_cti_LineEdit_9.textChanged.connect(self.Page3_cti_No_Telepon_Sales_Completer)
        self.page3_cti_LineEdit_10.textChanged.connect(self.Page3_cti_No_Telepon_Sales_Completer)
        self.page3_cti_ComboBox_6.currentTextChanged.connect(self.Page3_cti_Keuntungan)
        self.page3_cti_ComboBox_6.currentTextChanged.connect(self.Page3_cti_Hitungan_Laba_Dasar_Dalam_Persen)
        self.page3_cti_ComboBox_6.currentTextChanged.connect(self.Page3_cti_Hitungan_Laba_Saat_Diskon_Dalam_Persen)
        self.page3_cti_ComboBox_6.currentTextChanged.connect(self.Page3_cti_Hitungan_Grosir_1_Laba_Dalam_Persen)
        self.page3_cti_ComboBox_6.currentTextChanged.connect(self.Page3_cti_Hitungan_Grosir_2_Laba_Dalam_Persen)
        self.page3_cti_ComboBox_6.currentTextChanged.connect(self.Page3_cti_Hitungan_Grosir_3_Laba_Dalam_Persen)
        self.page3_cti_LineEdit_13.textChanged.connect(self.Page3_cti_Hitungan_Biaya_Penanganan)
        self.page3_cti_LineEdit_13.textChanged.connect(self.Page3_cti_Hitungan_Laba_Dasar_Dalam_Rupiah)
        self.page3_cti_LineEdit_13.textChanged.connect(self.Page3_cti_Hitungan_Laba_Saat_Diskon_Dalam_Rupiah)
        self.page3_cti_LineEdit_13.textChanged.connect(self.Page3_cti_Hitungan_Grosir_1_Laba_Dalam_Rupiah)
        self.page3_cti_LineEdit_13.textChanged.connect(self.Page3_cti_Hitungan_Grosir_2_Laba_Dalam_Rupiah)
        self.page3_cti_LineEdit_13.textChanged.connect(self.Page3_cti_Hitungan_Grosir_3_Laba_Dalam_Rupiah)


        self.Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.Cek_Barcode()

    # Cek apakah produk dengan barcode yang sama telah ada
    def Cek_Barcode(self):
        DB = DatabaseProduk()
        conn = sqlite3.connect(DB)
        curr = conn.cursor()

        Dialog = QtWidgets.QDialog()
        Dialog.setModal(True)
        Dialog.setWindowTitle("Cek Produk")
        Layout = QtWidgets.QGridLayout(Dialog)

        Label_Text = QtWidgets.QLabel("Masukkan barcode produk baru anda terlebih dahulu")
        Layout.addWidget(Label_Text, 0, 0, 1, 3)

        LineEdit_Barcode = QtWidgets.QLineEdit()
        Layout.addWidget(LineEdit_Barcode, 1, 0, 1, 3)

        PushButton_Cek = QtWidgets.QPushButton("Cek")
        Layout.addWidget(PushButton_Cek, 2, 2)

        PushButton_Tidak = QtWidgets.QPushButton("Tanpa Barcode")
        PushButton_Tidak.setMinimumWidth(100)
        Layout.addWidget(PushButton_Tidak, 2, 1)

        Barcode = []
        def Database():
            BarcodeList = curr.execute("select Barcode_Produk from Data_Produk_Master").fetchall()
            for item in range(len(BarcodeList)):
                Barcode.append(BarcodeList[item][0])
            if LineEdit_Barcode.text() in Barcode:
                self.Page3_cti_Pesan_Error("Produk sudah ada", "Produk dengan Barcode ini telah ada, Anda dapat menambahkan transaksi untuk produk tersebut daripada"
                                                               "menambah produk baru")
            elif len(LineEdit_Barcode.text()) == 0:
                LineEdit_Barcode.setFocus()
                pass
            else:
                Dialog.close()
                self.page3_cti_LineEdit_4.setText("{}".format(LineEdit_Barcode.text()))
                self.Dialog.show()
                self.Dialog.exec_()
                pass

        def TanpaBarcode():
            conn.close()
            Dialog.close()
            self.Dialog.show()
            self.Dialog.exec_()

        PushButton_Cek.clicked.connect(Database)
        PushButton_Tidak.clicked.connect(TanpaBarcode)

        Dialog.show()
        Dialog.exec_()

    # Label pembuka
    def Page3_cti_Label(self):
        self.page3_cti_Label = QtWidgets.QLabel("FORM TAMBAH PRODUK BARU :")
        self.page3_cti_Label.setObjectName('Label')
        self.page3_cti_layout.addWidget(self.page3_cti_Label)

    # Label Nomor
    def Page3_cti_Label_2(self):
        widget_sebelumnya = None
        if widget_sebelumnya is None:
            pass
        else:
            pass
        self.page3_cti_Label_2 = QtWidgets.QLabel("No : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_2, 0, 0)

    # LineEdit Nomor
    def Page3_cti_LineEdit(self):
        self.page3_cti_LineEdit = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit.setValidator(IntegerValidator())
        self.page3_cti_LineEdit.setReadOnly(True)
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit, 0, 1)

    # Label SKU Induk
    def Page3_cti_Label_65(self):
        self.page3_cti_Label_65 = QtWidgets.QLabel("SKU Induk : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_65, 1, 0)

    # LineEdit SKU Induk
    def Page3_cti_LineEdit_34(self):
        self.page3_cti_LineEdit_34 = QtWidgets.QLineEdit()
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit_34, 1, 1)

    # Label SKU Varian 1
    def Page3_cti_Label_66(self):
        self.page3_cti_Label_66 = QtWidgets.QLabel("SKU Varian 1 : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_66, 2, 0)

    # LineEdit SKU Varian 1
    def Page3_cti_LineEdit_35(self):
        self.page3_cti_LineEdit_35 = QtWidgets.QLineEdit()
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit_35, 2, 1)

    # Label SKU Varian 2
    def Page3_cti_Label_67(self):
        self.page3_cti_Label_67 = QtWidgets.QLabel("SKU Varian 2 : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_67, 3, 0)

    # LineEdit SKU Varian 2
    def Page3_cti_LineEdit_36(self):
        self.page3_cti_LineEdit_36 = QtWidgets.QLineEdit()
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit_36, 3, 1)

    # Label Kode_Toko
    def Page3_cti_Label_3(self):
        self.page3_cti_Label_3 = QtWidgets.QLabel("Kode Produk di Toko : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_3, 4, 0)

    # LineEdit Kode_Toko
    def Page3_cti_LineEdit_2(self):
        self.page3_cti_LineEdit_2 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_2.setReadOnly(True)
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit_2, 4, 1)

    # Label Nama_Produk
    def Page3_cti_Label_4(self):
        self.page3_cti_Label_4 = QtWidgets.QLabel("Nama Produk : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_4, 7, 0)

    # LineEdit Nama_Produk
    def Page3_cti_LineEdit_3(self):
        self.page3_cti_LineEdit_3 = QtWidgets.QLineEdit()
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit_3, 7, 1)

    # Label Barcode_Produk
    def Page3_cti_Label_5(self):
        self.page3_cti_Label_5 = QtWidgets.QLabel("Barcode Produk : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_5, 5, 0)

    # LineEdit Barcode_Produk
    def Page3_cti_LineEdit_4(self):
        self.page3_cti_LineEdit_4 = QtWidgets.QLineEdit()
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit_4, 5, 1)

    # Label Nama Produk di distributor
    def Page3_cti_Label_6(self):
        self.page3_cti_Label_6 = QtWidgets.QLabel("Nama Produk di Distributor : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_6, 6, 0)

    # LineEdit Nama Produk di Distributor
    def Page3_cti_LineEdit_5(self):
        self.page3_cti_LineEdit_5 = QtWidgets.QLineEdit()
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit_5, 6, 1)

    # Label Deskripsi_Produk
    def Page3_cti_Label_7(self):
        self.page3_cti_Label_7 = QtWidgets.QLabel("Deskripsi Produk : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_7, 8, 0)

    # TextEdit Deskripsi_Produk
    def Page3_cti_TextEdit(self):
        self.page3_cti_TextEdit = QtWidgets.QTextEdit()
        self.page3_cti_TextEdit.setPlaceholderText("Optional")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_TextEdit, 8, 1, 3, 1)

    # Label Total Stok
    def Page3_cti_Label_68(self):
        self.page3_cti_Label_68 = QtWidgets.QLabel("Total Stok : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_68, 11, 0)

    # HBoxLayout Total Stok
    def Page3_cti_HBoxLayout_19(self):
        self.page3_cti_HBoxLayout_19 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_19, 11, 1)

    # LineEdit Total Stok
    def Page3_cti_LineEdit_37(self):
        self.page3_cti_LineEdit_37 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_37.setValidator(IntegerValidator())
        self.page3_cti_HBoxLayout_19.addWidget(self.page3_cti_LineEdit_37)

    # ComboBox Total Stok Satuan
    def Page3_cti_ComboBox_4(self):
        self.page3_cti_ComboBox_4 = QtWidgets.QComboBox()
        self.page3_cti_ComboBox_4.addItem("pcs")
        self.page3_cti_HBoxLayout_19.addWidget(self.page3_cti_ComboBox_4)

    # Label Warning Stok
    def Page3_cti_Label_73(self):
        self.page3_cti_Label_73 = QtWidgets.QLabel("Set Warning Stok : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_73, 12, 0)

    # HBbox Layout Warning Stok
    def Page3_cti_HBoxLayout_23(self):
        self.page3_cti_HBoxLayout_23 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_23, 12, 1)

    # LineEdit Warning Stok
    def Page3_cti_LineEdit_40(self):
        self.page3_cti_LineEdit_39 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_39.setValidator(IntegerValidator())
        self.page3_cti_HBoxLayout_23.addWidget(self.page3_cti_LineEdit_39)

    # ComboBox Warning Stok
    def Page3_cti_ComboBox_7(self):
        self.page3_cti_ComboBox_7 = QtWidgets.QComboBox()
        self.page3_cti_ComboBox_7.addItem("pcs", 0)
        self.page3_cti_HBoxLayout_23.addWidget(self.page3_cti_ComboBox_7)



    # Label Berat/Volume di Kemasan
    def Page3_cti_Label_69(self):
        self.page3_cti_Label_69 = QtWidgets.QLabel("Berat/Volume di Kemasan : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_69, 13, 0)

    # HBoxLayout Berat/Volume di Kemasan
    def Page3_cti_HBoxLayout_20(self):
        self.page3_cti_HBoxLayout_20 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_20, 13, 1)

    # LineEdit Berat/Volume di Kemasan
    def Page3_cti_LineEdit_38(self):
        self.page3_cti_LineEdit_38 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_38.setValidator(IntegerValidator())
        self.page3_cti_HBoxLayout_20.addWidget(self.page3_cti_LineEdit_38)

    #  ComboBox Berat/Volume di Kemasan Satuan
    def Page3_cti_ComboBox_5(self):
        self.page3_cti_ComboBox_5 = QtWidgets.QComboBox()
        self.page3_cti_ComboBox_5.addItem("Kilogram")
        self.page3_cti_ComboBox_5.addItem("Gram")
        self.page3_cti_ComboBox_5.addItem("Liter")
        self.page3_cti_ComboBox_5.addItem("mL")
        self.page3_cti_HBoxLayout_20.addWidget(self.page3_cti_ComboBox_5)

    # Label Berat_Untuk_Pengiriman
    def Page3_cti_Label_8(self):
        self.page3_cti_Label_8 = QtWidgets.QLabel("Berat untuk pengiriman : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_8, 14, 0)

    # HBoxLayout Berat_Untuk_Pengiriman
    def Page3_cti_HBoxLayout(self):
        self.page3_cti_HBoxLayout = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout, 14, 1)

    # LineEdit Berat_Untuk_Pengiriman
    def Page3_cti_LineEdit_6(self):
        self.page3_cti_LineEdit_6 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_6.setReadOnly(True)
        self.page3_cti_HBoxLayout.addWidget(self.page3_cti_LineEdit_6)

    # Label Gram untuk Berat_Untuk_Pengiriman
    def Page3_cti_Label_9(self):
        self.page3_cti_Label_9 = QtWidgets.QLabel("Gram")
        self.page3_cti_HBoxLayout.addWidget(self.page3_cti_Label_9)

    # Label Kemasan
    def Page3_cti_Label_10(self):
        self.page3_cti_Label_10 = QtWidgets.QLabel("Kemasan : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_10, 15, 0)

    # ComboBox Kemasan
    def Page3_cti_ComboBox(self):
        self.page3_cti_ComboBox = QtWidgets.QComboBox()
        self.page3_cti_ComboBox.addItem("-", 0)
        self.page3_cti_ComboBox.addItem("Standing Pouch", 1)
        self.page3_cti_ComboBox.addItem("Botol", 2)
        self.page3_cti_ComboBox.addItem("Plastik", 3)
        self.page3_cti_ComboBox.addItem("Sachet", 4)
        self.page3_cti_ComboBox.addItem("Pack", 5)
        self.page3_cti_ComboBox.addItem("Kotak", 6)
        self.page3_cti_ComboBox.addItem("Kaleng", 7)
        self.page3_cti_ComboBox.addItem("Pail", 8)
        self.page3_cti_ComboBox.addItem("Plastik OPP", 9)
        self.page3_cti_ComboBox.addItem("Zak", 10)
        self.page3_cti_ComboBox.addItem("Carton", 11)
        self.page3_cti_ComboBox.addItem("Tanpa Kemasan", 12)
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_ComboBox, 15, 1)

    # Label Perizinan
    def Page3_cti_Label_11(self):
        self.page3_cti_Label_11 = QtWidgets.QLabel("Perizinan : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_11, 16, 0)

    # ComboBox Perizinan
    def Page3_cti_ComboBox_2(self):
        self.page3_cti_ComboBox_2 = QtWidgets.QComboBox()
        self.page3_cti_ComboBox_2.addItem("-", 0)
        self.page3_cti_ComboBox_2.addItem("BPOM", 1)
        self.page3_cti_ComboBox_2.addItem("PIRT", 2)
        self.page3_cti_ComboBox_2.addItem("Tanpa Izin Resmi", 3)
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_ComboBox_2, 16, 1)

    # Label Kode_BPOM_atau_PIRT
    def Page3_cti_Label_12(self):
        self.page3_cti_Label_12 = QtWidgets.QLabel("Kode BPOM atau PIRT : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_12, 17, 0)

    # LineEdit Kode_BPOM_atau_PIRT
    def Page3_cti_LineEdit_7(self):
        self.page3_cti_LineEdit_7 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_7.setDisabled(True)
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit_7, 17, 1)

    # Label Label_Halal
    def Page3_cti_Label_13(self):
        self.page3_cti_Label_13 = QtWidgets.QLabel("Label Halal : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_13, 18, 0)

    # ComboBox Label_Halal
    def Page3_cti_ComboBox_3(self):
        self.page3_cti_ComboBox_3 = QtWidgets.QComboBox()
        self.page3_cti_ComboBox_3.addItem("-", 0)
        self.page3_cti_ComboBox_3.addItem("Ada", 1)
        self.page3_cti_ComboBox_3.addItem("Tidak Ada", 2)
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_ComboBox_3, 18, 1)

    # Label Produsen
    def Page3_cti_Label_14(self):
        self.page3_cti_Label_14 = QtWidgets.QLabel("Produsen : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_14, 19, 0)

    # LineEdit Produsen
    def Page3_cti_LineEdit_8(self):
        self.page3_cti_LineEdit_8 = QtWidgets.QLineEdit()
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit_8, 19, 1)

    # Label Distributor
    def Page3_cti_Label_15(self):
        self.page3_cti_Label_15 = QtWidgets.QLabel("Distributor : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_15, 20, 0)

    # LineEdit Distributor
    def Page3_cti_LineEdit_9(self):
        self.page3_cti_LineEdit_9 = QtWidgets.QLineEdit()
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit_9, 20, 1)

    # Label Nama_Sales
    def Page3_cti_Label_16(self):
        self.page3_cti_Label_16 = QtWidgets.QLabel("Nama Sales : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_16, 21, 0)

    # LineEdit Nama_Sales
    def Page3_cti_LineEdit_10(self):
        self.page3_cti_LineEdit_10 = QtWidgets.QLineEdit()
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit_10, 21, 1)

    # Label Nomor_Telepon_Sales
    def Page3_cti_Label_17(self):
        self.page3_cti_Label_17 = QtWidgets.QLabel("No.Telp Sales : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_17, 22, 0)

    # LineEdit Nomor_Telepon_Sales
    def Page3_cti_LineEdit_11(self):
        self.page3_cti_LineEdit_11 = QtWidgets.QLineEdit()
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit_11, 22, 1)

    # Label Barang Umum atau Khusus
    def Page3_cti_Label_18(self):
        self.page3_cti_Label_18 = QtWidgets.QLabel("Barang Umum/Khusus: ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_18, 23, 0)

    # HBoxLayout Barang Umum atau Khusus
    def Page3_cti_HBoxLayout_21(self):
        self.page3_cti_HBoxLayout_21 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_21, 23, 1)

    # ComboBox Barang Umum atau Khusus
    def Page3_cti_ComboBox_6(self):
        self.page3_cti_ComboBox_6 = QtWidgets.QComboBox()
        self.page3_cti_ComboBox_6.addItem("-")
        self.page3_cti_ComboBox_6.addItem("Umum")
        self.page3_cti_ComboBox_6.addItem("Jarang")
        self.page3_cti_ComboBox_6.addItem("Sangat Jarang")
        self.page3_cti_ComboBox_6.addItem("Produk Sendiri")
        self.page3_cti_HBoxLayout_21.addWidget(self.page3_cti_ComboBox_6)

    # SpacerItem
    def Page3_cti_SpacerItem(self):
        self.page3_cti_SpacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                                          QtWidgets.QSizePolicy.Fixed)
        self.page3_cti_GridLayout_2.addItem(self.page3_cti_SpacerItem, 24, 0)

    # Label PENJUALAN
    def Page3_cti_Label_19(self):
        self.page3_cti_Label_19 = QtWidgets.QLabel("PENJUALAN")
        self.page3_cti_Label_19.setFont(Font(8, True))
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_19, 25, 0)

    # Label Harga_Beli_Terakhir_Per_Satuan_Terkecil
    def Page3_cti_Label_20(self):
        self.page3_cti_Label_20 = QtWidgets.QLabel("Harga Beli Terakhir : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_20, 26, 0)

    # LineEdit Harga_Beli_Terakhir_Per_Satuan_Terkecil
    def Page3_cti_LineEdit_13(self):
        self.page3_cti_LineEdit_13 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_13.setValidator(IntegerValidator())
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit_13, 26, 1)

    # Label Biaya Penanganan
    def Page3_cti_Label_70(self):
        self.page3_cti_Label_70 = QtWidgets.QLabel("Biaya Penanganan : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_70, 27, 0)

    # HBoxLayout Biaya Penanganan
    def Page3_cti_HBoxLayout_22(self):
        self.page3_cti_HBoxLayout_22 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_22, 27, 1)

    # Label "Rp. " Biaya Penanganan
    def Page3_cti_Label_71(self):
        self.page3_cti_Label_71 = QtWidgets.QLabel("Rp. ")
        self.page3_cti_HBoxLayout_22.addWidget(self.page3_cti_Label_71)

    # LineEdit Biaya Penanganan
    def Page3_cti_LineEdit_12(self):
        self.page3_cti_LineEdit_12 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_12.setValidator(IntegerValidator())
        self.page3_cti_HBoxLayout_22.addWidget(self.page3_cti_LineEdit_12)

    # Label ",-" Biaya Penanganan
    def Page3_cti_Label_72(self):
        self.page3_cti_Label_72 = QtWidgets.QLabel(",-")
        self.page3_cti_HBoxLayout_22.addWidget(self.page3_cti_Label_72)

    # Label Laba_Dasar (dalam persen dan rupiah)
    def Page3_cti_Label_21(self):
        self.page3_cti_Label_21 = QtWidgets.QLabel("Laba Dasar : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_21, 28, 0)

    # HBoxLayout Laba_Dasar (dalam persen dan rupiah)
    def Page3_cti_HBoxLayout_2(self):
        self.page3_cti_HBoxLayout_2 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_2, 28, 1)

    # LineEdit % Laba_Dasar (dalam persen dan rupiah)
    def Page3_cti_LineEdit_14(self):
        self.page3_cti_LineEdit_14 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_14.setValidator(FloatValidator())
        self.page3_cti_HBoxLayout_2.addWidget(self.page3_cti_LineEdit_14)

    # Label % Laba_Dasar (dalam persen dan rupiah)
    def Page3_cti_Label_22(self):
        self.page3_cti_Label_22 = QtWidgets.QLabel("%")
        self.page3_cti_HBoxLayout_2.addWidget(self.page3_cti_Label_22)

    # Label "-->" Laba_Dasar (dalam persen dan rupiah)
    def Page3_cti_Label_23(self):
        self.page3_cti_Label_23 = QtWidgets.QLabel("    -->   ")
        self.page3_cti_HBoxLayout_2.addWidget(self.page3_cti_Label_23)

    # LineEdit rupiah Laba_Dasar (dalam persen dan rupiah)
    def Page3_cti_LineEdit_15(self):
        self.page3_cti_LineEdit_15 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_15.setValidator(FloatValidator())
        self.page3_cti_HBoxLayout_2.addWidget(self.page3_cti_LineEdit_15)

    # Label " rupiah" Laba_Dasar (dalam persen dan rupiah)
    def Page3_cti_Label_24(self):
        self.page3_cti_Label_24 = QtWidgets.QLabel(" Rp. ")
        self.page3_cti_HBoxLayout_2.addWidget(self.page3_cti_Label_24)

    # Label Harga_Jual_Dasar
    def Page3_cti_Label_25(self):
        self.page3_cti_Label_25 = QtWidgets.QLabel("Harga Jual Dasar : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_25, 29, 0)

    # HBoxLayout Harga_Jual_Dasar
    def Page3_cti_HBoxLayout_3(self):
        self.page3_cti_HBoxLayout_3 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_3, 29, 1)

    # Label Rupiah Harga_Jual_Dasar
    def Page3_cti_Label_26(self):
        self.page3_cti_Label_26 = QtWidgets.QLabel("Rp. ")
        self.page3_cti_HBoxLayout_3.addWidget(self.page3_cti_Label_26)

    # LineEdit Harga_Jual_Dasar
    def Page3_cti_LineEdit_16(self):
        self.page3_cti_LineEdit_16 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_16.setValidator(IntegerValidator())
        self.page3_cti_LineEdit_16.setReadOnly(True)
        self.page3_cti_HBoxLayout_3.addWidget(self.page3_cti_LineEdit_16)

    # Label Laba_Saat_Diskon
    def Page3_cti_Label_27(self):
        self.page3_cti_Label_27 = QtWidgets.QLabel("Laba Saat Diskon : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_27, 30, 0)

    # HBoxLayout Laba_Saat_Diskon
    def Page3_cti_HBoxLayout_4(self):
        self.page3_cti_HBoxLayout_4 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_4, 30, 1)

    # LineEdit Laba_Saat_Diskon (Persen)
    def Page3_cti_LineEdit_17(self):
        self.page3_cti_LineEdit_17 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_17.setValidator(FloatValidator())
        self.page3_cti_HBoxLayout_4.addWidget(self.page3_cti_LineEdit_17)

    # Label % Laba_Saat_Diskon
    def Page3_cti_Label_28(self):
        self.page3_cti_Label_28 = QtWidgets.QLabel("%")
        self.page3_cti_HBoxLayout_4.addWidget(self.page3_cti_Label_28)

    # Label --> Laba_Saat_Diskon
    def Page3_cti_Label_29(self):
        self.page3_cti_Label_29 = QtWidgets.QLabel("    -->    ")
        self.page3_cti_HBoxLayout_4.addWidget(self.page3_cti_Label_29)

    # Label Rupiah Laba_Saat_Diskon
    def Page3_cti_Label_30(self):
        self.page3_cti_Label_30 = QtWidgets.QLabel("Rp. ")
        self.page3_cti_HBoxLayout_4.addWidget(self.page3_cti_Label_30)

    # LineEdit Laba_Saat_Diskon (Rupiah)
    def Page3_cti_LineEdit_18(self):
        self.page3_cti_LineEdit_18 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_18.setValidator(FloatValidator())
        self.page3_cti_HBoxLayout_4.addWidget(self.page3_cti_LineEdit_18)

    # Label Harga_Jual_Saat_Diskon
    def Page3_cti_Label_31(self):
        self.page3_cti_Label_31 = QtWidgets.QLabel("Harga Jual Saat Diskon : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_31, 31, 0)

    # HBoxLayout Harga_Jual_Saat_Diskon
    def Page3_cti_HBoxLayout_5(self):
        self.page3_cti_HBoxLayout_5 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_5, 31, 1)

    # Label Rupiah Harga_Jual_Saat_Diskon
    def Page3_cti_Label_32(self):
        self.page3_cti_Label_32 = QtWidgets.QLabel("Rp. ")
        self.page3_cti_HBoxLayout_5.addWidget(self.page3_cti_Label_32)

    # LineEdit Rupiah Harga_Jual_Saat_Diskon
    def Page3_cti_LineEdit_19(self):
        self.page3_cti_LineEdit_19 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_19.setValidator(IntegerValidator())
        self.page3_cti_LineEdit_19.setReadOnly(True)
        self.page3_cti_HBoxLayout_5.addWidget(self.page3_cti_LineEdit_19)

    # Label Grosir_1
    def Page3_cti_Label_33(self):
        self.page3_cti_Label_33 = QtWidgets.QLabel("Grosir 1")
        self.page3_cti_Label_33.setFont(Font(8, True))
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_33, 32, 0)

    # Label Minimal_Pembelian_Grosir_1
    def Page3_cti_Label_34(self):
        self.page3_cti_Label_34 = QtWidgets.QLabel("Minimal Pembelian Grosir 1 : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_34, 33, 0)

    # HBoxLayout Minimal_Pembelian_Grosir_1
    def Page3_cti_HBoxLayout_6(self):
        self.page3_cti_HBoxLayout_6 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_6, 33, 1)

    # LineEdit Minimal_Pembelian_Grosir_1
    def Page3_cti_LineEdit_20(self):
        self.page3_cti_LineEdit_20 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_20.setValidator(IntegerValidator())
        self.page3_cti_HBoxLayout_6.addWidget(self.page3_cti_LineEdit_20)

    # Label Satuan Minimal_Pembelian_Grosir_1
    def Page3_cti_Label_35(self):
        self.page3_cti_Label_35 = QtWidgets.QLabel("Pcs")
        self.page3_cti_HBoxLayout_6.addWidget(self.page3_cti_Label_35)

    # Label Laba_Saat_Grosir_1
    def Page3_cti_Label_36(self):
        self.page3_cti_Label_36 = QtWidgets.QLabel("Laba Saat Grosir 1 : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_36, 34, 0)

    # HBoxLayout Laba_Saat_Grosir_1
    def Page3_cti_HBoxLayout_7(self):
        self.page3_cti_HBoxLayout_7 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_7, 34, 1)

    # LineEdit % Laba_Saat_Grosir_1
    def Page3_cti_LineEdit_21(self):
        self.page3_cti_LineEdit_21 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_21.setValidator(FloatValidator())
        self.page3_cti_HBoxLayout_7.addWidget(self.page3_cti_LineEdit_21)

    # Label % Laba_Saat_Grosir_1
    def Page3_cti_Label_37(self):
        self.page3_cti_Label_37 = QtWidgets.QLabel("%")
        self.page3_cti_HBoxLayout_7.addWidget(self.page3_cti_Label_37)

    # Label --> Laba_Saat_Grosir_1
    def Page3_cti_Label_38(self):
        self.page3_cti_Label_38 = QtWidgets.QLabel("    -->    ")
        self.page3_cti_HBoxLayout_7.addWidget(self.page3_cti_Label_38)

    # Label Rupiah Laba_Saat_Grosir_1
    def Page3_cti_Label_39(self):
        self.page3_cti_Label_39 = QtWidgets.QLabel("Rp. ")
        self.page3_cti_HBoxLayout_7.addWidget(self.page3_cti_Label_39)

    # LineEdit Rupiah Laba_Saat_Grosir_1
    def Page3_cti_LineEdit_22(self):
        self.page3_cti_LineEdit_22 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_22.setValidator(FloatValidator())
        self.page3_cti_HBoxLayout_7.addWidget(self.page3_cti_LineEdit_22)

    # Label Harga_Jual_Saat_Grosir_1
    def Page3_cti_Label_40(self):
        self.page3_cti_Label_40 = QtWidgets.QLabel("Harga Jual Saat Grosir 1 : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_40, 35, 0)

    # HBoxLayout Harga_Jual_Saat_Grosir_1
    def Page3_cti_HBoxLayout_8(self):
        self.page3_cti_HBoxLayout_8 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_8, 35, 1)

    # Label Rupiah Harga_Jual_Saat_Grosir_1
    def Page3_cti_Label_41(self):
        self.page3_cti_Label_41 = QtWidgets.QLabel("Rp. ")
        self.page3_cti_HBoxLayout_8.addWidget(self.page3_cti_Label_41)

    # LineEdit Rupiah Harga_Jual_Saat_Grosir_1
    def Page3_cti_LineEdit_23(self):
        self.page3_cti_LineEdit_23 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_23.setValidator(IntegerValidator())
        self.page3_cti_LineEdit_23.setReadOnly(True)
        self.page3_cti_HBoxLayout_8.addWidget(self.page3_cti_LineEdit_23)

    # Label Grosir_2
    def Page3_cti_Label_42(self):
        self.page3_cti_Label_42 = QtWidgets.QLabel("Grosir 2")
        self.page3_cti_Label_42.setFont(Font(8, True))
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_42, 36, 0)

    # Label Minimal_Pembelian_Grosir_2
    def Page3_cti_Label_43(self):
        self.page3_cti_Label_43 = QtWidgets.QLabel("Minimal Pembelian Grosir 2 : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_43, 37, 0)

    # HBoxLayout Minimal_Pembelian_Grosir_2
    def Page3_cti_HBoxLayout_9(self):
        self.page3_cti_HBoxLayout_9 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_9, 37, 1)

    # LineEdit Minimal_Pembelian_Grosir_2
    def Page3_cti_LineEdit_24(self):
        self.page3_cti_LineEdit_24 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_24.setValidator(IntegerValidator())
        self.page3_cti_HBoxLayout_9.addWidget(self.page3_cti_LineEdit_24)

    # Label Satuan Minimal_Pembelian_Grosir_2
    def Page3_cti_Label_44(self):
        self.page3_cti_Label_44 = QtWidgets.QLabel("Pcs")
        self.page3_cti_HBoxLayout_9.addWidget(self.page3_cti_Label_44)

    # Label Laba_Saat_Grosir_2
    def Page3_cti_Label_45(self):
        self.page3_cti_Label_45 = QtWidgets.QLabel("Laba Saat Grosir 2 : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_45, 38, 0)

    # HBoxLayout Laba_Saat_Grosir_2
    def Page3_cti_HBoxLayout_10(self):
        self.page3_cti_HBoxLayout_10 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_10, 38, 1)

    # LineEdit % Laba_Saat_Grosir_2
    def Page3_cti_LineEdit_25(self):
        self.page3_cti_LineEdit_25 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_25.setValidator(FloatValidator())
        self.page3_cti_HBoxLayout_10.addWidget(self.page3_cti_LineEdit_25)

    # Label % Laba_Saat_Grosir_2
    def Page3_cti_Label_46(self):
        self.page3_cti_Label_46 = QtWidgets.QLabel("%")
        self.page3_cti_HBoxLayout_10.addWidget(self.page3_cti_Label_46)

    # Label --> Laba_Saat_Grosir_2
    def Page3_cti_Label_47(self):
        self.page3_cti_Label_47 = QtWidgets.QLabel("    -->    ")
        self.page3_cti_HBoxLayout_10.addWidget(self.page3_cti_Label_47)

    # Label Rupiah Laba_Saat_Grosir_2
    def Page3_cti_Label_48(self):
        self.page3_cti_Label_48 = QtWidgets.QLabel("Rp. ")
        self.page3_cti_HBoxLayout_10.addWidget(self.page3_cti_Label_48)

    # LineEdit Rupiah Laba_Saat_Grosir_2
    def Page3_cti_LineEdit_26(self):
        self.page3_cti_LineEdit_26 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_26.setValidator(FloatValidator())
        self.page3_cti_HBoxLayout_10.addWidget(self.page3_cti_LineEdit_26)

    # Label Harga_Jual_Saat_Grosir_2
    def Page3_cti_Label_49(self):
        self.page3_cti_Label_49 = QtWidgets.QLabel("Harga Jual Saat Grosir 2 : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_49, 39, 0)

    # HBoxLayout Harga_Jual_Saat_Grosir_2
    def Page3_cti_HBoxLayout_11(self):
        self.page3_cti_HBoxLayout_11 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_11, 39, 1)

    # Label Rupiah Harga_Jual_Saat_Grosir_2
    def Page3_cti_Label_50(self):
        self.page3_cti_Label_50 = QtWidgets.QLabel("Rp. ")
        self.page3_cti_HBoxLayout_11.addWidget(self.page3_cti_Label_50)

    # LineEdit Harga_Jual_Saat_Grosir_2
    def Page3_cti_LineEdit_27(self):
        self.page3_cti_LineEdit_27 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_27.setValidator(IntegerValidator())
        self.page3_cti_LineEdit_27.setReadOnly(True)
        self.page3_cti_HBoxLayout_11.addWidget(self.page3_cti_LineEdit_27)

    # Label Grosir_3
    def Page3_cti_Label_51(self):
        self.page3_cti_Label_51 = QtWidgets.QLabel("Grosir 3")
        self.page3_cti_Label_51.setFont(Font(8, True))
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_51, 40, 0)

    # Label Minimal_Pembelian_Saat_Grosir_3
    def Page3_cti_Label_52(self):
        self.page3_cti_Label_52 = QtWidgets.QLabel("Minimal Pembelian Grosir 3 : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_52, 41, 0)

    # HBoxLayout Minimal_Pembelian_Saat_Grosir_3
    def Page3_cti_HBoxLayout_12(self):
        self.page3_cti_HBoxLayout_12 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_12, 41, 1)

    # LineEdit Minimal_Pembelian_Saat_Grosir_3
    def Page3_cti_LineEdit_28(self):
        self.page3_cti_LineEdit_28 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_28.setValidator(IntegerValidator())
        self.page3_cti_HBoxLayout_12.addWidget(self.page3_cti_LineEdit_28)

    # Label Pcs Minimal_Pembelian_Saat_Grosir_3
    def Page3_cti_Label_53(self):
        self.page3_cti_Label_53 = QtWidgets.QLabel("Pcs")
        self.page3_cti_HBoxLayout_12.addWidget(self.page3_cti_Label_53)

    # Label Laba_Saat_Grosir_3
    def Page3_cti_Label_54(self):
        self.page3_cti_Label_54 = QtWidgets.QLabel("Laba Saat Grosir 3 : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_54, 42, 0)

    # HBoxLayout Laba_Saat_Grosir_3
    def Page3_cti_HBoxLayout_13(self):
        self.page3_cti_HBoxLayout_13 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_13, 42, 1)

    # LineEdit % Laba_Saat_Grosir_3
    def Page3_cti_LineEdit_29(self):
        self.page3_cti_LineEdit_29 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_29.setValidator(FloatValidator())
        self.page3_cti_HBoxLayout_13.addWidget(self.page3_cti_LineEdit_29)

    # Label% Laba_Saat_Grosir_3
    def Page3_cti_Label_55(self):
        self.page3_cti_Label_55 = QtWidgets.QLabel("%")
        self.page3_cti_HBoxLayout_13.addWidget(self.page3_cti_Label_55)

    # Label --> Laba_Saat_Grosir_3
    def Page3_cti_Label_56(self):
        self.page3_cti_Label_56 = QtWidgets.QLabel("    -->    ")
        self.page3_cti_HBoxLayout_13.addWidget(self.page3_cti_Label_56)

    # Label Rupiah Laba_Saat_Grosir_3
    def Page3_cti_Label_57(self):
        self.page3_cti_Label_57 = QtWidgets.QLabel("Rp. ")
        self.page3_cti_HBoxLayout_13.addWidget(self.page3_cti_Label_57)

    # LineEdit Rupiah Laba_Saat_Grosir_3
    def Page3_cti_LineEdit_30(self):
        self.page3_cti_LineEdit_30 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_30.setValidator(FloatValidator())
        self.page3_cti_HBoxLayout_13.addWidget(self.page3_cti_LineEdit_30)

    # Label Harga_Jual_Saat_Grosir_3
    def Page3_cti_Label_58(self):
        self.page3_cti_Label_58 = QtWidgets.QLabel("Harga Jual Saat Grosir 3 : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_58, 43, 0)

    # HBoxLayout Harga_Jual_Saat_Grosir_3
    def Page3_cti_HBoxLayout_14(self):
        self.page3_cti_HBoxLayout_14 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_14, 43, 1)

    # Label Rupiah Harga_Jual_Saat_Grosir_3
    def Page3_cti_Label_59(self):
        self.page3_cti_Label_59 = QtWidgets.QLabel("Rp. ")
        self.page3_cti_HBoxLayout_14.addWidget(self.page3_cti_Label_59)

    # LineEdit Harga_Jual_Saat_Grosir_3
    def Page3_cti_LineEdit_31(self):
        self.page3_cti_LineEdit_31 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_31.setValidator(IntegerValidator())
        self.page3_cti_LineEdit_31.setReadOnly(True)
        self.page3_cti_HBoxLayout_14.addWidget(self.page3_cti_LineEdit_31)

    # SpacerItem INFORMASI TAMBAHAN
    def Page3_cti_SpacerItem_2(self):
        self.page3_cti_SpacerItem_2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                                            QtWidgets.QSizePolicy.Fixed)
        self.page3_cti_GridLayout_2.addItem(self.page3_cti_SpacerItem_2, 44, 0)

    # Label INFORMASI TAMBAHAN
    def Page3_cti_Label_60(self):
        self.page3_cti_Label_60 = QtWidgets.QLabel("INFORMASI TAMBAHAN")
        self.page3_cti_Label_60.setFont(Font(8, True))
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_60, 45, 0)

    # Label Catatan
    def Page3_cti_Label_61(self):
        self.page3_cti_Label_61 = QtWidgets.QLabel("Catatan : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_61, 46, 0)

    # TextEdit Catatan
    def Page3_cti_TextEdit_2(self):
        self.page3_cti_TextEdit_2 = QtWidgets.QTextEdit()
        self.page3_cti_TextEdit_2.setPlaceholderText("Optional")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_TextEdit_2, 46, 1, 3, 1)

    # Label Foto_Produk
    def Page3_cti_Label_63(self):
        self.page3_cti_Label_63 = QtWidgets.QLabel("Foto Produk : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_63, 49, 0)

    # HBoxLayout Foto_Produk
    def Page3_cti_HBoxLayout_16(self):
        self.page3_cti_HBoxLayout_16 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_16, 49, 1)

    # LineEdit Foto_Produk
    def Page3_cti_LineEdit_33(self):
        self.page3_cti_LineEdit_33 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_33.setPlaceholderText("Optional")
        self.page3_cti_HBoxLayout_16.addWidget(self.page3_cti_LineEdit_33)

    # PushButton Tambah Foto_Produk
    def Page3_cti_PushButton_3(self):
        self.page3_cti_PushButton_3 = QtWidgets.QPushButton("Tambah")
        self.page3_cti_HBoxLayout_16.addWidget(self.page3_cti_PushButton_3)

    # PushButton Hapus Foto_Produk
    def Page3_cti_PushButton_9(self):
        self.page3_cti_PushButton_9 = QtWidgets.QPushButton("Hapus")
        self.page3_cti_HBoxLayout_16.addWidget(self.page3_cti_PushButton_9)

    # Label Gambar Foto_Produk
    def Page3_cti_Label_64(self):
        self.page3_cti_Label_64 = QtWidgets.QLabel("Tidak Ada Foto Produk")
        # self.page3_cti_Label_64.setFixedWidth(300)
        self.page3_cti_Label_64.setFixedHeight(250)
        self.page3_cti_Label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.page3_cti_Label_64.setFrameStyle(6)
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_64, 50, 1)

    # HBoxLayout Gambar Foto_Produk
    def Page3_cti_HBoxLayout_17(self):
        self.page3_cti_HBoxLayout_17 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_17, 51, 1)

    # PushButton Gambar1 Foto_Produk
    def Page3_cti_PushButton_4(self):
        self.page3_cti_PushButton_4 = QtWidgets.QPushButton("1")
        self.page3_cti_PushButton_4.setMinimumWidth(50)
        self.page3_cti_HBoxLayout_17.addWidget(self.page3_cti_PushButton_4)

    # PushButton Gambar2 Foto_Produk
    def Page3_cti_PushButton_5(self):
        self.page3_cti_PushButton_5 = QtWidgets.QPushButton("2")
        self.page3_cti_PushButton_5.setMinimumWidth(50)
        self.page3_cti_HBoxLayout_17.addWidget(self.page3_cti_PushButton_5)

    # PushButton Gambar3 Foto_Produk
    def Page3_cti_PushButton_6(self):
        self.page3_cti_PushButton_6 = QtWidgets.QPushButton("3")
        self.page3_cti_PushButton_6.setMinimumWidth(50)
        self.page3_cti_HBoxLayout_17.addWidget(self.page3_cti_PushButton_6)

    # PushButton Gambar4 Foto_Produk
    def Page3_cti_PushButton_7(self):
        self.page3_cti_PushButton_7 = QtWidgets.QPushButton("4")
        self.page3_cti_PushButton_7.setMinimumWidth(50)
        self.page3_cti_HBoxLayout_17.addWidget(self.page3_cti_PushButton_7)

    # PushButton Gambar5 Foto_Produk
    def Page3_cti_PushButton_8(self):
        self.page3_cti_PushButton_8 = QtWidgets.QPushButton("5")
        self.page3_cti_PushButton_8.setMinimumWidth(50)
        self.page3_cti_HBoxLayout_17.addWidget(self.page3_cti_PushButton_8)

    # HBoxLayout Gambar5 Foto_Produk Baris Kedua
    def Page3_cti_HBoxLayout_18(self):
        self.page3_cti_HBoxLayout_18 = QtWidgets.QHBoxLayout()
        self.page3_cti_GridLayout_2.addLayout(self.page3_cti_HBoxLayout_18, 52, 1)

    # PushButton Gambar6 Foto_Produk
    def Page3_cti_PushButton_10(self):
        self.page3_cti_PushButton_10 = QtWidgets.QPushButton("6")
        self.page3_cti_PushButton_10.setMinimumWidth(50)
        self.page3_cti_HBoxLayout_18.addWidget(self.page3_cti_PushButton_10)

    # PushButton Gambar7 Foto_Produk
    def Page3_cti_PushButton_11(self):
        self.page3_cti_PushButton_11 = QtWidgets.QPushButton("7")
        self.page3_cti_PushButton_11.setMinimumWidth(50)
        self.page3_cti_HBoxLayout_18.addWidget(self.page3_cti_PushButton_11)

    # PushButton Gambar8 Foto_Produk
    def Page3_cti_PushButton_12(self):
        self.page3_cti_PushButton_12 = QtWidgets.QPushButton("8")
        self.page3_cti_PushButton_12.setMinimumWidth(50)
        self.page3_cti_HBoxLayout_18.addWidget(self.page3_cti_PushButton_12)

    # PushButton Gambar9 Foto_Produk
    def Page3_cti_PushButton_13(self):
        self.page3_cti_PushButton_13 = QtWidgets.QPushButton("9")
        self.page3_cti_PushButton_13.setMinimumWidth(50)
        self.page3_cti_HBoxLayout_18.addWidget(self.page3_cti_PushButton_13)

    # PushButton GambarVid Foto_Produk
    def Page3_cti_PushButton_14(self):
        self.page3_cti_PushButton_14 = QtWidgets.QPushButton("Video")
        self.page3_cti_PushButton_14.setMinimumWidth(50)
        self.page3_cti_HBoxLayout_18.addWidget(self.page3_cti_PushButton_14)

    # Label Posisi_Barang
    def Page3_cti_Label_62(self):
        self.page3_cti_Label_62 = QtWidgets.QLabel("Posisi Barang : ")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_Label_62, 53, 0)

    # LineEdit Posisi_Barang
    def Page3_cti_LineEdit_32(self):
        self.page3_cti_LineEdit_32 = QtWidgets.QLineEdit()
        self.page3_cti_LineEdit_32.setPlaceholderText("Optional")
        self.page3_cti_GridLayout_2.addWidget(self.page3_cti_LineEdit_32, 53, 1)

    # HBoxLayout untuk PushButton Batalkan dan Simpan
    def Page3_cti_HBoxLayout_15(self):
        self.page3_cti_HBoxLayout_15 = QtWidgets.QHBoxLayout()
        self.page3_cti_layout.addLayout(self.page3_cti_HBoxLayout_15)

    # Spacer di HBoxLayout (agar tombol rata kanan)
    def Page3_cti_Spacer_3(self):
        self.page3_cti_Spacer_3 = QtWidgets.QSpacerItem(20, 20,
                                                        QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Fixed)
        self.page3_cti_HBoxLayout_15.addItem(self.page3_cti_Spacer_3)

    # PushButton Batalkan
    def Page3_cti_PushButton(self):
        self.page3_cti_PushButton = QtWidgets.QPushButton("Batal")
        self.page3_cti_PushButton.setObjectName('page3_cti_PushButton')
        self.page3_cti_HBoxLayout_15.addWidget(self.page3_cti_PushButton)

    # PushButton Simpan
    def Page3_cti_PushButton_2(self):
        self.page3_cti_PushButton_2 = QtWidgets.QPushButton("Simpan")
        self.page3_cti_PushButton_2.setObjectName('page3_cti_PushButton_2')
        self.page3_cti_PushButton_2.setDefault(True)
        self.page3_cti_HBoxLayout_15.addWidget(self.page3_cti_PushButton_2)

    # PushButton Cetak Label Harga
    def Page3_cti_PushButton_15(self):
        self.page3_cti_PushButton_15 = QtWidgets.QPushButton("Cetak Harga")
        self.page3_cti_HBoxLayout_15.addWidget(self.page3_cti_PushButton_15)

    # LineEdit Terpakai :       Page3_cti_LineEdit_39
    # Label Terpakai :          Page3_cti_Label_73
    # HBoxLayout Terpakai :     Page3_cti_HBoxLayout_23
    # TextEdit Terpakai :       Page3_cti_TextEdit_2
    # SpacerItem Terpakai :     Page3_cti_SpacerItem_3
    # PushButton Terpakai :     Page3_cti_PushButton_10
    # ComboBox Terpakai :       Page3_cti_ComboBox_7

    # INISIALISASI
    # Aktifkan untuk mode editing script
    def Page3_cti_Mode_Editing(self):
        self.page3_cti_LineEdit.setPlaceholderText("page3_cti_LineEdit")
        self.page3_cti_LineEdit_34.setPlaceholderText("page3_cti_LineEdit_34")
        self.page3_cti_LineEdit_35.setPlaceholderText("page3_cti_LineEdit_35")
        self.page3_cti_LineEdit_36.setPlaceholderText("page3_cti_LineEdit_36")
        self.page3_cti_LineEdit_2.setPlaceholderText("page3_cti_LineEdit_2")
        self.page3_cti_LineEdit_3.setPlaceholderText("page3_cti_LineEdit_3")
        self.page3_cti_LineEdit_4.setPlaceholderText("page3_cti_LineEdit_4")
        self.page3_cti_LineEdit_5.setPlaceholderText("page3_cti_LineEdit_5")
        self.page3_cti_TextEdit.setPlaceholderText("page3_cti_TextEdit")
        self.page3_cti_LineEdit_37.setPlaceholderText("page3_cti_LineEdit_37")
        self.page3_cti_LineEdit_38.setPlaceholderText("page3_cti_LineEdit_38")
        self.page3_cti_LineEdit_6.setPlaceholderText("page3_cti_LineEdit_6")
        self.page3_cti_LineEdit_7.setPlaceholderText("page3_cti_LineEdit_7")
        self.page3_cti_LineEdit_8.setPlaceholderText("page3_cti_LineEdit_8")
        self.page3_cti_LineEdit_9.setPlaceholderText("page3_cti_LineEdit_9")
        self.page3_cti_LineEdit_10.setPlaceholderText("page3_cti_LineEdit_10")
        self.page3_cti_LineEdit_11.setPlaceholderText("page3_cti_LineEdit_11")
        self.page3_cti_LineEdit_13.setPlaceholderText("page3_cti_LineEdit_13")
        self.page3_cti_LineEdit_12.setPlaceholderText("page3_cti_LineEdit_12")
        self.page3_cti_LineEdit_14.setPlaceholderText("page3_cti_LineEdit_14")
        self.page3_cti_LineEdit_15.setPlaceholderText("page3_cti_LineEdit_15")
        self.page3_cti_LineEdit_16.setPlaceholderText("page3_cti_LineEdit_16")
        self.page3_cti_LineEdit_17.setPlaceholderText("page3_cti_LineEdit_17")
        self.page3_cti_LineEdit_18.setPlaceholderText("page3_cti_LineEdit_18")
        self.page3_cti_LineEdit_19.setPlaceholderText("page3_cti_LineEdit_19")
        self.page3_cti_LineEdit_20.setPlaceholderText("page3_cti_LineEdit_20")
        self.page3_cti_LineEdit_21.setPlaceholderText("page3_cti_LineEdit_21")
        self.page3_cti_LineEdit_22.setPlaceholderText("page3_cti_LineEdit_22")
        self.page3_cti_LineEdit_23.setPlaceholderText("page3_cti_LineEdit_23")
        self.page3_cti_LineEdit_24.setPlaceholderText("page3_cti_LineEdit_24")
        self.page3_cti_LineEdit_25.setPlaceholderText("page3_cti_LineEdit_25")
        self.page3_cti_LineEdit_26.setPlaceholderText("page3_cti_LineEdit_26")
        self.page3_cti_LineEdit_27.setPlaceholderText("page3_cti_LineEdit_27")
        self.page3_cti_LineEdit_28.setPlaceholderText("page3_cti_LineEdit_28")
        self.page3_cti_LineEdit_29.setPlaceholderText("page3_cti_LineEdit_29")
        self.page3_cti_LineEdit_30.setPlaceholderText("page3_cti_LineEdit_30")
        self.page3_cti_LineEdit_31.setPlaceholderText("page3_cti_LineEdit_31")
        self.page3_cti_TextEdit_2.setPlaceholderText("page3_cti_TextEdit_2")
        self.page3_cti_LineEdit_33.setPlaceholderText("page3_cti_LineEdit_33")
        self.page3_cti_LineEdit_32.setPlaceholderText("page3_cti_LineEdit_32")
        self.page3_cti_LineEdit_39.setPlaceholderText("page3_cti_LineEdit_39")
        pass

    # Definisikan data yang akan diambil
    def Page3_cti_Definisikan_Data(self):
        self.page3_cti_No = ""
        self.page3_cti_No_terpakai = []
        self.page3_cti_SKU_Induk = ""
        self.page3_cti_SKU_Induk_terpakai = []
        self.page3_cti_SKU_Varian_1 = ""
        self.page3_cti_SKU_Varian_1_terpakai = []
        self.page3_cti_SKU_Varian_2 = ""
        self.page3_cti_SKU_Varian_2_terpakai = []
        self.page3_cti_Kode_Toko = ""
        self.page3_cti_Barcode_Produk = ""
        self.page3_cti_Nama_Produk_Di_Distributor = ""
        self.page3_cti_Nama_Produk_Di_Distributor_terpakai = []
        self.page3_cti_Nama_Produk_Di_Toko = ""
        self.page3_cti_Repack = ""
        self.page3_cti_Produk_umum_khusus = ""
        self.page3_cti_Deskripsi_Produk = ""
        self.page3_cti_Total_Stok = ""
        self.page3_cti_Total_Stok_Satuan = ""
        self.page3_cti_Warning_Stok = ""
        self.page3_cti_Berat_atau_Volume_Bersih = ""
        self.page3_cti_Satuan_Berat_Bersih = ""
        self.page3_cti_Berat_Untuk_Pengiriman_Dalam_Gram = ""
        self.page3_cti_Kemasan = ""
        self.page3_cti_Perizinan = ""
        self.page3_cti_Kode_BPOM_atau_PIRT = ""
        self.page3_cti_Label_Halal = ""
        self.page3_cti_Produsen = ""
        self.page3_cti_Produsen_terpakai = []
        self.page3_cti_Distributor = ""
        self.page3_cti_Distributor_terpakai = []
        self.page3_cti_Nama_Sales = ""
        self.page3_cti_Nama_Sales_terpakai = []
        self.page3_cti_No_Telepon_Sales = ""
        self.page3_cti_No_Telepon_Sales_terpakai = []
        self.page3_cti_Harga_Beli_Terakhir = ""
        self.page3_cti_Biaya_Penanganan = ""
        self.page3_cti_Laba_Dasar_Dalam_Persen = ""
        self.page3_cti_Laba_Dasar_Dalam_Rupiah = ""
        self.page3_cti_Harga_Jual_Dasar = ""
        self.page3_cti_Laba_Saat_Diskon_Dalam_Persen = ""
        self.page3_cti_Laba_Saat_Diskon_Dalam_Rupiah = ""
        self.page3_cti_Harga_Jual_Saat_Diskon = ""
        self.page3_cti_Minimal_Pembelian_Grosir_1 = ""
        self.page3_cti_Laba_Saat_Grosir_1_Dalam_Persen = ""
        self.page3_cti_Laba_Saat_Grosir_1_Dalam_Rupiah = ""
        self.page3_cti_Harga_Jual_Saat_Grosir_1 = ""
        self.page3_cti_Minimal_Pembelian_Grosir_2 = ""
        self.page3_cti_Laba_Saat_Grosir_2_Dalam_Persen = ""
        self.page3_cti_Laba_Saat_Grosir_2_Dalam_Rupiah = ""
        self.page3_cti_Harga_Jual_Saat_Grosir_2 = ""
        self.page3_cti_Minimal_Pembelian_Grosir_3 = ""
        self.page3_cti_Laba_Saat_Grosir_3_Dalam_Persen = ""
        self.page3_cti_Laba_Saat_Grosir_3_Dalam_Rupiah = ""
        self.page3_cti_Harga_Jual_Saat_Grosir_3 = ""
        self.page3_cti_Catatan = ""
        self.page3_cti_Foto_Produk1 = ""
        self.page3_cti_Foto_Produk_2 = ""
        self.page3_cti_Foto_Produk_3 = ""
        self.page3_cti_Foto_Produk_4 = ""
        self.page3_cti_Foto_Produk_5 = ""
        self.page3_cti_Foto_Produk_6 = ""
        self.page3_cti_Foto_Produk_7 = ""
        self.page3_cti_Foto_Produk_8 = ""
        self.page3_cti_Foto_Produk_9 = ""
        self.page3_cti_Foto_Video = ""
        self.page3_cti_Posisi_Barang = ""

    # Database_Load
    def Page3_cti_Database_Load(self):
        database = DatabaseProduk()
        self.page3_cti_DBProduk_connection = sqlite3.connect(database)
        self.page3_cti_DBProduk_connection.row_factory = sqlite3.Row
        self.page3_cti_DBProduk_cursor = self.page3_cti_DBProduk_connection.cursor()

    # Definisikan Nomor Urut
    def Page3_cti_Nomor_Urut(self):
        # Definisikan nomor urut di database yang belum terpakai
        Load_No_terpakai = self.page3_cti_DBProduk_cursor.execute("select No from Data_Produk_Master").fetchall()
        for item in range(len(Load_No_terpakai)):
            self.page3_cti_No_terpakai.append(int(Load_No_terpakai[item]["No"]))
        No_belum_terpakai = 1
        while No_belum_terpakai in self.page3_cti_No_terpakai:
            No_belum_terpakai += 1
        else:
            self.page3_cti_LineEdit.setText(str(No_belum_terpakai))

    # Definisikan Completer SKU_Induk
    def Page3_cti_SKU_Induk_Completer(self):
        Load_SKU_Induk_terpakai = self.page3_cti_DBProduk_cursor.execute("select SKU_Induk from Data_Produk_Master").fetchall()
        for item in range(len(Load_SKU_Induk_terpakai)):
            if Load_SKU_Induk_terpakai[item]["SKU_Induk"] not in self.page3_cti_SKU_Induk_terpakai:
                self.page3_cti_SKU_Induk_terpakai.append((Load_SKU_Induk_terpakai[item]["SKU_Induk"]))
            else:
                pass
        self.page3_cti_SKU_Induk_terpakai.sort()
        SKU_Induk_completer = QtWidgets.QCompleter(self.page3_cti_SKU_Induk_terpakai)
        SKU_Induk_completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        SKU_Induk_completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cti_LineEdit_34.setCompleter(SKU_Induk_completer)

        SKU_Induk_completer.activated.connect(self.Page3_cti_SKU_Varian_1_Completer)

    # Definisikan Completer SKU_Varian_1
    def Page3_cti_SKU_Varian_1_Completer(self):
        self.page3_cti_SKU_Varian_1_terpakai.clear()
        self.page3_cti_SKU_Varian_2_terpakai.clear()
        self.page3_cti_LineEdit_35.clear()
        self.page3_cti_LineEdit_36.clear()
        SKU_Varian1_item = self.page3_cti_DBProduk_cursor.execute("select SKU_Varian_1 from Data_Produk_Master where SKU_Induk='{}'".format(self.page3_cti_LineEdit_34.text())).fetchall()
        for item in range(len(SKU_Varian1_item)):
            if SKU_Varian1_item[item]["SKU_Varian_1"] not in self.page3_cti_SKU_Varian_1_terpakai:
                self.page3_cti_SKU_Varian_1_terpakai.append(SKU_Varian1_item[item]["SKU_Varian_1"])
            else:
                pass
        SKU_Varian_1_Completer = QtWidgets.QCompleter(self.page3_cti_SKU_Varian_1_terpakai)
        SKU_Varian_1_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        SKU_Varian_1_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cti_LineEdit_35.setCompleter(SKU_Varian_1_Completer)
        SKU_Varian_1_Completer.activated.connect(self.Page3_cti_SKU_Varian_2_Completer)

    # Definisikan Completer SKU_Varian_2
    def Page3_cti_SKU_Varian_2_Completer(self):
        self.page3_cti_SKU_Varian_2_terpakai.clear()
        self.page3_cti_LineEdit_36.clear()
        SKU_Varian2_item = self.page3_cti_DBProduk_cursor.execute("select SKU_Varian_2 from Data_Produk_Master where SKU_Induk='{}'".format(self.page3_cti_LineEdit_34.text())).fetchall()
        for item in range(len(SKU_Varian2_item)):
            if SKU_Varian2_item[item]["SKU_Varian_2"] not in self.page3_cti_SKU_Varian_2_terpakai:
                self.page3_cti_SKU_Varian_2_terpakai.append(SKU_Varian2_item[item]["SKU_Varian_2"])
            else:
                pass
        SKU_Varian_2_Completer = QtWidgets.QCompleter(self.page3_cti_SKU_Varian_2_terpakai)
        SKU_Varian_2_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        SKU_Varian_2_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cti_LineEdit_36.setCompleter(SKU_Varian_2_Completer)

    # Definisikan Kode Produk Di Toko
    def Page3_cti_Kode_Produk_Di_Toko(self):
        text = str(self.page3_cti_LineEdit_34.text()) + str(self.page3_cti_LineEdit_35.text()) + str(self.page3_cti_LineEdit_36.text())
        self.page3_cti_LineEdit_2.setText(text)

    # Definisikan Nama Produk di Distributor
    def Page3_cti_Nama_Produk_Di_Distributor_Completer(self):
        self.page3_cti_Nama_Produk_Di_Distributor_terpakai.clear()
        self.page3_cti_LineEdit_5.clear()
        Nama_Produk_Di_Distributor_item = self.page3_cti_DBProduk_cursor.execute("select Nama_Produk_Di_Distributor from Data_Produk_Master where Kode_Toko='{}'".format(self.page3_cti_LineEdit_2.text())).fetchall()
        for item in range(len(Nama_Produk_Di_Distributor_item)):
            self.page3_cti_Nama_Produk_Di_Distributor_terpakai.append(Nama_Produk_Di_Distributor_item[item]["Nama_Produk_Di_Distributor"])
        Nama_Produk_Di_Distributor_Completer = QtWidgets.QCompleter(self.page3_cti_Nama_Produk_Di_Distributor_terpakai)
        Nama_Produk_Di_Distributor_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        Nama_Produk_Di_Distributor_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cti_LineEdit_5.setCompleter(Nama_Produk_Di_Distributor_Completer)

    # Operasi Hitungan Berat Untuk Pengiriman
    def Page3_cti_Berat_Untuk_Pengiriman(self):
        Pengali = 1
        Berat_atau_Volume_Produk = self.page3_cti_LineEdit_38.text()
        Berat_atau_Volume_Produk_Satuan = self.page3_cti_ComboBox_5.currentText()
        if Berat_atau_Volume_Produk_Satuan == "Kilogram":
            Pengali = 1000
        elif Berat_atau_Volume_Produk_Satuan == "Liter":
            Pengali = 1000
        else:
            pass

        try:
            Berat_dalam_gram = float(self.page3_cti_LineEdit_38.text()) * Pengali
            if Berat_dalam_gram >= 10:
                Berat_Untuk_Pengiriman = float(Berat_dalam_gram) + ((float(Berat_dalam_gram))*10)/100
                self.page3_cti_LineEdit_6.setText(str(int(Berat_Untuk_Pengiriman)))
            else:
                Berat_Untuk_Pengiriman = float(Berat_dalam_gram) + ((float(Berat_dalam_gram)) * 10) / 100 + 2
                self.page3_cti_LineEdit_6.setText(str(int(Berat_Untuk_Pengiriman)))
        except:
            self.page3_cti_LineEdit_6.clear()
            pass

    # Operasi Kode BPOM atau PIRT
    def Page3_cti_KodeBPOM_atau_PIRT(self):
        Jenis_Perizinan = self.page3_cti_ComboBox_2.currentText()
        if Jenis_Perizinan == "BPOM":
            self.page3_cti_LineEdit_7.clear()
            self.page3_cti_LineEdit_7.setEnabled(True)
        elif Jenis_Perizinan == "PIRT":
            self.page3_cti_LineEdit_7.clear()
            self.page3_cti_LineEdit_7.setEnabled(True)
        else:
            self.page3_cti_LineEdit_7.clear()
            self.page3_cti_LineEdit_7.setText("Tidak ada izin resmi")
            self.page3_cti_LineEdit_7.setDisabled(True)
            pass

    # Produsen Completer
    def Page3_cti_Produsen_Completer(self):
        self.page3_cti_Produsen_terpakai.clear()
        Daftar_Produsen = self.page3_cti_DBProduk_cursor.execute("select Produsen from Data_Produk_Master").fetchall()
        for item in range(len(Daftar_Produsen)):
            if Daftar_Produsen[item]["Produsen"] not in self.page3_cti_Produsen_terpakai:
                self.page3_cti_Produsen_terpakai.append(Daftar_Produsen[item]["Produsen"])
            else:
                pass

        Daftar_Produsen_Completer = QtWidgets.QCompleter(self.page3_cti_Produsen_terpakai)
        Daftar_Produsen_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        Daftar_Produsen_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cti_LineEdit_8.setCompleter(Daftar_Produsen_Completer)

    # Distributor Completer
    def Page3_cti_Distributor_Completer(self):
        self.page3_cti_Distributor_terpakai.clear()
        self.page3_cti_LineEdit_9.clear()
        Daftar_Distributor = self.page3_cti_DBProduk_cursor.execute("select Distributor from Data_Produk_Master where Produsen='{}'".format(self.page3_cti_LineEdit_8.text())).fetchall()
        for item in range(len(Daftar_Distributor)):
            if Daftar_Distributor[item]["Distributor"] not in self.page3_cti_Distributor_terpakai:
                self.page3_cti_Distributor_terpakai.append(Daftar_Distributor[item]["Distributor"])
            else:
                pass

        Daftar_Distributor_Completer = QtWidgets.QCompleter(self.page3_cti_Distributor_terpakai)
        Daftar_Distributor_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        Daftar_Distributor_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cti_LineEdit_9.setCompleter(Daftar_Distributor_Completer)

    # Nama Sales Completer
    def Page3_cti_Nama_Sales_Completer(self):
        self.page3_cti_Nama_Sales_terpakai.clear()
        self.page3_cti_LineEdit_10.clear()
        Daftar_Nama_Sales = self.page3_cti_DBProduk_cursor.execute("select Nama_Sales from Data_Produk_Master where Distributor='{}'".format(self.page3_cti_LineEdit_9.text())).fetchall()
        for item in range(len(Daftar_Nama_Sales)):
            if Daftar_Nama_Sales[item]["Nama_Sales"] not in self.page3_cti_Nama_Sales_terpakai:
                self.page3_cti_Nama_Sales_terpakai.append(Daftar_Nama_Sales[item]["Nama_Sales"])
            else:
                pass

        Daftar_Nama_Sales_Completer = QtWidgets.QCompleter(self.page3_cti_Nama_Sales_terpakai)
        Daftar_Nama_Sales_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        Daftar_Nama_Sales_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cti_LineEdit_10.setCompleter(Daftar_Nama_Sales_Completer)

    # No Telepon Sales Completer
    def Page3_cti_No_Telepon_Sales_Completer(self):
        self.page3_cti_No_Telepon_Sales_terpakai.clear()
        self.page3_cti_LineEdit_11.clear()
        Daftar_No_Telepon_Sales = self.page3_cti_DBProduk_cursor.execute("select No_Telepon_Sales from Data_Produk_Master where Nama_Sales='{}'".format(self.page3_cti_LineEdit_10.text())).fetchall()
        try:
            No_Telepon_Sales = Daftar_No_Telepon_Sales[0]["No_Telepon_Sales"]
        except:
            No_Telepon_Sales = ""
        for item in range(len(Daftar_No_Telepon_Sales)):
            if Daftar_No_Telepon_Sales[item]["No_Telepon_Sales"] not in self.page3_cti_No_Telepon_Sales_terpakai:
                self.page3_cti_No_Telepon_Sales_terpakai.append(Daftar_No_Telepon_Sales[item]["No_Telepon_Sales"])
            else:
                pass
        self.page3_cti_LineEdit_11.setText(str(No_Telepon_Sales))
        Daftar_No_Telepon_Sales_Completer = QtWidgets.QCompleter(self.page3_cti_No_Telepon_Sales_terpakai)
        Daftar_No_Telepon_Sales_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        Daftar_No_Telepon_Sales_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cti_LineEdit_11.setCompleter(Daftar_No_Telepon_Sales_Completer)

    # Definisikan Keuntungan
    def Page3_cti_Keuntungan(self):
        self.page3_cti_LineEdit_14.clear()
        if self.page3_cti_ComboBox_6.currentText() == "Umum":
            self.laba_dasar = 7
        elif self.page3_cti_ComboBox_6.currentText() == "Jarang":
            self.laba_dasar = 8
        elif self.page3_cti_ComboBox_6.currentText() == "Sangat Jarang":
            self.laba_dasar = 9
        elif self.page3_cti_ComboBox_6.currentText() == "Produk Sendiri":
            self.laba_dasar = 10
        else:
            self.laba_dasar = 9
            self.page3_cti_LineEdit_14.setText("0")
        self.laba_diskon = self.laba_dasar - 1
        self.laba_grosir_1 = self.laba_dasar - 2
        self.laba_grosir_2 = self.laba_dasar - 3
        self.laba_grosir_3 = self.laba_dasar - 4

    # Hitungan Biaya Penanganan
    def Page3_cti_Hitungan_Biaya_Penanganan(self):
        self.page3_cti_LineEdit_12.clear()
        try:
            Harga_Beli_Terakhir = int(self.page3_cti_LineEdit_13.text())
        except:
            Harga_Beli_Terakhir = 0

        Biaya_Penanganan_Dasar = 100
        if int(Harga_Beli_Terakhir) == 0:
            Biaya_Penanganan = 0
        elif int(Harga_Beli_Terakhir) <= 5000:
            Biaya_Penanganan = Biaya_Penanganan_Dasar * 1
        elif int(Harga_Beli_Terakhir) <= 10000:
            Biaya_Penanganan = Biaya_Penanganan_Dasar * 2
        elif int(Harga_Beli_Terakhir) <= 50000:
            Biaya_Penanganan = Biaya_Penanganan_Dasar * 4
        elif int(Harga_Beli_Terakhir) <= 100000:
            Biaya_Penanganan = Biaya_Penanganan_Dasar * 8
        elif int(Harga_Beli_Terakhir) <= 200000:
            Biaya_Penanganan = Biaya_Penanganan_Dasar * 16
        elif int(Harga_Beli_Terakhir) <= 400000:
            Biaya_Penanganan = Biaya_Penanganan_Dasar * 32
        elif int(Harga_Beli_Terakhir) > 400000:
            Biaya_Penanganan = Biaya_Penanganan_Dasar * 64
        else:
            Biaya_Penanganan = Biaya_Penanganan_Dasar
            pass

        self.page3_cti_LineEdit_12.setText(str(Biaya_Penanganan))

    # Hitungan Laba_Dasar_Dalam_Persen
    def Page3_cti_Hitungan_Laba_Dasar_Dalam_Persen(self):
        self.page3_cti_LineEdit_14.setText(str(self.laba_dasar))
        self.Page3_cti_Hitungan_Laba_Dasar_Dalam_Rupiah()
        self.page3_cti_LineEdit_14.textChanged.connect(self.Page3_cti_Hitungan_Laba_Dasar_Dalam_Rupiah)

    # Hitungan Laba_Dasar_Dalam_Rupiah
    def Page3_cti_Hitungan_Laba_Dasar_Dalam_Rupiah(self):
        try:
            self.page3_cti_LineEdit_15.clear()
            Harga_Beli_Terakhir = int(self.page3_cti_LineEdit_13.text())
            Laba_Dasar_Dalam_Persen = int(self.page3_cti_LineEdit_14.text())
            Laba_Dasar_Dalam_Rupiah = int((Laba_Dasar_Dalam_Persen/100)*Harga_Beli_Terakhir)
            self.page3_cti_LineEdit_15.setText(str(Laba_Dasar_Dalam_Rupiah))
        except:
            self.page3_cti_LineEdit_15.setText("error")
        self.Page3_cti_Hitungan_Harga_Jual_Dasar()

    # Hitungan Harga Jual Dasar
    def Page3_cti_Hitungan_Harga_Jual_Dasar(self):
        try:
            self.page3_cti_LineEdit_16.clear()
            Harga_Beli_Terakhir = int(self.page3_cti_LineEdit_13.text())
            Biaya_Penanganan = int(self.page3_cti_LineEdit_12.text())
            Laba_Dasar_Dalam_Rupiah = int(self.page3_cti_LineEdit_15.text())
            Harga_Jual_Dasar = int(RoundUp100(Harga_Beli_Terakhir + Biaya_Penanganan + Laba_Dasar_Dalam_Rupiah))
            self.page3_cti_LineEdit_16.setText(str(Harga_Jual_Dasar))
        except:
            self.page3_cti_LineEdit_16.setText("0")

    # Hitungan Laba Saat Diskon Dalam Persen
    def Page3_cti_Hitungan_Laba_Saat_Diskon_Dalam_Persen(self):
        Laba_Saat_Diskon_Dalam_Persen = self.laba_diskon
        self.page3_cti_LineEdit_17.setText(str(Laba_Saat_Diskon_Dalam_Persen))
        self.Page3_cti_Hitungan_Laba_Saat_Diskon_Dalam_Rupiah()
        self.page3_cti_LineEdit_17.textChanged.connect(self.Page3_cti_Hitungan_Laba_Saat_Diskon_Dalam_Rupiah)

    # Hitungan Laba Saat Diskon Dalam Rupiah
    def Page3_cti_Hitungan_Laba_Saat_Diskon_Dalam_Rupiah(self):
        try:
            self.page3_cti_LineEdit_18.clear()
            Harga_Beli_Terakhir = int(self.page3_cti_LineEdit_13.text())
            Laba_Saat_Diskon_Dalam_Persen = int(self.page3_cti_LineEdit_17.text())
            Laba_Saat_Diskon_Dalam_Rupiah = int((Laba_Saat_Diskon_Dalam_Persen/100)*Harga_Beli_Terakhir)
            self.page3_cti_LineEdit_18.setText(str(Laba_Saat_Diskon_Dalam_Rupiah))
        except:
            Laba_Saat_Diskon_Dalam_Persen = 0
            self.page3_cti_LineEdit_18.setText("0")
        self.Page3_cti_Hitungan_Harga_Jual_Saat_Diskon()

    # Hitungan Harga Jual Saat Diskon
    def Page3_cti_Hitungan_Harga_Jual_Saat_Diskon(self):
        try:
            Harga_Beli_Terakhir = int(self.page3_cti_LineEdit_13.text())
            Biaya_Penanganan = int(self.page3_cti_LineEdit_12.text())
            Laba_Saat_Diskon_Dalam_Rupiah = int(self.page3_cti_LineEdit_18.text())
            Harga_Jual_Saat_Diskon = RoundUp100(Harga_Beli_Terakhir + Biaya_Penanganan + Laba_Saat_Diskon_Dalam_Rupiah)
            self.page3_cti_LineEdit_19.setText(str(Harga_Jual_Saat_Diskon))
        except:
            self.page3_cti_LineEdit_19.setText("0")

    # Hitungan Grosir 1 (Minimal Pembelian)
    def Page3_cti_Hitungan_Grosir_1_Minimal_Pembelian(self):
        self.page3_cti_LineEdit_20.setText("3")

    # Hitungan Grosir 1 (Laba dalam persen)
    def Page3_cti_Hitungan_Grosir_1_Laba_Dalam_Persen(self):
        if self.laba_grosir_1 <= 0:
            Grosir_1_Laba_Dalam_Persen = 0
        elif self.laba_grosir_1 > 0:
            Grosir_1_Laba_Dalam_Persen = self.laba_grosir_1
        else:
            self.page3_cti_LineEdit_21.setText("0")
        self.page3_cti_LineEdit_21.setText(str(Grosir_1_Laba_Dalam_Persen))
        self.Page3_cti_Hitungan_Grosir_1_Laba_Dalam_Rupiah()
        self.page3_cti_LineEdit_21.textChanged.connect(self.Page3_cti_Hitungan_Grosir_1_Laba_Dalam_Rupiah)

    # Hitungan Grosir 1 (Laba dalam rupiah)
    def Page3_cti_Hitungan_Grosir_1_Laba_Dalam_Rupiah(self):
        try:
            Grosir_1_Laba_Dalam_Persen = int(self.page3_cti_LineEdit_21.text())
            Harga_Beli_Terakhir = int(self.page3_cti_LineEdit_13.text())
            Grosir_1_Laba_Dalam_Rupiah = int((Grosir_1_Laba_Dalam_Persen/100) * Harga_Beli_Terakhir)
            self.page3_cti_LineEdit_22.setText(str(Grosir_1_Laba_Dalam_Rupiah))
        except:
            self.page3_cti_LineEdit_22.setText("0")
        self.Page3_cti_Hitungan_Grosir_1_Harga_Jual()

    # Hitungan_Grosir 1 (Harga jual)
    def Page3_cti_Hitungan_Grosir_1_Harga_Jual(self):
        try:
            Harga_Beli_Terakhir = int(self.page3_cti_LineEdit_13.text())
            Biaya_Penanganan = int(self.page3_cti_LineEdit_12.text())
            Grosir_1_Laba_Dalam_Rupiah = int(self.page3_cti_LineEdit_22.text())
            Grosir_1_Harga_Jual = RoundUp100(int(Harga_Beli_Terakhir + Biaya_Penanganan + Grosir_1_Laba_Dalam_Rupiah))
            self.page3_cti_LineEdit_23.setText(str(Grosir_1_Harga_Jual))
        except:
            self.page3_cti_LineEdit_23.setText("0")

    # Hitungan Grosir 2 (Minimal Pembelian)
    def Page3_cti_Hitungan_Grosir_2_Minimal_Pembelian(self):
        self.page3_cti_LineEdit_24.setText("6")

    # Hitungan Grosir 2 (Laba dalam persen)
    def Page3_cti_Hitungan_Grosir_2_Laba_Dalam_Persen(self):
        if self.laba_grosir_2 <= 0:
            Grosir_2_Laba_Dalam_Persen = 0
        elif self.laba_grosir_2 > 0:
            Grosir_2_Laba_Dalam_Persen = self.laba_grosir_2
        else:
            self.page3_cti_LineEdit_25.setText("0")
        self.page3_cti_LineEdit_25.setText(str(Grosir_2_Laba_Dalam_Persen))
        self.Page3_cti_Hitungan_Grosir_2_Laba_Dalam_Rupiah()
        self.page3_cti_LineEdit_25.textChanged.connect(self.Page3_cti_Hitungan_Grosir_2_Laba_Dalam_Rupiah)

    # Hitungan Grosir 2 (Laba dalam rupiah)
    def Page3_cti_Hitungan_Grosir_2_Laba_Dalam_Rupiah(self):
        try:
            Grosir_2_Laba_Dalam_Persen = int(self.page3_cti_LineEdit_25.text())
            Harga_Beli_Terakhir = int(self.page3_cti_LineEdit_13.text())
            Grosir_2_Laba_Dalam_Rupiah = int((Grosir_2_Laba_Dalam_Persen/100)*Harga_Beli_Terakhir)
            self.page3_cti_LineEdit_26.setText(str(Grosir_2_Laba_Dalam_Rupiah))
        except:
            self.page3_cti_LineEdit_26.setText("0")
        self.Page3_cti_Hitungan_Grosir_2_Harga_Jual()

    # Hitungan Grosir 2 (Harga Jual)
    def Page3_cti_Hitungan_Grosir_2_Harga_Jual(self):
        try:
            Harga_Beli_Terakhir = int(self.page3_cti_LineEdit_13.text())
            Grosir_2_Laba_Dalam_Rupiah = int(self.page3_cti_LineEdit_26.text())
            Biaya_Penanganan = int(self.page3_cti_LineEdit_12.text())
            Grosir_2_Harga_Jual = RoundUp100(int(Harga_Beli_Terakhir + Biaya_Penanganan + Grosir_2_Laba_Dalam_Rupiah))
            self.page3_cti_LineEdit_27.setText(str(Grosir_2_Harga_Jual))
        except:
            self.page3_cti_LineEdit_27.setText("0")

    # Hitungan Grosir 3 (Minimal Pembelian)
    def Page3_cti_Hitungan_Grosir_3_Minimal_Pembelian(self):
        self.page3_cti_LineEdit_28.setText("12")

    # Hitungan Grosir 3 (Laba dalam persen)
    def Page3_cti_Hitungan_Grosir_3_Laba_Dalam_Persen(self):
        if self.laba_grosir_3 <= 0:
            Grosir_3_Laba_Dalam_Persen = 0
        elif self.laba_grosir_3 > 0:
            Grosir_3_Laba_Dalam_Persen = self.laba_grosir_3
        else:
            self.page3_cti_LineEdit_29.setText("0")
        self.page3_cti_LineEdit_29.setText(str(Grosir_3_Laba_Dalam_Persen))
        self.Page3_cti_Hitungan_Grosir_3_Laba_Dalam_Rupiah()
        self.page3_cti_LineEdit_29.textChanged.connect(self.Page3_cti_Hitungan_Grosir_3_Laba_Dalam_Rupiah)

    # Hitungan Grosir 3 (Laba dalam Rupiah)
    def Page3_cti_Hitungan_Grosir_3_Laba_Dalam_Rupiah(self):
        try:
            Grosir_3_Laba_Dalam_Persen = int(self.page3_cti_LineEdit_29.text())
            Harga_Beli_Terakhir = int(self.page3_cti_LineEdit_13.text())
            Grosir_3_Laba_Dalam_Rupiah = int((Grosir_3_Laba_Dalam_Persen/100)*Harga_Beli_Terakhir)
            self.page3_cti_LineEdit_30.setText(str(Grosir_3_Laba_Dalam_Rupiah))
        except:
            self.page3_cti_LineEdit_30.setText("0")
        self.Page3_cti_Hitungan_Grosir_3_Harga_Jual()

    # Hitungan Grosir 3 (Harga Jual)
    def Page3_cti_Hitungan_Grosir_3_Harga_Jual(self):
        try:
            self.page3_cti_LineEdit_31.clear()
            Harga_Beli_Terakhir = int(self.page3_cti_LineEdit_13.text())
            Biaya_Penanganan = int(self.page3_cti_LineEdit_12.text())
            Grosir_3_Laba_Dalam_Rupiah = int(self.page3_cti_LineEdit_30.text())
            Grosir_3_Harga_Jual = RoundUp100(int(Harga_Beli_Terakhir + Biaya_Penanganan + Grosir_3_Laba_Dalam_Rupiah))
            self.page3_cti_LineEdit_31.setText(str(Grosir_3_Harga_Jual))
        except:
            self.page3_cti_LineEdit_31.setText("0")

    # Tambah Gambar
    def Page3_cti_Tambah_Gambar(self):
        Pilih_Gambar = QtWidgets.QFileDialog()
        Gambar_Terpilih = Pilih_Gambar.getOpenFileUrl()
        Lokasi_Gambar_Terpilih = Gambar_Terpilih[0].url()[8:]
        self.page3_cti_LineEdit_33.setText(Lokasi_Gambar_Terpilih)

    # Dialog Konfirmasi Tombol Batal Diklik
    def Page3_cti_Konfirmasi_Tombol_Batal_klik(self):
        Dialog = QtWidgets.QDialog()
        Layout = QtWidgets.QGridLayout(Dialog)
        Dialog.setModal(True)
        Dialog.setWindowTitle("Konfirmasi Batal")

        Text = QtWidgets.QLabel("""Apakah anda ingin keluar?\nData tidak akan tersimpan jika anda keluar""")
        PushButton_Ya = QtWidgets.QPushButton("Ya")
        PushButton_Tidak = QtWidgets.QPushButton("Tidak")
        Layout.addWidget(Text, 0, 1, 1, 3)
        Layout.addWidget(PushButton_Ya, 1, 2)
        Layout.addWidget(PushButton_Tidak, 1, 3)

        def closeAll():
            Dialog.close()
            self.Dialog.close()

        PushButton_Tidak.clicked.connect(Dialog.close)
        PushButton_Ya.clicked.connect(closeAll)

        Dialog.show()
        Dialog.exec_()

    # Definisikan pesan error
    def Page3_cti_Pesan_Error(self, judul, pesan):
        Window_Messege_Error = QtWidgets.QMessageBox()
        Window_Messege_Error.setWindowTitle(str(judul))
        Window_Messege_Error.setText(str(pesan))

        Window_Messege_Error.show()
        Window_Messege_Error.exec_()

    # Validasi Data
    def Page3_cti_Validasi_Data(self):
        def Validasi_Nomor():
            try:
                self.page3_cti_LineEdit.setStyleSheet("color: black")
                int(self.page3_cti_LineEdit.text())/1
                Validasi_SKU_Induk()
            except:
                self.page3_cti_LineEdit.setStyleSheet("color: red")
                self.Page3_cti_Pesan_Error("Error", "Nomor yang anda masukkan salah")

        def Validasi_SKU_Induk():
            text = self.page3_cti_LineEdit_34.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_34.setStyleSheet("color: black")
                self.page3_cti_LineEdit_34.setPlaceholderText("")
                Validasi_SKU_Varian_1()
            else:
                self.page3_cti_LineEdit_34.setStyleSheet("color: red")
                self.page3_cti_LineEdit_34.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "SKU Induk tidak boleh kosong")
                self.page3_cti_LineEdit_34.setFocus()

        def Validasi_SKU_Varian_1():
            text = self.page3_cti_LineEdit_35.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_35.setStyleSheet("color: black")
                Validasi_SKU_Varian_2()
            else:
                self.page3_cti_LineEdit_35.setStyleSheet("color: red")
                self.page3_cti_LineEdit_35.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", 'Masukkan SKU Varian 1, apabila tidak ada varian, isikan dengan "V1"')
                self.page3_cti_LineEdit_35.setFocus()

        def Validasi_SKU_Varian_2():
            text = self.page3_cti_LineEdit_36.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_36.setStyleSheet("color: black")
                Validasi_Kode_Produk_Di_Toko()
            else:
                self.page3_cti_LineEdit_36.setStyleSheet("color: red")
                self.page3_cti_LineEdit_36.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", 'Masukkan nilai SKU Varian 2, apabila tidak ada varian isikan dengan "V1"')
                self.page3_cti_LineEdit_36.setFocus()

        def Validasi_Kode_Produk_Di_Toko():
            text = self.page3_cti_LineEdit_2.text()
            Kode_Produk_Terpakai = []
            Kode_Produk = self.page3_cti_DBProduk_cursor.execute("select Kode_Toko from Data_Produk_Master").fetchall()
            for item in range(len(Kode_Produk)):
                Kode_Produk_Terpakai.append(Kode_Produk[item]["Kode_Toko"])

            if text not in Kode_Produk_Terpakai:
                self.page3_cti_LineEdit_2.setStyleSheet("color: black")
                self.page3_cti_LineEdit_34.setStyleSheet("color: black")
                self.page3_cti_LineEdit_35.setStyleSheet("color: black")
                self.page3_cti_LineEdit_36.setStyleSheet("color: black")
                Validasi_Barcode_Produk()
            else:
                self.page3_cti_LineEdit_2.setStyleSheet("color: red")
                self.page3_cti_LineEdit_34.setStyleSheet("color: red")
                self.page3_cti_LineEdit_35.setStyleSheet("color: red")
                self.page3_cti_LineEdit_36.setStyleSheet("color: red")
                self.Page3_cti_Pesan_Error("Data Duplikat", "Data Kode 'Produk di Toko' sudah ada dalam database.\n\nTambahkan transaksi produk apabila produk yang anda masukkan telah ada dalam database \nATAU\nTambahkan SKU Varian baru (SKU Varian 1 atau 2) apabila produk tersebut memiliki varian baru")

        def Validasi_Barcode_Produk():
            text = self.page3_cti_LineEdit_4.text()
            Barcode_Produk_terpakai = []
            Barcode = self.page3_cti_DBProduk_cursor.execute("select Barcode_Produk from Data_Produk_Master").fetchall()
            for item in range(len(Barcode)):
                Barcode_Produk_terpakai.append(Barcode[item]["Barcode_Produk"])

            if text not in Barcode_Produk_terpakai:
                if len(text) > 0:
                    self.page3_cti_LineEdit_4.setStyleSheet("color: black")
                    Validasi_Nama_Produk_Di_Distributor()
                else:
                    self.page3_cti_LineEdit_4.setStyleSheet("color: red")
                    self.Page3_cti_Pesan_Error("Data tidak lengkap", "Data 'Barcode Produk' belum diisi.\nJika produk tidak memiliki barcode, isi kolom ini dengan data yang sama dengan data 'Kode Produk di Toko'")
                    self.page3_cti_LineEdit_4.setPlaceholderText("Tidak boleh kosong")
                    self.page3_cti_LineEdit_4.setFocus()
            else:
                self.page3_cti_LineEdit_4.setStyleSheet("color: red")
                Barcode_Duplikat_Terpakai = self.page3_cti_DBProduk_cursor.execute("select Nama_Produk_Di_Toko from Data_Produk_Master where Barcode_Produk='{}'".format(text)).fetchone()["Nama_Produk_Di_Toko"]
                self.Page3_cti_Pesan_Error("Data Duplikat", "Barcode yang anda masukkan telah terpakai di produk lain.\nSilakan cek produk berikut :\n\nNama Produk : {}\nBarcode Produk : {}".format(Barcode_Duplikat_Terpakai, text))
                self.page3_cti_LineEdit_4.setFocus()

        def Validasi_Nama_Produk_Di_Distributor():
            text = self.page3_cti_LineEdit_5.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_5.setStyleSheet("color: black")
                Validasi_Nama_Produk()
            else:
                self.page3_cti_LineEdit_5.setStyleSheet("color: red")
                self.page3_cti_LineEdit_5.setPlaceholderText("Tidak boleh kosong")
                self.page3_cti_LineEdit_5.setFocus()
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Data 'Nama Distributor' belum diisi")

        def Validasi_Nama_Produk():
            text = self.page3_cti_LineEdit_3.text()
            Nama_Produk_terpakai = []
            Nama_Produk = self.page3_cti_DBProduk_cursor.execute("select Nama_Produk_Di_Toko from Data_Produk_Master").fetchall()
            for item in range(len(Nama_Produk)):
                Nama_Produk_terpakai.append(Nama_Produk[item]["Nama_Produk_Di_Toko"])

            if text not in Nama_Produk_terpakai:
                if len(text) > 0:
                    self.page3_cti_LineEdit_3.setStyleSheet("color: black")
                    Validasi_Deskripsi_Produk()
                else:
                    self.page3_cti_LineEdit_3.setStyleSheet("color: red")
                    self.Page3_cti_Pesan_Error("Data tidak lengkap", "Data 'Nama Produk' belum diisi.")
                    self.page3_cti_LineEdit_3.setPlaceholderText("Tidak boleh kosong")
                    self.page3_cti_LineEdit_3.setFocus()
            else:
                self.page3_cti_LineEdit_3.setStyleSheet("color: red")
                Nama_Produk_Duplikat_Terpakai = self.page3_cti_DBProduk_cursor.execute("select Nama_Produk_Di_Toko from Data_Produk_Master").fetchone()["Nama_Produk_Di_Toko"]
                self.Page3_cti_Pesan_Error("Data Duplikat", "Nama Produk yang anda masukkan telah terpakai di produk lain.\nSilakan cek produk berikut :\n\nNama Produk : {}".format(Nama_Produk_Duplikat_Terpakai))
                self.page3_cti_LineEdit_3.setFocus()

        # Tidak divalidasi
        def Validasi_Deskripsi_Produk():
            text = self.page3_cti_TextEdit.toPlainText()
            Validasi_Total_Stok()

        def Validasi_Total_Stok():
            text = self.page3_cti_LineEdit_37.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_37.setStyleSheet("color: black")
                Validasi_Warning_Stok()
            else:
                self.page3_cti_LineEdit_37.setStyleSheet("color: red")
                self.page3_cti_LineEdit_37.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Informasi Stok tidak boleh kosong")

        def Validasi_Warning_Stok():
            text = self.page3_cti_LineEdit_39.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_39.setStyleSheet("color: black")
                Validasi_Total_Stok_Satuan()
            else:
                self.page3_cti_LineEdit_39.setStyleSheet("color: red")
                self.page3_cti_LineEdit_39.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Informasi Warning Stok tidak boleh kosong")
                pass

        # Tidak divalidasi
        def Validasi_Total_Stok_Satuan():
            text = self.page3_cti_ComboBox_4.currentText()
            Validasi_Berat_atau_Volume_Di_Kemasan()

        def Validasi_Berat_atau_Volume_Di_Kemasan():
            text = self.page3_cti_LineEdit_38.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_38.setStyleSheet("color: black")
                Validasi_Berat_atau_Volume_Di_Kemasan_Satuan()
            else:
                self.page3_cti_LineEdit_38.setStyleSheet("color: red")
                self.page3_cti_LineEdit_38.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Data 'berat / volume produk di kemasan' tidak boleh kosong")

        # Tidak divalidasi
        def Validasi_Berat_atau_Volume_Di_Kemasan_Satuan():
            text = self.page3_cti_ComboBox_5.currentText()
            Validasi_Berat_Untuk_Pengiriman()

        # Tidak divalidasi
        def Validasi_Berat_Untuk_Pengiriman():
            text = self.page3_cti_LineEdit_6.text()
            Validasi_Kemasan()

        def Validasi_Kemasan():
            text = self.page3_cti_ComboBox.currentText()
            if text != "-":
                self.page3_cti_ComboBox.setStyleSheet("color: black")
                Validasi_Perizinan()
            else:
                self.page3_cti_ComboBox.setStyleSheet("color: red")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Data 'Kemasan' belum dipilih dengan benar")
                self.page3_cti_ComboBox.setFocus()

        def Validasi_Perizinan():
            text = self.page3_cti_ComboBox_2.currentText()
            if text != "-":
                self.page3_cti_ComboBox_2.setStyleSheet("color: black")
                Validasi_Kode_BPOM_atau_PIRT()
            else:
                self.page3_cti_ComboBox_2.setStyleSheet("color: red")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Data 'Perizinan' belum dipilih dengan benar")

        def Validasi_Kode_BPOM_atau_PIRT():
            text = self.page3_cti_LineEdit_7.text()
            self.page3_cti_LineEdit_7.setStyleSheet("color: black")
            if self.page3_cti_ComboBox_2.currentText() == "BPOM":
                if len(text) > 0:
                    Validasi_Label_Halal()
                else:
                    self.page3_cti_LineEdit_7.setStyleSheet("color: red")
                    self.page3_cti_LineEdit_7.setPlaceholderText("Kode {} tidak boleh kosong".format(self.page3_cti_ComboBox_2.currentText()))
                    self.Page3_cti_Pesan_Error("Data tidak lengkap", "Perizinan jenis {} telah dipilih. \nKode {} tidak boleh kosong".format(self.page3_cti_ComboBox_2.currentText(), self.page3_cti_ComboBox_2.currentText()))
            elif self.page3_cti_ComboBox_2.currentText() == "PIRT":
                if len(text) > 0:
                    Validasi_Label_Halal()
                else:
                    self.page3_cti_LineEdit_7.setStyleSheet("color: red")
                    self.page3_cti_LineEdit_7.setPlaceholderText("Kode {} tidak boleh kosong".format(self.page3_cti_ComboBox_2.currentText()))
                    self.Page3_cti_Pesan_Error("Data tidak lengkap", "Perizinan jenis {} telah dipilih. \nKode {} tidak boleh kosong".format(self.page3_cti_ComboBox_2.currentText(), self.page3_cti_ComboBox_2.currentText()))
            else:
                Validasi_Label_Halal()

        def Validasi_Label_Halal():
            text = self.page3_cti_ComboBox_3.currentText()
            if text != "-":
                self.page3_cti_ComboBox_3.setStyleSheet("color: black")
                Validasi_Produsen()
            else:
                self.page3_cti_ComboBox_3.setStyleSheet("color: red")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Data 'Label Halal' belum dipilih")

        def Validasi_Produsen():
            text = self.page3_cti_LineEdit_8.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_8.setStyleSheet("color: black")
                Validasi_Distributor()
            else:
                self.page3_cti_LineEdit_8.setStyleSheet("color: red")
                self.page3_cti_LineEdit_8.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Nama Produsen harus diisi")
                self.page3_cti_LineEdit_8.setFocus()

        def Validasi_Distributor():
            text = self.page3_cti_LineEdit_9.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_9.setStyleSheet("color: black")
                Validasi_Nama_Sales()
            else:
                self.page3_cti_LineEdit_9.setStyleSheet("color: red")
                self.page3_cti_LineEdit_9.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Nama Distributor harus diisi")
                self.page3_cti_LineEdit_9.setFocus()

        def Validasi_Nama_Sales():
            text = self.page3_cti_LineEdit_10.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_10.setStyleSheet("color: black")
                Validasi_Nomor_Telepon_Sales()
            else:
                self.page3_cti_LineEdit_10.setStyleSheet("color: red")
                self.page3_cti_LineEdit_10.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Nama Sales harus diisi")
                self.page3_cti_LineEdit_10.setFocus()

        def Validasi_Nomor_Telepon_Sales():
            text = self.page3_cti_LineEdit_11.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_11.setStyleSheet("color: black")
                Validasi_Barang_Umum_atau_Khusus()
            else:
                self.page3_cti_LineEdit_11.setStyleSheet("color: red")
                self.page3_cti_LineEdit_11.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Nomor telepon sales harus diisi")
                self.page3_cti_LineEdit_11.setFocus()

        def Validasi_Barang_Umum_atau_Khusus():
            text = self.page3_cti_ComboBox_6.currentText()
            if text != "-":
                self.page3_cti_ComboBox_6.setStyleSheet("color: black")
                Validasi_Harga_Beli_Terakhir()
            else:
                self.page3_cti_ComboBox_6.setStyleSheet("color: red")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Kode Barang Umum atau Khusus harus diisi")
                self.page3_cti_ComboBox_6.setFocus()

        def Validasi_Harga_Beli_Terakhir():
            text = self.page3_cti_LineEdit_13.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_13.setStyleSheet("color: black")
                Validasi_Biaya_Penanganan()
            else:
                self.page3_cti_LineEdit_13.setStyleSheet("color: red")
                self.page3_cti_LineEdit_13.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Harga beli terakhir harus diisi")
                self.page3_cti_LineEdit_13.setFocus()

        def Validasi_Biaya_Penanganan():
            text = self.page3_cti_LineEdit_12.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_12.setStyleSheet("color: black")
                Validasi_Laba_Dasar_Dalam_Persen()
            else:
                self.page3_cti_LineEdit_12.setStyleSheet("color: red")
                self.page3_cti_LineEdit_12.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Biaya Penanganan harus diisi")
                self.page3_cti_LineEdit_12.setFocus()

        def Validasi_Laba_Dasar_Dalam_Persen():
            text = self.page3_cti_LineEdit_14.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_14.setStyleSheet("color: black")
                Validasi_Laba_Dasar_Dalam_Rupiah()
            else:
                self.page3_cti_LineEdit_14.setStyleSheet("color: red")
                self.page3_cti_LineEdit_14.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Laba Dasar Dalam Persen harus diisi")
                self.page3_cti_LineEdit_14.setFocus()

        def Validasi_Laba_Dasar_Dalam_Rupiah():
            text = self.page3_cti_LineEdit_15.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_15.setStyleSheet("color: black")
                Validasi_Harga_Jual_Dasar()
            else:
                self.page3_cti_LineEdit_15.setStyleSheet("color: red")
                self.page3_cti_LineEdit_15.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Laba Dasar Dalam Rupiah harus diisi")
                self.page3_cti_LineEdit_15.setFocus()

        def Validasi_Harga_Jual_Dasar():
            text = self.page3_cti_LineEdit_16.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_16.setStyleSheet("color: black")
                Validasi_Laba_Saat_Diskon_Dalam_Persen()
            else:
                self.page3_cti_LineEdit_16.setStyleSheet("color: red")
                self.page3_cti_LineEdit_16.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "Harga Jual Dasar harus diisi")
                self.page3_cti_LineEdit_16.setFocus()

        def Validasi_Laba_Saat_Diskon_Dalam_Persen():
            text = self.page3_cti_LineEdit_17.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_17.setStyleSheet("color: black")
                Validasi_Laba_Saat_Diskon_Dalam_Rupiah()
            else:
                self.page3_cti_LineEdit_17.setStyleSheet("color: red")
                self.page3_cti_LineEdit_17.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Laba saat diskon dalam persen' harus diisi")
                self.page3_cti_LineEdit_17.setFocus()

        def Validasi_Laba_Saat_Diskon_Dalam_Rupiah():
            text = self.page3_cti_LineEdit_18.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_18.setStyleSheet("color: black")
                Validasi_Harga_Jual_Saat_Diskon()
            else:
                self.page3_cti_LineEdit_18.setStyleSheet("color: red")
                self.page3_cti_LineEdit_18.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Laba saat diskon dalam rupiah' harus diisi")
                self.page3_cti_LineEdit_18.setFocus()

        def Validasi_Harga_Jual_Saat_Diskon():
            text = self.page3_cti_LineEdit_19.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_19.setStyleSheet("color: black")
                Validasi_Grosir_1_Minimal_Pembelian()
            else:
                self.page3_cti_LineEdit_19.setStyleSheet("color: red")
                self.page3_cti_LineEdit_19.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Harga Jual Saat Diskon' harus diisi")
                self.page3_cti_LineEdit_19.setFocus()

        def Validasi_Grosir_1_Minimal_Pembelian():
            text = self.page3_cti_LineEdit_20.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_20.setStyleSheet("color: black")
                Validasi_Grosir_1_Laba_Dalam_Persen()
            else:
                self.page3_cti_LineEdit_20.setStyleSheet("color: red")
                self.page3_cti_LineEdit_20.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Minimal pembelian Grosir 1' harus diisi")
                self.page3_cti_LineEdit_20.setFocus()

        def Validasi_Grosir_1_Laba_Dalam_Persen():
            text = self.page3_cti_LineEdit_21.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_21.setStyleSheet("color: black")
                Validasi_Grosir_1_Laba_Dalam_Rupiah()
            else:
                self.page3_cti_LineEdit_21.setStyleSheet("color: red")
                self.page3_cti_LineEdit_21.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Laba dalam persen untuk Grosir 1' harus diisi")
                self.page3_cti_LineEdit_21.setFocus()

        def Validasi_Grosir_1_Laba_Dalam_Rupiah():
            text = self.page3_cti_LineEdit_22.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_22.setStyleSheet("color: black")
                Validasi_Grosir_1_Harga_Jual()
            else:
                self.page3_cti_LineEdit_22.setStyleSheet("color: red")
                self.page3_cti_LineEdit_22.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Laba dalam rupiah untuk Grosir 1' harus diisi")
                self.page3_cti_LineEdit_22.setFocus()

        def Validasi_Grosir_1_Harga_Jual():
            text = self.page3_cti_LineEdit_23.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_23.setStyleSheet("color: black")
                Validasi_Grosir_2_Minimal_Pembelian()
            else:
                self.page3_cti_LineEdit_23.setStyleSheet("color: red")
                self.page3_cti_LineEdit_23.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Harga jual untuk Grosir 1' harus diisi")
                self.page3_cti_LineEdit_23.setFocus()

        def Validasi_Grosir_2_Minimal_Pembelian():
            text = self.page3_cti_LineEdit_24.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_24.setStyleSheet("color: black")
                Validasi_Grosir_2_Laba_Dalam_Persen()
            else:
                self.page3_cti_LineEdit_24.setStyleSheet("color: red")
                self.page3_cti_LineEdit_24.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Minimal pembelian untuk Grosir 2' harus diisi")
                self.page3_cti_LineEdit_24.setFocus()

        def Validasi_Grosir_2_Laba_Dalam_Persen():
            text = self.page3_cti_LineEdit_25.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_25.setStyleSheet("color: black")
                Validasi_Grosir_2_Laba_Dalam_Rupiah()
            else:
                self.page3_cti_LineEdit_25.setStyleSheet("color: red")
                self.page3_cti_LineEdit_25.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Laba dalam persen untuk Grosir 2' harus diisi")
                self.page3_cti_LineEdit_25.setFocus()

        def Validasi_Grosir_2_Laba_Dalam_Rupiah():
            text = self.page3_cti_LineEdit_26.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_26.setStyleSheet("color: black")
                Validasi_Grosir_2_Harga_Jual()
            else:
                self.page3_cti_LineEdit_26.setStyleSheet("color: red")
                self.page3_cti_LineEdit_26.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Laba dalam rupiah untuk Grosir 2' harus diisi")
                self.page3_cti_LineEdit_26.setFocus()

        def Validasi_Grosir_2_Harga_Jual():
            text = self.page3_cti_LineEdit_27.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_27.setStyleSheet("color: black")
                Validasi_Grosir_3_Minimal_Pembelian()
            else:
                self.page3_cti_LineEdit_27.setStyleSheet("color: red")
                self.page3_cti_LineEdit_27.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Harga jual untuk Grosir 2' harus diisi")
                self.page3_cti_LineEdit_27.setFocus()

        def Validasi_Grosir_3_Minimal_Pembelian():
            text = self.page3_cti_LineEdit_28.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_28.setStyleSheet("color: black")
                Validasi_Grosir_3_Laba_Dalam_Persen()
            else:
                self.page3_cti_LineEdit_28.setStyleSheet("color: red")
                self.page3_cti_LineEdit_28.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Minimal pembelian untuk Grosir 3' harus diisi")
                self.page3_cti_LineEdit_28.setFocus()

        def Validasi_Grosir_3_Laba_Dalam_Persen():
            text = self.page3_cti_LineEdit_29.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_29.setStyleSheet("color: black")
                Validasi_Grosir_3_Laba_Dalam_Rupiah()
            else:
                self.page3_cti_LineEdit_29.setStyleSheet("color: red")
                self.page3_cti_LineEdit_29.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Laba dalam persen untuk Grosir 3' harus diisi")
                self.page3_cti_LineEdit_29.setFocus()

        def Validasi_Grosir_3_Laba_Dalam_Rupiah():
            text = self.page3_cti_LineEdit_30.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_30.setStyleSheet("color: black")
                Validasi_Grosir_3_Harga_Jual()
            else:
                self.page3_cti_LineEdit_30.setStyleSheet("color: red")
                self.page3_cti_LineEdit_30.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Laba dalam rupiah untuk Grosir 3' harus diisi")
                self.page3_cti_LineEdit_30.setFocus()

        def Validasi_Grosir_3_Harga_Jual():
            text = self.page3_cti_LineEdit_31.text()
            if len(text) > 0:
                self.page3_cti_LineEdit_31.setStyleSheet("color: black")
                Validasi_Catatan()
            else:
                self.page3_cti_LineEdit_31.setStyleSheet("color: red")
                self.page3_cti_LineEdit_31.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cti_Pesan_Error("Data tidak lengkap", "'Harga jual untuk Grosir 3' harus diisi")
                self.page3_cti_LineEdit_31.setFocus()

        # Tidak divalidasi
        def Validasi_Catatan():
            text = self.page3_cti_TextEdit_2.toPlainText()
            Validasi_Foto_Produk()

        # Tidak divalidasi
        def Validasi_Foto_Produk():
            text = self.page3_cti_LineEdit_33.text()
            Validasi_Posisi_Barang()

        # Tidak divalidasi
        def Validasi_Posisi_Barang():
            text = self.page3_cti_LineEdit_32.text()
            Validasi_Kepantasan_Harga()

        # Validasi Kepantasan Harga
        def Validasi_Kepantasan_Harga():
            Laba_Dasar = int(self.page3_cti_LineEdit_15.text())
            Laba_Saat_Diskon = int(self.page3_cti_LineEdit_18.text())
            Laba_Saat_Grosir_1 = int(self.page3_cti_LineEdit_22.text())
            Laba_Saat_Grosir_2 = int(self.page3_cti_LineEdit_26.text())
            Laba_Saat_Grosir_3 = int(self.page3_cti_LineEdit_30.text())
            if Laba_Dasar >= Laba_Saat_Diskon:
                if Laba_Saat_Diskon >= Laba_Saat_Grosir_1:
                    if Laba_Saat_Grosir_1 >= Laba_Saat_Grosir_2:
                        if Laba_Saat_Grosir_2 >= Laba_Saat_Grosir_3:
                            Validasi_Selesai()
                        else:
                            self.Page3_cti_Pesan_Error("Harga tidak valid", "Harga Jual Grosir 3 tidak boleh lebih besar daripada Harga Jual Grosir 2")
                            self.page3_cti_LineEdit_29.setFocus()
                    else:
                        self.Page3_cti_Pesan_Error("Harga tidak valid", "Harga Jual Grosir 2 tidak boleh lebih besar daripada Harga Jual Grosir 1")
                        self.page3_cti_LineEdit_25.setFocus()
                else:
                    self.Page3_cti_Pesan_Error("Harga tidak valid", "Harga Jual Grosir 1 tidak boleh lebih besar daripada Harga Jual Diskon")
                    self.page3_cti_LineEdit_21.setFocus()
            else:
                self.Page3_cti_Pesan_Error("Harga tidak valid", "Harga Jual Diskon tidak boleh lebih besar daripada Harga Jual Dasar")
                self.page3_cti_LineEdit_17.setFocus()

        def Validasi_Selesai():
            self.Page3_cti_Validasi_Selesai()

        # Style
        def Rubah_Warna_Text_SKU_Induk():
            if len(self.page3_cti_LineEdit_34.text()) > 0:
                self.page3_cti_LineEdit_34.setStyleSheet("color: black")
            else:
                self.page3_cti_LineEdit_34.setStyleSheet("color: red")

        def Rubah_Warna_Text_SKU_Varian_1():
            if len(self.page3_cti_LineEdit_35.text()) > 0:
                self.page3_cti_LineEdit_35.setStyleSheet("color: black")
            else:
                self.page3_cti_LineEdit_35.setStyleSheet("color: red")

        def Rubah_Warna_Text_SKU_Varian_2():
            if len(self.page3_cti_LineEdit_36.text()) > 0:
                self.page3_cti_LineEdit_36.setStyleSheet("color: black")
            else:
                self.page3_cti_LineEdit_36.setStyleSheet("color: red")

        # PERINTAH
        self.page3_cti_LineEdit_34.textChanged.connect(Rubah_Warna_Text_SKU_Induk)
        self.page3_cti_LineEdit_35.textChanged.connect(Rubah_Warna_Text_SKU_Varian_1)
        self.page3_cti_LineEdit_36.textChanged.connect(Rubah_Warna_Text_SKU_Varian_2)
        Validasi_Nomor()

    # Validasi Data selesai
    def Page3_cti_Validasi_Selesai(self):
        self.Page3_cti_Kumpulkan_Data()
        # Konfirmasi
        self.Dialog_Simpan = QtWidgets.QDialog()
        self.Dialog_Simpan.setWindowTitle("Konfirmasi Data")
        self.Dialog_Simpan.setModal(True)
        Layout = QtWidgets.QGridLayout(self.Dialog_Simpan)
        Label1 = QtWidgets.QLabel("Apakah anda ingin menyimpan data ini?")
        PushButton_Ya = QtWidgets.QPushButton("Ya")
        PushButton_Tidak = QtWidgets.QPushButton("Tidak")
        Layout.addWidget(Label1, 0, 1, 1, 3)
        Layout.addWidget(PushButton_Ya, 1, 2)
        Layout.addWidget(PushButton_Tidak, 1, 3)
        PushButton_Tidak.clicked.connect(self.Dialog_Simpan.close)
        PushButton_Ya.clicked.connect(self.Page3_cti_Simpan_Data)
        self.Dialog_Simpan.show()
        self.Dialog_Simpan.exec_()

    # Pada Saat Tombol Simpan Diklik
    def Page3_cti_PushButton_2_klik(self):
        self.Page3_cti_Validasi_Data()

    # Kumpulkan data Aplikasi
    def Page3_cti_Kumpulkan_Data(self):
        self.page3_cti_No = self.page3_cti_LineEdit.text()
        self.page3_cti_SKU_Induk = self.page3_cti_LineEdit_34.text()
        self.page3_cti_SKU_Varian_1 = self.page3_cti_LineEdit_35.text()
        self.page3_cti_SKU_Varian_2 = self.page3_cti_LineEdit_36.text()
        self.page3_cti_Kode_Toko = self.page3_cti_LineEdit_2.text()
        self.page3_cti_Barcode_Produk = self.page3_cti_LineEdit_4.text()
        self.page3_cti_Nama_Produk_Di_Distributor = self.page3_cti_LineEdit_5.text()
        self.page3_cti_Nama_Produk_Di_Toko = self.page3_cti_LineEdit_3.text()
        self.page3_cti_Repack = ""
        self.page3_cti_Produk_umum_khusus = self.page3_cti_ComboBox_6.currentText()
        self.page3_cti_Deskripsi_Produk = self.page3_cti_TextEdit.toPlainText()
        self.page3_cti_Total_Stok = self.page3_cti_LineEdit_37.text()
        self.page3_cti_Total_Stok_Satuan = self.page3_cti_ComboBox_4.currentText()
        self.page3_cti_Berat_atau_Volume_Bersih = self.page3_cti_LineEdit_38.text()
        self.page3_cti_Satuan_Berat_Bersih = self.page3_cti_ComboBox_5.currentText()
        self.page3_cti_Berat_Untuk_Pengiriman_Dalam_Gram = self.page3_cti_LineEdit_6.text()
        self.page3_cti_Kemasan = self.page3_cti_ComboBox.currentText()
        self.page3_cti_Perizinan = self.page3_cti_ComboBox_2.currentText()
        self.page3_cti_Kode_BPOM_atau_PIRT = self.page3_cti_LineEdit_7.text()
        self.page3_cti_Label_Halal = self.page3_cti_ComboBox_3.currentText()
        self.page3_cti_Produsen = self.page3_cti_LineEdit_8.text()
        self.page3_cti_Distributor = self.page3_cti_LineEdit_9.text()
        self.page3_cti_Nama_Sales = self.page3_cti_LineEdit_10.text()
        self.page3_cti_No_Telepon_Sales = self.page3_cti_LineEdit_11.text()
        self.page3_cti_Harga_Beli_Terakhir = self.page3_cti_LineEdit_13.text()
        self.page3_cti_Biaya_Penanganan = self.page3_cti_LineEdit_12.text()
        self.page3_cti_Laba_Dasar_Dalam_Persen = self.page3_cti_LineEdit_14.text()
        self.page3_cti_Laba_Dasar_Dalam_Rupiah = self.page3_cti_LineEdit_15.text()
        self.page3_cti_Harga_Jual_Dasar = self.page3_cti_LineEdit_16.text()
        self.page3_cti_Laba_Saat_Diskon_Dalam_Persen = self.page3_cti_LineEdit_17.text()
        self.page3_cti_Laba_Saat_Diskon_Dalam_Rupiah = self.page3_cti_LineEdit_18.text()
        self.page3_cti_Harga_Jual_Saat_Diskon = self.page3_cti_LineEdit_19.text()
        self.page3_cti_Minimal_Pembelian_Grosir_1 = self.page3_cti_LineEdit_20.text()
        self.page3_cti_Laba_Saat_Grosir_1_Dalam_Persen = self.page3_cti_LineEdit_21.text()
        self.page3_cti_Laba_Saat_Grosir_1_Dalam_Rupiah = self.page3_cti_LineEdit_22.text()
        self.page3_cti_Harga_Jual_Saat_Grosir_1 = self.page3_cti_LineEdit_23.text()
        self.page3_cti_Minimal_Pembelian_Grosir_2 = self.page3_cti_LineEdit_24.text()
        self.page3_cti_Laba_Saat_Grosir_2_Dalam_Persen = self.page3_cti_LineEdit_25.text()
        self.page3_cti_Laba_Saat_Grosir_2_Dalam_Rupiah = self.page3_cti_LineEdit_26.text()
        self.page3_cti_Harga_Jual_Saat_Grosir_2 = self.page3_cti_LineEdit_27.text()
        self.page3_cti_Minimal_Pembelian_Grosir_3 = self.page3_cti_LineEdit_28.text()
        self.page3_cti_Laba_Saat_Grosir_3_Dalam_Persen = self.page3_cti_LineEdit_29.text()
        self.page3_cti_Laba_Saat_Grosir_3_Dalam_Rupiah = self.page3_cti_LineEdit_30.text()
        self.page3_cti_Harga_Jual_Saat_Grosir_3 = self.page3_cti_LineEdit_31.text()
        self.page3_cti_Catatan = self.page3_cti_TextEdit_2.toPlainText()
        self.page3_cti_Foto_Produk_1 = self.page3_cti_LineEdit_33.text()
        self.page3_cti_Foto_Produk_2 = ""
        self.page3_cti_Foto_Produk_3 = ""
        self.page3_cti_Foto_Produk_4 = ""
        self.page3_cti_Foto_Produk_5 = ""
        self.page3_cti_Foto_Produk_6 = ""
        self.page3_cti_Foto_Produk_7 = ""
        self.page3_cti_Foto_Produk_8 = ""
        self.page3_cti_Foto_Produk_9 = ""
        self.page3_cti_Foto_Video = ""
        self.page3_cti_Posisi_Barang = self.page3_cti_LineEdit_32.text()
        self.page3_cti_Warning_Stok = str(self.page3_cti_LineEdit_39.text())

    # Simpan Data
    def Page3_cti_Simpan_Data(self):
        # Proses dalam Database
        # kolom = "No, SKU_Induk, SKU_Varian_1, SKU_Varian_2, Kode_Toko, Barcode_Produk, Nama_Produk_Di_Distributor, Nama_Produk_Di_Toko, Repack, Produk_umum_khusus, Deskripsi_Produk, Total_Stok, Total_Stok_Satuan, Berat_atau_Volume_Bersih, Satuan_Berat_Bersih, Berat_Untuk_Pengiriman_Dalam_Gram, Kemasan, Perizinan, Kode_BPOM_atau_PIRT, Label_Halal, Produsen, Distributor, Nama_Sales, No_Telepon_Sales, Harga_Beli_Terakhir, Biaya_Penanganan, Laba_Dasar_Dalam_Persen, Laba_Dasar_Dalam_Rupiah, Harga_Jual_Dasar, Laba_Saat_Diskon_Dalam_Persen, Laba_Saat_Diskon_Dalam_Rupiah, Harga_Jual_Saat_Diskon, Minimal_Pembelian_Grosir_1, Laba_Saat_Grosir_1_Dalam_Persen, Laba_Saat_Grosir_1_Dalam_Rupiah, Harga_Jual_Saat_Grosir_1, Minimal_Pembelian_Grosir_2, Laba_Saat_Grosir_2_Dalam_Persen, Laba_Saat_Grosir_2_Dalam_Rupiah, Harga_Jual_Saat_Grosir_2, Minimal_Pembelian_Grosir_3, Laba_Saat_Grosir_3_Dalam_Persen, Laba_Saat_Grosir_3_Dalam_Rupiah, Harga_Jual_Saat_Grosir_3, Catatan, Foto_Produk_1, Foto_Produk_2, Foto_Produk_3, Foto_Produk_4, Foto_Produk_5, Foto_Produk_6, Foto_Produk_7, Foto_Produk_8, Foto_Produk_9, Foto_Video, Posisi_Barang"
        # value ="{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, "
        # self.page3_cti_No, self.page3_cti_SKU_Induk, self.page3_cti_SKU_Varian_1, self.page3_cti_SKU_Varian_2, self.page3_cti_Kode_Toko, self.page3_cti_Barcode_Produk, self.page3_cti_Nama_Produk_Di_Distributor, self.page3_cti_Nama_Produk_Di_Toko, self.page3_cti_Repack, self.page3_cti_Produk_umum_khusus, self.page3_cti_Deskripsi_Produk, self.page3_cti_Total_Stok, self.page3_cti_Total_Stok_Satuan, self.page3_cti_Berat_atau_Volume_Bersih, self.page3_cti_Satuan_Berat_Bersih, self.page3_cti_Berat_Untuk_Pengiriman_Dalam_Gram, self.page3_cti_Kemasan, self.page3_cti_Perizinan, self.page3_cti_Kode_BPOM_atau_PIRT, self.page3_cti_Label_Halal, self.page3_cti_Produsen, self.page3_cti_Distributor, self.page3_cti_Nama_Sales, self.page3_cti_No_Telepon_Sales, self.page3_cti_Harga_Beli_Terakhir, self.page3_cti_Biaya_Penanganan, self.page3_cti_Laba_Dasar_Dalam_Persen, self.page3_cti_Laba_Dasar_Dalam_Rupiah, self.page3_cti_Harga_Jual_Dasar, self.page3_cti_Laba_Saat_Diskon_Dalam_Persen, self.page3_cti_Laba_Saat_Diskon_Dalam_Rupiah, self.page3_cti_Harga_Jual_Saat_Diskon, self.page3_cti_Minimal_Pembelian_Grosir_1, self.page3_cti_Laba_Saat_Grosir_1_Dalam_Persen, self.page3_cti_Laba_Saat_Grosir_1_Dalam_Rupiah, self.page3_cti_Harga_Jual_Saat_Grosir_1, self.page3_cti_Minimal_Pembelian_Grosir_2, self.page3_cti_Laba_Saat_Grosir_2_Dalam_Persen, self.page3_cti_Laba_Saat_Grosir_2_Dalam_Rupiah, self.page3_cti_Harga_Jual_Saat_Grosir_2, self.page3_cti_Minimal_Pembelian_Grosir_3, self.page3_cti_Laba_Saat_Grosir_3_Dalam_Persen, self.page3_cti_Laba_Saat_Grosir_3_Dalam_Rupiah, self.page3_cti_Harga_Jual_Saat_Grosir_3, self.page3_cti_Catatan, self.page3_cti_Foto_Produk_1, self.page3_cti_Foto_Produk_2, self.page3_cti_Foto_Produk_3, self.page3_cti_Foto_Produk_4, self.page3_cti_Foto_Produk_5, self.page3_cti_Foto_Produk_6, self.page3_cti_Foto_Produk_7, self.page3_cti_Foto_Produk_8, self.page3_cti_Foto_Produk_9, self.page3_cti_Foto_Video, self.page3_cti_Posisi_Barang
        self.page3_cti_DBProduk_cursor.execute("insert into `Data_Produk_Master` ('No','SKU_Induk','SKU_Varian_1','SKU_Varian_2','Kode_Toko','Barcode_Produk','Nama_Produk_Di_Distributor','Nama_Produk_Di_Toko','Repack','Produk_umum_khusus','Deskripsi_Produk','Total_Stok','Total_Stok_Satuan','Berat_atau_Volume_Bersih','Satuan_Berat_Bersih','Berat_Untuk_Pengiriman_Dalam_Gram','Kemasan','Perizinan','Kode_BPOM_atau_PIRT','Label_Halal','Produsen','Distributor','Nama_Sales','No_Telepon_Sales','Harga_Beli_Terakhir','Biaya_Penanganan','Laba_Dasar_Dalam_Persen','Laba_Dasar_Dalam_Rupiah','Harga_Jual_Dasar','Laba_Saat_Diskon_Dalam_Persen','Laba_Saat_Diskon_Dalam_Rupiah','Harga_Jual_Saat_Diskon','Minimal_Pembelian_Grosir_1','Laba_Saat_Grosir_1_Dalam_Persen','Laba_Saat_Grosir_1_Dalam_Rupiah','Harga_Jual_Saat_Grosir_1','Minimal_Pembelian_Grosir_2','Laba_Saat_Grosir_2_Dalam_Persen','Laba_Saat_Grosir_2_Dalam_Rupiah','Harga_Jual_Saat_Grosir_2','Minimal_Pembelian_Grosir_3','Laba_Saat_Grosir_3_Dalam_Persen','Laba_Saat_Grosir_3_Dalam_Rupiah','Harga_Jual_Saat_Grosir_3','Catatan','Foto_Produk_1','Foto_Produk_2','Foto_Produk_3','Foto_Produk_4','Foto_Produk_5','Foto_Produk_6','Foto_Produk_7','Foto_Produk_8','Foto_Produk_9','Foto_Video','Posisi_Barang', 'Warning_Stok') Values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}', '{}')".format(self.page3_cti_No, self.page3_cti_SKU_Induk, self.page3_cti_SKU_Varian_1, self.page3_cti_SKU_Varian_2, self.page3_cti_Kode_Toko, self.page3_cti_Barcode_Produk, self.page3_cti_Nama_Produk_Di_Distributor, self.page3_cti_Nama_Produk_Di_Toko, self.page3_cti_Repack, self.page3_cti_Produk_umum_khusus, self.page3_cti_Deskripsi_Produk, self.page3_cti_Total_Stok, self.page3_cti_Total_Stok_Satuan, self.page3_cti_Berat_atau_Volume_Bersih, self.page3_cti_Satuan_Berat_Bersih, self.page3_cti_Berat_Untuk_Pengiriman_Dalam_Gram, self.page3_cti_Kemasan, self.page3_cti_Perizinan, self.page3_cti_Kode_BPOM_atau_PIRT, self.page3_cti_Label_Halal, self.page3_cti_Produsen, self.page3_cti_Distributor, self.page3_cti_Nama_Sales, self.page3_cti_No_Telepon_Sales, self.page3_cti_Harga_Beli_Terakhir, self.page3_cti_Biaya_Penanganan, self.page3_cti_Laba_Dasar_Dalam_Persen, self.page3_cti_Laba_Dasar_Dalam_Rupiah, self.page3_cti_Harga_Jual_Dasar, self.page3_cti_Laba_Saat_Diskon_Dalam_Persen, self.page3_cti_Laba_Saat_Diskon_Dalam_Rupiah, self.page3_cti_Harga_Jual_Saat_Diskon, self.page3_cti_Minimal_Pembelian_Grosir_1, self.page3_cti_Laba_Saat_Grosir_1_Dalam_Persen, self.page3_cti_Laba_Saat_Grosir_1_Dalam_Rupiah, self.page3_cti_Harga_Jual_Saat_Grosir_1, self.page3_cti_Minimal_Pembelian_Grosir_2, self.page3_cti_Laba_Saat_Grosir_2_Dalam_Persen, self.page3_cti_Laba_Saat_Grosir_2_Dalam_Rupiah, self.page3_cti_Harga_Jual_Saat_Grosir_2, self.page3_cti_Minimal_Pembelian_Grosir_3, self.page3_cti_Laba_Saat_Grosir_3_Dalam_Persen, self.page3_cti_Laba_Saat_Grosir_3_Dalam_Rupiah, self.page3_cti_Harga_Jual_Saat_Grosir_3, self.page3_cti_Catatan, self.page3_cti_Foto_Produk_1, self.page3_cti_Foto_Produk_2, self.page3_cti_Foto_Produk_3, self.page3_cti_Foto_Produk_4, self.page3_cti_Foto_Produk_5, self.page3_cti_Foto_Produk_6, self.page3_cti_Foto_Produk_7, self.page3_cti_Foto_Produk_8, self.page3_cti_Foto_Produk_9, self.page3_cti_Foto_Video, self.page3_cti_Posisi_Barang, self.page3_cti_Warning_Stok))

        def Buat_Table_Baru_Di_Database():
            Nomor_Barcode = self.page3_cti_LineEdit_4.text()
            Kolom = '''No text unique,
Kode_Toko text,
Nama_Produk text,
Distributor text,
Nama_Sales text,
Nomor_Telepon_Sales text,
Kode_Produksi text,
Tanggal_Produksi text,
Expired_Date text,
Set_Warning_Sebelum_Expired_Date text,
Kode_Order text unique,
Tanggal_Order text,
Jumlah_Barang_Diorder text,
Jumlah_Barang_Diorder_Satuan text,
Satuan_Terkecil text,
Satuan_Terkecil_Satuan text,
Tanggal_Kedatangan text,
Nomor_Faktur_Dari_Distributor text unique,
Jumlah_Barang_Datang text,
Jumlah_Barang_Datang_Satuan text,
Harga_Beli_Lama_Per_Satuan_Terkecil text,
Harga_Beli_Baru_Per_Satuan_Terkecil_Dasar text,
Harga_Beli_Baru_Per_Satuan_Terkecil_Promo_Distributor text,
Status_Perubahan_Harga_Beli text,
Harga_Beli_Rata_Rata,
Perubahan_Harga_Beli_Rata_Rata,
Biaya_Penanganan,
Laba_Dasar_Dalam_Persen,
Laba_Dasar_Dalam_Rupiah,
Harga_Jual_Dasar,
Laba_Saat_Diskon_Dalam_Persen,
Laba_Saat_Diskon_Dalam_Rupiah,
Harga_Jual_Saat_Diskon,
Grosir_1_Minimal_Pembelian,
Grosir_1_Laba_Dalam_Persen,
Grosir_1_Laba_Dalam_Rupiah,
Grosir_1_Harga_Jual,
Grosir_2_Minimal_Pembelian,
Grosir_2_Laba_Dalam_Persen,
Grosir_2_Laba_Dalam_Rupiah,
Grosir_2_Harga_Jual,
Grosir_3_Minimal_Pembelian,
Grosir_3_Laba_Dalam_Persen,
Grosir_3_Laba_Dalam_Rupiah,
Grosir_3_Harga_Jual,
Total_Transaksi text,
Konsinasi_Atau_Bukan text,
Tipe_Pembayaran text,
Status_Pembayaran text,
Telah_Dibayarkan text,
Belum_Dibayarkan text,
Tipe_Tempo text,
Tanggal_Jatuh_Tempo text,
Status_Return text,
Batas_Waktu_Return_Sebelum_ED text,
Set_Warning_Return_Sebelum_Batas_Waktu_Return text,
Status_Dikembalikan_Ke_Distributor text,
Jumlah_Dikembalikan_Ke_Distributor text,
Jumlah_Dikembalikan_Ke_Distributor_Satuan text,
Nilai_Dikembalikan_Ke_Distributor_Per_Satuan_Terkecil text,
Total_Nilai_Dikembalikan_Ke_Distributor text,
Alasan_Dikembalikan_Ke_Distributor text,
Total_Stok_Sekarang text,
Total_Stok_Sekarang_Satuan text,
Limit_Stok_Bawah text,
Catatan text,
ED_Kurang_Berapa_Hari text,
Terjual text, 
Dipindahkan_Ke_Produk_Repack,
Dipindahkan_Ke_Produk_Repack_Satuan,
Jumlah_Rusak_Hilang_Expired,
Jumlah_Rusak_Hilang_Expired_Satuan,
Alasan_Rusak_Hilang_Expired,
Harga_Beli_Pasaran_Terkini,
Harga_Jual_Pasaran_Terkini,
Harga_Jual_Pandanarum_Terkini,
Tombol_1,
Tombol_2,
Tombol_3,
Tombol_4,
Tombol_5,
Status_Upload_Ke_Marketplace'''
            No = "1"
            KodeToko = self.page3_cti_LineEdit_2.text()
            NamaProduk = self.page3_cti_LineEdit_3.text()
            NamaDistributor = self.page3_cti_LineEdit_9.text()
            NamaSales = self.page3_cti_LineEdit_10.text()
            NomorTeleponSales = self.page3_cti_LineEdit_11.text()
            JumlahBarangDatang = self.page3_cti_LineEdit_37.text()
            JumlahBarangDatangSatuan = self.page3_cti_ComboBox_4.currentText()
            HargaBeliLamaPerSatuanTerkecil = self.page3_cti_LineEdit_13.text()
            HargaBeliBaruPerSatuanTerkecil = self.page3_cti_LineEdit_13.text()
            StatusPerubahanHargaBeli = "0"
            TotalStokSekarang = JumlahBarangDatang
            TotalStokSekarangSatuan = JumlahBarangDatangSatuan
            LimitStokBawah = self.page3_cti_LineEdit_39.text()
            TotalTransaksi = int(JumlahBarangDatang)*int(HargaBeliBaruPerSatuanTerkecil)
            ED_Kurang_Berapa_Hari = ""
            Terjual = "0"
            Dipindahkan_Ke_Produk_Repack = "0"
            Dipindahkan_Ke_Produk_Repack_Satuan = "pcs"
            Jumlah_Rusak_Hilang_Expired = "0"
            Jumlah_Rusak_Hilang_Expired_Satuan = "pcs"
            Alasan_Rusak_Hilang_Expired = "-"
            Harga_Beli_Pasaran_Terkini = ""
            Harga_Jual_Pasaran_Terkini = ""
            Harga_Jual_Pandanarum_Terkini = ""
            Status_Upload_Ke_Marketplace = "Belum Upload"

            # Buat Tabel Baru dengan Barcode yang telah diinput
            self.page3_cti_DBProduk_cursor.execute("CREATE TABLE IF NOT EXISTS '{}'({})".format(str(Nomor_Barcode), Kolom))
            self.page3_cti_DBProduk_connection.commit()
            self.page3_cti_DBProduk_cursor.execute("INSERT INTO '{}' ('No',"
                                                   "'Kode_Toko',"
                                                   "'Nama_Produk',"
                                                   "'Distributor',"
                                                   "'Nama_Sales',"
                                                   "'Nomor_Telepon_Sales',"
                                                   "'Jumlah_Barang_Datang',"
                                                   "'Jumlah_Barang_Datang_Satuan',"
                                                   "'Harga_Beli_Lama_Per_Satuan_Terkecil',"
                                                   "'Harga_Beli_Baru_Per_Satuan_Terkecil_Dasar',"
                                                   "'Status_Perubahan_Harga_Beli',"
                                                   "'Total_Transaksi',"
                                                   "'Total_Stok_Sekarang',"
                                                   "'Total_Stok_Sekarang_Satuan',"
                                                   "'Limit_Stok_Bawah',"
                                                   "'ED_Kurang_Berapa_Hari',"
                                                   "'Terjual',"
                                                   "'Dipindahkan_Ke_Produk_Repack',"
                                                   "'Dipindahkan_Ke_Produk_Repack_Satuan',"
                                                   "'Jumlah_Rusak_Hilang_Expired',"
                                                   "'Jumlah_Rusak_Hilang_Expired_Satuan',"
                                                   "'Alasan_Rusak_Hilang_Expired',"
                                                   "'Harga_Beli_Pasaran_Terkini',"
                                                   "'Harga_Jual_Pasaran_Terkini',"
                                                   "'Harga_Jual_Pandanarum_Terkini',"
                                                   "'Status_Upload_Ke_Marketplace') "
                                                   "VALUES ('{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}',"
                                                   "'{}')".format(str(Nomor_Barcode),
                                                                  str(No),
                                                                  str(KodeToko),
                                                                  str(NamaProduk),
                                                                  str(NamaDistributor),
                                                                  str(NamaSales),
                                                                  str(NomorTeleponSales),
                                                                  str(JumlahBarangDatang),
                                                                  str(JumlahBarangDatangSatuan),
                                                                  str(HargaBeliLamaPerSatuanTerkecil),
                                                                  str(HargaBeliBaruPerSatuanTerkecil),
                                                                  str(StatusPerubahanHargaBeli),
                                                                  str(TotalTransaksi),
                                                                  str(TotalStokSekarang),
                                                                  str(TotalStokSekarangSatuan),
                                                                  str(LimitStokBawah),
                                                                  str(ED_Kurang_Berapa_Hari),
                                                                  str(Terjual),
                                                                  str(Dipindahkan_Ke_Produk_Repack),
                                                                  str(Dipindahkan_Ke_Produk_Repack_Satuan),
                                                                  str(Jumlah_Rusak_Hilang_Expired),
                                                                  str(Jumlah_Rusak_Hilang_Expired_Satuan),
                                                                  str(Alasan_Rusak_Hilang_Expired),
                                                                  str(Harga_Beli_Pasaran_Terkini),
                                                                  str(Harga_Jual_Pasaran_Terkini),
                                                                  str(Harga_Jual_Pandanarum_Terkini),
                                                                  str(Status_Upload_Ke_Marketplace)))

        Buat_Table_Baru_Di_Database()
        self.page3_cti_DBProduk_connection.commit()
        self.page3_cti_DBProduk_connection.close()
        self.Dialog_Simpan.close()
        self.Page3_cti_Cetak_Label_Harga1()
        self.Dialog.close()
        self.Data.page3_pushButton_3.click()
        print(self.Data.page3_tableWidget.rowCount())
        # self.Data.page3_tableWidget.scrollToItem(self.Data.page3_tableWidget.item(self.Data.page3_tableWidget.rowCount(), 1))
        # self.page3_tableWidget.scrollToBottom()
        self.Data.page3_tableWidget.scrollToBottom()

    # Cetak Label Harga (Inisiasi)
    def Page3_cti_Cetak_Label_Harga1(self):
        Barcode = self.page3_cti_LineEdit_4.text()
        Nama_Produk = self.page3_cti_LineEdit_3.text()
        Harga = self.page3_cti_LineEdit_19.text()

        def Rak():
            if len(Barcode) > 0:
                if len(Nama_Produk) > 0:
                    if len(Harga) > 1:
                        Dialog.close()
                        self.Page3_cti_Cetak_Label_Harga2(Barcode, Nama_Produk, Harga)
                    else:
                        Dialog.close()
                        self.Page3_cti_Pesan_Error("Gagal Cetak Harga", "Harga Jual Produk tidak boleh kosong")
                else:
                    Dialog.close()
                    self.Page3_cti_Pesan_Error("Gagal Cetak Harga", "Nama Produk tidak boleh kosong")
            else:
                Dialog.close()
                self.Page3_cti_Pesan_Error("Gagal Cetak Harga", "Barcode Produk tidak boleh kosong")

        def Showcase():
            if len(Barcode) > 0:
                if len(Nama_Produk) > 0:
                    if len(Harga) > 1:
                        Dialog.close()
                        self.Page3_cti_Cetak_Label_Harga3(Barcode, Nama_Produk, Harga)
                    else:
                        Dialog.close()
                        self.Page3_cti_Pesan_Error("Gagal Cetak Harga", "Harga Jual Produk tidak boleh kosong")
                else:
                    Dialog.close()
                    self.Page3_cti_Pesan_Error("Gagal Cetak Harga", "Nama Produk tidak boleh kosong")
            else:
                Dialog.close()
                self.Page3_cti_Pesan_Error("Gagal Cetak Harga", "Barcode Produk tidak boleh kosong")

        Dialog = QtWidgets.QDialog()
        Dialog.setWindowTitle("Cetak Harga")
        Dialog.setModal(True)

        Layout = QtWidgets.QGridLayout(Dialog)
        Text = QtWidgets.QLabel("Pilih ukuran hasil cetak")
        Layout.addWidget(Text, 0, 1, 1, 3)

        PushButton_Showcase = QtWidgets.QPushButton("Showcase")
        Layout.addWidget(PushButton_Showcase, 1, 2)
        PushButton_Showcase.clicked.connect(Showcase)

        PushButton_Rak = QtWidgets.QPushButton("Gondola Rak")
        Layout.addWidget(PushButton_Rak, 1, 3)
        PushButton_Rak.clicked.connect(Rak)

        Dialog.show()
        Dialog.exec_()

    # Cetak Label untuk Rak
    def Page3_cti_Cetak_Label_Harga2(self, Barcode, Nama_Produk, Harga):
        printer = Usb(0x0483, 0x5840, 0, 0x58, 0x03)
        locale.setlocale(locale.LC_ALL, "en_ID")
        NamaProduk = Nama_Produk
        Harga = locale.format_string("%d", int(Harga), grouping=True)

        lebar_cetak = 402
        tinggi_barcode = 100

        code128.image(Barcode, tinggi_barcode).save("{}.png".format(Barcode))
        img = Image.open('{}.png'.format(Barcode))
        wpercent = (lebar_cetak / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((lebar_cetak, hsize), Image.ANTIALIAS)
        img.save("{}.png".format(Barcode))

        printer.set("center", "a", False, 0, width=1, height=1, custom_size=False)
        printer.text("--------------------------------")
        printer.text("\n{}".format(NamaProduk))
        printer.text("\n")
        printer.set("center", "a", True, 0, width=8, height=8, custom_size=True)
        printer.text("\nRp. " + str(Harga) + ",-")
        printer.set("center", "a", False, 0, width=1, height=1, custom_size=False)
        printer.text("\n")
        printer.text("\n({})".format(Barcode))
        printer.text("\n--------------------------------")
        printer.text("\n\n")
        printer.close()

    # Cetak Label untuk Showcase
    def Page3_cti_Cetak_Label_Harga3(self, Barcode, Nama_Produk, harga):
        printer = Usb(0x0483, 0x5840, 0, 0x58, 0x03)
        NamaProduk = Nama_Produk
        locale.setlocale(locale.LC_ALL, "en_ID")
        Harga = locale.format_string("%d", val=int(harga), grouping=True)

        lebar_cetak = 402
        tinggi_barcode = 100

        code128.image(Barcode, tinggi_barcode).save("{}.png".format(Barcode))
        img = Image.open('{}.png'.format(Barcode))
        wpercent = (lebar_cetak / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((lebar_cetak, hsize), Image.ANTIALIAS)
        img.save("{}.png".format(Barcode))

        printer.set("center", "b", False, 0, width=1, height=1, custom_size=False)
        printer.text("\n------------------------------------------")
        printer.text("\n{}".format(NamaProduk))
        printer.set("center", "a", True, 0, width=8, height=8, custom_size=True)
        printer.text("\nRp. " + str(Harga) + ",-")
        printer.set("center", "b", False, 0, width=1, height=1, custom_size=False)
        printer.text("\n({})".format(Barcode))
        printer.text("\n------------------------------------------")
        printer.text("\n\n")
        printer.close()


# Page3_cui = Page3_ClassUbahItem (untuk merubah item dalam database)
class Page3_cui(Page3):
    def __init__(self, data, parent=None):
        super(Page3_cui, self).__init__()
        self.Data = data
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setModal(True)
        self.Dialog.setMinimumSize(500, 600)
        self.Dialog.setWindowTitle("Rubah Produk")
        self.page3_cui_layout = QtWidgets.QVBoxLayout(self.Dialog)
        self.Page3_cui_Label()  # Label pembuka
        self.page3_cui_scrollArea = QtWidgets.QScrollArea()
        self.page3_cui_scrollArea.setWidgetResizable(True)
        self.page3_cui_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.page3_cui_GridLayout_2 = QtWidgets.QGridLayout(self.page3_cui_scrollAreaWidgetContents)
        self.page3_cui_scrollArea.setWidget(self.page3_cui_scrollAreaWidgetContents)
        self.page3_cui_layout.addWidget(self.page3_cui_scrollArea)


        self.Page3_cui_Label_2()        # Label Nomor
        self.Page3_cui_LineEdit()       # LineEdit Nomor
        self.Page3_cui_Label_65()       # Label SKU Induk
        self.Page3_cui_LineEdit_34()    # LineEdit SKU Induk
        self.Page3_cui_Label_66()       # Label SKU Varian 1
        self.Page3_cui_LineEdit_35()    # LineEdit SKU Varian 1
        self.Page3_cui_Label_67()       # Label SKU Varian 2
        self.Page3_cui_LineEdit_36()    # LineEdit SKU Varian 2
        self.Page3_cui_Label_3()        # Label Kode_Toko
        self.Page3_cui_LineEdit_2()     # LineEdit Kode_Toko
        self.Page3_cui_Label_5()        # Label Barcode_Produk
        self.Page3_cui_LineEdit_4()     # LineEdit Barcode_Produk
        self.Page3_cui_Label_6()        # Label Nama Produk di Distributor
        self.Page3_cui_LineEdit_5()     # LineEdit Nama Produk di Distributor
        self.Page3_cui_Label_4()        # Label Nama_Produk
        self.Page3_cui_LineEdit_3()     # LineEdit Nama_Produk
        self.Page3_cui_Label_7()        # Label Deskripsi_Produk
        self.Page3_cui_TextEdit()       # TextEdit Deskripsi_Produk
        self.Page3_cui_Label_68()       # Label Total Stok
        self.Page3_cui_HBoxLayout_19()  # HBoxLayout Total Stok
        self.Page3_cui_LineEdit_37()    # LineEdit Total Stok
        self.Page3_cui_ComboBox_4()     # ComboBox Total Stok Satuan
        self.Page3_cui_Label_73()       # Label Warning Stok
        self.Page3_cui_HBoxLayout_23()  # HBoxLayout Warning Stok
        self.Page3_cui_LineEdit_40()    # LineEdit Warning Stok
        self.Page3_cui_ComboBox_7()     # ComboBox Warning Stok
        self.Page3_cui_Label_69()       # Label Berat/Volume di Kemasan
        self.Page3_cui_HBoxLayout_20()  # HBoxLayout Berat/Volume di Kemasan
        self.Page3_cui_LineEdit_38()    # LineEdit Berat/Volume di Kemasan
        self.Page3_cui_ComboBox_5()     # ComboBox Berat/Volume di Kemasan Satuan
        self.Page3_cui_Label_8()        # Label Berat_Untuk_Pengiriman
        self.Page3_cui_HBoxLayout()     # HBoxLayout Berat_Untuk_Pengiriman
        self.Page3_cui_LineEdit_6()     # LineEdit Berat_Untuk_Pengiriman
        self.Page3_cui_Label_9()        # Label Gram untuk Berat_Untuk_Pengiriman
        self.Page3_cui_Label_10()       # Label Kemasan
        self.Page3_cui_ComboBox()       # ComboBox Kemasan
        self.Page3_cui_Label_11()       # Label Perizinan
        self.Page3_cui_ComboBox_2()     # ComboBox Perizinan
        self.Page3_cui_Label_12()       # Label Kode_BPOM_atau_PIRT
        self.Page3_cui_LineEdit_7()     # LineEdit Kode_BPOM_atau_PIRT
        self.Page3_cui_Label_13()       # Label Label_Halal
        self.Page3_cui_ComboBox_3()     # ComboBox Label_Halal
        self.Page3_cui_Label_14()       # Label Produsen
        self.Page3_cui_LineEdit_8()     # LineEdit Produsen
        self.Page3_cui_Label_15()       # Label Distributor
        self.Page3_cui_LineEdit_9()     # LineEdit Distributor
        self.Page3_cui_Label_16()       # Label Nama_Sales
        self.Page3_cui_LineEdit_10()    # LineEdit Nama_Sales
        self.Page3_cui_Label_17()       # Label Nomor_Telepon_Sales
        self.Page3_cui_LineEdit_11()    # LineEdit Nomor_Telepon_Sales
        self.Page3_cui_Label_18()       # Label Barang Umum / Khusus
        self.Page3_cui_HBoxLayout_21()  # HBoxLayout Barang Umum atau Khusus
        self.Page3_cui_ComboBox_6()     # ComboBox Barang Umum atau Khusus
        self.Page3_cui_SpacerItem()     # SpacerItem
        self.Page3_cui_Label_19()       # Label PENJUALAN
        self.Page3_cui_Label_20()       # Label Harga_Beli_Terakhir_Per_Satuan_Terkecil
        self.Page3_cui_LineEdit_13()    # LineEdit Harga_Beli_Terakhir_Per_Satuan_Terkecil
        self.Page3_cui_Label_70()       # Label_Biaya Penanganan
        self.Page3_cui_HBoxLayout_22()  # HBoxLayout Biaya Penanganan
        self.Page3_cui_Label_71()       # Label "Rp. " Biaya Penanganan
        self.Page3_cui_LineEdit_12()    # LineEdit Biaya Penanganan
        self.Page3_cui_Label_72()       # Label ",-" Biaya Penanganan
        self.Page3_cui_Label_21()       # Label Laba_Dasar (dalam persen dan rupiah)
        self.Page3_cui_HBoxLayout_2()   # HBoxLayout Laba_Dasar (dalam persen dan rupiah)
        self.Page3_cui_LineEdit_14()    # LineEdit % Laba_Dasar (dalam persen dan rupiah)
        self.Page3_cui_Label_22()       # Label % Laba_Dasar (dalam persen dan rupiah)
        self.Page3_cui_Label_23()       # Label "-->" Laba_Dasar (dalam persen dan rupiah)
        self.Page3_cui_Label_24()       # Label " rupiah" Laba_Dasar (dalam persen dan rupiah)
        self.Page3_cui_LineEdit_15()    # LineEdit rupiah Laba_Dasar (dalam persen dan rupiah)
        self.Page3_cui_Label_25()       # Label Harga_Jual_Dasar
        self.Page3_cui_HBoxLayout_3()   # HBoxLayout Harga_Jual_Dasar
        self.Page3_cui_Label_26()       # Label Rupiah Harga_Jual_Dasar
        self.Page3_cui_LineEdit_16()    # LineEdit Harga_Jual_Dasar
        self.Page3_cui_Label_27()       # Label Laba_Saat_Diskon
        self.Page3_cui_HBoxLayout_4()   # HBoxLayout Laba_Saat_Diskon
        self.Page3_cui_LineEdit_17()    # LineEdit Laba_Saat_Diskon (Persen)
        self.Page3_cui_Label_28()       # Label % Laba_Saat_Diskon
        self.Page3_cui_Label_29()       # Label --> Laba_Saat_Diskon
        self.Page3_cui_Label_30()       # Label Rupiah Laba_Saat_Diskon
        self.Page3_cui_LineEdit_18()    # LineEdit Laba_Saat_Diskon (Rupiah)
        self.Page3_cui_Label_31()       # Label Harga_Jual_Saat_Diskon
        self.Page3_cui_HBoxLayout_5()   # HBoxLayout Harga_Jual_Saat_Diskon
        self.Page3_cui_Label_32()       # Label Rupiah Harga_Jual_Saat_Diskon
        self.Page3_cui_LineEdit_19()    # LineEdit Rupiah Harga_Jual_Saat_Diskon
        self.Page3_cui_Label_33()       # Label Grosir_1
        self.Page3_cui_Label_34()       # Label Minimal_Pembelian_Grosir_1
        self.Page3_cui_HBoxLayout_6()   # HBoxLayout Minimal_Pembelian_Grosir_1
        self.Page3_cui_LineEdit_20()    # LineEdit Minimal_Pembelian_Grosir_1
        self.Page3_cui_Label_35()       # Label Satuan Minimal_Pembelian_Grosir_1
        self.Page3_cui_Label_36()       # Label Laba_Saat_Grosir_1
        self.Page3_cui_HBoxLayout_7()   # HBoxLayout Laba_Saat_Grosir_1
        self.Page3_cui_LineEdit_21()    # LineEdit % Laba_Saat_Grosir_1
        self.Page3_cui_Label_37()       # Label % Laba_Saat_Grosir_1
        self.Page3_cui_Label_38()       # Label --> Laba_Saat_Grosir_1
        self.Page3_cui_Label_39()       # Label Rupiah Laba_Saat_Grosir_1
        self.Page3_cui_LineEdit_22()    # LineEdit Rupiah Laba_Saat_Grosir_1
        self.Page3_cui_Label_40()       # Label Harga_Jual_Saat_Grosir_1
        self.Page3_cui_HBoxLayout_8()   # HBoxLayout Harga_Jual_Saat_Grosir_1
        self.Page3_cui_Label_41()       # Label Rupiah Harga_Jual_Saat_Grosir_1
        self.Page3_cui_LineEdit_23()    # LineEdit Rupiah Harga_Jual_Saat_Grosir_1
        self.Page3_cui_Label_42()       # Label Grosir_2
        self.Page3_cui_Label_43()       # Label Minimal_Pembelian_Grosir_2
        self.Page3_cui_HBoxLayout_9()   # HBoxLayout Minimal_Pembelian_Grosir_2
        self.Page3_cui_LineEdit_24()    # LineEdit Minimal_Pembelian_Grosir_2
        self.Page3_cui_Label_44()       # Label Satuan Minimal_Pembelian_Grosir_2
        self.Page3_cui_Label_45()       # Label Laba_Saat_Grosir_2
        self.Page3_cui_HBoxLayout_10()  # HBoxLayout Laba_Saat_Grosir_2
        self.Page3_cui_LineEdit_25()    # LineEdit % Laba_Saat_Grosir_2
        self.Page3_cui_Label_46()       # Label % Laba_Saat_Grosir_2
        self.Page3_cui_Label_47()       # Label --> Laba_Saat_Grosir_2
        self.Page3_cui_Label_48()       # Label Rupiah Laba_Saat_Grosir_2
        self.Page3_cui_LineEdit_26()    # LineEdit Rupiah Laba_Saat_Grosir_2
        self.Page3_cui_Label_49()       # Label Harga_Jual_Saat_Grosir_2
        self.Page3_cui_HBoxLayout_11()  # HBoxLayout Harga_Jual_Saat_Grosir_2
        self.Page3_cui_Label_50()       # Label Rupiah Harga_Jual_Saat_Grosir_2
        self.Page3_cui_LineEdit_27()    # LineEdit Harga_Jual_Saat_Grosir_2
        self.Page3_cui_Label_51()       # Label Grosir_3
        self.Page3_cui_Label_52()       # Label Minimal_Pembelian_Saat_Grosir_3
        self.Page3_cui_HBoxLayout_12()  # HBoxLayout Minimal_Pembelian_Saat_Grosir_3
        self.Page3_cui_LineEdit_28()    # LineEdit Minimal_Pembelian_Saat_Grosir_3
        self.Page3_cui_Label_53()       # Label Pcs Minimal_Pembelian_Saat_Grosir_3
        self.Page3_cui_Label_54()       # Label Laba_Saat_Grosir_3
        self.Page3_cui_HBoxLayout_13()  # HBoxLayout Laba_Saat_Grosir_3
        self.Page3_cui_LineEdit_29()    # LineEdit % Laba_Saat_Grosir_3
        self.Page3_cui_Label_55()       # Label% Laba_Saat_Grosir_3
        self.Page3_cui_Label_56()       # Label --> Laba_Saat_Grosir_3
        self.Page3_cui_Label_57()       # Label Rupiah Laba_Saat_Grosir_3
        self.Page3_cui_LineEdit_30()    # LineEdit Rupiah Laba_Saat_Grosir_3
        self.Page3_cui_Label_58()       # Label Harga_Jual_Saat_Grosir_3
        self.Page3_cui_HBoxLayout_14()  # HBoxLayout Harga_Jual_Saat_Grosir_3
        self.Page3_cui_Label_59()       # Label Rupiah Harga_Jual_Saat_Grosir_3
        self.Page3_cui_LineEdit_31()    # LineEdit Harga_Jual_Saat_Grosir_3
        self.Page3_cui_SpacerItem_2()   # SpacerItem INFORMASI TAMBAHAN
        self.Page3_cui_Label_60()       # Label INFORMASI TAMBAHAN
        self.Page3_cui_Label_61()       # Label Catatan
        self.Page3_cui_TextEdit_2()     # TextEdit Catatan
        self.Page3_cui_Label_63()       # Label Foto_Produk
        self.Page3_cui_HBoxLayout_16()  # HBoxLayout Foto_Produk
        self.Page3_cui_LineEdit_33()    # LineEdit Foto_Produk
        self.Page3_cui_PushButton_3()   # PushButton Tambah Foto_Produk
        self.Page3_cui_PushButton_9()   # PushButton Hapus Foto_Produk
        self.Page3_cui_Label_64()       # Label Gambar Foto_Produk
        self.Page3_cui_HBoxLayout_17()  # HBoxLayout Gambar Foto_Produk
        self.Page3_cui_PushButton_4()   # PushButton Gambar1 Foto_Produk
        self.Page3_cui_PushButton_5()   # PushButton Gambar2 Foto_Produk
        self.Page3_cui_PushButton_6()   # PushButton Gambar3 Foto_Produk
        self.Page3_cui_PushButton_7()   # PushButton Gambar4 Foto_Produk
        self.Page3_cui_PushButton_8()   # PushButton Gambar5 Foto_Produk
        self.Page3_cui_HBoxLayout_18()  # HBoxLayout Gambar5 Foto_Produk Baris Kedua
        self.Page3_cui_PushButton_10()  # PushButton Gambar6 Foto_Produk
        self.Page3_cui_PushButton_11()  # PushButton Gambar7 Foto_Produk
        self.Page3_cui_PushButton_12()  # PushButton Gambar8 Foto_Produk
        self.Page3_cui_PushButton_13()  # PushButton Gambar9 Foto_Produk
        self.Page3_cui_PushButton_14()  # PushButton GambarVid Foto_Produk
        self.Page3_cui_Label_62()       # Label Posisi_Barang
        self.Page3_cui_LineEdit_32()    # LineEdit Posisi_Barang
        self.Page3_cui_HBoxLayout_15()  # HBoxLayout untuk PushButton Batalkan dan Simpan
        self.Page3_cui_Spacer_3()       # Spacer di HBoxLayout (agar tombol rata kanan)
        self.Page3_cui_PushButton()     # PushButton Batalkan
        self.Page3_cui_PushButton_2()   # PushButton Simpan
        self.Page3_cui_PushButton_15()  # PushButton Cetak Label Harga

        # INISIASI
        self.Page3_cui_Mode_Editing() # Aktifkan untuk mode editing script
        self.Page3_cui_Definisikan_Data()
        self.Page3_cui_Database_Load()  # Database_Load
        self.Page3_cui_Nomor_Urut()
        self.Page3_cui_SKU_Induk_Completer()  # Database_Kumpulkan Data Awal SKU_Induk
        self.Page3_cui_Produsen_Completer()
        self.Page3_cui_Distributor_Completer()
        self.Page3_cui_Nama_Sales_Completer()
        self.Page3_cui_No_Telepon_Sales_Completer()
        self.Page3_cui_Keuntungan()
        self.Page3_cui_Hitungan_Biaya_Penanganan()
        self.Page3_cui_Hitungan_Laba_Dasar_Dalam_Persen()
        self.Page3_cui_Hitungan_Laba_Saat_Diskon_Dalam_Persen()
        self.Page3_cui_Hitungan_Laba_Saat_Diskon_Dalam_Rupiah()
        self.Page3_cui_Hitungan_Grosir_1_Minimal_Pembelian()
        self.Page3_cui_Hitungan_Grosir_2_Minimal_Pembelian()
        self.Page3_cui_Hitungan_Grosir_3_Minimal_Pembelian()

        # PERINTAH
        self.page3_cui_LineEdit_34.textChanged.connect(self.Page3_cui_Kode_Produk_Di_Toko)
        self.page3_cui_LineEdit_35.textChanged.connect(self.Page3_cui_Kode_Produk_Di_Toko)
        self.page3_cui_LineEdit_36.textChanged.connect(self.Page3_cui_Kode_Produk_Di_Toko)
        self.page3_cui_LineEdit_2.textChanged.connect(self.Page3_cui_Nama_Produk_Di_Distributor_Completer)
        self.page3_cui_LineEdit_38.textChanged.connect(self.Page3_cui_Berat_Untuk_Pengiriman)
        self.page3_cui_ComboBox_5.currentTextChanged.connect(self.Page3_cui_Berat_Untuk_Pengiriman)
        self.page3_cui_PushButton.clicked.connect(self.Page3_cui_Konfirmasi_Tombol_Batal_klik)
        self.page3_cui_PushButton_2.clicked.connect(self.Page3_cui_PushButton_2_klik)
        self.page3_cui_PushButton_15.clicked.connect(self.Page3_cui_Cetak_Label_Harga1)
        self.page3_cui_PushButton_3.clicked.connect(self.Page3_cui_Tambah_Gambar)
        self.page3_cui_ComboBox_2.currentTextChanged.connect(self.Page3_cui_KodeBPOM_atau_PIRT)
        self.page3_cui_LineEdit_8.textChanged.connect(self.Page3_cui_Distributor_Completer)
        self.page3_cui_LineEdit_8.textChanged.connect(self.Page3_cui_Nama_Sales_Completer)
        self.page3_cui_LineEdit_8.textChanged.connect(self.Page3_cui_No_Telepon_Sales_Completer)
        self.page3_cui_LineEdit_9.textChanged.connect(self.Page3_cui_Nama_Sales_Completer)
        self.page3_cui_LineEdit_9.textChanged.connect(self.Page3_cui_No_Telepon_Sales_Completer)
        self.page3_cui_LineEdit_10.textChanged.connect(self.Page3_cui_No_Telepon_Sales_Completer)
        self.page3_cui_ComboBox_6.currentTextChanged.connect(self.Page3_cui_Keuntungan)
        self.page3_cui_ComboBox_6.currentTextChanged.connect(self.Page3_cui_Hitungan_Laba_Dasar_Dalam_Persen)
        self.page3_cui_ComboBox_6.currentTextChanged.connect(self.Page3_cui_Hitungan_Laba_Saat_Diskon_Dalam_Persen)
        self.page3_cui_ComboBox_6.currentTextChanged.connect(self.Page3_cui_Hitungan_Grosir_1_Laba_Dalam_Persen)
        self.page3_cui_ComboBox_6.currentTextChanged.connect(self.Page3_cui_Hitungan_Grosir_2_Laba_Dalam_Persen)
        self.page3_cui_ComboBox_6.currentTextChanged.connect(self.Page3_cui_Hitungan_Grosir_3_Laba_Dalam_Persen)
        self.page3_cui_LineEdit_13.textChanged.connect(self.Page3_cui_Hitungan_Biaya_Penanganan)
        self.page3_cui_LineEdit_13.textChanged.connect(self.Page3_cui_Hitungan_Laba_Dasar_Dalam_Rupiah)
        self.page3_cui_LineEdit_13.textChanged.connect(self.Page3_cui_Hitungan_Laba_Saat_Diskon_Dalam_Rupiah)
        self.page3_cui_LineEdit_13.textChanged.connect(self.Page3_cui_Hitungan_Grosir_1_Laba_Dalam_Rupiah)
        self.page3_cui_LineEdit_13.textChanged.connect(self.Page3_cui_Hitungan_Grosir_2_Laba_Dalam_Rupiah)
        self.page3_cui_LineEdit_13.textChanged.connect(self.Page3_cui_Hitungan_Grosir_3_Laba_Dalam_Rupiah)

        self.Page3_cui_Cek_Produk_Terpilih()
        self.Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

    # Cek apakah produk telah dipilih atau belum
    def Page3_cui_Cek_Produk_Terpilih(self):
        try:
            Row_Dipilih = self.Data.page3_tableWidget.currentRow()
            Kode_Toko = self.Data.page3_tableWidget.item(Row_Dipilih, 4).text()
            # print(Kode_Toko)
        except:
            self.Page3_cui_Cek_Barcode()
            # print("Anda belum memilih produk yang akan diedit")
        pass

    # Cek apakah produk dengan barcode yang sama telah ada
    def Page3_cui_Cek_Barcode(self):

        DB = DatabaseProduk()
        conn = sqlite3.connect(DB)
        curr = conn.cursor()

        Dialog = QtWidgets.QDialog()
        Dialog.setModal(True)
        Dialog.setWindowTitle("Cek Produk")
        Layout = QtWidgets.QGridLayout(Dialog)

        Label_Text = QtWidgets.QLabel("Masukkan barcode produk akan anda ubah")
        Layout.addWidget(Label_Text, 0, 0, 1, 3)

        LineEdit_Barcode = QtWidgets.QLineEdit()
        Layout.addWidget(LineEdit_Barcode, 1, 0, 1, 3)

        PushButton_Cek = QtWidgets.QPushButton("Rubah")
        Layout.addWidget(PushButton_Cek, 2, 2)

        Barcode = []
        def Database():
            BarcodeList = curr.execute("select Barcode_Produk from Data_Produk_Master").fetchall()
            for item in range(len(BarcodeList)):
                Barcode.append(str(BarcodeList[item][0]).lower())
            if LineEdit_Barcode.text().lower() not in Barcode:
                self.Page3_cui_Pesan_Error("Produk tidak ditemukan", "Data produk dengan Nomor Barcode ini belum dibuat,"
                                                                     "silakan tambahkan Data produk terlebih dahulu")
            elif len(LineEdit_Barcode.text()) == 0:
                LineEdit_Barcode.setFocus()
            else:
                Dialog.close()
                self.Dialog.show()
                self.Dialog.exec_()

        PushButton_Cek.clicked.connect(Database)

        Dialog.show()
        Dialog.exec_()
        conn.close()

    # Label pembuka
    def Page3_cui_Label(self):
        self.page3_cui_Label = QtWidgets.QLabel("FORM TAMBAH PRODUK BARU :")
        self.page3_cui_Label.setObjectName('Label')
        self.page3_cui_layout.addWidget(self.page3_cui_Label)

    # Label Nomor
    def Page3_cui_Label_2(self):
        widget_sebelumnya = None
        if widget_sebelumnya is None:
            pass
        else:
            pass
        self.page3_cui_Label_2 = QtWidgets.QLabel("No : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_2, 0, 0)

    # LineEdit Nomor
    def Page3_cui_LineEdit(self):
        self.page3_cui_LineEdit = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit.setValidator(IntegerValidator())
        self.page3_cui_LineEdit.setReadOnly(True)
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit, 0, 1)

    # Label SKU Induk
    def Page3_cui_Label_65(self):
        self.page3_cui_Label_65 = QtWidgets.QLabel("SKU Induk : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_65, 1, 0)

    # LineEdit SKU Induk
    def Page3_cui_LineEdit_34(self):
        self.page3_cui_LineEdit_34 = QtWidgets.QLineEdit()
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit_34, 1, 1)

    # Label SKU Varian 1
    def Page3_cui_Label_66(self):
        self.page3_cui_Label_66 = QtWidgets.QLabel("SKU Varian 1 : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_66, 2, 0)

    # LineEdit SKU Varian 1
    def Page3_cui_LineEdit_35(self):
        self.page3_cui_LineEdit_35 = QtWidgets.QLineEdit()
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit_35, 2, 1)

    # Label SKU Varian 2
    def Page3_cui_Label_67(self):
        self.page3_cui_Label_67 = QtWidgets.QLabel("SKU Varian 2 : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_67, 3, 0)

    # LineEdit SKU Varian 2
    def Page3_cui_LineEdit_36(self):
        self.page3_cui_LineEdit_36 = QtWidgets.QLineEdit()
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit_36, 3, 1)

    # Label Kode_Toko
    def Page3_cui_Label_3(self):
        self.page3_cui_Label_3 = QtWidgets.QLabel("Kode Produk di Toko : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_3, 4, 0)

    # LineEdit Kode_Toko
    def Page3_cui_LineEdit_2(self):
        self.page3_cui_LineEdit_2 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_2.setReadOnly(True)
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit_2, 4, 1)

    # Label Nama_Produk
    def Page3_cui_Label_4(self):
        self.page3_cui_Label_4 = QtWidgets.QLabel("Nama Produk : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_4, 7, 0)

    # LineEdit Nama_Produk
    def Page3_cui_LineEdit_3(self):
        self.page3_cui_LineEdit_3 = QtWidgets.QLineEdit()
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit_3, 7, 1)

    # Label Barcode_Produk
    def Page3_cui_Label_5(self):
        self.page3_cui_Label_5 = QtWidgets.QLabel("Barcode Produk : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_5, 5, 0)

    # LineEdit Barcode_Produk
    def Page3_cui_LineEdit_4(self):
        self.page3_cui_LineEdit_4 = QtWidgets.QLineEdit()
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit_4, 5, 1)

    # Label Nama Produk di distributor
    def Page3_cui_Label_6(self):
        self.page3_cui_Label_6 = QtWidgets.QLabel("Nama Produk di Distributor : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_6, 6, 0)

    # LineEdit Nama Produk di Distributor
    def Page3_cui_LineEdit_5(self):
        self.page3_cui_LineEdit_5 = QtWidgets.QLineEdit()
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit_5, 6, 1)

    # Label Deskripsi_Produk
    def Page3_cui_Label_7(self):
        self.page3_cui_Label_7 = QtWidgets.QLabel("Deskripsi Produk : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_7, 8, 0)

    # TextEdit Deskripsi_Produk
    def Page3_cui_TextEdit(self):
        self.page3_cui_TextEdit = QtWidgets.QTextEdit()
        self.page3_cui_TextEdit.setPlaceholderText("Optional")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_TextEdit, 8, 1, 3, 1)

    # Label Total Stok
    def Page3_cui_Label_68(self):
        self.page3_cui_Label_68 = QtWidgets.QLabel("Total Stok : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_68, 11, 0)

    # HBoxLayout Total Stok
    def Page3_cui_HBoxLayout_19(self):
        self.page3_cui_HBoxLayout_19 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_19, 11, 1)

    # LineEdit Total Stok
    def Page3_cui_LineEdit_37(self):
        self.page3_cui_LineEdit_37 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_37.setValidator(IntegerValidator())
        self.page3_cui_HBoxLayout_19.addWidget(self.page3_cui_LineEdit_37)

    # ComboBox Total Stok Satuan
    def Page3_cui_ComboBox_4(self):
        self.page3_cui_ComboBox_4 = QtWidgets.QComboBox()
        self.page3_cui_ComboBox_4.addItem("pcs")
        self.page3_cui_HBoxLayout_19.addWidget(self.page3_cui_ComboBox_4)

    # Label Warning Stok
    def Page3_cui_Label_73(self):
        self.page3_cui_Label_73 = QtWidgets.QLabel("Set Warning Stok : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_73, 12, 0)

    # HBbox Layout Warning Stok
    def Page3_cui_HBoxLayout_23(self):
        self.page3_cui_HBoxLayout_23 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_23, 12, 1)

    # LineEdit Warning Stok
    def Page3_cui_LineEdit_40(self):
        self.page3_cui_LineEdit_39 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_39.setValidator(IntegerValidator())
        self.page3_cui_HBoxLayout_23.addWidget(self.page3_cui_LineEdit_39)

    # ComboBox Warning Stok
    def Page3_cui_ComboBox_7(self):
        self.page3_cui_ComboBox_7 = QtWidgets.QComboBox()
        self.page3_cui_ComboBox_7.addItem("pcs", 0)
        self.page3_cui_HBoxLayout_23.addWidget(self.page3_cui_ComboBox_7)



    # Label Berat/Volume di Kemasan
    def Page3_cui_Label_69(self):
        self.page3_cui_Label_69 = QtWidgets.QLabel("Berat/Volume di Kemasan : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_69, 13, 0)

    # HBoxLayout Berat/Volume di Kemasan
    def Page3_cui_HBoxLayout_20(self):
        self.page3_cui_HBoxLayout_20 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_20, 13, 1)

    # LineEdit Berat/Volume di Kemasan
    def Page3_cui_LineEdit_38(self):
        self.page3_cui_LineEdit_38 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_38.setValidator(IntegerValidator())
        self.page3_cui_HBoxLayout_20.addWidget(self.page3_cui_LineEdit_38)

    #  ComboBox Berat/Volume di Kemasan Satuan
    def Page3_cui_ComboBox_5(self):
        self.page3_cui_ComboBox_5 = QtWidgets.QComboBox()
        self.page3_cui_ComboBox_5.addItem("Kilogram")
        self.page3_cui_ComboBox_5.addItem("Gram")
        self.page3_cui_ComboBox_5.addItem("Liter")
        self.page3_cui_ComboBox_5.addItem("mL")
        self.page3_cui_HBoxLayout_20.addWidget(self.page3_cui_ComboBox_5)

    # Label Berat_Untuk_Pengiriman
    def Page3_cui_Label_8(self):
        self.page3_cui_Label_8 = QtWidgets.QLabel("Berat untuk pengiriman : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_8, 14, 0)

    # HBoxLayout Berat_Untuk_Pengiriman
    def Page3_cui_HBoxLayout(self):
        self.page3_cui_HBoxLayout = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout, 14, 1)

    # LineEdit Berat_Untuk_Pengiriman
    def Page3_cui_LineEdit_6(self):
        self.page3_cui_LineEdit_6 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_6.setReadOnly(True)
        self.page3_cui_HBoxLayout.addWidget(self.page3_cui_LineEdit_6)

    # Label Gram untuk Berat_Untuk_Pengiriman
    def Page3_cui_Label_9(self):
        self.page3_cui_Label_9 = QtWidgets.QLabel("Gram")
        self.page3_cui_HBoxLayout.addWidget(self.page3_cui_Label_9)

    # Label Kemasan
    def Page3_cui_Label_10(self):
        self.page3_cui_Label_10 = QtWidgets.QLabel("Kemasan : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_10, 15, 0)

    # ComboBox Kemasan
    def Page3_cui_ComboBox(self):
        self.page3_cui_ComboBox = QtWidgets.QComboBox()
        self.page3_cui_ComboBox.addItem("-", 0)
        self.page3_cui_ComboBox.addItem("Standing Pouch", 1)
        self.page3_cui_ComboBox.addItem("Botol", 2)
        self.page3_cui_ComboBox.addItem("Plastik", 3)
        self.page3_cui_ComboBox.addItem("Sachet", 4)
        self.page3_cui_ComboBox.addItem("Pack", 5)
        self.page3_cui_ComboBox.addItem("Kotak", 6)
        self.page3_cui_ComboBox.addItem("Kaleng", 7)
        self.page3_cui_ComboBox.addItem("Pail", 8)
        self.page3_cui_ComboBox.addItem("Plastik OPP", 9)
        self.page3_cui_ComboBox.addItem("Tanpa Kemasan", 10)
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_ComboBox, 15, 1)

    # Label Perizinan
    def Page3_cui_Label_11(self):
        self.page3_cui_Label_11 = QtWidgets.QLabel("Perizinan : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_11, 16, 0)

    # ComboBox Perizinan
    def Page3_cui_ComboBox_2(self):
        self.page3_cui_ComboBox_2 = QtWidgets.QComboBox()
        self.page3_cui_ComboBox_2.addItem("-", 0)
        self.page3_cui_ComboBox_2.addItem("BPOM", 1)
        self.page3_cui_ComboBox_2.addItem("PIRT", 2)
        self.page3_cui_ComboBox_2.addItem("Tanpa Izin Resmi", 3)
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_ComboBox_2, 16, 1)

    # Label Kode_BPOM_atau_PIRT
    def Page3_cui_Label_12(self):
        self.page3_cui_Label_12 = QtWidgets.QLabel("Kode BPOM atau PIRT : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_12, 17, 0)

    # LineEdit Kode_BPOM_atau_PIRT
    def Page3_cui_LineEdit_7(self):
        self.page3_cui_LineEdit_7 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_7.setDisabled(True)
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit_7, 17, 1)

    # Label Label_Halal
    def Page3_cui_Label_13(self):
        self.page3_cui_Label_13 = QtWidgets.QLabel("Label Halal : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_13, 18, 0)

    # ComboBox Label_Halal
    def Page3_cui_ComboBox_3(self):
        self.page3_cui_ComboBox_3 = QtWidgets.QComboBox()
        self.page3_cui_ComboBox_3.addItem("-", 0)
        self.page3_cui_ComboBox_3.addItem("Ada", 1)
        self.page3_cui_ComboBox_3.addItem("Tidak Ada", 2)
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_ComboBox_3, 18, 1)

    # Label Produsen
    def Page3_cui_Label_14(self):
        self.page3_cui_Label_14 = QtWidgets.QLabel("Produsen : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_14, 19, 0)

    # LineEdit Produsen
    def Page3_cui_LineEdit_8(self):
        self.page3_cui_LineEdit_8 = QtWidgets.QLineEdit()
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit_8, 19, 1)

    # Label Distributor
    def Page3_cui_Label_15(self):
        self.page3_cui_Label_15 = QtWidgets.QLabel("Distributor : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_15, 20, 0)

    # LineEdit Distributor
    def Page3_cui_LineEdit_9(self):
        self.page3_cui_LineEdit_9 = QtWidgets.QLineEdit()
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit_9, 20, 1)

    # Label Nama_Sales
    def Page3_cui_Label_16(self):
        self.page3_cui_Label_16 = QtWidgets.QLabel("Nama Sales : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_16, 21, 0)

    # LineEdit Nama_Sales
    def Page3_cui_LineEdit_10(self):
        self.page3_cui_LineEdit_10 = QtWidgets.QLineEdit()
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit_10, 21, 1)

    # Label Nomor_Telepon_Sales
    def Page3_cui_Label_17(self):
        self.page3_cui_Label_17 = QtWidgets.QLabel("No.Telp Sales : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_17, 22, 0)

    # LineEdit Nomor_Telepon_Sales
    def Page3_cui_LineEdit_11(self):
        self.page3_cui_LineEdit_11 = QtWidgets.QLineEdit()
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit_11, 22, 1)

    # Label Barang Umum atau Khusus
    def Page3_cui_Label_18(self):
        self.page3_cui_Label_18 = QtWidgets.QLabel("Barang Umum/Khusus: ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_18, 23, 0)

    # HBoxLayout Barang Umum atau Khusus
    def Page3_cui_HBoxLayout_21(self):
        self.page3_cui_HBoxLayout_21 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_21, 23, 1)

    # ComboBox Barang Umum atau Khusus
    def Page3_cui_ComboBox_6(self):
        self.page3_cui_ComboBox_6 = QtWidgets.QComboBox()
        self.page3_cui_ComboBox_6.addItem("-")
        self.page3_cui_ComboBox_6.addItem("Umum")
        self.page3_cui_ComboBox_6.addItem("Jarang")
        self.page3_cui_ComboBox_6.addItem("Sangat Jarang")
        self.page3_cui_ComboBox_6.addItem("Produk Sendiri")
        self.page3_cui_HBoxLayout_21.addWidget(self.page3_cui_ComboBox_6)

    # SpacerItem
    def Page3_cui_SpacerItem(self):
        self.page3_cui_SpacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                                          QtWidgets.QSizePolicy.Fixed)
        self.page3_cui_GridLayout_2.addItem(self.page3_cui_SpacerItem, 24, 0)

    # Label PENJUALAN
    def Page3_cui_Label_19(self):
        self.page3_cui_Label_19 = QtWidgets.QLabel("PENJUALAN")
        self.page3_cui_Label_19.setFont(Font(8, True))
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_19, 25, 0)

    # Label Harga_Beli_Terakhir_Per_Satuan_Terkecil
    def Page3_cui_Label_20(self):
        self.page3_cui_Label_20 = QtWidgets.QLabel("Harga Beli Terakhir : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_20, 26, 0)

    # LineEdit Harga_Beli_Terakhir_Per_Satuan_Terkecil
    def Page3_cui_LineEdit_13(self):
        self.page3_cui_LineEdit_13 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_13.setValidator(IntegerValidator())
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit_13, 26, 1)

    # Label Biaya Penanganan
    def Page3_cui_Label_70(self):
        self.page3_cui_Label_70 = QtWidgets.QLabel("Biaya Penanganan : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_70, 27, 0)

    # HBoxLayout Biaya Penanganan
    def Page3_cui_HBoxLayout_22(self):
        self.page3_cui_HBoxLayout_22 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_22, 27, 1)

    # Label "Rp. " Biaya Penanganan
    def Page3_cui_Label_71(self):
        self.page3_cui_Label_71 = QtWidgets.QLabel("Rp. ")
        self.page3_cui_HBoxLayout_22.addWidget(self.page3_cui_Label_71)

    # LineEdit Biaya Penanganan
    def Page3_cui_LineEdit_12(self):
        self.page3_cui_LineEdit_12 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_12.setValidator(IntegerValidator())
        self.page3_cui_HBoxLayout_22.addWidget(self.page3_cui_LineEdit_12)

    # Label ",-" Biaya Penanganan
    def Page3_cui_Label_72(self):
        self.page3_cui_Label_72 = QtWidgets.QLabel(",-")
        self.page3_cui_HBoxLayout_22.addWidget(self.page3_cui_Label_72)

    # Label Laba_Dasar (dalam persen dan rupiah)
    def Page3_cui_Label_21(self):
        self.page3_cui_Label_21 = QtWidgets.QLabel("Laba Dasar : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_21, 28, 0)

    # HBoxLayout Laba_Dasar (dalam persen dan rupiah)
    def Page3_cui_HBoxLayout_2(self):
        self.page3_cui_HBoxLayout_2 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_2, 28, 1)

    # LineEdit % Laba_Dasar (dalam persen dan rupiah)
    def Page3_cui_LineEdit_14(self):
        self.page3_cui_LineEdit_14 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_14.setValidator(FloatValidator())
        self.page3_cui_HBoxLayout_2.addWidget(self.page3_cui_LineEdit_14)

    # Label % Laba_Dasar (dalam persen dan rupiah)
    def Page3_cui_Label_22(self):
        self.page3_cui_Label_22 = QtWidgets.QLabel("%")
        self.page3_cui_HBoxLayout_2.addWidget(self.page3_cui_Label_22)

    # Label "-->" Laba_Dasar (dalam persen dan rupiah)
    def Page3_cui_Label_23(self):
        self.page3_cui_Label_23 = QtWidgets.QLabel("    -->   ")
        self.page3_cui_HBoxLayout_2.addWidget(self.page3_cui_Label_23)

    # LineEdit rupiah Laba_Dasar (dalam persen dan rupiah)
    def Page3_cui_LineEdit_15(self):
        self.page3_cui_LineEdit_15 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_15.setValidator(FloatValidator())
        self.page3_cui_HBoxLayout_2.addWidget(self.page3_cui_LineEdit_15)

    # Label " rupiah" Laba_Dasar (dalam persen dan rupiah)
    def Page3_cui_Label_24(self):
        self.page3_cui_Label_24 = QtWidgets.QLabel(" Rp. ")
        self.page3_cui_HBoxLayout_2.addWidget(self.page3_cui_Label_24)

    # Label Harga_Jual_Dasar
    def Page3_cui_Label_25(self):
        self.page3_cui_Label_25 = QtWidgets.QLabel("Harga Jual Dasar : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_25, 29, 0)

    # HBoxLayout Harga_Jual_Dasar
    def Page3_cui_HBoxLayout_3(self):
        self.page3_cui_HBoxLayout_3 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_3, 29, 1)

    # Label Rupiah Harga_Jual_Dasar
    def Page3_cui_Label_26(self):
        self.page3_cui_Label_26 = QtWidgets.QLabel("Rp. ")
        self.page3_cui_HBoxLayout_3.addWidget(self.page3_cui_Label_26)

    # LineEdit Harga_Jual_Dasar
    def Page3_cui_LineEdit_16(self):
        self.page3_cui_LineEdit_16 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_16.setValidator(IntegerValidator())
        self.page3_cui_LineEdit_16.setReadOnly(True)
        self.page3_cui_HBoxLayout_3.addWidget(self.page3_cui_LineEdit_16)

    # Label Laba_Saat_Diskon
    def Page3_cui_Label_27(self):
        self.page3_cui_Label_27 = QtWidgets.QLabel("Laba Saat Diskon : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_27, 30, 0)

    # HBoxLayout Laba_Saat_Diskon
    def Page3_cui_HBoxLayout_4(self):
        self.page3_cui_HBoxLayout_4 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_4, 30, 1)

    # LineEdit Laba_Saat_Diskon (Persen)
    def Page3_cui_LineEdit_17(self):
        self.page3_cui_LineEdit_17 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_17.setValidator(FloatValidator())
        self.page3_cui_HBoxLayout_4.addWidget(self.page3_cui_LineEdit_17)

    # Label % Laba_Saat_Diskon
    def Page3_cui_Label_28(self):
        self.page3_cui_Label_28 = QtWidgets.QLabel("%")
        self.page3_cui_HBoxLayout_4.addWidget(self.page3_cui_Label_28)

    # Label --> Laba_Saat_Diskon
    def Page3_cui_Label_29(self):
        self.page3_cui_Label_29 = QtWidgets.QLabel("    -->    ")
        self.page3_cui_HBoxLayout_4.addWidget(self.page3_cui_Label_29)

    # Label Rupiah Laba_Saat_Diskon
    def Page3_cui_Label_30(self):
        self.page3_cui_Label_30 = QtWidgets.QLabel("Rp. ")
        self.page3_cui_HBoxLayout_4.addWidget(self.page3_cui_Label_30)

    # LineEdit Laba_Saat_Diskon (Rupiah)
    def Page3_cui_LineEdit_18(self):
        self.page3_cui_LineEdit_18 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_18.setValidator(FloatValidator())
        self.page3_cui_HBoxLayout_4.addWidget(self.page3_cui_LineEdit_18)

    # Label Harga_Jual_Saat_Diskon
    def Page3_cui_Label_31(self):
        self.page3_cui_Label_31 = QtWidgets.QLabel("Harga Jual Saat Diskon : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_31, 31, 0)

    # HBoxLayout Harga_Jual_Saat_Diskon
    def Page3_cui_HBoxLayout_5(self):
        self.page3_cui_HBoxLayout_5 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_5, 31, 1)

    # Label Rupiah Harga_Jual_Saat_Diskon
    def Page3_cui_Label_32(self):
        self.page3_cui_Label_32 = QtWidgets.QLabel("Rp. ")
        self.page3_cui_HBoxLayout_5.addWidget(self.page3_cui_Label_32)

    # LineEdit Rupiah Harga_Jual_Saat_Diskon
    def Page3_cui_LineEdit_19(self):
        self.page3_cui_LineEdit_19 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_19.setValidator(IntegerValidator())
        self.page3_cui_LineEdit_19.setReadOnly(True)
        self.page3_cui_HBoxLayout_5.addWidget(self.page3_cui_LineEdit_19)

    # Label Grosir_1
    def Page3_cui_Label_33(self):
        self.page3_cui_Label_33 = QtWidgets.QLabel("Grosir 1")
        self.page3_cui_Label_33.setFont(Font(8, True))
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_33, 32, 0)

    # Label Minimal_Pembelian_Grosir_1
    def Page3_cui_Label_34(self):
        self.page3_cui_Label_34 = QtWidgets.QLabel("Minimal Pembelian Grosir 1 : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_34, 32, 0)

    # HBoxLayout Minimal_Pembelian_Grosir_1
    def Page3_cui_HBoxLayout_6(self):
        self.page3_cui_HBoxLayout_6 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_6, 33, 1)

    # LineEdit Minimal_Pembelian_Grosir_1
    def Page3_cui_LineEdit_20(self):
        self.page3_cui_LineEdit_20 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_20.setValidator(IntegerValidator())
        self.page3_cui_HBoxLayout_6.addWidget(self.page3_cui_LineEdit_20)

    # Label Satuan Minimal_Pembelian_Grosir_1
    def Page3_cui_Label_35(self):
        self.page3_cui_Label_35 = QtWidgets.QLabel("Pcs")
        self.page3_cui_HBoxLayout_6.addWidget(self.page3_cui_Label_35)

    # Label Laba_Saat_Grosir_1
    def Page3_cui_Label_36(self):
        self.page3_cui_Label_36 = QtWidgets.QLabel("Laba Saat Grosir 1 : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_36, 34, 0)

    # HBoxLayout Laba_Saat_Grosir_1
    def Page3_cui_HBoxLayout_7(self):
        self.page3_cui_HBoxLayout_7 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_7, 34, 1)

    # LineEdit % Laba_Saat_Grosir_1
    def Page3_cui_LineEdit_21(self):
        self.page3_cui_LineEdit_21 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_21.setValidator(FloatValidator())
        self.page3_cui_HBoxLayout_7.addWidget(self.page3_cui_LineEdit_21)

    # Label % Laba_Saat_Grosir_1
    def Page3_cui_Label_37(self):
        self.page3_cui_Label_37 = QtWidgets.QLabel("%")
        self.page3_cui_HBoxLayout_7.addWidget(self.page3_cui_Label_37)

    # Label --> Laba_Saat_Grosir_1
    def Page3_cui_Label_38(self):
        self.page3_cui_Label_38 = QtWidgets.QLabel("    -->    ")
        self.page3_cui_HBoxLayout_7.addWidget(self.page3_cui_Label_38)

    # Label Rupiah Laba_Saat_Grosir_1
    def Page3_cui_Label_39(self):
        self.page3_cui_Label_39 = QtWidgets.QLabel("Rp. ")
        self.page3_cui_HBoxLayout_7.addWidget(self.page3_cui_Label_39)

    # LineEdit Rupiah Laba_Saat_Grosir_1
    def Page3_cui_LineEdit_22(self):
        self.page3_cui_LineEdit_22 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_22.setValidator(FloatValidator())
        self.page3_cui_HBoxLayout_7.addWidget(self.page3_cui_LineEdit_22)

    # Label Harga_Jual_Saat_Grosir_1
    def Page3_cui_Label_40(self):
        self.page3_cui_Label_40 = QtWidgets.QLabel("Harga Jual Saat Grosir 1 : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_40, 35, 0)

    # HBoxLayout Harga_Jual_Saat_Grosir_1
    def Page3_cui_HBoxLayout_8(self):
        self.page3_cui_HBoxLayout_8 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_8, 35, 1)

    # Label Rupiah Harga_Jual_Saat_Grosir_1
    def Page3_cui_Label_41(self):
        self.page3_cui_Label_41 = QtWidgets.QLabel("Rp. ")
        self.page3_cui_HBoxLayout_8.addWidget(self.page3_cui_Label_41)

    # LineEdit Rupiah Harga_Jual_Saat_Grosir_1
    def Page3_cui_LineEdit_23(self):
        self.page3_cui_LineEdit_23 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_23.setValidator(IntegerValidator())
        self.page3_cui_LineEdit_23.setReadOnly(True)
        self.page3_cui_HBoxLayout_8.addWidget(self.page3_cui_LineEdit_23)

    # Label Grosir_2
    def Page3_cui_Label_42(self):
        self.page3_cui_Label_42 = QtWidgets.QLabel("Grosir 2")
        self.page3_cui_Label_42.setFont(Font(8, True))
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_42, 36, 0)

    # Label Minimal_Pembelian_Grosir_2
    def Page3_cui_Label_43(self):
        self.page3_cui_Label_43 = QtWidgets.QLabel("Minimal Pembelian Grosir 2 : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_43, 37, 0)

    # HBoxLayout Minimal_Pembelian_Grosir_2
    def Page3_cui_HBoxLayout_9(self):
        self.page3_cui_HBoxLayout_9 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_9, 37, 1)

    # LineEdit Minimal_Pembelian_Grosir_2
    def Page3_cui_LineEdit_24(self):
        self.page3_cui_LineEdit_24 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_24.setValidator(IntegerValidator())
        self.page3_cui_HBoxLayout_9.addWidget(self.page3_cui_LineEdit_24)

    # Label Satuan Minimal_Pembelian_Grosir_2
    def Page3_cui_Label_44(self):
        self.page3_cui_Label_44 = QtWidgets.QLabel("Pcs")
        self.page3_cui_HBoxLayout_9.addWidget(self.page3_cui_Label_44)

    # Label Laba_Saat_Grosir_2
    def Page3_cui_Label_45(self):
        self.page3_cui_Label_45 = QtWidgets.QLabel("Laba Saat Grosir 2 : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_45, 38, 0)

    # HBoxLayout Laba_Saat_Grosir_2
    def Page3_cui_HBoxLayout_10(self):
        self.page3_cui_HBoxLayout_10 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_10, 38, 1)

    # LineEdit % Laba_Saat_Grosir_2
    def Page3_cui_LineEdit_25(self):
        self.page3_cui_LineEdit_25 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_25.setValidator(FloatValidator())
        self.page3_cui_HBoxLayout_10.addWidget(self.page3_cui_LineEdit_25)

    # Label % Laba_Saat_Grosir_2
    def Page3_cui_Label_46(self):
        self.page3_cui_Label_46 = QtWidgets.QLabel("%")
        self.page3_cui_HBoxLayout_10.addWidget(self.page3_cui_Label_46)

    # Label --> Laba_Saat_Grosir_2
    def Page3_cui_Label_47(self):
        self.page3_cui_Label_47 = QtWidgets.QLabel("    -->    ")
        self.page3_cui_HBoxLayout_10.addWidget(self.page3_cui_Label_47)

    # Label Rupiah Laba_Saat_Grosir_2
    def Page3_cui_Label_48(self):
        self.page3_cui_Label_48 = QtWidgets.QLabel("Rp. ")
        self.page3_cui_HBoxLayout_10.addWidget(self.page3_cui_Label_48)

    # LineEdit Rupiah Laba_Saat_Grosir_2
    def Page3_cui_LineEdit_26(self):
        self.page3_cui_LineEdit_26 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_26.setValidator(FloatValidator())
        self.page3_cui_HBoxLayout_10.addWidget(self.page3_cui_LineEdit_26)

    # Label Harga_Jual_Saat_Grosir_2
    def Page3_cui_Label_49(self):
        self.page3_cui_Label_49 = QtWidgets.QLabel("Harga Jual Saat Grosir 2 : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_49, 39, 0)

    # HBoxLayout Harga_Jual_Saat_Grosir_2
    def Page3_cui_HBoxLayout_11(self):
        self.page3_cui_HBoxLayout_11 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_11, 39, 1)

    # Label Rupiah Harga_Jual_Saat_Grosir_2
    def Page3_cui_Label_50(self):
        self.page3_cui_Label_50 = QtWidgets.QLabel("Rp. ")
        self.page3_cui_HBoxLayout_11.addWidget(self.page3_cui_Label_50)

    # LineEdit Harga_Jual_Saat_Grosir_2
    def Page3_cui_LineEdit_27(self):
        self.page3_cui_LineEdit_27 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_27.setValidator(IntegerValidator())
        self.page3_cui_LineEdit_27.setReadOnly(True)
        self.page3_cui_HBoxLayout_11.addWidget(self.page3_cui_LineEdit_27)

    # Label Grosir_3
    def Page3_cui_Label_51(self):
        self.page3_cui_Label_51 = QtWidgets.QLabel("Grosir 3")
        self.page3_cui_Label_51.setFont(Font(8, True))
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_51, 40, 0)

    # Label Minimal_Pembelian_Saat_Grosir_3
    def Page3_cui_Label_52(self):
        self.page3_cui_Label_52 = QtWidgets.QLabel("Minimal Pembelian Grosir 3 : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_52, 41, 0)

    # HBoxLayout Minimal_Pembelian_Saat_Grosir_3
    def Page3_cui_HBoxLayout_12(self):
        self.page3_cui_HBoxLayout_12 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_12, 41, 1)

    # LineEdit Minimal_Pembelian_Saat_Grosir_3
    def Page3_cui_LineEdit_28(self):
        self.page3_cui_LineEdit_28 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_28.setValidator(IntegerValidator())
        self.page3_cui_HBoxLayout_12.addWidget(self.page3_cui_LineEdit_28)

    # Label Pcs Minimal_Pembelian_Saat_Grosir_3
    def Page3_cui_Label_53(self):
        self.page3_cui_Label_53 = QtWidgets.QLabel("Pcs")
        self.page3_cui_HBoxLayout_12.addWidget(self.page3_cui_Label_53)

    # Label Laba_Saat_Grosir_3
    def Page3_cui_Label_54(self):
        self.page3_cui_Label_54 = QtWidgets.QLabel("Laba Saat Grosir 3 : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_54, 42, 0)

    # HBoxLayout Laba_Saat_Grosir_3
    def Page3_cui_HBoxLayout_13(self):
        self.page3_cui_HBoxLayout_13 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_13, 42, 1)

    # LineEdit % Laba_Saat_Grosir_3
    def Page3_cui_LineEdit_29(self):
        self.page3_cui_LineEdit_29 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_29.setValidator(FloatValidator())
        self.page3_cui_HBoxLayout_13.addWidget(self.page3_cui_LineEdit_29)

    # Label% Laba_Saat_Grosir_3
    def Page3_cui_Label_55(self):
        self.page3_cui_Label_55 = QtWidgets.QLabel("%")
        self.page3_cui_HBoxLayout_13.addWidget(self.page3_cui_Label_55)

    # Label --> Laba_Saat_Grosir_3
    def Page3_cui_Label_56(self):
        self.page3_cui_Label_56 = QtWidgets.QLabel("    -->    ")
        self.page3_cui_HBoxLayout_13.addWidget(self.page3_cui_Label_56)

    # Label Rupiah Laba_Saat_Grosir_3
    def Page3_cui_Label_57(self):
        self.page3_cui_Label_57 = QtWidgets.QLabel("Rp. ")
        self.page3_cui_HBoxLayout_13.addWidget(self.page3_cui_Label_57)

    # LineEdit Rupiah Laba_Saat_Grosir_3
    def Page3_cui_LineEdit_30(self):
        self.page3_cui_LineEdit_30 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_30.setValidator(FloatValidator())
        self.page3_cui_HBoxLayout_13.addWidget(self.page3_cui_LineEdit_30)

    # Label Harga_Jual_Saat_Grosir_3
    def Page3_cui_Label_58(self):
        self.page3_cui_Label_58 = QtWidgets.QLabel("Harga Jual Saat Grosir 3 : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_58, 43, 0)

    # HBoxLayout Harga_Jual_Saat_Grosir_3
    def Page3_cui_HBoxLayout_14(self):
        self.page3_cui_HBoxLayout_14 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_14, 43, 1)

    # Label Rupiah Harga_Jual_Saat_Grosir_3
    def Page3_cui_Label_59(self):
        self.page3_cui_Label_59 = QtWidgets.QLabel("Rp. ")
        self.page3_cui_HBoxLayout_14.addWidget(self.page3_cui_Label_59)

    # LineEdit Harga_Jual_Saat_Grosir_3
    def Page3_cui_LineEdit_31(self):
        self.page3_cui_LineEdit_31 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_31.setValidator(IntegerValidator())
        self.page3_cui_LineEdit_31.setReadOnly(True)
        self.page3_cui_HBoxLayout_14.addWidget(self.page3_cui_LineEdit_31)

    # SpacerItem INFORMASI TAMBAHAN
    def Page3_cui_SpacerItem_2(self):
        self.page3_cui_SpacerItem_2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding,
                                                            QtWidgets.QSizePolicy.Fixed)
        self.page3_cui_GridLayout_2.addItem(self.page3_cui_SpacerItem_2, 44, 0)

    # Label INFORMASI TAMBAHAN
    def Page3_cui_Label_60(self):
        self.page3_cui_Label_60 = QtWidgets.QLabel("INFORMASI TAMBAHAN")
        self.page3_cui_Label_60.setFont(Font(8, True))
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_60, 45, 0)

    # Label Catatan
    def Page3_cui_Label_61(self):
        self.page3_cui_Label_61 = QtWidgets.QLabel("Catatan : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_61, 46, 0)

    # TextEdit Catatan
    def Page3_cui_TextEdit_2(self):
        self.page3_cui_TextEdit_2 = QtWidgets.QTextEdit()
        self.page3_cui_TextEdit_2.setPlaceholderText("Optional")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_TextEdit_2, 46, 1, 3, 1)

    # Label Foto_Produk
    def Page3_cui_Label_63(self):
        self.page3_cui_Label_63 = QtWidgets.QLabel("Foto Produk : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_63, 49, 0)

    # HBoxLayout Foto_Produk
    def Page3_cui_HBoxLayout_16(self):
        self.page3_cui_HBoxLayout_16 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_16, 49, 1)

    # LineEdit Foto_Produk
    def Page3_cui_LineEdit_33(self):
        self.page3_cui_LineEdit_33 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_33.setPlaceholderText("Optional")
        self.page3_cui_HBoxLayout_16.addWidget(self.page3_cui_LineEdit_33)

    # PushButton Tambah Foto_Produk
    def Page3_cui_PushButton_3(self):
        self.page3_cui_PushButton_3 = QtWidgets.QPushButton("Tambah")
        self.page3_cui_HBoxLayout_16.addWidget(self.page3_cui_PushButton_3)

    # PushButton Hapus Foto_Produk
    def Page3_cui_PushButton_9(self):
        self.page3_cui_PushButton_9 = QtWidgets.QPushButton("Hapus")
        self.page3_cui_HBoxLayout_16.addWidget(self.page3_cui_PushButton_9)

    # Label Gambar Foto_Produk
    def Page3_cui_Label_64(self):
        self.page3_cui_Label_64 = QtWidgets.QLabel("Tidak Ada Foto Produk")
        # self.page3_cui_Label_64.setFixedWidth(300)
        self.page3_cui_Label_64.setFixedHeight(250)
        self.page3_cui_Label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.page3_cui_Label_64.setFrameStyle(6)
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_64, 50, 1)

    # HBoxLayout Gambar Foto_Produk
    def Page3_cui_HBoxLayout_17(self):
        self.page3_cui_HBoxLayout_17 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_17, 51, 1)

    # PushButton Gambar1 Foto_Produk
    def Page3_cui_PushButton_4(self):
        self.page3_cui_PushButton_4 = QtWidgets.QPushButton("1")
        self.page3_cui_PushButton_4.setMinimumWidth(50)
        self.page3_cui_HBoxLayout_17.addWidget(self.page3_cui_PushButton_4)

    # PushButton Gambar2 Foto_Produk
    def Page3_cui_PushButton_5(self):
        self.page3_cui_PushButton_5 = QtWidgets.QPushButton("2")
        self.page3_cui_PushButton_5.setMinimumWidth(50)
        self.page3_cui_HBoxLayout_17.addWidget(self.page3_cui_PushButton_5)

    # PushButton Gambar3 Foto_Produk
    def Page3_cui_PushButton_6(self):
        self.page3_cui_PushButton_6 = QtWidgets.QPushButton("3")
        self.page3_cui_PushButton_6.setMinimumWidth(50)
        self.page3_cui_HBoxLayout_17.addWidget(self.page3_cui_PushButton_6)

    # PushButton Gambar4 Foto_Produk
    def Page3_cui_PushButton_7(self):
        self.page3_cui_PushButton_7 = QtWidgets.QPushButton("4")
        self.page3_cui_PushButton_7.setMinimumWidth(50)
        self.page3_cui_HBoxLayout_17.addWidget(self.page3_cui_PushButton_7)

    # PushButton Gambar5 Foto_Produk
    def Page3_cui_PushButton_8(self):
        self.page3_cui_PushButton_8 = QtWidgets.QPushButton("5")
        self.page3_cui_PushButton_8.setMinimumWidth(50)
        self.page3_cui_HBoxLayout_17.addWidget(self.page3_cui_PushButton_8)

    # HBoxLayout Gambar5 Foto_Produk Baris Kedua
    def Page3_cui_HBoxLayout_18(self):
        self.page3_cui_HBoxLayout_18 = QtWidgets.QHBoxLayout()
        self.page3_cui_GridLayout_2.addLayout(self.page3_cui_HBoxLayout_18, 52, 1)

    # PushButton Gambar6 Foto_Produk
    def Page3_cui_PushButton_10(self):
        self.page3_cui_PushButton_10 = QtWidgets.QPushButton("6")
        self.page3_cui_PushButton_10.setMinimumWidth(50)
        self.page3_cui_HBoxLayout_18.addWidget(self.page3_cui_PushButton_10)

    # PushButton Gambar7 Foto_Produk
    def Page3_cui_PushButton_11(self):
        self.page3_cui_PushButton_11 = QtWidgets.QPushButton("7")
        self.page3_cui_PushButton_11.setMinimumWidth(50)
        self.page3_cui_HBoxLayout_18.addWidget(self.page3_cui_PushButton_11)

    # PushButton Gambar8 Foto_Produk
    def Page3_cui_PushButton_12(self):
        self.page3_cui_PushButton_12 = QtWidgets.QPushButton("8")
        self.page3_cui_PushButton_12.setMinimumWidth(50)
        self.page3_cui_HBoxLayout_18.addWidget(self.page3_cui_PushButton_12)

    # PushButton Gambar9 Foto_Produk
    def Page3_cui_PushButton_13(self):
        self.page3_cui_PushButton_13 = QtWidgets.QPushButton("9")
        self.page3_cui_PushButton_13.setMinimumWidth(50)
        self.page3_cui_HBoxLayout_18.addWidget(self.page3_cui_PushButton_13)

    # PushButton GambarVid Foto_Produk
    def Page3_cui_PushButton_14(self):
        self.page3_cui_PushButton_14 = QtWidgets.QPushButton("Video")
        self.page3_cui_PushButton_14.setMinimumWidth(50)
        self.page3_cui_HBoxLayout_18.addWidget(self.page3_cui_PushButton_14)

    # Label Posisi_Barang
    def Page3_cui_Label_62(self):
        self.page3_cui_Label_62 = QtWidgets.QLabel("Posisi Barang : ")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_Label_62, 53, 0)

    # LineEdit Posisi_Barang
    def Page3_cui_LineEdit_32(self):
        self.page3_cui_LineEdit_32 = QtWidgets.QLineEdit()
        self.page3_cui_LineEdit_32.setPlaceholderText("Optional")
        self.page3_cui_GridLayout_2.addWidget(self.page3_cui_LineEdit_32, 53, 1)

    # HBoxLayout untuk PushButton Batalkan dan Simpan
    def Page3_cui_HBoxLayout_15(self):
        self.page3_cui_HBoxLayout_15 = QtWidgets.QHBoxLayout()
        self.page3_cui_layout.addLayout(self.page3_cui_HBoxLayout_15)

    # Spacer di HBoxLayout (agar tombol rata kanan)
    def Page3_cui_Spacer_3(self):
        self.page3_cui_Spacer_3 = QtWidgets.QSpacerItem(20, 20,
                                                        QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Fixed)
        self.page3_cui_HBoxLayout_15.addItem(self.page3_cui_Spacer_3)

    # PushButton Batalkan
    def Page3_cui_PushButton(self):
        self.page3_cui_PushButton = QtWidgets.QPushButton("Batal")
        self.page3_cui_PushButton.setObjectName('page3_cui_PushButton')
        self.page3_cui_HBoxLayout_15.addWidget(self.page3_cui_PushButton)

    # PushButton Simpan
    def Page3_cui_PushButton_2(self):
        self.page3_cui_PushButton_2 = QtWidgets.QPushButton("Simpan")
        self.page3_cui_PushButton_2.setObjectName('page3_cui_PushButton_2')
        self.page3_cui_PushButton_2.setDefault(True)
        self.page3_cui_HBoxLayout_15.addWidget(self.page3_cui_PushButton_2)

    # PushButton Cetak Label Harga
    def Page3_cui_PushButton_15(self):
        self.page3_cui_PushButton_15 = QtWidgets.QPushButton("Cetak Harga")
        self.page3_cui_HBoxLayout_15.addWidget(self.page3_cui_PushButton_15)

    # LineEdit Terpakai :       Page3_cui_LineEdit_39
    # Label Terpakai :          Page3_cui_Label_73
    # HBoxLayout Terpakai :     Page3_cui_HBoxLayout_23
    # TextEdit Terpakai :       Page3_cui_TextEdit_2
    # SpacerItem Terpakai :     Page3_cui_SpacerItem_3
    # PushButton Terpakai :     Page3_cui_PushButton_10
    # ComboBox Terpakai :       Page3_cui_ComboBox_7

    # INISIALISASI
    # Aktifkan untuk mode editing script
    def Page3_cui_Mode_Editing(self):
        self.page3_cui_LineEdit.setPlaceholderText("page3_cui_LineEdit")
        self.page3_cui_LineEdit_34.setPlaceholderText("page3_cui_LineEdit_34")
        self.page3_cui_LineEdit_35.setPlaceholderText("page3_cui_LineEdit_35")
        self.page3_cui_LineEdit_36.setPlaceholderText("page3_cui_LineEdit_36")
        self.page3_cui_LineEdit_2.setPlaceholderText("page3_cui_LineEdit_2")
        self.page3_cui_LineEdit_3.setPlaceholderText("page3_cui_LineEdit_3")
        self.page3_cui_LineEdit_4.setPlaceholderText("page3_cui_LineEdit_4")
        self.page3_cui_LineEdit_5.setPlaceholderText("page3_cui_LineEdit_5")
        self.page3_cui_TextEdit.setPlaceholderText("page3_cui_TextEdit")
        self.page3_cui_LineEdit_37.setPlaceholderText("page3_cui_LineEdit_37")
        self.page3_cui_LineEdit_38.setPlaceholderText("page3_cui_LineEdit_38")
        self.page3_cui_LineEdit_6.setPlaceholderText("page3_cui_LineEdit_6")
        self.page3_cui_LineEdit_7.setPlaceholderText("page3_cui_LineEdit_7")
        self.page3_cui_LineEdit_8.setPlaceholderText("page3_cui_LineEdit_8")
        self.page3_cui_LineEdit_9.setPlaceholderText("page3_cui_LineEdit_9")
        self.page3_cui_LineEdit_10.setPlaceholderText("page3_cui_LineEdit_10")
        self.page3_cui_LineEdit_11.setPlaceholderText("page3_cui_LineEdit_11")
        self.page3_cui_LineEdit_13.setPlaceholderText("page3_cui_LineEdit_13")
        self.page3_cui_LineEdit_12.setPlaceholderText("page3_cui_LineEdit_12")
        self.page3_cui_LineEdit_14.setPlaceholderText("page3_cui_LineEdit_14")
        self.page3_cui_LineEdit_15.setPlaceholderText("page3_cui_LineEdit_15")
        self.page3_cui_LineEdit_16.setPlaceholderText("page3_cui_LineEdit_16")
        self.page3_cui_LineEdit_17.setPlaceholderText("page3_cui_LineEdit_17")
        self.page3_cui_LineEdit_18.setPlaceholderText("page3_cui_LineEdit_18")
        self.page3_cui_LineEdit_19.setPlaceholderText("page3_cui_LineEdit_19")
        self.page3_cui_LineEdit_20.setPlaceholderText("page3_cui_LineEdit_20")
        self.page3_cui_LineEdit_21.setPlaceholderText("page3_cui_LineEdit_21")
        self.page3_cui_LineEdit_22.setPlaceholderText("page3_cui_LineEdit_22")
        self.page3_cui_LineEdit_23.setPlaceholderText("page3_cui_LineEdit_23")
        self.page3_cui_LineEdit_24.setPlaceholderText("page3_cui_LineEdit_24")
        self.page3_cui_LineEdit_25.setPlaceholderText("page3_cui_LineEdit_25")
        self.page3_cui_LineEdit_26.setPlaceholderText("page3_cui_LineEdit_26")
        self.page3_cui_LineEdit_27.setPlaceholderText("page3_cui_LineEdit_27")
        self.page3_cui_LineEdit_28.setPlaceholderText("page3_cui_LineEdit_28")
        self.page3_cui_LineEdit_29.setPlaceholderText("page3_cui_LineEdit_29")
        self.page3_cui_LineEdit_30.setPlaceholderText("page3_cui_LineEdit_30")
        self.page3_cui_LineEdit_31.setPlaceholderText("page3_cui_LineEdit_31")
        self.page3_cui_TextEdit_2.setPlaceholderText("page3_cui_TextEdit_2")
        self.page3_cui_LineEdit_33.setPlaceholderText("page3_cui_LineEdit_33")
        self.page3_cui_LineEdit_32.setPlaceholderText("page3_cui_LineEdit_32")
        self.page3_cui_LineEdit_39.setPlaceholderText("page3_cui_LineEdit_39")
        pass

    # Definisikan data yang akan diambil
    def Page3_cui_Definisikan_Data(self):
        self.page3_cui_No = ""
        self.page3_cui_No_terpakai = []
        self.page3_cui_SKU_Induk = ""
        self.page3_cui_SKU_Induk_terpakai = []
        self.page3_cui_SKU_Varian_1 = ""
        self.page3_cui_SKU_Varian_1_terpakai = []
        self.page3_cui_SKU_Varian_2 = ""
        self.page3_cui_SKU_Varian_2_terpakai = []
        self.page3_cui_Kode_Toko = ""
        self.page3_cui_Barcode_Produk = ""
        self.page3_cui_Nama_Produk_Di_Distributor = ""
        self.page3_cui_Nama_Produk_Di_Distributor_terpakai = []
        self.page3_cui_Nama_Produk_Di_Toko = ""
        self.page3_cui_Repack = ""
        self.page3_cui_Produk_umum_khusus = ""
        self.page3_cui_Deskripsi_Produk = ""
        self.page3_cui_Total_Stok = ""
        self.page3_cui_Total_Stok_Satuan = ""
        self.page3_cui_Warning_Stok = ""
        self.page3_cui_Berat_atau_Volume_Bersih = ""
        self.page3_cui_Satuan_Berat_Bersih = ""
        self.page3_cui_Berat_Untuk_Pengiriman_Dalam_Gram = ""
        self.page3_cui_Kemasan = ""
        self.page3_cui_Perizinan = ""
        self.page3_cui_Kode_BPOM_atau_PIRT = ""
        self.page3_cui_Label_Halal = ""
        self.page3_cui_Produsen = ""
        self.page3_cui_Produsen_terpakai = []
        self.page3_cui_Distributor = ""
        self.page3_cui_Distributor_terpakai = []
        self.page3_cui_Nama_Sales = ""
        self.page3_cui_Nama_Sales_terpakai = []
        self.page3_cui_No_Telepon_Sales = ""
        self.page3_cui_No_Telepon_Sales_terpakai = []
        self.page3_cui_Harga_Beli_Terakhir = ""
        self.page3_cui_Biaya_Penanganan = ""
        self.page3_cui_Laba_Dasar_Dalam_Persen = ""
        self.page3_cui_Laba_Dasar_Dalam_Rupiah = ""
        self.page3_cui_Harga_Jual_Dasar = ""
        self.page3_cui_Laba_Saat_Diskon_Dalam_Persen = ""
        self.page3_cui_Laba_Saat_Diskon_Dalam_Rupiah = ""
        self.page3_cui_Harga_Jual_Saat_Diskon = ""
        self.page3_cui_Minimal_Pembelian_Grosir_1 = ""
        self.page3_cui_Laba_Saat_Grosir_1_Dalam_Persen = ""
        self.page3_cui_Laba_Saat_Grosir_1_Dalam_Rupiah = ""
        self.page3_cui_Harga_Jual_Saat_Grosir_1 = ""
        self.page3_cui_Minimal_Pembelian_Grosir_2 = ""
        self.page3_cui_Laba_Saat_Grosir_2_Dalam_Persen = ""
        self.page3_cui_Laba_Saat_Grosir_2_Dalam_Rupiah = ""
        self.page3_cui_Harga_Jual_Saat_Grosir_2 = ""
        self.page3_cui_Minimal_Pembelian_Grosir_3 = ""
        self.page3_cui_Laba_Saat_Grosir_3_Dalam_Persen = ""
        self.page3_cui_Laba_Saat_Grosir_3_Dalam_Rupiah = ""
        self.page3_cui_Harga_Jual_Saat_Grosir_3 = ""
        self.page3_cui_Catatan = ""
        self.page3_cui_Foto_Produk1 = ""
        self.page3_cui_Foto_Produk_2 = ""
        self.page3_cui_Foto_Produk_3 = ""
        self.page3_cui_Foto_Produk_4 = ""
        self.page3_cui_Foto_Produk_5 = ""
        self.page3_cui_Foto_Produk_6 = ""
        self.page3_cui_Foto_Produk_7 = ""
        self.page3_cui_Foto_Produk_8 = ""
        self.page3_cui_Foto_Produk_9 = ""
        self.page3_cui_Foto_Video = ""
        self.page3_cui_Posisi_Barang = ""

    # Database_Load
    def Page3_cui_Database_Load(self):
        database = DatabaseProduk()
        self.page3_cui_DBProduk_connection = sqlite3.connect(database)
        self.page3_cui_DBProduk_connection.row_factory = sqlite3.Row
        self.page3_cui_DBProduk_cursor = self.page3_cui_DBProduk_connection.cursor()

    # Definisikan Nomor Urut
    def Page3_cui_Nomor_Urut(self):
        # Definisikan nomor urut di database yang belum terpakai
        Load_No_terpakai = self.page3_cui_DBProduk_cursor.execute("select No from Data_Produk_Master").fetchall()
        for item in range(len(Load_No_terpakai)):
            self.page3_cui_No_terpakai.append(int(Load_No_terpakai[item]["No"]))
        No_belum_terpakai = 1
        while No_belum_terpakai in self.page3_cui_No_terpakai:
            No_belum_terpakai += 1
        else:
            self.page3_cui_LineEdit.setText(str(No_belum_terpakai))

    # Definisikan Completer SKU_Induk
    def Page3_cui_SKU_Induk_Completer(self):
        Load_SKU_Induk_terpakai = self.page3_cui_DBProduk_cursor.execute("select SKU_Induk from Data_Produk_Master").fetchall()
        for item in range(len(Load_SKU_Induk_terpakai)):
            if Load_SKU_Induk_terpakai[item]["SKU_Induk"] not in self.page3_cui_SKU_Induk_terpakai:
                self.page3_cui_SKU_Induk_terpakai.append((Load_SKU_Induk_terpakai[item]["SKU_Induk"]))
            else:
                pass
        SKU_Induk_completer = QtWidgets.QCompleter(self.page3_cui_SKU_Induk_terpakai)
        SKU_Induk_completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        SKU_Induk_completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cui_LineEdit_34.setCompleter(SKU_Induk_completer)

        SKU_Induk_completer.activated.connect(self.Page3_cui_SKU_Varian_1_Completer)

    # Definisikan Completer SKU_Varian_1
    def Page3_cui_SKU_Varian_1_Completer(self):
        self.page3_cui_SKU_Varian_1_terpakai.clear()
        self.page3_cui_SKU_Varian_2_terpakai.clear()
        self.page3_cui_LineEdit_35.clear()
        self.page3_cui_LineEdit_36.clear()
        SKU_Varian1_item = self.page3_cui_DBProduk_cursor.execute("select SKU_Varian_1 from Data_Produk_Master where SKU_Induk='{}'".format(self.page3_cui_LineEdit_34.text())).fetchall()
        for item in range(len(SKU_Varian1_item)):
            if SKU_Varian1_item[item]["SKU_Varian_1"] not in self.page3_cui_SKU_Varian_1_terpakai:
                self.page3_cui_SKU_Varian_1_terpakai.append(SKU_Varian1_item[item]["SKU_Varian_1"])
            else:
                pass
        SKU_Varian_1_Completer = QtWidgets.QCompleter(self.page3_cui_SKU_Varian_1_terpakai)
        SKU_Varian_1_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        SKU_Varian_1_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cui_LineEdit_35.setCompleter(SKU_Varian_1_Completer)
        SKU_Varian_1_Completer.activated.connect(self.Page3_cui_SKU_Varian_2_Completer)

    # Definisikan Completer SKU_Varian_2
    def Page3_cui_SKU_Varian_2_Completer(self):
        self.page3_cui_SKU_Varian_2_terpakai.clear()
        self.page3_cui_LineEdit_36.clear()
        SKU_Varian2_item = self.page3_cui_DBProduk_cursor.execute("select SKU_Varian_2 from Data_Produk_Master where SKU_Induk='{}'".format(self.page3_cui_LineEdit_34.text())).fetchall()
        for item in range(len(SKU_Varian2_item)):
            if SKU_Varian2_item[item]["SKU_Varian_2"] not in self.page3_cui_SKU_Varian_2_terpakai:
                self.page3_cui_SKU_Varian_2_terpakai.append(SKU_Varian2_item[item]["SKU_Varian_2"])
            else:
                pass
        SKU_Varian_2_Completer = QtWidgets.QCompleter(self.page3_cui_SKU_Varian_2_terpakai)
        SKU_Varian_2_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        SKU_Varian_2_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cui_LineEdit_36.setCompleter(SKU_Varian_2_Completer)

    # Definisikan Kode Produk Di Toko
    def Page3_cui_Kode_Produk_Di_Toko(self):
        text = str(self.page3_cui_LineEdit_34.text()) + str(self.page3_cui_LineEdit_35.text()) + str(self.page3_cui_LineEdit_36.text())
        self.page3_cui_LineEdit_2.setText(text)

    # Definisikan Nama Produk di Distributor
    def Page3_cui_Nama_Produk_Di_Distributor_Completer(self):
        self.page3_cui_Nama_Produk_Di_Distributor_terpakai.clear()
        self.page3_cui_LineEdit_5.clear()
        Nama_Produk_Di_Distributor_item = self.page3_cui_DBProduk_cursor.execute("select Nama_Produk_Di_Distributor from Data_Produk_Master where Kode_Toko='{}'".format(self.page3_cui_LineEdit_2.text())).fetchall()
        for item in range(len(Nama_Produk_Di_Distributor_item)):
            self.page3_cui_Nama_Produk_Di_Distributor_terpakai.append(Nama_Produk_Di_Distributor_item[item]["Nama_Produk_Di_Distributor"])
        Nama_Produk_Di_Distributor_Completer = QtWidgets.QCompleter(self.page3_cui_Nama_Produk_Di_Distributor_terpakai)
        Nama_Produk_Di_Distributor_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        Nama_Produk_Di_Distributor_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cui_LineEdit_5.setCompleter(Nama_Produk_Di_Distributor_Completer)

    # Operasi Hitungan Berat Untuk Pengiriman
    def Page3_cui_Berat_Untuk_Pengiriman(self):
        Pengali = 1
        Berat_atau_Volume_Produk = self.page3_cui_LineEdit_38.text()
        Berat_atau_Volume_Produk_Satuan = self.page3_cui_ComboBox_5.currentText()
        if Berat_atau_Volume_Produk_Satuan == "Kilogram":
            Pengali = 1000
        elif Berat_atau_Volume_Produk_Satuan == "Liter":
            Pengali = 1000
        else:
            pass

        try:
            Berat_dalam_gram = float(self.page3_cui_LineEdit_38.text()) * Pengali
            if Berat_dalam_gram >= 10:
                Berat_Untuk_Pengiriman = float(Berat_dalam_gram) + ((float(Berat_dalam_gram))*10)/100
                self.page3_cui_LineEdit_6.setText(str(int(Berat_Untuk_Pengiriman)))
            else:
                Berat_Untuk_Pengiriman = float(Berat_dalam_gram) + ((float(Berat_dalam_gram)) * 10) / 100 + 2
                self.page3_cui_LineEdit_6.setText(str(int(Berat_Untuk_Pengiriman)))
        except:
            self.page3_cui_LineEdit_6.clear()
            pass

    # Operasi Kode BPOM atau PIRT
    def Page3_cui_KodeBPOM_atau_PIRT(self):
        Jenis_Perizinan = self.page3_cui_ComboBox_2.currentText()
        if Jenis_Perizinan == "BPOM":
            self.page3_cui_LineEdit_7.clear()
            self.page3_cui_LineEdit_7.setEnabled(True)
        elif Jenis_Perizinan == "PIRT":
            self.page3_cui_LineEdit_7.clear()
            self.page3_cui_LineEdit_7.setEnabled(True)
        else:
            self.page3_cui_LineEdit_7.clear()
            self.page3_cui_LineEdit_7.setText("Tidak ada izin resmi")
            self.page3_cui_LineEdit_7.setDisabled(True)
            pass

    # Produsen Completer
    def Page3_cui_Produsen_Completer(self):
        self.page3_cui_Produsen_terpakai.clear()
        Daftar_Produsen = self.page3_cui_DBProduk_cursor.execute("select Produsen from Data_Produk_Master").fetchall()
        for item in range(len(Daftar_Produsen)):
            if Daftar_Produsen[item]["Produsen"] not in self.page3_cui_Produsen_terpakai:
                self.page3_cui_Produsen_terpakai.append(Daftar_Produsen[item]["Produsen"])
            else:
                pass

        Daftar_Produsen_Completer = QtWidgets.QCompleter(self.page3_cui_Produsen_terpakai)
        Daftar_Produsen_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        Daftar_Produsen_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cui_LineEdit_8.setCompleter(Daftar_Produsen_Completer)

    # Distributor Completer
    def Page3_cui_Distributor_Completer(self):
        self.page3_cui_Distributor_terpakai.clear()
        self.page3_cui_LineEdit_9.clear()
        Daftar_Distributor = self.page3_cui_DBProduk_cursor.execute("select Distributor from Data_Produk_Master where Produsen='{}'".format(self.page3_cui_LineEdit_8.text())).fetchall()
        for item in range(len(Daftar_Distributor)):
            if Daftar_Distributor[item]["Distributor"] not in self.page3_cui_Distributor_terpakai:
                self.page3_cui_Distributor_terpakai.append(Daftar_Distributor[item]["Distributor"])
            else:
                pass

        Daftar_Distributor_Completer = QtWidgets.QCompleter(self.page3_cui_Distributor_terpakai)
        Daftar_Distributor_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        Daftar_Distributor_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cui_LineEdit_9.setCompleter(Daftar_Distributor_Completer)

    # Nama Sales Completer
    def Page3_cui_Nama_Sales_Completer(self):
        self.page3_cui_Nama_Sales_terpakai.clear()
        self.page3_cui_LineEdit_10.clear()
        Daftar_Nama_Sales = self.page3_cui_DBProduk_cursor.execute("select Nama_Sales from Data_Produk_Master where Distributor='{}'".format(self.page3_cui_LineEdit_9.text())).fetchall()
        for item in range(len(Daftar_Nama_Sales)):
            if Daftar_Nama_Sales[item]["Nama_Sales"] not in self.page3_cui_Nama_Sales_terpakai:
                self.page3_cui_Nama_Sales_terpakai.append(Daftar_Nama_Sales[item]["Nama_Sales"])
            else:
                pass

        Daftar_Nama_Sales_Completer = QtWidgets.QCompleter(self.page3_cui_Nama_Sales_terpakai)
        Daftar_Nama_Sales_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        Daftar_Nama_Sales_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cui_LineEdit_10.setCompleter(Daftar_Nama_Sales_Completer)

    # No Telepon Sales Completer
    def Page3_cui_No_Telepon_Sales_Completer(self):
        self.page3_cui_No_Telepon_Sales_terpakai.clear()
        self.page3_cui_LineEdit_11.clear()
        Daftar_No_Telepon_Sales = self.page3_cui_DBProduk_cursor.execute("select No_Telepon_Sales from Data_Produk_Master where Nama_Sales='{}'".format(self.page3_cui_LineEdit_10.text())).fetchall()
        try:
            No_Telepon_Sales = Daftar_No_Telepon_Sales[0]["No_Telepon_Sales"]
        except:
            No_Telepon_Sales = ""
        for item in range(len(Daftar_No_Telepon_Sales)):
            if Daftar_No_Telepon_Sales[item]["No_Telepon_Sales"] not in self.page3_cui_No_Telepon_Sales_terpakai:
                self.page3_cui_No_Telepon_Sales_terpakai.append(Daftar_No_Telepon_Sales[item]["No_Telepon_Sales"])
            else:
                pass
        self.page3_cui_LineEdit_11.setText(str(No_Telepon_Sales))
        Daftar_No_Telepon_Sales_Completer = QtWidgets.QCompleter(self.page3_cui_No_Telepon_Sales_terpakai)
        Daftar_No_Telepon_Sales_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        Daftar_No_Telepon_Sales_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_cui_LineEdit_11.setCompleter(Daftar_No_Telepon_Sales_Completer)

    # Definisikan Keuntungan
    def Page3_cui_Keuntungan(self):
        self.page3_cui_LineEdit_14.clear()
        if self.page3_cui_ComboBox_6.currentText() == "Umum":
            self.laba_dasar = 7
        elif self.page3_cui_ComboBox_6.currentText() == "Jarang":
            self.laba_dasar = 8
        elif self.page3_cui_ComboBox_6.currentText() == "Sangat Jarang":
            self.laba_dasar = 9
        elif self.page3_cui_ComboBox_6.currentText() == "Produk Sendiri":
            self.laba_dasar = 10
        else:
            self.laba_dasar = 9
            self.page3_cui_LineEdit_14.setText("0")
        self.laba_diskon = self.laba_dasar - 1
        self.laba_grosir_1 = self.laba_dasar - 2
        self.laba_grosir_2 = self.laba_dasar - 3
        self.laba_grosir_3 = self.laba_dasar - 4

    # Hitungan Biaya Penanganan
    def Page3_cui_Hitungan_Biaya_Penanganan(self):
        self.page3_cui_LineEdit_12.clear()
        try:
            Harga_Beli_Terakhir = int(self.page3_cui_LineEdit_13.text())
        except:
            Harga_Beli_Terakhir = 0

        Biaya_Penanganan_Dasar = 100
        if int(Harga_Beli_Terakhir) == 0:
            Biaya_Penanganan = 0
        elif int(Harga_Beli_Terakhir) <= 5000:
            Biaya_Penanganan = Biaya_Penanganan_Dasar * 1
        elif int(Harga_Beli_Terakhir) <= 10000:
            Biaya_Penanganan = Biaya_Penanganan_Dasar * 2
        elif int(Harga_Beli_Terakhir) <= 50000:
            Biaya_Penanganan = Biaya_Penanganan_Dasar * 4
        elif int(Harga_Beli_Terakhir) <= 100000:
            Biaya_Penanganan = Biaya_Penanganan_Dasar * 8
        elif int(Harga_Beli_Terakhir) <= 200000:
            Biaya_Penanganan = Biaya_Penanganan_Dasar * 16
        elif int(Harga_Beli_Terakhir) <= 400000:
            Biaya_Penanganan = Biaya_Penanganan_Dasar * 32
        elif int(Harga_Beli_Terakhir) > 400000:
            Biaya_Penanganan = Biaya_Penanganan_Dasar * 64
        else:
            Biaya_Penanganan = Biaya_Penanganan_Dasar
            pass

        self.page3_cui_LineEdit_12.setText(str(Biaya_Penanganan))

    # Hitungan Laba_Dasar_Dalam_Persen
    def Page3_cui_Hitungan_Laba_Dasar_Dalam_Persen(self):
        self.page3_cui_LineEdit_14.setText(str(self.laba_dasar))
        self.Page3_cui_Hitungan_Laba_Dasar_Dalam_Rupiah()
        self.page3_cui_LineEdit_14.textChanged.connect(self.Page3_cui_Hitungan_Laba_Dasar_Dalam_Rupiah)

    # Hitungan Laba_Dasar_Dalam_Rupiah
    def Page3_cui_Hitungan_Laba_Dasar_Dalam_Rupiah(self):
        try:
            self.page3_cui_LineEdit_15.clear()
            Harga_Beli_Terakhir = int(self.page3_cui_LineEdit_13.text())
            Laba_Dasar_Dalam_Persen = int(self.page3_cui_LineEdit_14.text())
            Laba_Dasar_Dalam_Rupiah = int((Laba_Dasar_Dalam_Persen/100)*Harga_Beli_Terakhir)
            self.page3_cui_LineEdit_15.setText(str(Laba_Dasar_Dalam_Rupiah))
        except:
            self.page3_cui_LineEdit_15.setText("error")
        self.Page3_cui_Hitungan_Harga_Jual_Dasar()

    # Hitungan Harga Jual Dasar
    def Page3_cui_Hitungan_Harga_Jual_Dasar(self):
        try:
            self.page3_cui_LineEdit_16.clear()
            Harga_Beli_Terakhir = int(self.page3_cui_LineEdit_13.text())
            Biaya_Penanganan = int(self.page3_cui_LineEdit_12.text())
            Laba_Dasar_Dalam_Rupiah = int(self.page3_cui_LineEdit_15.text())
            Harga_Jual_Dasar = int(RoundUp100(Harga_Beli_Terakhir + Biaya_Penanganan + Laba_Dasar_Dalam_Rupiah))
            self.page3_cui_LineEdit_16.setText(str(Harga_Jual_Dasar))
        except:
            self.page3_cui_LineEdit_16.setText("0")

    # Hitungan Laba Saat Diskon Dalam Persen
    def Page3_cui_Hitungan_Laba_Saat_Diskon_Dalam_Persen(self):
        Laba_Saat_Diskon_Dalam_Persen = self.laba_diskon
        self.page3_cui_LineEdit_17.setText(str(Laba_Saat_Diskon_Dalam_Persen))
        self.Page3_cui_Hitungan_Laba_Saat_Diskon_Dalam_Rupiah()
        self.page3_cui_LineEdit_17.textChanged.connect(self.Page3_cui_Hitungan_Laba_Saat_Diskon_Dalam_Rupiah)

    # Hitungan Laba Saat Diskon Dalam Rupiah
    def Page3_cui_Hitungan_Laba_Saat_Diskon_Dalam_Rupiah(self):
        try:
            self.page3_cui_LineEdit_18.clear()
            Harga_Beli_Terakhir = int(self.page3_cui_LineEdit_13.text())
            Laba_Saat_Diskon_Dalam_Persen = int(self.page3_cui_LineEdit_17.text())
            Laba_Saat_Diskon_Dalam_Rupiah = int((Laba_Saat_Diskon_Dalam_Persen/100)*Harga_Beli_Terakhir)
            self.page3_cui_LineEdit_18.setText(str(Laba_Saat_Diskon_Dalam_Rupiah))
        except:
            Laba_Saat_Diskon_Dalam_Persen = 0
            self.page3_cui_LineEdit_18.setText("0")
        self.Page3_cui_Hitungan_Harga_Jual_Saat_Diskon()

    # Hitungan Harga Jual Saat Diskon
    def Page3_cui_Hitungan_Harga_Jual_Saat_Diskon(self):
        try:
            Harga_Beli_Terakhir = int(self.page3_cui_LineEdit_13.text())
            Biaya_Penanganan = int(self.page3_cui_LineEdit_12.text())
            Laba_Saat_Diskon_Dalam_Rupiah = int(self.page3_cui_LineEdit_18.text())
            Harga_Jual_Saat_Diskon = RoundUp100(Harga_Beli_Terakhir + Biaya_Penanganan + Laba_Saat_Diskon_Dalam_Rupiah)
            self.page3_cui_LineEdit_19.setText(str(Harga_Jual_Saat_Diskon))
        except:
            self.page3_cui_LineEdit_19.setText("0")

    # Hitungan Grosir 1 (Minimal Pembelian)
    def Page3_cui_Hitungan_Grosir_1_Minimal_Pembelian(self):
        self.page3_cui_LineEdit_20.setText("3")

    # Hitungan Grosir 1 (Laba dalam persen)
    def Page3_cui_Hitungan_Grosir_1_Laba_Dalam_Persen(self):
        if self.laba_grosir_1 <= 0:
            Grosir_1_Laba_Dalam_Persen = 0
        elif self.laba_grosir_1 > 0:
            Grosir_1_Laba_Dalam_Persen = self.laba_grosir_1
        else:
            self.page3_cui_LineEdit_21.setText("0")
        self.page3_cui_LineEdit_21.setText(str(Grosir_1_Laba_Dalam_Persen))
        self.Page3_cui_Hitungan_Grosir_1_Laba_Dalam_Rupiah()
        self.page3_cui_LineEdit_21.textChanged.connect(self.Page3_cui_Hitungan_Grosir_1_Laba_Dalam_Rupiah)

    # Hitungan Grosir 1 (Laba dalam rupiah)
    def Page3_cui_Hitungan_Grosir_1_Laba_Dalam_Rupiah(self):
        try:
            Grosir_1_Laba_Dalam_Persen = int(self.page3_cui_LineEdit_21.text())
            Harga_Beli_Terakhir = int(self.page3_cui_LineEdit_13.text())
            Grosir_1_Laba_Dalam_Rupiah = int((Grosir_1_Laba_Dalam_Persen/100) * Harga_Beli_Terakhir)
            self.page3_cui_LineEdit_22.setText(str(Grosir_1_Laba_Dalam_Rupiah))
        except:
            self.page3_cui_LineEdit_22.setText("0")
        self.Page3_cui_Hitungan_Grosir_1_Harga_Jual()

    # Hitungan_Grosir 1 (Harga jual)
    def Page3_cui_Hitungan_Grosir_1_Harga_Jual(self):
        try:
            Harga_Beli_Terakhir = int(self.page3_cui_LineEdit_13.text())
            Biaya_Penanganan = int(self.page3_cui_LineEdit_12.text())
            Grosir_1_Laba_Dalam_Rupiah = int(self.page3_cui_LineEdit_22.text())
            Grosir_1_Harga_Jual = RoundUp100(int(Harga_Beli_Terakhir + Biaya_Penanganan + Grosir_1_Laba_Dalam_Rupiah))
            self.page3_cui_LineEdit_23.setText(str(Grosir_1_Harga_Jual))
        except:
            self.page3_cui_LineEdit_23.setText("0")

    # Hitungan Grosir 2 (Minimal Pembelian)
    def Page3_cui_Hitungan_Grosir_2_Minimal_Pembelian(self):
        self.page3_cui_LineEdit_24.setText("6")

    # Hitungan Grosir 2 (Laba dalam persen)
    def Page3_cui_Hitungan_Grosir_2_Laba_Dalam_Persen(self):
        if self.laba_grosir_2 <= 0:
            Grosir_2_Laba_Dalam_Persen = 0
        elif self.laba_grosir_2 > 0:
            Grosir_2_Laba_Dalam_Persen = self.laba_grosir_2
        else:
            self.page3_cui_LineEdit_25.setText("0")
        self.page3_cui_LineEdit_25.setText(str(Grosir_2_Laba_Dalam_Persen))
        self.Page3_cui_Hitungan_Grosir_2_Laba_Dalam_Rupiah()
        self.page3_cui_LineEdit_25.textChanged.connect(self.Page3_cui_Hitungan_Grosir_2_Laba_Dalam_Rupiah)

    # Hitungan Grosir 2 (Laba dalam rupiah)
    def Page3_cui_Hitungan_Grosir_2_Laba_Dalam_Rupiah(self):
        try:
            Grosir_2_Laba_Dalam_Persen = int(self.page3_cui_LineEdit_25.text())
            Harga_Beli_Terakhir = int(self.page3_cui_LineEdit_13.text())
            Grosir_2_Laba_Dalam_Rupiah = int((Grosir_2_Laba_Dalam_Persen/100)*Harga_Beli_Terakhir)
            self.page3_cui_LineEdit_26.setText(str(Grosir_2_Laba_Dalam_Rupiah))
        except:
            self.page3_cui_LineEdit_26.setText("0")
        self.Page3_cui_Hitungan_Grosir_2_Harga_Jual()

    # Hitungan Grosir 2 (Harga Jual)
    def Page3_cui_Hitungan_Grosir_2_Harga_Jual(self):
        try:
            Harga_Beli_Terakhir = int(self.page3_cui_LineEdit_13.text())
            Grosir_2_Laba_Dalam_Rupiah = int(self.page3_cui_LineEdit_26.text())
            Biaya_Penanganan = int(self.page3_cui_LineEdit_12.text())
            Grosir_2_Harga_Jual = RoundUp100(int(Harga_Beli_Terakhir + Biaya_Penanganan + Grosir_2_Laba_Dalam_Rupiah))
            self.page3_cui_LineEdit_27.setText(str(Grosir_2_Harga_Jual))
        except:
            self.page3_cui_LineEdit_27.setText("0")

    # Hitungan Grosir 3 (Minimal Pembelian)
    def Page3_cui_Hitungan_Grosir_3_Minimal_Pembelian(self):
        self.page3_cui_LineEdit_28.setText("12")

    # Hitungan Grosir 3 (Laba dalam persen)
    def Page3_cui_Hitungan_Grosir_3_Laba_Dalam_Persen(self):
        if self.laba_grosir_3 <= 0:
            Grosir_3_Laba_Dalam_Persen = 0
        elif self.laba_grosir_3 > 0:
            Grosir_3_Laba_Dalam_Persen = self.laba_grosir_3
        else:
            self.page3_cui_LineEdit_29.setText("0")
        self.page3_cui_LineEdit_29.setText(str(Grosir_3_Laba_Dalam_Persen))
        self.Page3_cui_Hitungan_Grosir_3_Laba_Dalam_Rupiah()
        self.page3_cui_LineEdit_29.textChanged.connect(self.Page3_cui_Hitungan_Grosir_3_Laba_Dalam_Rupiah)

    # Hitungan Grosir 3 (Laba dalam Rupiah)
    def Page3_cui_Hitungan_Grosir_3_Laba_Dalam_Rupiah(self):
        try:
            Grosir_3_Laba_Dalam_Persen = int(self.page3_cui_LineEdit_29.text())
            Harga_Beli_Terakhir = int(self.page3_cui_LineEdit_13.text())
            Grosir_3_Laba_Dalam_Rupiah = int((Grosir_3_Laba_Dalam_Persen/100)*Harga_Beli_Terakhir)
            self.page3_cui_LineEdit_30.setText(str(Grosir_3_Laba_Dalam_Rupiah))
        except:
            self.page3_cui_LineEdit_30.setText("0")
        self.Page3_cui_Hitungan_Grosir_3_Harga_Jual()

    # Hitungan Grosir 3 (Harga Jual)
    def Page3_cui_Hitungan_Grosir_3_Harga_Jual(self):
        try:
            self.page3_cui_LineEdit_31.clear()
            Harga_Beli_Terakhir = int(self.page3_cui_LineEdit_13.text())
            Biaya_Penanganan = int(self.page3_cui_LineEdit_12.text())
            Grosir_3_Laba_Dalam_Rupiah = int(self.page3_cui_LineEdit_30.text())
            Grosir_3_Harga_Jual = RoundUp100(int(Harga_Beli_Terakhir + Biaya_Penanganan + Grosir_3_Laba_Dalam_Rupiah))
            self.page3_cui_LineEdit_31.setText(str(Grosir_3_Harga_Jual))
        except:
            self.page3_cui_LineEdit_31.setText("0")

    # Tambah Gambar
    def Page3_cui_Tambah_Gambar(self):
        Pilih_Gambar = QtWidgets.QFileDialog()
        Gambar_Terpilih = Pilih_Gambar.getOpenFileUrl()
        Lokasi_Gambar_Terpilih = Gambar_Terpilih[0].url()[8:]
        self.page3_cui_LineEdit_33.setText(Lokasi_Gambar_Terpilih)

    # Dialog Konfirmasi Tombol Batal Diklik
    def Page3_cui_Konfirmasi_Tombol_Batal_klik(self):
        Dialog = QtWidgets.QDialog()
        Layout = QtWidgets.QGridLayout(Dialog)
        Dialog.setModal(True)
        Dialog.setWindowTitle("Konfirmasi Batal")

        Text = QtWidgets.QLabel("""Apakah anda ingin keluar?\nData tidak akan tersimpan jika anda keluar""")
        PushButton_Ya = QtWidgets.QPushButton("Ya")
        PushButton_Tidak = QtWidgets.QPushButton("Tidak")
        Layout.addWidget(Text, 0, 1, 1, 3)
        Layout.addWidget(PushButton_Ya, 1, 2)
        Layout.addWidget(PushButton_Tidak, 1, 3)

        def closeAll():
            Dialog.close()
            self.Dialog.close()

        PushButton_Tidak.clicked.connect(Dialog.close)
        PushButton_Ya.clicked.connect(closeAll)

        Dialog.show()
        Dialog.exec_()

    # Definisikan pesan error
    def Page3_cui_Pesan_Error(self, judul, pesan):
        Window_Messege_Error = QtWidgets.QMessageBox()
        Window_Messege_Error.setWindowTitle(str(judul))
        Window_Messege_Error.setText(str(pesan))

        Window_Messege_Error.show()
        Window_Messege_Error.exec_()

    # Validasi Data
    def Page3_cui_Validasi_Data(self):
        def Validasi_Nomor():
            try:
                self.page3_cui_LineEdit.setStyleSheet("color: black")
                int(self.page3_cui_LineEdit.text())/1
                Validasi_SKU_Induk()
            except:
                self.page3_cui_LineEdit.setStyleSheet("color: red")
                self.Page3_cui_Pesan_Error("Error", "Nomor yang anda masukkan salah")

        def Validasi_SKU_Induk():
            text = self.page3_cui_LineEdit_34.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_34.setStyleSheet("color: black")
                self.page3_cui_LineEdit_34.setPlaceholderText("")
                Validasi_SKU_Varian_1()
            else:
                self.page3_cui_LineEdit_34.setStyleSheet("color: red")
                self.page3_cui_LineEdit_34.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "SKU Induk tidak boleh kosong")
                self.page3_cui_LineEdit_34.setFocus()

        def Validasi_SKU_Varian_1():
            text = self.page3_cui_LineEdit_35.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_35.setStyleSheet("color: black")
                Validasi_SKU_Varian_2()
            else:
                self.page3_cui_LineEdit_35.setStyleSheet("color: red")
                self.page3_cui_LineEdit_35.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", 'Masukkan SKU Varian 1, apabila tidak ada varian, isikan dengan "V1"')
                self.page3_cui_LineEdit_35.setFocus()

        def Validasi_SKU_Varian_2():
            text = self.page3_cui_LineEdit_36.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_36.setStyleSheet("color: black")
                Validasi_Kode_Produk_Di_Toko()
            else:
                self.page3_cui_LineEdit_36.setStyleSheet("color: red")
                self.page3_cui_LineEdit_36.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", 'Masukkan nilai SKU Varian 2, apabila tidak ada varian isikan dengan "V1"')
                self.page3_cui_LineEdit_36.setFocus()

        def Validasi_Kode_Produk_Di_Toko():
            text = self.page3_cui_LineEdit_2.text()
            Kode_Produk_Terpakai = []
            Kode_Produk = self.page3_cui_DBProduk_cursor.execute("select Kode_Toko from Data_Produk_Master").fetchall()
            for item in range(len(Kode_Produk)):
                Kode_Produk_Terpakai.append(Kode_Produk[item]["Kode_Toko"])

            if text not in Kode_Produk_Terpakai:
                self.page3_cui_LineEdit_2.setStyleSheet("color: black")
                self.page3_cui_LineEdit_34.setStyleSheet("color: black")
                self.page3_cui_LineEdit_35.setStyleSheet("color: black")
                self.page3_cui_LineEdit_36.setStyleSheet("color: black")
                Validasi_Barcode_Produk()
            else:
                self.page3_cui_LineEdit_2.setStyleSheet("color: red")
                self.page3_cui_LineEdit_34.setStyleSheet("color: red")
                self.page3_cui_LineEdit_35.setStyleSheet("color: red")
                self.page3_cui_LineEdit_36.setStyleSheet("color: red")
                self.Page3_cui_Pesan_Error("Data Duplikat", "Data Kode 'Produk di Toko' sudah ada dalam database.\n\nTambahkan transaksi produk apabila produk yang anda masukkan telah ada dalam database \nATAU\nTambahkan SKU Varian baru (SKU Varian 1 atau 2) apabila produk tersebut memiliki varian baru")

        def Validasi_Barcode_Produk():
            text = self.page3_cui_LineEdit_4.text()
            Barcode_Produk_terpakai = []
            Barcode = self.page3_cui_DBProduk_cursor.execute("select Barcode_Produk from Data_Produk_Master").fetchall()
            for item in range(len(Barcode)):
                Barcode_Produk_terpakai.append(Barcode[item]["Barcode_Produk"])

            if text not in Barcode_Produk_terpakai:
                if len(text) > 0:
                    self.page3_cui_LineEdit_4.setStyleSheet("color: black")
                    Validasi_Nama_Produk_Di_Distributor()
                else:
                    self.page3_cui_LineEdit_4.setStyleSheet("color: red")
                    self.Page3_cui_Pesan_Error("Data tidak lengkap", "Data 'Barcode Produk' belum diisi.\nJika produk tidak memiliki barcode, isi kolom ini dengan data yang sama dengan data 'Kode Produk di Toko'")
                    self.page3_cui_LineEdit_4.setPlaceholderText("Tidak boleh kosong")
                    self.page3_cui_LineEdit_4.setFocus()
            else:
                self.page3_cui_LineEdit_4.setStyleSheet("color: red")
                Barcode_Duplikat_Terpakai = self.page3_cui_DBProduk_cursor.execute("select Nama_Produk_Di_Toko from Data_Produk_Master where Barcode_Produk='{}'".format(text)).fetchone()["Nama_Produk_Di_Toko"]
                self.Page3_cui_Pesan_Error("Data Duplikat", "Barcode yang anda masukkan telah terpakai di produk lain.\nSilakan cek produk berikut :\n\nNama Produk : {}\nBarcode Produk : {}".format(Barcode_Duplikat_Terpakai, text))
                self.page3_cui_LineEdit_4.setFocus()

        def Validasi_Nama_Produk_Di_Distributor():
            text = self.page3_cui_LineEdit_5.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_5.setStyleSheet("color: black")
                Validasi_Nama_Produk()
            else:
                self.page3_cui_LineEdit_5.setStyleSheet("color: red")
                self.page3_cui_LineEdit_5.setPlaceholderText("Tidak boleh kosong")
                self.page3_cui_LineEdit_5.setFocus()
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Data 'Nama Distributor' belum diisi")

        def Validasi_Nama_Produk():
            text = self.page3_cui_LineEdit_3.text()
            Nama_Produk_terpakai = []
            Nama_Produk = self.page3_cui_DBProduk_cursor.execute("select Nama_Produk_Di_Toko from Data_Produk_Master").fetchall()
            for item in range(len(Nama_Produk)):
                Nama_Produk_terpakai.append(Nama_Produk[item]["Nama_Produk_Di_Toko"])

            if text not in Nama_Produk_terpakai:
                if len(text) > 0:
                    self.page3_cui_LineEdit_3.setStyleSheet("color: black")
                    Validasi_Deskripsi_Produk()
                else:
                    self.page3_cui_LineEdit_3.setStyleSheet("color: red")
                    self.Page3_cui_Pesan_Error("Data tidak lengkap", "Data 'Nama Produk' belum diisi.")
                    self.page3_cui_LineEdit_3.setPlaceholderText("Tidak boleh kosong")
                    self.page3_cui_LineEdit_3.setFocus()
            else:
                self.page3_cui_LineEdit_3.setStyleSheet("color: red")
                Nama_Produk_Duplikat_Terpakai = self.page3_cui_DBProduk_cursor.execute("select Nama_Produk_Di_Toko from Data_Produk_Master").fetchone()["Nama_Produk_Di_Toko"]
                self.Page3_cui_Pesan_Error("Data Duplikat", "Nama Produk yang anda masukkan telah terpakai di produk lain.\nSilakan cek produk berikut :\n\nNama Produk : {}".format(Nama_Produk_Duplikat_Terpakai))
                self.page3_cui_LineEdit_3.setFocus()

        # Tidak divalidasi
        def Validasi_Deskripsi_Produk():
            text = self.page3_cui_TextEdit.toPlainText()
            Validasi_Total_Stok()

        def Validasi_Total_Stok():
            text = self.page3_cui_LineEdit_37.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_37.setStyleSheet("color: black")
                Validasi_Warning_Stok()
            else:
                self.page3_cui_LineEdit_37.setStyleSheet("color: red")
                self.page3_cui_LineEdit_37.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Informasi Stok tidak boleh kosong")

        def Validasi_Warning_Stok():
            text = self.page3_cui_LineEdit_39.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_39.setStyleSheet("color: black")
                Validasi_Total_Stok_Satuan()
            else:
                self.page3_cui_LineEdit_39.setStyleSheet("color: red")
                self.page3_cui_LineEdit_39.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Informasi Warning Stok tidak boleh kosong")
                pass

        # Tidak divalidasi
        def Validasi_Total_Stok_Satuan():
            text = self.page3_cui_ComboBox_4.currentText()
            Validasi_Berat_atau_Volume_Di_Kemasan()

        def Validasi_Berat_atau_Volume_Di_Kemasan():
            text = self.page3_cui_LineEdit_38.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_38.setStyleSheet("color: black")
                Validasi_Berat_atau_Volume_Di_Kemasan_Satuan()
            else:
                self.page3_cui_LineEdit_38.setStyleSheet("color: red")
                self.page3_cui_LineEdit_38.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Data 'berat / volume produk di kemasan' tidak boleh kosong")

        # Tidak divalidasi
        def Validasi_Berat_atau_Volume_Di_Kemasan_Satuan():
            text = self.page3_cui_ComboBox_5.currentText()
            Validasi_Berat_Untuk_Pengiriman()

        # Tidak divalidasi
        def Validasi_Berat_Untuk_Pengiriman():
            text = self.page3_cui_LineEdit_6.text()
            Validasi_Kemasan()

        def Validasi_Kemasan():
            text = self.page3_cui_ComboBox.currentText()
            if text != "-":
                self.page3_cui_ComboBox.setStyleSheet("color: black")
                Validasi_Perizinan()
            else:
                self.page3_cui_ComboBox.setStyleSheet("color: red")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Data 'Kemasan' belum dipilih dengan benar")
                self.page3_cui_ComboBox.setFocus()

        def Validasi_Perizinan():
            text = self.page3_cui_ComboBox_2.currentText()
            if text != "-":
                self.page3_cui_ComboBox_2.setStyleSheet("color: black")
                Validasi_Kode_BPOM_atau_PIRT()
            else:
                self.page3_cui_ComboBox_2.setStyleSheet("color: red")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Data 'Perizinan' belum dipilih dengan benar")

        def Validasi_Kode_BPOM_atau_PIRT():
            text = self.page3_cui_LineEdit_7.text()
            self.page3_cui_LineEdit_7.setStyleSheet("color: black")
            if self.page3_cui_ComboBox_2.currentText() == "BPOM":
                if len(text) > 0:
                    Validasi_Label_Halal()
                else:
                    self.page3_cui_LineEdit_7.setStyleSheet("color: red")
                    self.page3_cui_LineEdit_7.setPlaceholderText("Kode {} tidak boleh kosong".format(self.page3_cui_ComboBox_2.currentText()))
                    self.Page3_cui_Pesan_Error("Data tidak lengkap", "Perizinan jenis {} telah dipilih. \nKode {} tidak boleh kosong".format(self.page3_cui_ComboBox_2.currentText(), self.page3_cui_ComboBox_2.currentText()))
            elif self.page3_cui_ComboBox_2.currentText() == "PIRT":
                if len(text) > 0:
                    Validasi_Label_Halal()
                else:
                    self.page3_cui_LineEdit_7.setStyleSheet("color: red")
                    self.page3_cui_LineEdit_7.setPlaceholderText("Kode {} tidak boleh kosong".format(self.page3_cui_ComboBox_2.currentText()))
                    self.Page3_cui_Pesan_Error("Data tidak lengkap", "Perizinan jenis {} telah dipilih. \nKode {} tidak boleh kosong".format(self.page3_cui_ComboBox_2.currentText(), self.page3_cui_ComboBox_2.currentText()))
            else:
                Validasi_Label_Halal()

        def Validasi_Label_Halal():
            text = self.page3_cui_ComboBox_3.currentText()
            if text != "-":
                self.page3_cui_ComboBox_3.setStyleSheet("color: black")
                Validasi_Produsen()
            else:
                self.page3_cui_ComboBox_3.setStyleSheet("color: red")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Data 'Label Halal' belum dipilih")

        def Validasi_Produsen():
            text = self.page3_cui_LineEdit_8.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_8.setStyleSheet("color: black")
                Validasi_Distributor()
            else:
                self.page3_cui_LineEdit_8.setStyleSheet("color: red")
                self.page3_cui_LineEdit_8.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Nama Produsen harus diisi")
                self.page3_cui_LineEdit_8.setFocus()

        def Validasi_Distributor():
            text = self.page3_cui_LineEdit_9.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_9.setStyleSheet("color: black")
                Validasi_Nama_Sales()
            else:
                self.page3_cui_LineEdit_9.setStyleSheet("color: red")
                self.page3_cui_LineEdit_9.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Nama Distributor harus diisi")
                self.page3_cui_LineEdit_9.setFocus()

        def Validasi_Nama_Sales():
            text = self.page3_cui_LineEdit_10.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_10.setStyleSheet("color: black")
                Validasi_Nomor_Telepon_Sales()
            else:
                self.page3_cui_LineEdit_10.setStyleSheet("color: red")
                self.page3_cui_LineEdit_10.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Nama Sales harus diisi")
                self.page3_cui_LineEdit_10.setFocus()

        def Validasi_Nomor_Telepon_Sales():
            text = self.page3_cui_LineEdit_11.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_11.setStyleSheet("color: black")
                Validasi_Barang_Umum_atau_Khusus()
            else:
                self.page3_cui_LineEdit_11.setStyleSheet("color: red")
                self.page3_cui_LineEdit_11.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Nomor telepon sales harus diisi")
                self.page3_cui_LineEdit_11.setFocus()

        def Validasi_Barang_Umum_atau_Khusus():
            text = self.page3_cui_ComboBox_6.currentText()
            if text != "-":
                self.page3_cui_ComboBox_6.setStyleSheet("color: black")
                Validasi_Harga_Beli_Terakhir()
            else:
                self.page3_cui_ComboBox_6.setStyleSheet("color: red")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Kode Barang Umum atau Khusus harus diisi")
                self.page3_cui_ComboBox_6.setFocus()

        def Validasi_Harga_Beli_Terakhir():
            text = self.page3_cui_LineEdit_13.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_13.setStyleSheet("color: black")
                Validasi_Biaya_Penanganan()
            else:
                self.page3_cui_LineEdit_13.setStyleSheet("color: red")
                self.page3_cui_LineEdit_13.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Harga beli terakhir harus diisi")
                self.page3_cui_LineEdit_13.setFocus()

        def Validasi_Biaya_Penanganan():
            text = self.page3_cui_LineEdit_12.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_12.setStyleSheet("color: black")
                Validasi_Laba_Dasar_Dalam_Persen()
            else:
                self.page3_cui_LineEdit_12.setStyleSheet("color: red")
                self.page3_cui_LineEdit_12.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Biaya Penanganan harus diisi")
                self.page3_cui_LineEdit_12.setFocus()

        def Validasi_Laba_Dasar_Dalam_Persen():
            text = self.page3_cui_LineEdit_14.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_14.setStyleSheet("color: black")
                Validasi_Laba_Dasar_Dalam_Rupiah()
            else:
                self.page3_cui_LineEdit_14.setStyleSheet("color: red")
                self.page3_cui_LineEdit_14.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Laba Dasar Dalam Persen harus diisi")
                self.page3_cui_LineEdit_14.setFocus()

        def Validasi_Laba_Dasar_Dalam_Rupiah():
            text = self.page3_cui_LineEdit_15.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_15.setStyleSheet("color: black")
                Validasi_Harga_Jual_Dasar()
            else:
                self.page3_cui_LineEdit_15.setStyleSheet("color: red")
                self.page3_cui_LineEdit_15.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Laba Dasar Dalam Rupiah harus diisi")
                self.page3_cui_LineEdit_15.setFocus()

        def Validasi_Harga_Jual_Dasar():
            text = self.page3_cui_LineEdit_16.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_16.setStyleSheet("color: black")
                Validasi_Laba_Saat_Diskon_Dalam_Persen()
            else:
                self.page3_cui_LineEdit_16.setStyleSheet("color: red")
                self.page3_cui_LineEdit_16.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "Harga Jual Dasar harus diisi")
                self.page3_cui_LineEdit_16.setFocus()

        def Validasi_Laba_Saat_Diskon_Dalam_Persen():
            text = self.page3_cui_LineEdit_17.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_17.setStyleSheet("color: black")
                Validasi_Laba_Saat_Diskon_Dalam_Rupiah()
            else:
                self.page3_cui_LineEdit_17.setStyleSheet("color: red")
                self.page3_cui_LineEdit_17.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Laba saat diskon dalam persen' harus diisi")
                self.page3_cui_LineEdit_17.setFocus()

        def Validasi_Laba_Saat_Diskon_Dalam_Rupiah():
            text = self.page3_cui_LineEdit_18.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_18.setStyleSheet("color: black")
                Validasi_Harga_Jual_Saat_Diskon()
            else:
                self.page3_cui_LineEdit_18.setStyleSheet("color: red")
                self.page3_cui_LineEdit_18.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Laba saat diskon dalam rupiah' harus diisi")
                self.page3_cui_LineEdit_18.setFocus()

        def Validasi_Harga_Jual_Saat_Diskon():
            text = self.page3_cui_LineEdit_19.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_19.setStyleSheet("color: black")
                Validasi_Grosir_1_Minimal_Pembelian()
            else:
                self.page3_cui_LineEdit_19.setStyleSheet("color: red")
                self.page3_cui_LineEdit_19.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Harga Jual Saat Diskon' harus diisi")
                self.page3_cui_LineEdit_19.setFocus()

        def Validasi_Grosir_1_Minimal_Pembelian():
            text = self.page3_cui_LineEdit_20.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_20.setStyleSheet("color: black")
                Validasi_Grosir_1_Laba_Dalam_Persen()
            else:
                self.page3_cui_LineEdit_20.setStyleSheet("color: red")
                self.page3_cui_LineEdit_20.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Minimal pembelian Grosir 1' harus diisi")
                self.page3_cui_LineEdit_20.setFocus()

        def Validasi_Grosir_1_Laba_Dalam_Persen():
            text = self.page3_cui_LineEdit_21.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_21.setStyleSheet("color: black")
                Validasi_Grosir_1_Laba_Dalam_Rupiah()
            else:
                self.page3_cui_LineEdit_21.setStyleSheet("color: red")
                self.page3_cui_LineEdit_21.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Laba dalam persen untuk Grosir 1' harus diisi")
                self.page3_cui_LineEdit_21.setFocus()

        def Validasi_Grosir_1_Laba_Dalam_Rupiah():
            text = self.page3_cui_LineEdit_22.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_22.setStyleSheet("color: black")
                Validasi_Grosir_1_Harga_Jual()
            else:
                self.page3_cui_LineEdit_22.setStyleSheet("color: red")
                self.page3_cui_LineEdit_22.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Laba dalam rupiah untuk Grosir 1' harus diisi")
                self.page3_cui_LineEdit_22.setFocus()

        def Validasi_Grosir_1_Harga_Jual():
            text = self.page3_cui_LineEdit_23.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_23.setStyleSheet("color: black")
                Validasi_Grosir_2_Minimal_Pembelian()
            else:
                self.page3_cui_LineEdit_23.setStyleSheet("color: red")
                self.page3_cui_LineEdit_23.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Harga jual untuk Grosir 1' harus diisi")
                self.page3_cui_LineEdit_23.setFocus()

        def Validasi_Grosir_2_Minimal_Pembelian():
            text = self.page3_cui_LineEdit_24.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_24.setStyleSheet("color: black")
                Validasi_Grosir_2_Laba_Dalam_Persen()
            else:
                self.page3_cui_LineEdit_24.setStyleSheet("color: red")
                self.page3_cui_LineEdit_24.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Minimal pembelian untuk Grosir 2' harus diisi")
                self.page3_cui_LineEdit_24.setFocus()

        def Validasi_Grosir_2_Laba_Dalam_Persen():
            text = self.page3_cui_LineEdit_25.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_25.setStyleSheet("color: black")
                Validasi_Grosir_2_Laba_Dalam_Rupiah()
            else:
                self.page3_cui_LineEdit_25.setStyleSheet("color: red")
                self.page3_cui_LineEdit_25.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Laba dalam persen untuk Grosir 2' harus diisi")
                self.page3_cui_LineEdit_25.setFocus()

        def Validasi_Grosir_2_Laba_Dalam_Rupiah():
            text = self.page3_cui_LineEdit_26.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_26.setStyleSheet("color: black")
                Validasi_Grosir_2_Harga_Jual()
            else:
                self.page3_cui_LineEdit_26.setStyleSheet("color: red")
                self.page3_cui_LineEdit_26.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Laba dalam rupiah untuk Grosir 2' harus diisi")
                self.page3_cui_LineEdit_26.setFocus()

        def Validasi_Grosir_2_Harga_Jual():
            text = self.page3_cui_LineEdit_27.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_27.setStyleSheet("color: black")
                Validasi_Grosir_3_Minimal_Pembelian()
            else:
                self.page3_cui_LineEdit_27.setStyleSheet("color: red")
                self.page3_cui_LineEdit_27.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Harga jual untuk Grosir 2' harus diisi")
                self.page3_cui_LineEdit_27.setFocus()

        def Validasi_Grosir_3_Minimal_Pembelian():
            text = self.page3_cui_LineEdit_28.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_28.setStyleSheet("color: black")
                Validasi_Grosir_3_Laba_Dalam_Persen()
            else:
                self.page3_cui_LineEdit_28.setStyleSheet("color: red")
                self.page3_cui_LineEdit_28.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Minimal pembelian untuk Grosir 3' harus diisi")
                self.page3_cui_LineEdit_28.setFocus()

        def Validasi_Grosir_3_Laba_Dalam_Persen():
            text = self.page3_cui_LineEdit_29.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_29.setStyleSheet("color: black")
                Validasi_Grosir_3_Laba_Dalam_Rupiah()
            else:
                self.page3_cui_LineEdit_29.setStyleSheet("color: red")
                self.page3_cui_LineEdit_29.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Laba dalam persen untuk Grosir 3' harus diisi")
                self.page3_cui_LineEdit_29.setFocus()

        def Validasi_Grosir_3_Laba_Dalam_Rupiah():
            text = self.page3_cui_LineEdit_30.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_30.setStyleSheet("color: black")
                Validasi_Grosir_3_Harga_Jual()
            else:
                self.page3_cui_LineEdit_30.setStyleSheet("color: red")
                self.page3_cui_LineEdit_30.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Laba dalam rupiah untuk Grosir 3' harus diisi")
                self.page3_cui_LineEdit_30.setFocus()

        def Validasi_Grosir_3_Harga_Jual():
            text = self.page3_cui_LineEdit_31.text()
            if len(text) > 0:
                self.page3_cui_LineEdit_31.setStyleSheet("color: black")
                Validasi_Catatan()
            else:
                self.page3_cui_LineEdit_31.setStyleSheet("color: red")
                self.page3_cui_LineEdit_31.setPlaceholderText("Tidak boleh kosong")
                self.Page3_cui_Pesan_Error("Data tidak lengkap", "'Harga jual untuk Grosir 3' harus diisi")
                self.page3_cui_LineEdit_31.setFocus()

        # Tidak divalidasi
        def Validasi_Catatan():
            text = self.page3_cui_TextEdit_2.toPlainText()
            Validasi_Foto_Produk()

        # Tidak divalidasi
        def Validasi_Foto_Produk():
            text = self.page3_cui_LineEdit_33.text()
            Validasi_Posisi_Barang()

        # Tidak divalidasi
        def Validasi_Posisi_Barang():
            text = self.page3_cui_LineEdit_32.text()
            Validasi_Kepantasan_Harga()

        # Validasi Kepantasan Harga
        def Validasi_Kepantasan_Harga():
            Laba_Dasar = int(self.page3_cui_LineEdit_15.text())
            Laba_Saat_Diskon = int(self.page3_cui_LineEdit_18.text())
            Laba_Saat_Grosir_1 = int(self.page3_cui_LineEdit_22.text())
            Laba_Saat_Grosir_2 = int(self.page3_cui_LineEdit_26.text())
            Laba_Saat_Grosir_3 = int(self.page3_cui_LineEdit_30.text())
            if Laba_Dasar > Laba_Saat_Diskon:
                if Laba_Saat_Diskon > Laba_Saat_Grosir_1:
                    if Laba_Saat_Grosir_1 > Laba_Saat_Grosir_2:
                        if Laba_Saat_Grosir_2 > Laba_Saat_Grosir_3:
                            Validasi_Selesai()
                        else:
                            self.Page3_cui_Pesan_Error("Harga tidak valid", "Harga Jual Grosir 3 tidak boleh lebih besar daripada Harga Jual Grosir 2")
                            self.page3_cui_LineEdit_29.setFocus()
                    else:
                        self.Page3_cui_Pesan_Error("Harga tidak valid", "Harga Jual Grosir 2 tidak boleh lebih besar daripada Harga Jual Grosir 1")
                        self.page3_cui_LineEdit_25.setFocus()
                else:
                    self.Page3_cui_Pesan_Error("Harga tidak valid", "Harga Jual Grosir 1 tidak boleh lebih besar daripada Harga Jual Diskon")
                    self.page3_cui_LineEdit_21.setFocus()
            else:
                self.Page3_cui_Pesan_Error("Harga tidak valid", "Harga Jual Diskon tidak boleh lebih besar daripada Harga Jual Dasar")
                self.page3_cui_LineEdit_17.setFocus()

        def Validasi_Selesai():
            self.Page3_cui_Validasi_Selesai()

        # Style
        def Rubah_Warna_Text_SKU_Induk():
            if len(self.page3_cui_LineEdit_34.text()) > 0:
                self.page3_cui_LineEdit_34.setStyleSheet("color: black")
            else:
                self.page3_cui_LineEdit_34.setStyleSheet("color: red")

        def Rubah_Warna_Text_SKU_Varian_1():
            if len(self.page3_cui_LineEdit_35.text()) > 0:
                self.page3_cui_LineEdit_35.setStyleSheet("color: black")
            else:
                self.page3_cui_LineEdit_35.setStyleSheet("color: red")

        def Rubah_Warna_Text_SKU_Varian_2():
            if len(self.page3_cui_LineEdit_36.text()) > 0:
                self.page3_cui_LineEdit_36.setStyleSheet("color: black")
            else:
                self.page3_cui_LineEdit_36.setStyleSheet("color: red")

        # PERINTAH
        self.page3_cui_LineEdit_34.textChanged.connect(Rubah_Warna_Text_SKU_Induk)
        self.page3_cui_LineEdit_35.textChanged.connect(Rubah_Warna_Text_SKU_Varian_1)
        self.page3_cui_LineEdit_36.textChanged.connect(Rubah_Warna_Text_SKU_Varian_2)
        Validasi_Nomor()

    # Validasi Data selesai
    def Page3_cui_Validasi_Selesai(self):
        self.Page3_cui_Kumpulkan_Data()
        # Konfirmasi
        self.Dialog_Simpan = QtWidgets.QDialog()
        self.Dialog_Simpan.setWindowTitle("Konfirmasi Data")
        self.Dialog_Simpan.setModal(True)
        Layout = QtWidgets.QGridLayout(self.Dialog_Simpan)
        Label1 = QtWidgets.QLabel("Apakah anda ingin menyimpan data ini?")
        PushButton_Ya = QtWidgets.QPushButton("Ya")
        PushButton_Tidak = QtWidgets.QPushButton("Tidak")
        Layout.addWidget(Label1, 0, 1, 1, 3)
        Layout.addWidget(PushButton_Ya, 1, 2)
        Layout.addWidget(PushButton_Tidak, 1, 3)
        PushButton_Tidak.clicked.connect(self.Dialog_Simpan.close)
        PushButton_Ya.clicked.connect(self.Page3_cui_Simpan_Data)
        self.Dialog_Simpan.show()
        self.Dialog_Simpan.exec_()

    # Pada Saat Tombol Simpan Diklik
    def Page3_cui_PushButton_2_klik(self):
        self.Page3_cui_Validasi_Data()

    # Kumpulkan data Aplikasi
    def Page3_cui_Kumpulkan_Data(self):
        self.page3_cui_No = self.page3_cui_LineEdit.text()
        self.page3_cui_SKU_Induk = self.page3_cui_LineEdit_34.text()
        self.page3_cui_SKU_Varian_1 = self.page3_cui_LineEdit_35.text()
        self.page3_cui_SKU_Varian_2 = self.page3_cui_LineEdit_36.text()
        self.page3_cui_Kode_Toko = self.page3_cui_LineEdit_2.text()
        self.page3_cui_Barcode_Produk = self.page3_cui_LineEdit_4.text()
        self.page3_cui_Nama_Produk_Di_Distributor = self.page3_cui_LineEdit_5.text()
        self.page3_cui_Nama_Produk_Di_Toko = self.page3_cui_LineEdit_3.text()
        self.page3_cui_Repack = ""
        self.page3_cui_Produk_umum_khusus = self.page3_cui_ComboBox_6.currentText()
        self.page3_cui_Deskripsi_Produk = self.page3_cui_TextEdit.toPlainText()
        self.page3_cui_Total_Stok = self.page3_cui_LineEdit_37.text()
        self.page3_cui_Total_Stok_Satuan = self.page3_cui_ComboBox_4.currentText()
        self.page3_cui_Berat_atau_Volume_Bersih = self.page3_cui_LineEdit_38.text()
        self.page3_cui_Satuan_Berat_Bersih = self.page3_cui_ComboBox_5.currentText()
        self.page3_cui_Berat_Untuk_Pengiriman_Dalam_Gram = self.page3_cui_LineEdit_6.text()
        self.page3_cui_Kemasan = self.page3_cui_ComboBox.currentText()
        self.page3_cui_Perizinan = self.page3_cui_ComboBox_2.currentText()
        self.page3_cui_Kode_BPOM_atau_PIRT = self.page3_cui_LineEdit_7.text()
        self.page3_cui_Label_Halal = self.page3_cui_ComboBox_3.currentText()
        self.page3_cui_Produsen = self.page3_cui_LineEdit_8.text()
        self.page3_cui_Distributor = self.page3_cui_LineEdit_9.text()
        self.page3_cui_Nama_Sales = self.page3_cui_LineEdit_10.text()
        self.page3_cui_No_Telepon_Sales = self.page3_cui_LineEdit_11.text()
        self.page3_cui_Harga_Beli_Terakhir = self.page3_cui_LineEdit_13.text()
        self.page3_cui_Biaya_Penanganan = self.page3_cui_LineEdit_12.text()
        self.page3_cui_Laba_Dasar_Dalam_Persen = self.page3_cui_LineEdit_14.text()
        self.page3_cui_Laba_Dasar_Dalam_Rupiah = self.page3_cui_LineEdit_15.text()
        self.page3_cui_Harga_Jual_Dasar = self.page3_cui_LineEdit_16.text()
        self.page3_cui_Laba_Saat_Diskon_Dalam_Persen = self.page3_cui_LineEdit_17.text()
        self.page3_cui_Laba_Saat_Diskon_Dalam_Rupiah = self.page3_cui_LineEdit_18.text()
        self.page3_cui_Harga_Jual_Saat_Diskon = self.page3_cui_LineEdit_19.text()
        self.page3_cui_Minimal_Pembelian_Grosir_1 = self.page3_cui_LineEdit_20.text()
        self.page3_cui_Laba_Saat_Grosir_1_Dalam_Persen = self.page3_cui_LineEdit_21.text()
        self.page3_cui_Laba_Saat_Grosir_1_Dalam_Rupiah = self.page3_cui_LineEdit_22.text()
        self.page3_cui_Harga_Jual_Saat_Grosir_1 = self.page3_cui_LineEdit_23.text()
        self.page3_cui_Minimal_Pembelian_Grosir_2 = self.page3_cui_LineEdit_24.text()
        self.page3_cui_Laba_Saat_Grosir_2_Dalam_Persen = self.page3_cui_LineEdit_25.text()
        self.page3_cui_Laba_Saat_Grosir_2_Dalam_Rupiah = self.page3_cui_LineEdit_26.text()
        self.page3_cui_Harga_Jual_Saat_Grosir_2 = self.page3_cui_LineEdit_27.text()
        self.page3_cui_Minimal_Pembelian_Grosir_3 = self.page3_cui_LineEdit_28.text()
        self.page3_cui_Laba_Saat_Grosir_3_Dalam_Persen = self.page3_cui_LineEdit_29.text()
        self.page3_cui_Laba_Saat_Grosir_3_Dalam_Rupiah = self.page3_cui_LineEdit_30.text()
        self.page3_cui_Harga_Jual_Saat_Grosir_3 = self.page3_cui_LineEdit_31.text()
        self.page3_cui_Catatan = self.page3_cui_TextEdit_2.toPlainText()
        self.page3_cui_Foto_Produk_1 = self.page3_cui_LineEdit_33.text()
        self.page3_cui_Foto_Produk_2 = ""
        self.page3_cui_Foto_Produk_3 = ""
        self.page3_cui_Foto_Produk_4 = ""
        self.page3_cui_Foto_Produk_5 = ""
        self.page3_cui_Foto_Produk_6 = ""
        self.page3_cui_Foto_Produk_7 = ""
        self.page3_cui_Foto_Produk_8 = ""
        self.page3_cui_Foto_Produk_9 = ""
        self.page3_cui_Foto_Video = ""
        self.page3_cui_Posisi_Barang = self.page3_cui_LineEdit_32.text()
        self.page3_cui_Warning_Stok = str(self.page3_cui_LineEdit_39.text())

    # Simpan Data
    def Page3_cui_Simpan_Data(self):
        # Proses dalam Database
        # kolom = "No, SKU_Induk, SKU_Varian_1, SKU_Varian_2, Kode_Toko, Barcode_Produk, Nama_Produk_Di_Distributor, Nama_Produk_Di_Toko, Repack, Produk_umum_khusus, Deskripsi_Produk, Total_Stok, Total_Stok_Satuan, Berat_atau_Volume_Bersih, Satuan_Berat_Bersih, Berat_Untuk_Pengiriman_Dalam_Gram, Kemasan, Perizinan, Kode_BPOM_atau_PIRT, Label_Halal, Produsen, Distributor, Nama_Sales, No_Telepon_Sales, Harga_Beli_Terakhir, Biaya_Penanganan, Laba_Dasar_Dalam_Persen, Laba_Dasar_Dalam_Rupiah, Harga_Jual_Dasar, Laba_Saat_Diskon_Dalam_Persen, Laba_Saat_Diskon_Dalam_Rupiah, Harga_Jual_Saat_Diskon, Minimal_Pembelian_Grosir_1, Laba_Saat_Grosir_1_Dalam_Persen, Laba_Saat_Grosir_1_Dalam_Rupiah, Harga_Jual_Saat_Grosir_1, Minimal_Pembelian_Grosir_2, Laba_Saat_Grosir_2_Dalam_Persen, Laba_Saat_Grosir_2_Dalam_Rupiah, Harga_Jual_Saat_Grosir_2, Minimal_Pembelian_Grosir_3, Laba_Saat_Grosir_3_Dalam_Persen, Laba_Saat_Grosir_3_Dalam_Rupiah, Harga_Jual_Saat_Grosir_3, Catatan, Foto_Produk_1, Foto_Produk_2, Foto_Produk_3, Foto_Produk_4, Foto_Produk_5, Foto_Produk_6, Foto_Produk_7, Foto_Produk_8, Foto_Produk_9, Foto_Video, Posisi_Barang"
        # value ="{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, "
        # self.page3_cui_No, self.page3_cui_SKU_Induk, self.page3_cui_SKU_Varian_1, self.page3_cui_SKU_Varian_2, self.page3_cui_Kode_Toko, self.page3_cui_Barcode_Produk, self.page3_cui_Nama_Produk_Di_Distributor, self.page3_cui_Nama_Produk_Di_Toko, self.page3_cui_Repack, self.page3_cui_Produk_umum_khusus, self.page3_cui_Deskripsi_Produk, self.page3_cui_Total_Stok, self.page3_cui_Total_Stok_Satuan, self.page3_cui_Berat_atau_Volume_Bersih, self.page3_cui_Satuan_Berat_Bersih, self.page3_cui_Berat_Untuk_Pengiriman_Dalam_Gram, self.page3_cui_Kemasan, self.page3_cui_Perizinan, self.page3_cui_Kode_BPOM_atau_PIRT, self.page3_cui_Label_Halal, self.page3_cui_Produsen, self.page3_cui_Distributor, self.page3_cui_Nama_Sales, self.page3_cui_No_Telepon_Sales, self.page3_cui_Harga_Beli_Terakhir, self.page3_cui_Biaya_Penanganan, self.page3_cui_Laba_Dasar_Dalam_Persen, self.page3_cui_Laba_Dasar_Dalam_Rupiah, self.page3_cui_Harga_Jual_Dasar, self.page3_cui_Laba_Saat_Diskon_Dalam_Persen, self.page3_cui_Laba_Saat_Diskon_Dalam_Rupiah, self.page3_cui_Harga_Jual_Saat_Diskon, self.page3_cui_Minimal_Pembelian_Grosir_1, self.page3_cui_Laba_Saat_Grosir_1_Dalam_Persen, self.page3_cui_Laba_Saat_Grosir_1_Dalam_Rupiah, self.page3_cui_Harga_Jual_Saat_Grosir_1, self.page3_cui_Minimal_Pembelian_Grosir_2, self.page3_cui_Laba_Saat_Grosir_2_Dalam_Persen, self.page3_cui_Laba_Saat_Grosir_2_Dalam_Rupiah, self.page3_cui_Harga_Jual_Saat_Grosir_2, self.page3_cui_Minimal_Pembelian_Grosir_3, self.page3_cui_Laba_Saat_Grosir_3_Dalam_Persen, self.page3_cui_Laba_Saat_Grosir_3_Dalam_Rupiah, self.page3_cui_Harga_Jual_Saat_Grosir_3, self.page3_cui_Catatan, self.page3_cui_Foto_Produk_1, self.page3_cui_Foto_Produk_2, self.page3_cui_Foto_Produk_3, self.page3_cui_Foto_Produk_4, self.page3_cui_Foto_Produk_5, self.page3_cui_Foto_Produk_6, self.page3_cui_Foto_Produk_7, self.page3_cui_Foto_Produk_8, self.page3_cui_Foto_Produk_9, self.page3_cui_Foto_Video, self.page3_cui_Posisi_Barang
        self.page3_cui_DBProduk_cursor.execute("insert into `Data_Produk_Master` ('No','SKU_Induk','SKU_Varian_1','SKU_Varian_2','Kode_Toko','Barcode_Produk','Nama_Produk_Di_Distributor','Nama_Produk_Di_Toko','Repack','Produk_umum_khusus','Deskripsi_Produk','Total_Stok','Total_Stok_Satuan','Berat_atau_Volume_Bersih','Satuan_Berat_Bersih','Berat_Untuk_Pengiriman_Dalam_Gram','Kemasan','Perizinan','Kode_BPOM_atau_PIRT','Label_Halal','Produsen','Distributor','Nama_Sales','No_Telepon_Sales','Harga_Beli_Terakhir','Biaya_Penanganan','Laba_Dasar_Dalam_Persen','Laba_Dasar_Dalam_Rupiah','Harga_Jual_Dasar','Laba_Saat_Diskon_Dalam_Persen','Laba_Saat_Diskon_Dalam_Rupiah','Harga_Jual_Saat_Diskon','Minimal_Pembelian_Grosir_1','Laba_Saat_Grosir_1_Dalam_Persen','Laba_Saat_Grosir_1_Dalam_Rupiah','Harga_Jual_Saat_Grosir_1','Minimal_Pembelian_Grosir_2','Laba_Saat_Grosir_2_Dalam_Persen','Laba_Saat_Grosir_2_Dalam_Rupiah','Harga_Jual_Saat_Grosir_2','Minimal_Pembelian_Grosir_3','Laba_Saat_Grosir_3_Dalam_Persen','Laba_Saat_Grosir_3_Dalam_Rupiah','Harga_Jual_Saat_Grosir_3','Catatan','Foto_Produk_1','Foto_Produk_2','Foto_Produk_3','Foto_Produk_4','Foto_Produk_5','Foto_Produk_6','Foto_Produk_7','Foto_Produk_8','Foto_Produk_9','Foto_Video','Posisi_Barang', 'Warning_Stok') Values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}', '{}')".format(self.page3_cui_No, self.page3_cui_SKU_Induk, self.page3_cui_SKU_Varian_1, self.page3_cui_SKU_Varian_2, self.page3_cui_Kode_Toko, self.page3_cui_Barcode_Produk, self.page3_cui_Nama_Produk_Di_Distributor, self.page3_cui_Nama_Produk_Di_Toko, self.page3_cui_Repack, self.page3_cui_Produk_umum_khusus, self.page3_cui_Deskripsi_Produk, self.page3_cui_Total_Stok, self.page3_cui_Total_Stok_Satuan, self.page3_cui_Berat_atau_Volume_Bersih, self.page3_cui_Satuan_Berat_Bersih, self.page3_cui_Berat_Untuk_Pengiriman_Dalam_Gram, self.page3_cui_Kemasan, self.page3_cui_Perizinan, self.page3_cui_Kode_BPOM_atau_PIRT, self.page3_cui_Label_Halal, self.page3_cui_Produsen, self.page3_cui_Distributor, self.page3_cui_Nama_Sales, self.page3_cui_No_Telepon_Sales, self.page3_cui_Harga_Beli_Terakhir, self.page3_cui_Biaya_Penanganan, self.page3_cui_Laba_Dasar_Dalam_Persen, self.page3_cui_Laba_Dasar_Dalam_Rupiah, self.page3_cui_Harga_Jual_Dasar, self.page3_cui_Laba_Saat_Diskon_Dalam_Persen, self.page3_cui_Laba_Saat_Diskon_Dalam_Rupiah, self.page3_cui_Harga_Jual_Saat_Diskon, self.page3_cui_Minimal_Pembelian_Grosir_1, self.page3_cui_Laba_Saat_Grosir_1_Dalam_Persen, self.page3_cui_Laba_Saat_Grosir_1_Dalam_Rupiah, self.page3_cui_Harga_Jual_Saat_Grosir_1, self.page3_cui_Minimal_Pembelian_Grosir_2, self.page3_cui_Laba_Saat_Grosir_2_Dalam_Persen, self.page3_cui_Laba_Saat_Grosir_2_Dalam_Rupiah, self.page3_cui_Harga_Jual_Saat_Grosir_2, self.page3_cui_Minimal_Pembelian_Grosir_3, self.page3_cui_Laba_Saat_Grosir_3_Dalam_Persen, self.page3_cui_Laba_Saat_Grosir_3_Dalam_Rupiah, self.page3_cui_Harga_Jual_Saat_Grosir_3, self.page3_cui_Catatan, self.page3_cui_Foto_Produk_1, self.page3_cui_Foto_Produk_2, self.page3_cui_Foto_Produk_3, self.page3_cui_Foto_Produk_4, self.page3_cui_Foto_Produk_5, self.page3_cui_Foto_Produk_6, self.page3_cui_Foto_Produk_7, self.page3_cui_Foto_Produk_8, self.page3_cui_Foto_Produk_9, self.page3_cui_Foto_Video, self.page3_cui_Posisi_Barang, self.page3_cui_Warning_Stok))
        self.page3_cui_DBProduk_connection.commit()
        self.page3_cui_DBProduk_connection.close()
        self.Dialog_Simpan.close()
        self.Page3_cui_Cetak_Label_Harga1()
        self.Dialog.close()
        self.Data.page3_pushButton_3.click()

    # Cetak Label Harga (Inisiasi)
    def Page3_cui_Cetak_Label_Harga1(self):
        Barcode = self.page3_cui_LineEdit_4.text()
        Nama_Produk = self.page3_cui_LineEdit_3.text()
        Harga = self.page3_cui_LineEdit_19.text()

        def Rak():
            if len(Barcode) > 0:
                if len(Nama_Produk) > 0:
                    if len(Harga) > 1:
                        Dialog.close()
                        self.Page3_cui_Cetak_Label_Harga2(Barcode, Nama_Produk, Harga)
                    else:
                        Dialog.close()
                        self.Page3_cui_Pesan_Error("Gagal Cetak Harga", "Harga Jual Produk tidak boleh kosong")
                else:
                    Dialog.close()
                    self.Page3_cui_Pesan_Error("Gagal Cetak Harga", "Nama Produk tidak boleh kosong")
            else:
                Dialog.close()
                self.Page3_cui_Pesan_Error("Gagal Cetak Harga", "Barcode Produk tidak boleh kosong")

        def Showcase():
            if len(Barcode) > 0:
                if len(Nama_Produk) > 0:
                    if len(Harga) > 1:
                        Dialog.close()
                        self.Page3_cui_Cetak_Label_Harga3(Barcode, Nama_Produk, Harga)
                    else:
                        Dialog.close()
                        self.Page3_cui_Pesan_Error("Gagal Cetak Harga", "Harga Jual Produk tidak boleh kosong")
                else:
                    Dialog.close()
                    self.Page3_cui_Pesan_Error("Gagal Cetak Harga", "Nama Produk tidak boleh kosong")
            else:
                Dialog.close()
                self.Page3_cui_Pesan_Error("Gagal Cetak Harga", "Barcode Produk tidak boleh kosong")

        Dialog = QtWidgets.QDialog()
        Dialog.setWindowTitle("Cetak Harga")
        Dialog.setModal(True)

        Layout = QtWidgets.QGridLayout(Dialog)
        Text = QtWidgets.QLabel("Pilih ukuran hasil cetak")
        Layout.addWidget(Text, 0, 1, 1, 3)

        PushButton_Showcase = QtWidgets.QPushButton("Showcase")
        Layout.addWidget(PushButton_Showcase, 1, 2)
        PushButton_Showcase.clicked.connect(Showcase)

        PushButton_Rak = QtWidgets.QPushButton("Gondola Rak")
        Layout.addWidget(PushButton_Rak, 1, 3)
        PushButton_Rak.clicked.connect(Rak)

        Dialog.show()
        Dialog.exec_()

    # Cetak Label untuk Rak
    def Page3_cui_Cetak_Label_Harga2(self, Barcode, Nama_Produk, Harga):
        printer = Usb(0x0483, 0x5840, 0, 0x58, 0x03)
        locale.setlocale(locale.LC_ALL, "en_ID")
        NamaProduk = Nama_Produk
        Harga = locale.format_string("%d", int(Harga), grouping=True)

        lebar_cetak = 402
        tinggi_barcode = 100

        code128.image(Barcode, tinggi_barcode).save("{}.png".format(Barcode))
        img = Image.open('{}.png'.format(Barcode))
        wpercent = (lebar_cetak / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((lebar_cetak, hsize), Image.ANTIALIAS)
        img.save("{}.png".format(Barcode))

        printer.set("center", "a", False, 0, width=1, height=1, custom_size=False)
        printer.text("--------------------------------")
        printer.text("\n{}".format(NamaProduk))
        printer.text("\n")
        printer.set("center", "a", True, 0, width=8, height=8, custom_size=True)
        printer.text("\nRp. " + str(Harga) + ",-")
        printer.set("center", "a", False, 0, width=1, height=1, custom_size=False)
        printer.text("\n")
        printer.text("\n({})".format(Barcode))
        printer.text("\n--------------------------------")
        printer.text("\n\n")
        printer.close()

    # Cetak Label untuk Showcase
    def Page3_cui_Cetak_Label_Harga3(self, Barcode, Nama_Produk, harga):
        printer = Usb(0x0483, 0x5840, 0, 0x58, 0x03)
        NamaProduk = Nama_Produk
        locale.setlocale(locale.LC_ALL, "en_ID")
        Harga = locale.format_string("%d", val=int(harga), grouping=True)

        lebar_cetak = 402
        tinggi_barcode = 100

        code128.image(Barcode, tinggi_barcode).save("{}.png".format(Barcode))
        img = Image.open('{}.png'.format(Barcode))
        wpercent = (lebar_cetak / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((lebar_cetak, hsize), Image.ANTIALIAS)
        img.save("{}.png".format(Barcode))

        printer.set("center", "b", False, 0, width=1, height=1, custom_size=False)
        printer.text("\n------------------------------------------")
        printer.text("\n{}".format(NamaProduk))
        printer.set("center", "a", True, 0, width=8, height=8, custom_size=True)
        printer.text("\nRp. " + str(Harga) + ",-")
        printer.set("center", "b", False, 0, width=1, height=1, custom_size=False)
        printer.text("\n({})".format(Barcode))
        printer.text("\n------------------------------------------")
        printer.text("\n\n")
        printer.close()


# Page3_Tab2
class Page3_t2(Page3):
    def __init__(self, data):
        self.Data = data
        self.Page3_t2_GridLayout()
        self.Page3_t2_HBoxLayout()
        self.Page3_t2_Label()
        self.Page3_t2_LineEdit()
        self.Page3_t2_PushButton()
        self.Page3_t2_TableWidget()
        self.Page3_t2_HBoxLayout_2()
        self.Page3_t2_PushButton_3()
        self.Page3_t2_PushButton_2()
        self.Page3_t2_PushButton_4()

        self.Page3_t2_Inisiasi_Data()
        self.Page3_t2_TableWidget_View()
        self.Page3_t2_LineEdit_Set_Completer()
        self.Page3_t2_Editing_Mode()

        # PERINTAH
        self.page3_t2_PushButton.clicked.connect(self.Page3_t2_PushButton_Clicked)
        self.page3_t2_PushButton_2.clicked.connect(lambda: self.Page3_t2_PushButton_2_Clicked())
        self.page3_t2_PushButton_3.clicked.connect(self.Page3_t2_PushButton_3_Clicked)
        self.page3_t2_PushButton_4.clicked.connect(self.Page3_t2_PushButton_4_Clicked)

    def Page3_t2_GridLayout(self):
        self.page3_t2_GridLayout = QtWidgets.QGridLayout(self.Data.page3_tab3_Tab2)

    def Page3_t2_HBoxLayout(self):
        self.page3_t2_HBoxLayout = QtWidgets.QHBoxLayout()
        self.page3_t2_GridLayout.addLayout(self.page3_t2_HBoxLayout, 0, 0)

    def Page3_t2_Label(self):
        self.page3_t2_label = QtWidgets.QLabel("Cari Item : ")
        self.page3_t2_HBoxLayout.addWidget(self.page3_t2_label)

    def Page3_t2_LineEdit(self):
        self.page3_t2_LineEdit = QtWidgets.QLineEdit()
        self.page3_t2_HBoxLayout.addWidget(self.page3_t2_LineEdit)

    def Page3_t2_PushButton(self):
        self.page3_t2_PushButton = QtWidgets.QPushButton("Cari")
        self.page3_t2_HBoxLayout.addWidget(self.page3_t2_PushButton)

    def Page3_t2_TableWidget(self):
        self.page3_t2_TableWidget = QtWidgets.QTableWidget()
        self.page3_t2_TableWidget.setSelectionBehavior(1)
        self.page3_t2_TableWidget.setSortingEnabled(True)
        self.page3_t2_GridLayout.addWidget(self.page3_t2_TableWidget, 1, 0)

    def Page3_t2_HBoxLayout_2(self):
        self.page3_t2_HBoxLayout_2 = QtWidgets.QHBoxLayout()
        self.page3_t2_GridLayout.addLayout(self.page3_t2_HBoxLayout_2, 2, 0)

    def Page3_t2_PushButton_3(self):
        self.page3_t2_PushButton_3 = QtWidgets.QPushButton("Refresh Halaman")
        self.page3_t2_HBoxLayout_2.addWidget(self.page3_t2_PushButton_3, alignment=Qt.AlignHCenter)

    def Page3_t2_PushButton_2(self):
        self.page3_t2_PushButton_2 = QtWidgets.QPushButton("Lihat Detail")
        self.page3_t2_HBoxLayout_2.addWidget(self.page3_t2_PushButton_2, alignment=Qt.AlignHCenter)

    def Page3_t2_PushButton_4(self):
        self.page3_t2_PushButton_4 = QtWidgets.QPushButton("To BlackList")
        self.page3_t2_HBoxLayout_2.addWidget(self.page3_t2_PushButton_4, alignment=Qt.AlignHCenter)

    def Page3_t2_Inisiasi_Data(self):
        conn = sqlite3.connect(DatabaseProduk())
        conn.row_factory = sqlite3.Row
        curr = conn.cursor()

        barcode = curr.execute("select name from sqlite_master where type='table' order by name").fetchall()
        self.page3_t2_Barcode = []
        for item in range(len(barcode)):
            if barcode[item]['name'] not in self.page3_t2_Barcode:
                self.page3_t2_Barcode.append(barcode[item]['name'])
            else:
                pass

        self.BlackList_conn = sqlite3.connect(DatabaseBlacklistProduk())
        self.BlackList_conn.row_factory = sqlite3.Row
        self.BlackList_curr = self.BlackList_conn.cursor()
        BlackListProduk = self.BlackList_curr.execute("select Barcode from BlackListOrder").fetchall()
        BlackListProduk_List = []
        for BlackListProduk_No in range(len(BlackListProduk)):
            BlackListProduk_List.append(str(BlackListProduk[BlackListProduk_No]["Barcode"]))

        for BlackListProduk_Item in BlackListProduk_List:
            try:
                self.page3_t2_Barcode.remove(str(BlackListProduk_Item))
            except:
                pass
        conn.close()

    def Page3_t2_TableWidget_View(self):
        jumlahbaris = self.page3_t2_TableWidget.rowCount()
        while jumlahbaris != 0:
            jumlahbaris = self.page3_t2_TableWidget.rowCount()
            self.page3_t2_TableWidget.removeRow(0)
        else:
            pass

        conn = sqlite3.connect(DatabaseProduk())
        conn.row_factory = sqlite3.Row
        curr = conn.cursor()

        # Inisialisasi Jumlah dan Nama pada Baris dan Kolom
        self.page3_t2_TableWidget_Kolom = ["No", "Barcode", "Kode Toko", "Nama Produk", "Current Stok", "Warning Stok", "Perlu Diorder", "Expired Date", "Jarak Ke Expired", "Distributor"]
        Jumlah_Kolom = len(self.page3_t2_TableWidget_Kolom)
        Jumlah_Baris = len(self.page3_t2_Barcode)
        Index_to_Kolom = {}
        Kolom_to_Index = {}
        No = 0
        self.page3_t2_TableWidget.setRowCount(Jumlah_Baris)
        self.page3_t2_TableWidget.setColumnCount(Jumlah_Kolom)
        self.page3_t2_TableWidget.verticalHeader().hide()

        for item in range(Jumlah_Kolom):
            Kolom_dict1 = {item: self.page3_t2_TableWidget_Kolom[item]}
            Index_to_Kolom.update(Kolom_dict1)
            Kolom_dict2 = {self.page3_t2_TableWidget_Kolom[item]: item}
            Kolom_to_Index.update(Kolom_dict2)

        for item2 in self.page3_t2_TableWidget_Kolom:
            self.page3_t2_TableWidget.setHorizontalHeaderItem(Kolom_to_Index[item2], QtWidgets.QTableWidgetItem(item2))

        for item3 in range(Jumlah_Baris):
            No += 1
            def KolomNomor():
                Nomor = QtWidgets.QTableWidgetItem()
                Nomor.setData(QtCore.Qt.DisplayRole, No)
                self.page3_t2_TableWidget.setItem(item3, Kolom_to_Index["No"], Nomor)
                self.page3_t2_TableWidget.horizontalHeader().setSectionResizeMode(Kolom_to_Index["No"], QtWidgets.QHeaderView.ResizeToContents)

            def KolomBarcode():
                Barcode = self.page3_t2_Barcode[item3]
                Barcode_item = QtWidgets.QTableWidgetItem()
                Barcode_item.setData(QtCore.Qt.DisplayRole, Barcode)
                self.page3_t2_TableWidget.setItem(item3, Kolom_to_Index["Barcode"], Barcode_item)

            def KolomKodeToko():
                current_row = item3
                Barcode_for_KodeToko = self.page3_t2_TableWidget.item(item3, Kolom_to_Index["Barcode"]).text()
                KodeToko = curr.execute("SELECT Kode_Toko FROM '{}'".format(str(Barcode_for_KodeToko))).fetchone()
                KodeToko_Value = KodeToko[0]
                KodeToko_Item = QtWidgets.QTableWidgetItem()
                KodeToko_Item.setData(QtCore.Qt.DisplayRole, KodeToko_Value)
                self.page3_t2_TableWidget.setItem(current_row, Kolom_to_Index["Kode Toko"], KodeToko_Item)

            def KolomNamaProduk():
                current_row = item3
                Barcode_for_NamaProduk = self.page3_t2_TableWidget.item(item3, Kolom_to_Index["Barcode"]).text()
                NamaProduk = curr.execute("SELECT Nama_Produk FROM '{}'".format(str(Barcode_for_NamaProduk))).fetchone()
                NamaProduk_Value = NamaProduk[0]
                NamaProduk_Item = QtWidgets.QTableWidgetItem()
                NamaProduk_Item.setData(QtCore.Qt.DisplayRole, NamaProduk_Value)
                self.page3_t2_TableWidget.setItem(current_row, Kolom_to_Index["Nama Produk"], NamaProduk_Item)


            def KolomCurrentStok():
                current_row = item3
                Barcode_for_Current_Stok = self.page3_t2_TableWidget.item(item3, Kolom_to_Index["Barcode"]).text()
                Stok = curr.execute("SELECT Total_Stok_Sekarang FROM '{}'".format(str(Barcode_for_Current_Stok))).fetchall()
                TotalStok = 0
                for item4 in range(len(Stok)):
                    stokPerItem = curr.execute("SELECT Total_Stok_Sekarang FROM '{}' WHERE No='{}'".format(Barcode_for_Current_Stok, item4+1)).fetchall()[0]["Total_Stok_Sekarang"]
                    try:
                        TotalStok += int(stokPerItem)
                    except:
                        TotalStok += 0
                TotalStok_Item = QtWidgets.QTableWidgetItem()
                TotalStok_Item.setData(QtCore.Qt.DisplayRole, TotalStok)
                self.page3_t2_TableWidget.setItem(current_row, Kolom_to_Index["Current Stok"], TotalStok_Item)

            def KolomWarningStok():
                current_row = item3
                Barcode_for_WarningStok = self.page3_t2_TableWidget.item(item3, Kolom_to_Index["Barcode"]).text()
                TotalTransaksi = curr.execute("SELECT Limit_Stok_Bawah FROM '{}'".format(Barcode_for_WarningStok)).fetchall()
                WarningStok = curr.execute("SELECT Limit_Stok_Bawah FROM '{}' WHERE No='{}'".format(Barcode_for_WarningStok, len(TotalTransaksi))).fetchone()[0]
                WarningStok_Item = QtWidgets.QTableWidgetItem()
                WarningStok_Item.setData(QtCore.Qt.DisplayRole, int(WarningStok))
                self.page3_t2_TableWidget.setItem(current_row, Kolom_to_Index["Warning Stok"], WarningStok_Item)

            def KolomPerluDiorder():
                current_row = item3
                TotalStok = int(self.page3_t2_TableWidget.item(current_row, Kolom_to_Index["Current Stok"]).text())
                WarningStok = int(self.page3_t2_TableWidget.item(current_row, Kolom_to_Index["Warning Stok"]).text())
                if TotalStok > WarningStok:
                    perluDiorder = 0
                else:
                    perluDiorder = (WarningStok - TotalStok) + 1
                perluDiorder_Item = QtWidgets.QTableWidgetItem()
                perluDiorder_Item.setData(QtCore.Qt.DisplayRole, perluDiorder)
                self.page3_t2_TableWidget.setItem(current_row, Kolom_to_Index["Perlu Diorder"], perluDiorder_Item)

            def KolomExpiredDate():
                current_row = int(self.page3_t2_TableWidget.item(item3, Kolom_to_Index["No"]).text())-1
                Barcode_for_ExpiredDate = self.page3_t2_TableWidget.item(item3, Kolom_to_Index["Barcode"]).text()
                ExpiredDate_AllItem = curr.execute("SELECT Expired_Date FROM '{}'".format(Barcode_for_ExpiredDate)).fetchall()
                ED_List = []
                for item4 in range(len(ExpiredDate_AllItem)):
                    ED = curr.execute("SELECT Expired_Date FROM '{}' WHERE No='{}'".format(Barcode_for_ExpiredDate, item4+1)).fetchone()[0]
                    StokPerItem = curr.execute("SELECT Total_Stok_Sekarang FROM '{}' WHERE No='{}'".format(Barcode_for_ExpiredDate, item4+1)).fetchone()[0]
                    try:
                        if int(StokPerItem) > 0:
                            ED_List.append(str(ED))
                        else:
                            ED_List.append("99991231")
                    except:
                        ED_List.append("")
                        pass
                ED_List.sort()
                try:
                    ED_Value = int(ED_List[0])
                except:
                    ED_Value = 99991231
                ED_Item = QtWidgets.QTableWidgetItem()
                ED_Item.setData(QtCore.Qt.DisplayRole, ED_Value)
                self.page3_t2_TableWidget.setItem(current_row, Kolom_to_Index["Expired Date"], ED_Item)

            def KolomJarakExpiredDate():
                currentDate = QtCore.QDate.currentDate()
                ExpiredDate = self.page3_t2_TableWidget.item(item3, Kolom_to_Index["Expired Date"]).text()
                ED_year = ExpiredDate[0:4]
                ED_month = ExpiredDate[4:6]
                ED_days = ExpiredDate[6:8]
                try:
                    Jarak = int(currentDate.daysTo(QtCore.QDate(int(ED_year), int(ED_month), int(ED_days))))
                except:
                    self.Page3_PesanError("Jarak Error", "Jarak yang ditampilkan tidak sesuai karena kesalahan input")
                    Jarak = 0
                Jarak_item = QtWidgets.QTableWidgetItem()
                Jarak_item.setData(QtCore.Qt.DisplayRole, Jarak)
                self.page3_t2_TableWidget.setItem(item3, Kolom_to_Index["Jarak Ke Expired"], Jarak_item)

            def KolomDistributor():
                barcode = self.page3_t2_TableWidget.item(item3, Kolom_to_Index["Barcode"]).text()
                jumlahTransaksiPerBarcode = curr.execute("SELECT * FROM '{}'".format(barcode)).fetchall()
                Distributor = curr.execute("SELECT Distributor FROM '{}' WHERE No='{}'".format(barcode, len(jumlahTransaksiPerBarcode))).fetchone()[0]
                Distributor_Item = QtWidgets.QTableWidgetItem()
                Distributor_Item.setData(QtCore.Qt.DisplayRole, Distributor)
                self.page3_t2_TableWidget.setItem(item3, Kolom_to_Index["Distributor"], Distributor_Item)

            KolomNomor()
            KolomBarcode()
            KolomKodeToko()
            KolomNamaProduk()
            KolomCurrentStok()
            KolomWarningStok()
            KolomPerluDiorder()
            KolomExpiredDate()
            KolomJarakExpiredDate()
            KolomDistributor()

        self.page3_t2_TableWidget.horizontalHeader().setSectionResizeMode(Kolom_to_Index["Nama Produk"], QtWidgets.QHeaderView.ResizeToContents)
        self.page3_t2_TableWidget.horizontalHeader().setSectionResizeMode(Kolom_to_Index["Distributor"], QtWidgets.QHeaderView.ResizeToContents)

        self.page3_t2_TableWidget.selectRow(-1)
        conn.close()

    def Page3_t2_LineEdit_Set_Completer(self):
        conn = sqlite3.connect(DatabaseProduk())
        curr = conn.cursor()
        ListBarcode = []
        Gabungan = []
        Barcode = curr.execute("select name from sqlite_master where type='table'").fetchall()
        for item in range(len(Barcode)):
            if Barcode[item][0] not in ListBarcode:
                ListBarcode.append(Barcode[item][0])

            if Barcode[item][0] not in Gabungan:
                Gabungan.append(Barcode[item][0])
        ListBarcode.remove("Data_Produk_Master")
        Gabungan.remove("Data_Produk_Master")
        for item in ListBarcode:
            Kode_Toko = curr.execute("select Kode_Toko from '{}'".format(item)).fetchone()[0]
            if Kode_Toko not in Gabungan:
                Gabungan.append(Kode_Toko)
            else:
                pass
            Nama_Produk = curr.execute("select Nama_Produk from '{}'".format(item)).fetchone()[0]
            if Nama_Produk not in Gabungan:
                Gabungan.append(Nama_Produk)
            else:
                pass
            Distributor = curr.execute("select Distributor from '{}'".format(item)).fetchall()
            for item2 in range(len(Distributor)):
                Distributor_Item = Distributor[item2][0]
                if Distributor_Item not in Gabungan:
                    Gabungan.append(Distributor_Item)
                else:
                    pass

        LineEdit_Completer = QtWidgets.QCompleter(Gabungan)
        LineEdit_Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        LineEdit_Completer.setFilterMode(QtCore.Qt.MatchContains)
        self.page3_t2_LineEdit.setCompleter(LineEdit_Completer)
        LineEdit_Completer.activated.connect(self.Page3_t2_PushButton_Clicked)
        conn.close()

    def Page3_t2_PushButton_Clicked(self):
        self.Page3_t2_TableWidget_View()
        self.Page3_t2_LineEdit_Set_Completer()

        JumlahData = self.page3_t2_TableWidget.rowCount()
        for Data in range(JumlahData):
            self.page3_t2_TableWidget.hideRow(Data)
        Barcode = []
        Kode_Toko = []
        Nama_Produk = []
        Distributor = []
        BarcodeDict = {}
        Kode_Toko_to_Row_dict = {}
        Nama_Produk_to_Row_dict = {}
        Distributor_to_Row_dict = {}
        for item in range(JumlahData):
            Barcode.append(self.page3_t2_TableWidget.item(item, 1).text())
            Nomor_Baris = item
            Kode_Toko.append(self.page3_t2_TableWidget.item(item, 2).text())
            Nama_Produk.append(self.page3_t2_TableWidget.item(item, 3).text())
            dict = {self.page3_t2_TableWidget.item(item, 1).text(): Nomor_Baris}
            dict2 = {self.page3_t2_TableWidget.item(item, 2).text(): Nomor_Baris}
            dict3 = {self.page3_t2_TableWidget.item(item, 3).text(): Nomor_Baris}
            try:
                if self.page3_t2_TableWidget.item(item, 9).text() not in Distributor:
                    Distributor.append(self.page3_t2_TableWidget.item(item, 9).text())
                    dict4 = {self.page3_t2_TableWidget.item(item, 9).text(): Nomor_Baris}
                else:
                    Distributor.append(((self.page3_t2_TableWidget.item(item, 9).text())+str(item)))
                    dict4 = {((self.page3_t2_TableWidget.item(item, 9).text())+str(item)): Nomor_Baris}
            except:
                dict4 = {"": ""}
                pass
            BarcodeDict.update(dict)
            Kode_Toko_to_Row_dict.update(dict2)
            Nama_Produk_to_Row_dict.update(dict3)
            Distributor_to_Row_dict.update(dict4)
        text = self.page3_t2_LineEdit.text().upper()
        for item2 in Barcode:
            if text in item2.upper():
                row = BarcodeDict["{}".format(item2)]
                self.page3_t2_TableWidget.showRow(row)
        for item3 in Kode_Toko:
            if text in item3.upper():
                row = Kode_Toko_to_Row_dict["{}".format(item3)]
                self.page3_t2_TableWidget.showRow(row)
        for item4 in Nama_Produk:
            if text in item4.upper():
                row = Nama_Produk_to_Row_dict["{}".format(item4)]
                self.page3_t2_TableWidget.showRow(row)
        for item5 in Distributor:
            if text in item5.upper():
                row = Distributor_to_Row_dict["{}".format(item5)]
                self.page3_t2_TableWidget.showRow(row)
        print(self.page3_t2_TableWidget.rowCount())

    def Page3_t2_PushButton_2_Clicked(self):
        try:
            row = self.page3_t2_TableWidget.currentItem().row()
            barcode = self.page3_t2_TableWidget.item(row, 1).text()
            namaproduk = self.page3_t2_TableWidget.item(row, 3).text()
            objek = Page3_t2_tt(self, barcode, namaproduk)
        except:
            self.Page3_PesanError("Tentukan Produk", "Anda belum memilih produk, \nsilakan pilih produk yang akan diedit terlebih dahulu")
            pass

    def Page3_t2_PushButton_3_Clicked(self):
        jumlahBaris = self.page3_t2_TableWidget.rowCount()
        self.page3_t2_TableWidget.sortByColumn(0, Qt.AscendingOrder)
        for item in range(jumlahBaris):
            self.page3_t2_TableWidget.removeRow(item)
            # self.page3_t2_TableWidget.setRowCount(jumlahBaris-(item+1))
        self.Page3_t2_TableWidget_View()
        self.Page3_t2_LineEdit_Set_Completer()

    def Page3_t2_PushButton_4_Clicked(self):
        conn = sqlite3.connect(DatabaseProduk())
        conn.row_factory = sqlite3.Row
        curr = conn.cursor()
        try:
            self.Page3_t2_Inisiasi_Data()
            CurrentRow = self.page3_t2_TableWidget.currentRow()
            ItemBarcode = self.page3_t2_TableWidget.item(CurrentRow, 1).text()
            ItemKode_Toko = self.page3_t2_TableWidget.item(CurrentRow, 2).text()
            NamaProduk = self.page3_t2_TableWidget.item(CurrentRow, 3).text()

            Dialog = QtWidgets.QDialog()
            Dialog.setModal(True)
            Dialog.setWindowTitle("Konfirmasi")
            Dialog_Layout = QtWidgets.QGridLayout(Dialog)
            Text = QtWidgets.QLabel("Apakah anda yakin akan memasukkan produk berikut : \n\n'{}' \n\nke dalam BlackList??\n".format(NamaProduk))
            Dialog_Layout.addWidget(Text, 0, 0)
            Dialog_HBoxLayout = QtWidgets.QHBoxLayout()
            Dialog_Layout.addLayout(Dialog_HBoxLayout, 1, 0)
            PushButton1 = QtWidgets.QPushButton("Ya")
            Dialog_HBoxLayout.addWidget(PushButton1, alignment=Qt.AlignHCenter)
            PushButton2 = QtWidgets.QPushButton("Tidak")
            Dialog_HBoxLayout.addWidget(PushButton2, alignment=Qt.AlignHCenter)
            def PushButton1_Clicked():
                try:
                    self.BlackList_curr.execute("INSERT INTO BlackListOrder (Barcode, Kode_Toko) VALUES ('{}','{}')".format(ItemBarcode, ItemKode_Toko))
                    self.BlackList_conn.commit()
                    self.BlackList_conn.close()
                    print(CurrentRow, ItemBarcode, ItemKode_Toko)
                    Dialog.close()
                    self.BlackList_conn.close()
                except:
                    self.Page3_PesanError("BlackList Duplikat", "Data sudah ada dalam BlackList")
                    self.BlackList_conn.close()
                    Dialog.close()
            def PushButton2_Clicked():
                Dialog.close()
            PushButton1.clicked.connect(PushButton1_Clicked)
            PushButton2.clicked.connect(PushButton2_Clicked)
            Dialog.show()
            Dialog.exec_()

        except:
            self.Page3_PesanError("Konfirmasi", "Anda belum menentukan pilihan.\nSilakan tentukan produk yang ingin dimasukkan ke dalam blacklist terlebih dahulu.")

        conn.close()

    def Page3_t2_SignalEmited(self):
        print("ini adalah signal")

    def Page3_t2_Editing_Mode(self):
        self.page3_t2_LineEdit.setPlaceholderText("page3_t2_LineEdit")
        self.page3_t2_PushButton.setText("page3_t2_PushButton")
        self.page3_t2_PushButton_2.setText("page3_t2_PushButton_2")
        self.page3_t2_PushButton_3.setText("page3_t2_PushButton_3")
        self.page3_t2_PushButton_4.setText("page3_t2_PushButton_4")


class Page3_t2_tt(Page3_t2):
    def __init__(self, data, Barcode, NamaProduk):
        self.Page3_t2_tt_Data = data
        self.Page3_t2_tt_Barcode = Barcode
        self.Page3_t2_tt_Nama_Produk = NamaProduk
        self.Page3_t2_tt_Dialog = QtWidgets.QDialog()
        self.Page3_t2_tt_Dialog.setWindowTitle(str(self.Page3_t2_tt_Barcode + " - " + self.Page3_t2_tt_Nama_Produk))
        self.Page3_t2_tt_Dialog.setModal(True)
        self.page3_t2_tt_GridLayout = QtWidgets.QGridLayout(self.Page3_t2_tt_Dialog)

        # LAYOUT
        self.Page3_t2_tt_Label()
        self.Page3_t2_tt_Label_2()
        self.Page3_t2_tt_TableWidget()
        self.Page3_t2_tt_HBoxLayout()
        self.Page3_t2_tt_SpacerItem()
        self.Page3_t2_tt_PushButton()
        self.Page3_t2_tt_PushButton_2()
        self.Page3_t2_tt_PushButton_3()
        self.Page3_t2_tt_SpacerItem_2()
        self.Page3_t2_tt_PushButton_4()

        # Inisiasi Awal
        self.Page3_t2_tt_InisiasiDatabase()
        self.Total_Stok = 0
        self.Total_Stok_Kali_Harga_Beli = 0
        self.Timer()
        self.Page3_t2_tt_TableView()

        # PERINTAH
        self.page3_t2_tt_PushButton.clicked.connect(self.Page3_t2_tt_Simpan)
        self.page3_t2_tt_PushButton_2.clicked.connect(self.Page3_t2_tt_TambahTransaksiBaru)
        self.page3_t2_tt_PushButton_3.clicked.connect(self.Page3_t2_tt_HapusTransaksi)
        self.page3_t2_tt_PushButton_4.clicked.connect(self.Page3_t2_tt_Kembali)
        # Editing Mode
        # self.Page3_t2_tt_EditingMode()

        self.Page3_t2_tt_Dialog.showMaximized()
        self.Page3_t2_tt_Dialog.exec_()
        self.timer0.stop()

    def Timer(self):
        self.timer0 = QtCore.QTimer()
        self.timer0.start(0)

    def Page3_t2_tt_Label(self):
        self.page3_t2_tt_Label = QtWidgets.QLabel("DAFTAR TRANSAKSI PRODUK")
        self.page3_t2_tt_Label.setFont(Font(12, True))
        self.page3_t2_tt_Label.setAlignment(QtCore.Qt.AlignHCenter)
        self.page3_t2_tt_GridLayout.addWidget(self.page3_t2_tt_Label, 0, 0)

    def Page3_t2_tt_Label_2(self):
        self.page3_t2_tt_Label_2 = QtWidgets.QLabel("\nNama Produk      : {}\nBarcode Produk   : {}\nTransaksi           : ".format(self.Page3_t2_tt_Nama_Produk, self.Page3_t2_tt_Barcode))
        self.page3_t2_tt_Label_2.setFont(Font(10, False))
        self.page3_t2_tt_GridLayout.addWidget(self.page3_t2_tt_Label_2, 1, 0)

    def Page3_t2_tt_TableWidget(self):
        self.page3_t2_tt_TableWidget = QtWidgets.QTableWidget()
        self.page3_t2_tt_GridLayout.addWidget(self.page3_t2_tt_TableWidget, 2, 0)

    def Page3_t2_tt_HBoxLayout(self):
        self.page3_t2_tt_HBoxLayout = QtWidgets.QHBoxLayout()
        self.page3_t2_tt_GridLayout.addLayout(self.page3_t2_tt_HBoxLayout, 3, 0)

    def Page3_t2_tt_SpacerItem(self):
        self.page3_t2_tt_SpacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.page3_t2_tt_HBoxLayout.addItem(self.page3_t2_tt_SpacerItem)

    def Page3_t2_tt_PushButton(self):
        self.page3_t2_tt_PushButton = QtWidgets.QPushButton("Simpan Data")
        self.page3_t2_tt_PushButton.setFont(Font(9, True))
        self.page3_t2_tt_PushButton.setFixedSize(200, 35)
        self.page3_t2_tt_HBoxLayout.addWidget(self.page3_t2_tt_PushButton, alignment=Qt.AlignRight)

    def Page3_t2_tt_PushButton_2(self):
        self.page3_t2_tt_PushButton_2 = QtWidgets.QPushButton("Transaksi Baru")
        self.page3_t2_tt_PushButton_2.setFont(Font(9, True))
        self.page3_t2_tt_PushButton_2.setFixedSize(200, 35)
        self.page3_t2_tt_HBoxLayout.addWidget(self.page3_t2_tt_PushButton_2, alignment=Qt.AlignRight)

    def Page3_t2_tt_PushButton_3(self):
        self.page3_t2_tt_PushButton_3 = QtWidgets.QPushButton("Hapus Transaksi")
        self.page3_t2_tt_PushButton_3.setFont(Font(9, True))
        self.page3_t2_tt_PushButton_3.setFixedSize(200, 35)
        self.page3_t2_tt_HBoxLayout.addWidget(self.page3_t2_tt_PushButton_3, alignment=Qt.AlignRight)

    def Page3_t2_tt_PushButton_4(self):
        self.page3_t2_tt_PushButton_4 = QtWidgets.QPushButton("Kembali")
        self.page3_t2_tt_PushButton_4.setFont(Font(9, True))
        self.page3_t2_tt_PushButton_4.setFixedSize(200, 35)
        self.page3_t2_tt_HBoxLayout.addWidget(self.page3_t2_tt_PushButton_4, alignment=Qt.AlignRight)

    def Page3_t2_tt_SpacerItem_2(self):
        self.page3_t2_tt_SpacerItem_2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.page3_t2_tt_HBoxLayout.addItem(self.page3_t2_tt_SpacerItem_2)

    def Page3_t2_tt_InisiasiDatabase(self):
        self.page3_t2_tt_DBConnection = sqlite3.connect(DatabaseProduk())
        self.page3_t2_tt_DBConnection.row_factory = sqlite3.Row
        self.page3_t2_tt_DBCurr = self.page3_t2_tt_DBConnection.cursor()

    def Page3_t2_tt_TableView(self):
        Table_Name = self.Page3_t2_tt_Barcode
        Produk_Name = self.Page3_t2_tt_Nama_Produk

        # Inisiasi Kolom / Horizontal Header
        Kolom = ['No',
                 'Kode_Toko',
                 'Nama_Produk',
                 'Distributor',
                 'Nama_Sales',
                 'Nomor_Telepon_Sales',
                 'Kode_Produksi',
                 'Tanggal_Produksi',
                 'Expired_Date',
                 'Set_Warning_Sebelum_Expired_Date',
                 'Kode_Order',
                 'Tanggal_Order',
                 'Jumlah_Barang_Diorder',
                 'Jumlah_Barang_Diorder_Satuan',
                 'Satuan_Terkecil',
                 'Satuan_Terkecil_Satuan',
                 'Tanggal_Kedatangan',
                 'Nomor_Faktur_Dari_Distributor',
                 'Jumlah_Barang_Datang',
                 'Jumlah_Barang_Datang_Satuan',
                 'Harga_Beli_Lama_Per_Satuan_Terkecil',
                 'Harga_Beli_Baru_Per_Satuan_Terkecil_Dasar',
                 'Harga_Beli_Baru_Per_Satuan_Terkecil_Promo_Distributor',
                 'Status_Perubahan_Harga_Beli',
                 'Harga_Beli_Rata_Rata',
                 'Perubahan_Harga_Beli_Rata_Rata',
                 'Biaya_Penanganan',
                 'Laba_Dasar_Dalam_Persen',
                 'Laba_Dasar_Dalam_Rupiah',
                 'Harga_Jual_Dasar',
                 'Laba_Saat_Diskon_Dalam_Persen',
                 'Laba_Saat_Diskon_Dalam_Rupiah',
                 'Harga_Jual_Saat_Diskon',
                 'Grosir_1_Minimal_Pembelian',
                 'Grosir_1_Laba_Dalam_Persen',
                 'Grosir_1_Laba_Dalam_Rupiah',
                 'Grosir_1_Harga_Jual',
                 'Grosir_2_Minimal_Pembelian',
                 'Grosir_2_Laba_Dalam_Persen',
                 'Grosir_2_Laba_Dalam_Rupiah',
                 'Grosir_2_Harga_Jual',
                 'Grosir_3_Minimal_Pembelian',
                 'Grosir_3_Laba_Dalam_Persen',
                 'Grosir_3_Laba_Dalam_Rupiah',
                 'Grosir_3_Harga_Jual',
                 'Total_Transaksi',
                 'Konsinasi_Atau_Bukan',
                 'Tipe_Pembayaran',
                 'Status_Pembayaran',
                 'Telah_Dibayarkan',
                 'Belum_Dibayarkan',
                 'Tipe_Tempo',
                 'Tanggal_Jatuh_Tempo',
                 'Status_Return',
                 'Batas_Waktu_Return_Sebelum_ED',
                 'Set_Warning_Return_Sebelum_Batas_Waktu_Return',
                 'Status_Dikembalikan_Ke_Distributor',
                 'Jumlah_Dikembalikan_Ke_Distributor',
                 'Jumlah_Dikembalikan_Ke_Distributor_Satuan',
                 'Nilai_Dikembalikan_Ke_Distributor_Per_Satuan_Terkecil',
                 'Total_Nilai_Dikembalikan_Ke_Distributor',
                 'Alasan_Dikembalikan_Ke_Distributor',
                 'Catatan',
                 'ED_Kurang_Berapa_Hari',
                 'Terjual',
                 'Dipindahkan_Ke_Produk_Repack',
                 'Dipindahkan_Ke_Produk_Repack_Satuan',
                 'Jumlah_Rusak_Hilang_Expired',
                 'Jumlah_Rusak_Hilang_Expired_Satuan',
                 'Alasan_Rusak_Hilang_Expired',
                 'Harga_Beli_Pasaran_Terkini',
                 'Harga_Jual_Pasaran_Terkini',
                 'Harga_Jual_Pandanarum_Terkini',
                 'Limit_Stok_Bawah',
                 'Total_Stok_Sekarang',
                 'Total_Stok_Sekarang_Satuan',
                 'Tombol_1',
                 'Tombol_2',
                 'Tombol_3',
                 'Tombol_4',
                 'Tombol_5',
                 'Status_Upload_Ke_Marketplace'
                 ]
        Kolom_to_Index = {}
        for item in range(len(Kolom)):
            Text = Kolom[item]
            Index = item
            Kolom_to_Index_dict = {Text: Index}
            Kolom_to_Index.update(Kolom_to_Index_dict)

        self.page3_t2_tt_TableWidget.setColumnCount(len(Kolom))
        for item in range(len(Kolom)):
            self.page3_t2_tt_TableWidget.setHorizontalHeaderItem(item, QtWidgets.QTableWidgetItem(Kolom[item]))
            self.page3_t2_tt_TableWidget.horizontalHeader().setSectionResizeMode(item, QtWidgets.QHeaderView.ResizeToContents)
        self.page3_t2_tt_TableWidget.horizontalHeader().setFont(Font(10, True))
        self.page3_t2_tt_TableWidget.horizontalHeader().setMinimumHeight(30)


        # Inisiasi Baris / Vertical Header
        Data = self.page3_t2_tt_DBCurr.execute("select * from '{}'".format(Table_Name)).fetchall()
        JumlahData = len(Data)
        self.page3_t2_tt_TableWidget.setRowCount(JumlahData)
        self.page3_t2_tt_TableWidget.verticalHeader().hide()

        # Inisiasi Isi Tabel
        for item in range(JumlahData):
            for item2 in Kolom:
                data = Kolom.index(item2)
                self.page3_t2_tt_TableWidget.setItem(item, data, QtWidgets.QTableWidgetItem(Data[item][item2]))

        for item3 in range(JumlahData):
            self.page3_t2_tt_TableWidget.setItem(item3, 0, QtWidgets.QTableWidgetItem(str(item3+1)))

        for item4 in range(JumlahData):
            Nomor_Baris = item4+1
            Index_Baris = item4
            Nomor_Baris_Terakhir = int(self.page3_t2_tt_TableWidget.item(Index_Baris, Kolom_to_Index['No']).text())

            # Kolom Harga_Beli_Baru_Per_Satuan_Terkecil_Promo_Distributor
            def Harga_Beli_Baru_Per_Satuan_Terkecil_Promo_Distributor():
                Text1 = self.page3_t2_tt_TableWidget.item(Index_Baris, Kolom_to_Index['Harga_Beli_Baru_Per_Satuan_Terkecil_Dasar']).text()
                Text2 = self.page3_t2_tt_TableWidget.item(Index_Baris, Kolom_to_Index['Harga_Beli_Baru_Per_Satuan_Terkecil_Promo_Distributor']).text()
                if len(Text2) == 0:
                    self.page3_t2_tt_TableWidget.item(Index_Baris, Kolom_to_Index['Harga_Beli_Baru_Per_Satuan_Terkecil_Promo_Distributor']).setText(str(Text1))
                else:
                    pass

            def Status_Perubahan_Harga_Beli():
                Harga_Beli_Lama_Per_Satuan_Terkecil = self.page3_t2_tt_TableWidget.item(item4, Kolom_to_Index['Harga_Beli_Lama_Per_Satuan_Terkecil']).text()
                Harga_Beli_Baru_Per_Satuan_Terkecil_Dasar = self.page3_t2_tt_TableWidget.item(item4, Kolom_to_Index['Harga_Beli_Baru_Per_Satuan_Terkecil_Dasar']).text()
                PerubahanHarga = int(Harga_Beli_Baru_Per_Satuan_Terkecil_Dasar) - int(Harga_Beli_Lama_Per_Satuan_Terkecil)
                if PerubahanHarga != 0:
                    self.page3_t2_tt_TableWidget.item(item4, Kolom_to_Index['Status_Perubahan_Harga_Beli']).setText(str(PerubahanHarga))
                else:
                    self.page3_t2_tt_TableWidget.item(item4, Kolom_to_Index['Status_Perubahan_Harga_Beli']).setText(str(0))

            def Harga_Beli_Rata_Rata():
                self.page3_t2_tt_TableWidget.item(item4, Kolom_to_Index['Harga_Beli_Rata_Rata']).setText("")
                try:
                    Total_Stok_Sebelumnya = int(self.page3_t2_tt_TableWidget.item((item4-1), Kolom_to_Index['Total_Stok_Sekarang']).text())
                except:
                    Total_Stok_Sebelumnya = 0
                print("totalstoksebelumnya = ", Total_Stok_Sebelumnya)
                Total_Stok_Sekarang = int(self.page3_t2_tt_TableWidget.item(item4, Kolom_to_Index['Total_Stok_Sekarang']).text())
                print("totalStokSekarang = ", Total_Stok_Sekarang)
                Harga_Beli_Sebelumnya = int(self.page3_t2_tt_TableWidget.item(item4, Kolom_to_Index['Harga_Beli_Lama_Per_Satuan_Terkecil']).text())
                Harga_Beli_Sekarang = int(self.page3_t2_tt_TableWidget.item(item4, Kolom_to_Index['Harga_Beli_Baru_Per_Satuan_Terkecil_Dasar']).text())
                Total_Stok = Total_Stok_Sebelumnya + Total_Stok_Sekarang
                Total_Harga_Beli = (Total_Stok_Sebelumnya * Harga_Beli_Sebelumnya) + (Total_Stok_Sekarang * Harga_Beli_Sekarang)
                try:
                    Harga_Beli_Rata_Rata = RoundTerdekat(1, Total_Harga_Beli / Total_Stok)
                except:
                    Harga_Beli_Rata_Rata = 0
                self.page3_t2_tt_TableWidget.item(item4, Kolom_to_Index['Harga_Beli_Rata_Rata']).setText(str(Harga_Beli_Rata_Rata))



            def Tombol1():
                # Tombol 1 (Cetak Harga Jual Terupdate)
                Tombol1 = QtWidgets.QPushButton("Cetak Harga")
                if Nomor_Baris == JumlahData:
                    self.page3_t2_tt_TableWidget.setCellWidget((Nomor_Baris-1), Kolom_to_Index['Tombol_1'], Tombol1)
                else:
                    pass

            Harga_Beli_Baru_Per_Satuan_Terkecil_Promo_Distributor()
            Harga_Beli_Rata_Rata()

            Tombol1()
            self.page3_t2_tt_DBConnection.commit()

    def Page3_t2_tt_TambahTransaksiBaru(self):
        # self.Page3_t2_tt_TableView()
        JumlahData = self.page3_t2_tt_TableWidget.rowCount()
        JumlahKolom = self.page3_t2_tt_TableWidget.columnCount()
        Kolom = [self.page3_t2_tt_TableWidget.horizontalHeaderItem(item).text() for item in range(JumlahKolom)]

        ColumnDict = {}
        for indexColumn in range(JumlahKolom):
            mydictColumnName_to_ColumnIndex = {self.page3_t2_tt_TableWidget.horizontalHeaderItem(indexColumn).text(): indexColumn}
            ColumnDict.update(mydictColumnName_to_ColumnIndex)

        No_terpakai = []
        for item2 in range(JumlahData):
            try:
                No_terpakai.append(self.page3_t2_tt_TableWidget.item(item2, 0).text())
            except:
                No_terpakai.append("")

        self.page3_t2_tt_TableWidget.setRowCount(JumlahData + 1)
        Jumlah_Data = self.page3_t2_tt_TableWidget.rowCount()
        if Jumlah_Data > 0:
            No = 0
            for row in range(Jumlah_Data):
                No += 1
                self.page3_t2_tt_TableWidget.setItem(row, ColumnDict['No'], QtWidgets.QTableWidgetItem(str(No)))
        else:
            pass

        KolomDisalin = ['Kode_Toko',
                        'Nama_Produk',
                        'Distributor',
                        'Nama_Sales',
                        'Nomor_Telepon_Sales',
                        'Tanggal_Produksi',
                        'Set_Warning_Sebelum_Expired_Date',
                        'Jumlah_Barang_Diorder_Satuan',
                        'Satuan_Terkecil',
                        'Satuan_Terkecil_Satuan',
                        'Jumlah_Barang_Datang_Satuan',
                        'Harga_Beli_Lama_Per_Satuan_Terkecil',
                        'Harga_Beli_Baru_Per_Satuan_Terkecil_Dasar',
                        'Harga_Beli_Baru_Per_Satuan_Terkecil_Promo_Distributor',
                        'Status_Perubahan_Harga_Beli',
                        'Konsinasi_Atau_Bukan',
                        'Tipe_Pembayaran',
                        'Status_Pembayaran',
                        'Tipe_Tempo',
                        'Tanggal_Jatuh_Tempo',
                        'Status_Return',
                        'Batas_Waktu_Return_Sebelum_ED',
                        'Set_Warning_Return_Sebelum_Batas_Waktu_Return',
                        'Status_Dikembalikan_Ke_Distributor',
                        'Jumlah_Dikembalikan_Ke_Distributor',
                        'Jumlah_Dikembalikan_Ke_Distributor_Satuan',
                        'Nilai_Dikembalikan_Ke_Distributor_Per_Satuan_Terkecil',
                        'Total_Nilai_Dikembalikan_Ke_Distributor',
                        'Alasan_Dikembalikan_Ke_Distributor',
                        'Catatan',
                        'ED_Kurang_Berapa_Hari',
                        'Dipindahkan_Ke_Produk_Repack_Satuan',
                        'Jumlah_Rusak_Hilang_Expired_Satuan',
                        'Harga_Beli_Pasaran_Terkini',
                        'Harga_Jual_Pasaran_Terkini',
                        'Harga_Jual_Pandanarum_Terkini',
                        'Limit_Stok_Bawah',
                        'Total_Stok_Sekarang_Satuan']

        for KolomItem in KolomDisalin:
            try:
                dataSebelum = self.page3_t2_tt_TableWidget.item(JumlahData-1, ColumnDict[KolomItem]).text()
            except:
                dataSebelum = "-"
            self.page3_t2_tt_TableWidget.setItem((JumlahData), ColumnDict[KolomItem], QtWidgets.QTableWidgetItem(str(dataSebelum)))

        List_ColumnDict_Keys = list(ColumnDict.keys())

        def RubahWarnaBackground():
            try:
                text = self.page3_t2_tt_TableWidget.item(self.page3_t2_tt_TableWidget.currentRow(), self.page3_t2_tt_TableWidget.currentColumn()).text()
                if text == "":
                    self.page3_t2_tt_TableWidget.item(self.page3_t2_tt_TableWidget.currentRow(), self.page3_t2_tt_TableWidget.currentColumn()).setBackground(QtGui.QColor("red"))
                elif len(text) < 1:
                    self.page3_t2_tt_TableWidget.item(self.page3_t2_tt_TableWidget.currentRow(), self.page3_t2_tt_TableWidget.currentColumn()).setBackground(QtGui.QColor("red"))
                else:
                    self.page3_t2_tt_TableWidget.item(self.page3_t2_tt_TableWidget.currentRow(), self.page3_t2_tt_TableWidget.currentColumn()).setBackground(QtGui.QColor("white"))
            except:
                pass

        for item3 in List_ColumnDict_Keys:
            KolomDisalin.append("No")
            self.page3_t2_tt_TableWidget.cellChanged.connect(RubahWarnaBackground)
            if item3 not in KolomDisalin:
                self.page3_t2_tt_TableWidget.setItem(JumlahData, ColumnDict[item3], QtWidgets.QTableWidgetItem())
                self.page3_t2_tt_TableWidget.item(JumlahData, ColumnDict[item3]).setBackground(QtGui.QColor("red"))
            else:
                pass
            KolomDisalin.remove("No")

    def Page3_t2_tt_HapusTransaksi(self):
        try:
            if self.page3_t2_tt_TableWidget.currentRow() < 0:
                self.Page3_PesanError("Error", "Anda belum memilih item yang akan dihapus")
            else:
                self.page3_t2_tt_TableWidget.removeRow(self.page3_t2_tt_TableWidget.currentRow())
        except:
            pass

        Jumlah_Data = self.page3_t2_tt_TableWidget.rowCount()
        if Jumlah_Data > 0:
            No = 0
            for row in range(Jumlah_Data):
                No += 1
                self.page3_t2_tt_TableWidget.item(row, 0).setText(str(No))
        else:
            pass
        self.page3_t2_tt_TableWidget.setCurrentCell(-1, -1)

    def Page3_t2_tt_Simpan(self):
        if self.page3_t2_tt_TableWidget.rowCount() < 1:
            self.Page3_t2_tt_TambahTransaksiBaru()
        else:
            pass

        def Cek_KodeOrder_Duplikat():
            JumlahData = self.page3_t2_tt_TableWidget.rowCount()
            JumlahKolom = self.page3_t2_tt_TableWidget.columnCount()
            ColumnDict = {}
            for item in range(JumlahKolom):
                mydictColumnName_to_ColumnIndex = {self.page3_t2_tt_TableWidget.horizontalHeaderItem(item).text(): item}
                ColumnDict.update(mydictColumnName_to_ColumnIndex)
            KodeOrder = []
            for item2 in range(JumlahData):
                try:
                    data = str(self.page3_t2_tt_TableWidget.item(item2, ColumnDict['Kode_Order']).text()).lower()
                except:
                    data = ""
                if str(data).lower() in KodeOrder:
                    self.Page3_PesanError("Kode Order Duplikat", 'Tidak bolah ada data "Kode_Order" yang duplikat')
                else:
                    KodeOrder.append(str(data).lower())
            if JumlahData == len(KodeOrder):
                Cek_Nomor_Faktur_Duplikat()
            else:
                pass

        def Cek_Nomor_Faktur_Duplikat():
            JumlahData = self.page3_t2_tt_TableWidget.rowCount()
            JumlahKolom = self.page3_t2_tt_TableWidget.columnCount()
            ColumnDict = {}
            for item in range(JumlahKolom):
                mydictColumnName_to_ColumnIndex = {self.page3_t2_tt_TableWidget.horizontalHeaderItem(item).text(): item}
                ColumnDict.update(mydictColumnName_to_ColumnIndex)
            NomorFaktur = []
            for item2 in range(JumlahData):
                try:
                    data = str(self.page3_t2_tt_TableWidget.item(item2, ColumnDict['Nomor_Faktur_Dari_Distributor']).text()).lower()
                except:
                    data = ""
                if str(data).lower() in NomorFaktur:
                    self.Page3_PesanError("Nomor Faktur Duplikat", 'Tidak bolah ada data "Nomor_Faktur_Dari_Distributor" yang duplikat')
                else:
                    NomorFaktur.append(str(data).lower())
            if JumlahData == len(NomorFaktur):
                SimpanData()
            else:
                pass

        def SimpanData():
            table_name = self.Page3_t2_tt_Barcode
            conn = sqlite3.connect(DatabaseProduk())
            conn.commit()
            print("sukses commit")
            curr = conn.cursor()
            data = curr.execute("select * from '{}'".format(table_name)).fetchall()
            curr.execute("DELETE FROM '{}'".format(table_name))

            kolom_di_table_widget = [self.page3_t2_tt_TableWidget.horizontalHeaderItem(item).text() for item in range(self.page3_t2_tt_TableWidget.columnCount())]
            for row in range(self.page3_t2_tt_TableWidget.rowCount()):
                Nomor_sekarang = self.page3_t2_tt_TableWidget.item(row, 0).text()
                curr.execute("INSERT INTO '{}' (No) VALUES ('{}')".format(table_name, Nomor_sekarang))
                conn.commit()
                for column in range(self.page3_t2_tt_TableWidget.columnCount()):
                    try:
                        Cell_sekarang = self.page3_t2_tt_TableWidget.item(row, column).text()
                    except:
                        Cell_sekarang = ""
                    Kolom_sekarang = self.page3_t2_tt_TableWidget.horizontalHeaderItem(column).text()
                    try:
                        curr.execute("UPDATE '{}' SET '{}'='{}' WHERE No='{}'".format(table_name, Kolom_sekarang, str(Cell_sekarang), Nomor_sekarang))
                    except:
                        print('Update error')
                conn.commit()
            self.Page3_t2_tt_Dialog.close()
            conn.close()

        Cek_KodeOrder_Duplikat()

    def Page3_t2_tt_Kembali(self):
        self.Page3_t2_tt_Dialog.close()

    def Page3_t2_tt_EditingMode(self):
        self.page3_t2_tt_Label.setText("page3_t2_tt_Label")
        self.page3_t2_tt_Label_2.setText("page3_t2_tt_Label_2")
        self.page3_t2_tt_PushButton.setText("page3_t2_tt_PushButton")
        self.page3_t2_tt_PushButton_2.setText("page3_t2_tt_PushButton_2")
        self.page3_t2_tt_PushButton_3.setText("page3_t2_tt_PushButton_3")
        self.page3_t2_tt_PushButton_4.setText("page3_t2_tt_PushButton_4")


class Page3_t3(Page3):
    def __init__(self, data):
        self.Data = data
        self.Page3_t3_GridLayout()
        self.Page3_t3_Label()
        self.Page3_t3_LineEdit()
        self.Page3_t3_PushButton()
        self.Page3_t3_TableWidget()
        self.Page3_t3_HBoxLayout()
        self.Page3_t3_SpacerItem()
        self.Page3_t3_PushButton_2()
        self.Page3_t3_PushButton_3()
        self.Page3_t3_SpacerItem_2()
        self.Page3_t3_TableWidget_View()
        self.Page3_t3_LineEdit_Completer()
        # self.Page3_t3_EditingMode()

        # PERINTAH
        self.page3_t3_PushButton.clicked.connect(lambda : self.Page3_t3_PushButton_Clicked())
        self.page3_t3_PushButton_2.clicked.connect(self.Page3_t3_PushButton_2_Clicked)
        self.page3_t3_PushButton_3.clicked.connect(self.Page3_t3_PushButton_3_Clicked)

    def Page3_t3_GridLayout(self):
        self.page3_t3_GridLayout = QtWidgets.QGridLayout(self.Data.page3_tab3_Tab3)

    def Page3_t3_Label(self):
        self.page3_t3_label = QtWidgets.QLabel("Cari Item : ")
        self.page3_t3_GridLayout.addWidget(self.page3_t3_label, 0, 0)

    def Page3_t3_LineEdit(self):
        self.page3_t3_LineEdit = QtWidgets.QLineEdit()
        self.page3_t3_GridLayout.addWidget(self.page3_t3_LineEdit, 0, 1)

    def Page3_t3_PushButton(self):
        self.page3_t3_PushButton = QtWidgets.QPushButton("Cari")
        self.page3_t3_GridLayout.addWidget(self.page3_t3_PushButton, 0, 2)

    def Page3_t3_TableWidget(self):
        self.page3_t3_TableWidget = QtWidgets.QTableWidget()
        self.page3_t3_TableWidget.setSortingEnabled(True)
        self.page3_t3_GridLayout.addWidget(self.page3_t3_TableWidget, 1, 0, 1, 3)

    def Page3_t3_HBoxLayout(self):
        self.page3_t3_HBoxLayout = QtWidgets.QHBoxLayout()
        self.page3_t3_GridLayout.addLayout(self.page3_t3_HBoxLayout, 2, 0, 1, 3)

    def Page3_t3_SpacerItem(self):
        self.page3_t3_SpacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.page3_t3_HBoxLayout.addItem(self.page3_t3_SpacerItem)

    def Page3_t3_PushButton_2(self):
        self.page3_t3_PushButton_2 = QtWidgets.QPushButton("Refresh Page")
        self.page3_t3_PushButton_2.setFixedSize(200, 35)
        self.page3_t3_PushButton_2.setFont(Font(8, True))
        self.page3_t3_HBoxLayout.addWidget(self.page3_t3_PushButton_2)

    def Page3_t3_PushButton_3(self):
        self.page3_t3_PushButton_3 = QtWidgets.QPushButton("Hapus dari BlackList")
        self.page3_t3_PushButton_3.setFixedSize(200, 35)
        self.page3_t3_PushButton_3.setFont(Font(8, True))
        self.page3_t3_HBoxLayout.addWidget(self.page3_t3_PushButton_3)

    def Page3_t3_SpacerItem_2(self):
        self.page3_t3_SpacerItem_2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.page3_t3_HBoxLayout.addItem(self.page3_t3_SpacerItem_2)

    def Page3_t3_TableWidget_View(self):
        Data = self.page3_t3_TableWidget.rowCount()
        for baris in range(Data):
            self.page3_t3_TableWidget.removeRow(baris)

        conn = sqlite3.connect(DatabaseBlacklistProduk())
        curr = conn.cursor()

        Data = curr.execute("select Barcode from BlackListOrder").fetchall()
        Kolom = ["No", "Barcode", "Kode Toko", "Nama Produk", "Total Stok"]

        self.page3_t3_TableWidget.setColumnCount(len(Kolom))
        self.page3_t3_TableWidget.setRowCount(len(Data))
        self.page3_t3_TableWidget.verticalHeader().hide()
        self.page3_t3_TableWidget_Kolom_to_Index = {}
        for item in range(len(Kolom)):
            Kolom_item_dict = {Kolom[item]: item}
            self.page3_t3_TableWidget_Kolom_to_Index.update(Kolom_item_dict)

        for item2 in Kolom:
            self.page3_t3_TableWidget.setHorizontalHeaderItem(self.page3_t3_TableWidget_Kolom_to_Index[item2], QtWidgets.QTableWidgetItem(str(item2)))

        def KolomNomor():
            No = 0
            for item3 in range(len(Data)):
                No += 1
                Item = QtWidgets.QTableWidgetItem()
                Item.setData(Qt.DisplayRole, No)
                self.page3_t3_TableWidget.setItem(item3, self.page3_t3_TableWidget_Kolom_to_Index["No"], Item)

        def KolomBarcode():
            Barcode = curr.execute("select Barcode from BlackListOrder").fetchall()
            for item3 in range(self.page3_t3_TableWidget.rowCount()):
                Item = QtWidgets.QTableWidgetItem()
                Item.setData(Qt.DisplayRole, Barcode[item3][0])
                self.page3_t3_TableWidget.setItem(item3, self.page3_t3_TableWidget_Kolom_to_Index["Barcode"], Item)

        def KolomKodeToko():
            for item3 in range(self.page3_t3_TableWidget.rowCount()):
                Barcode = self.page3_t3_TableWidget.item(item3, self.page3_t3_TableWidget_Kolom_to_Index["Barcode"]).text()
                KodeToko = curr.execute("select Kode_Toko from BlackListOrder where Barcode='{}'".format(Barcode)).fetchone()[0]
                Item = QtWidgets.QTableWidgetItem()
                Item.setData(Qt.DisplayRole, KodeToko)
                self.page3_t3_TableWidget.setItem(item3, self.page3_t3_TableWidget_Kolom_to_Index["Kode Toko"], Item)

        def KolomNamaProduk():
            conn2 = sqlite3.connect(DatabaseProduk())
            curr2 = conn2.cursor()
            for item3 in range(self.page3_t3_TableWidget.rowCount()):
                Barcode = self.page3_t3_TableWidget.item(item3, self.page3_t3_TableWidget_Kolom_to_Index["Barcode"]).text()
                try:
                    NamaProduk = curr2.execute("select Nama_Produk from '{}'".format(Barcode)).fetchone()[0]
                except:
                    NamaProduk = Barcode.upper()
                Item = QtWidgets.QTableWidgetItem()
                Item.setData(Qt.DisplayRole, NamaProduk)
                self.page3_t3_TableWidget.setItem(item3, self.page3_t3_TableWidget_Kolom_to_Index["Nama Produk"], Item)
            conn2.close()
        def KolomStok():
            conn2 = sqlite3.connect(DatabaseProduk())
            curr2 = conn2.cursor()

            for item3 in range(self.page3_t3_TableWidget.rowCount()):
                Barcode = self.page3_t3_TableWidget.item(item3, self.page3_t3_TableWidget_Kolom_to_Index["Barcode"]).text()
                try:
                    DataTransaksi = curr2.execute("select Total_Stok_Sekarang from '{}'".format(Barcode)).fetchall()
                    TotalStok = 0
                    for item4 in range(len(DataTransaksi)):
                        No = item4 + 1
                        Total_Stok_Sekarang = curr2.execute("select Total_Stok_Sekarang from '{}' where No='{}'".format(Barcode, No)).fetchone()[0]
                        TotalStok += int(Total_Stok_Sekarang)
                except:
                    TotalStok = 0
                Item = QtWidgets.QTableWidgetItem()
                Item.setData(Qt.DisplayRole, int(TotalStok))
                self.page3_t3_TableWidget.setItem(item3, self.page3_t3_TableWidget_Kolom_to_Index["Total Stok"], Item)
            conn2.close()
        KolomNomor()
        KolomBarcode()
        KolomKodeToko()
        KolomNamaProduk()
        KolomStok()

        self.page3_t3_TableWidget.horizontalHeader().setSectionResizeMode(self.page3_t3_TableWidget_Kolom_to_Index["No"], QtWidgets.QHeaderView.ResizeToContents)
        self.page3_t3_TableWidget.horizontalHeader().setSectionResizeMode(self.page3_t3_TableWidget_Kolom_to_Index["Barcode"], QtWidgets.QHeaderView.ResizeToContents)
        self.page3_t3_TableWidget.horizontalHeader().setSectionResizeMode(self.page3_t3_TableWidget_Kolom_to_Index["Kode Toko"], QtWidgets.QHeaderView.ResizeToContents)
        self.page3_t3_TableWidget.horizontalHeader().setSectionResizeMode(self.page3_t3_TableWidget_Kolom_to_Index["Nama Produk"], QtWidgets.QHeaderView.Stretch)
        self.page3_t3_TableWidget.horizontalHeader().setSectionResizeMode(self.page3_t3_TableWidget_Kolom_to_Index["Total Stok"], QtWidgets.QHeaderView.ResizeToContents)
        self.page3_t3_TableWidget.sortByColumn(self.page3_t3_TableWidget_Kolom_to_Index["No"], Qt.AscendingOrder)
        conn.close()

    def Page3_t3_LineEdit_Completer(self):
        Data = self.page3_t3_TableWidget.rowCount()
        Barcode = []
        KodeToko = []
        NamaProduk = []
        Gabungan = []

        KodeToko_to_Barcode = {}
        NamaProduk_to_Barcode = {}
        for item in range(Data):
            Barcode_item = self.page3_t3_TableWidget.item(item, self.page3_t3_TableWidget_Kolom_to_Index["Barcode"]).text()
            KodeToko_Item = self.page3_t3_TableWidget.item(item, self.page3_t3_TableWidget_Kolom_to_Index["Kode Toko"]).text()
            Kodetoko_to_Barcode_Item_Dict = {KodeToko_Item: Barcode_item}
            KodeToko_to_Barcode.update(Kodetoko_to_Barcode_Item_Dict)
            NamaProduk_Item = self.page3_t3_TableWidget.item(item, self.page3_t3_TableWidget_Kolom_to_Index["Nama Produk"]).text()
            NamaProduk_to_Barcode_Item_dict = {NamaProduk_Item: Barcode_item}
            NamaProduk_to_Barcode.update(NamaProduk_to_Barcode_Item_dict)
            if Barcode_item not in Barcode:
                Barcode.append(Barcode_item)
            else:
                pass
            if Barcode_item not in Gabungan:
                Gabungan.append(Barcode_item)
            else:
                pass
            if KodeToko_Item not in KodeToko:
                KodeToko.append(KodeToko_Item)
            else:
                pass
            if KodeToko_Item not in Gabungan:
                Gabungan.append(KodeToko_Item)
            else:
                pass
            if NamaProduk_Item not in NamaProduk:
                NamaProduk.append(NamaProduk_Item)
            else:
                pass
            if NamaProduk_Item not in Gabungan:
                Gabungan.append(NamaProduk_Item)
            else:
                pass

            Completer = QtWidgets.QCompleter(Gabungan)
            Completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            Completer.setFilterMode(QtCore.Qt.MatchContains)
            self.page3_t3_LineEdit.setCompleter(Completer)

    def Page3_t3_PushButton_Clicked(self):
        self.Page3_t3_TableWidget_View()
        Data = self.page3_t3_TableWidget.rowCount()
        Barcode = []
        KodeToko = []
        NamaProduk = []

        Barcode_to_baris = {}
        KodeToko_to_Barcode = {}
        NamaProduk_to_Barcode = {}
        for item in range(Data):
            self.page3_t3_TableWidget.hideRow(item)
            Barcode_item = self.page3_t3_TableWidget.item(item,
                                                          self.page3_t3_TableWidget_Kolom_to_Index["Barcode"]).text()
            Barcode_to_baris_Item = {str(Barcode_item): item}
            Barcode_to_baris.update(Barcode_to_baris_Item)
            KodeToko_Item = self.page3_t3_TableWidget.item(item,
                                                           self.page3_t3_TableWidget_Kolom_to_Index["Kode Toko"]).text()
            Kodetoko_to_Barcode_Item_Dict = {KodeToko_Item: Barcode_item}
            KodeToko_to_Barcode.update(Kodetoko_to_Barcode_Item_Dict)
            NamaProduk_Item = self.page3_t3_TableWidget.item(item, self.page3_t3_TableWidget_Kolom_to_Index[
                "Nama Produk"]).text()
            NamaProduk_to_Barcode_Item_dict = {NamaProduk_Item: Barcode_item}
            NamaProduk_to_Barcode.update(NamaProduk_to_Barcode_Item_dict)
            if Barcode_item not in Barcode:
                Barcode.append(Barcode_item)
            else:
                pass
            if KodeToko_Item not in KodeToko:
                KodeToko.append(KodeToko_Item)
            else:
                pass
            if NamaProduk_Item not in NamaProduk:
                NamaProduk.append(NamaProduk_Item)
            else:
                pass

        text = self.page3_t3_LineEdit.text()
        for item2 in Barcode:
            if text.upper() in item2.upper():
                Barcode = item2
                row = Barcode_to_baris[Barcode]
                self.page3_t3_TableWidget.showRow(row)
            else:
                pass
        for item3 in KodeToko:
            if text.upper() in item3.upper():
                Barcode = KodeToko_to_Barcode[item3]
                row = Barcode_to_baris[Barcode]
                self.page3_t3_TableWidget.showRow(row)
            else:
                pass
        for item4 in NamaProduk:
            if text.upper() in item4.upper():
                Barcode = NamaProduk_to_Barcode[item4]
                row = Barcode_to_baris[Barcode]
                self.page3_t3_TableWidget.showRow(row)
            else:
                pass


        print("test")

    def Page3_t3_PushButton_2_Clicked(self):
        for data in range(self.page3_t3_TableWidget.rowCount()):
            self.page3_t3_TableWidget.showRow(data)
        self.page3_t3_TableWidget.sortByColumn(self.page3_t3_TableWidget_Kolom_to_Index["No"], Qt.AscendingOrder)
        self.Page3_t3_TableWidget_View()

    def Page3_t3_PushButton_3_Clicked(self):
        conn = sqlite3.connect(DatabaseBlacklistProduk())
        curr = conn.cursor()
        baris_sekarang = self.page3_t3_TableWidget.currentRow()
        if baris_sekarang < 0:
            self.Data.Page3_PesanError("Produk Belum Dipilih", "Anda belum memilih produk yang akan dihapus dari blacklist. \nSilakan pilih produk terlebih dahulu untuk dihapus dari blacklist.")
        else:
            pass

        barcode_dipilih = self.page3_t3_TableWidget.item(baris_sekarang, self.page3_t3_TableWidget_Kolom_to_Index["Barcode"]).text()
        curr.execute("DELETE from BlackListOrder where Barcode='{}'".format(barcode_dipilih))
        conn.commit()
        conn.close()
        self.page3_t3_TableWidget.sortByColumn(self.page3_t3_TableWidget_Kolom_to_Index["No"], Qt.AscendingOrder)
        JumlahBaris = self.page3_t3_TableWidget.rowCount()
        for item in range(JumlahBaris):
            self.page3_t3_TableWidget.removeRow(item)
        self.Page3_t3_TableWidget_View()

    def Page3_t3_EditingMode(self):
        self.page3_t3_label.setText("page3_t3_label")
        self.page3_t3_LineEdit.setText("page3_t3_LineEdit")
        self.page3_t3_PushButton.setText("page3_t3_PushButton")
        self.page3_t3_PushButton_2.setText("page3_t3_PushButton_2")
        self.page3_t3_PushButton_3.setText("page3_t3_PushButton_3")


class Page3_t4(Page3):
    def __init__(self, data):
        super(Page3_t4, self).__init__()
        self.Data = data

        # Definisikan Kolom
        self.Page3_t4_Kolom1 = "No"
        self.Page3_t4_Kolom2 = "Merek"
        self.Page3_t4_Kolom3 = "Item"
        self.Page3_t4_Kolom4 = "Distributor"
        self.Page3_t4_Kolom5 = "Sales"
        self.Page3_t4_Kolom6 = "Kontak_Sales"
        self.Page3_t4_Kolom7 = "Kemasan_Di_Atas_Pcs"
        self.Page3_t4_Kolom8 = "Kemasan_Di_Atas_Pcs_Satuan"
        self.Page3_t4_Kolom9 = "Harga_Beli_Per_Kemasan_Di_Atas_Pcs"
        self.Page3_t4_Kolom10 = "Laba_Dalam_Persen_Per_Kemasan_Di_Atas_Pcs"
        self.Page3_t4_Kolom11 = "Laba_Dalam_Rupiah_Per_Kemasan_Di_Atas_Pcs"
        self.Page3_t4_Kolom12 = "Biaya_Penanganan_Per_Kemasan_Di_Atas_Pcs"
        self.Page3_t4_Kolom13 = "Diskon_Per_Kemasan_Di_Atas_Pcs"
        self.Page3_t4_Kolom14 = "Harga_Jual_Per_Kemasan_Di_Atas_Pcs"
        self.Page3_t4_Kolom15 = "Isi_Dalam_Pcs"
        self.Page3_t4_Kolom16 = "Volume_Isi_Dalam_Pcs"
        self.Page3_t4_Kolom17 = "Volume_Isi_Dalam_Pcs_Satuan"
        self.Page3_t4_Kolom18 = "Harga_Beli_Per_Isi_Dalam_Pcs"
        self.Page3_t4_Kolom19 = "Laba_Dalam_Persen_Per_Isi_Dalam_Pcs"
        self.Page3_t4_Kolom20 = "Laba_Dalam_Rupiah_Per_Isi_Dalam_Pcs"
        self.Page3_t4_Kolom21 = "Biaya_Penanganan_Per_Isi_Dalam_Pcs"
        self.Page3_t4_Kolom22 = "Diskon_Per_Isi_Dalam_Pcs"
        self.Page3_t4_Kolom23 = "Harga_Jual_Per_Isi_Dalam_Pcs"
        self.Page3_t4_Kolom24 = "Minimal_Order_Ke_Distributor"
        self.Page3_t4_Kolom25 = "Minimal_Order_Ke_Distributor_Satuan"
        self.Page3_t4_Kolom26 = "Catatan"

        # Definisikan Layout
        self.Page3_t4_GridLayout()
        self.Page3_t4_Label()
        self.Page3_t4_LineEdit()
        self.Page3_t4_PushButton()
        self.Page3_t4_TableWidget()
        self.Page3_t4_HBoxLayout()
        self.Page3_t4_SpacerItem()
        self.Page3_t4_PushButton_2()
        self.Page3_t4_PushButton_3()
        self.Page3_t4_PushButton_4()
        self.Page3_t4_PushButton_5()
        self.Page3_t4_TableWidget_View()

        self.Page3_t4_EditingMode()

        # PERINTAH
        self.page3_t4_PushButton_3.clicked.connect(lambda : self.Page3_t4_PushButton_3_Clicked())
        self.page3_t4_PushButton_4.clicked.connect(lambda : self.Page3_t4_PushButton_4_Clicked())
        self.page3_t4_PushButton_5.clicked.connect(lambda : self.Page3_t4_PushButton_5_Clicked())


    def Page3_t4_GridLayout(self):
        self.page3_t4_GridLayout = QtWidgets.QGridLayout(self.Data.page3_tab3_tab4)

    def Page3_t4_Label(self):
        self.page3_t4_Label = QtWidgets.QLabel("Cari Item : ")
        self.page3_t4_GridLayout.addWidget(self.page3_t4_Label, 0, 0)

    def Page3_t4_LineEdit(self):
        self.page3_t4_LineEdit = QtWidgets.QLineEdit()
        self.page3_t4_GridLayout.addWidget(self.page3_t4_LineEdit, 0, 1)

    def Page3_t4_PushButton(self):
        self.page3_t4_PushButton = QtWidgets.QPushButton("Cari")
        self.page3_t4_GridLayout.addWidget(self.page3_t4_PushButton, 0, 2)

    def Page3_t4_TableWidget(self):
        self.page3_t4_TableWidget = QtWidgets.QTableWidget()
        self.page3_t4_GridLayout.addWidget(self.page3_t4_TableWidget, 1, 0, 1, 3)

    def Page3_t4_HBoxLayout(self):
        self.page3_t4_HBoxLayout = QtWidgets.QHBoxLayout()
        self.page3_t4_GridLayout.addLayout(self.page3_t4_HBoxLayout, 2, 0, 1, 3)

    def Page3_t4_SpacerItem(self):
        self.page3_t4_SpacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding)
        self.page3_t4_HBoxLayout.addItem(self.page3_t4_SpacerItem)

    def Page3_t4_PushButton_2(self):
        self.page3_t4_PushButton_2 = QtWidgets.QPushButton("Simpan Data")
        self.page3_t4_HBoxLayout.addWidget(self.page3_t4_PushButton_2, alignment=Qt.AlignHCenter)

    def Page3_t4_PushButton_3(self):
        self.page3_t4_PushButton_3 = QtWidgets.QPushButton("Tambah Data Baru")
        self.page3_t4_HBoxLayout.addWidget(self.page3_t4_PushButton_3, alignment=Qt.AlignHCenter)

    def Page3_t4_PushButton_4(self):
        self.page3_t4_PushButton_4 = QtWidgets.QPushButton("Hapus Data")
        self.page3_t4_HBoxLayout.addWidget(self.page3_t4_PushButton_4, alignment=Qt.AlignHCenter)

    def Page3_t4_PushButton_5(self):
        self.page3_t4_PushButton_5 = QtWidgets.QPushButton("Refresh Halaman")
        self.page3_t4_HBoxLayout.addWidget(self.page3_t4_PushButton_5, alignment=Qt.AlignHCenter)

    def Page3_t4_TableWidget_View(self):
        # Bersihkan Tabel
        JumlahBaris = self.page3_t4_TableWidget.rowCount()
        for item in range(JumlahBaris):
            self.page3_t4_TableWidget.removeRow(item)

        conn = sqlite3.connect(DatabaseKatalogProdukDanDistributor())
        curr = conn.cursor()
        self.Page3_t4_Kolom = [self.Page3_t4_Kolom1,
                               self.Page3_t4_Kolom2,
                               self.Page3_t4_Kolom3,
                               self.Page3_t4_Kolom4,
                               self.Page3_t4_Kolom5,
                               self.Page3_t4_Kolom6,
                               self.Page3_t4_Kolom7,
                               self.Page3_t4_Kolom8,
                               self.Page3_t4_Kolom9,
                               self.Page3_t4_Kolom10,
                               self.Page3_t4_Kolom11,
                               self.Page3_t4_Kolom12,
                               self.Page3_t4_Kolom13,
                               self.Page3_t4_Kolom14,
                               self.Page3_t4_Kolom15,
                               self.Page3_t4_Kolom16,
                               self.Page3_t4_Kolom17,
                               self.Page3_t4_Kolom18,
                               self.Page3_t4_Kolom19,
                               self.Page3_t4_Kolom20,
                               self.Page3_t4_Kolom21,
                               self.Page3_t4_Kolom22,
                               self.Page3_t4_Kolom23,
                               self.Page3_t4_Kolom24,
                               self.Page3_t4_Kolom25,
                               self.Page3_t4_Kolom26]
        self.page3_t4_TableWidget.setColumnCount(len(self.Page3_t4_Kolom))
        self.page3_t4_TableWidget_Kolom_to_Index = {}
        for item in range(len(self.Page3_t4_Kolom)):
            Kolomdict = {self.Page3_t4_Kolom[item]: item}
            self.page3_t4_TableWidget_Kolom_to_Index.update(Kolomdict)
            self.page3_t4_TableWidget.setHorizontalHeaderItem(item, QtWidgets.QTableWidgetItem(self.Page3_t4_Kolom[item]))
            self.page3_t4_TableWidget.horizontalHeader().setSectionResizeMode(item, QtWidgets.QHeaderView.ResizeToContents)

        # Definisikan Tampilan Row
        Data = curr.execute("select * from Katalog_Produk_Distributor").fetchall()
        JumlahData = len(Data)
        self.page3_t4_TableWidget.setRowCount(JumlahData)


        def KolomNomor():
            No = 0
            for Nomor in range(JumlahData):
                No += 1
                DataNo = QtWidgets.QTableWidgetItem()
                DataNo.setData(Qt.DisplayRole, No)
                self.page3_t4_TableWidget.setItem(Nomor, self.page3_t4_TableWidget_Kolom_to_Index[self.Page3_t4_Kolom1], DataNo)




        KolomNomor()

        # PERINTAH MINOR
        # self.page3_t4_TableWidget..connect(KolomNomor)

        conn.close()

    def Page3_t4_PushButton_3_Clicked(self):
        self.page3_t4_TableWidget.insertRow(self.page3_t4_TableWidget.rowCount())

    def Page3_t4_PushButton_4_Clicked(self):
        currentRow = self.page3_t4_TableWidget.currentRow()
        try:
            self.page3_t4_TableWidget.removeRow(currentRow)
        except:
            pass

    def Page3_t4_PushButton_5_Clicked(self):
        print(self.page3_t4_TableWidget.rowCount())
        self.Page3_t4_TableWidget_View()

    def Page3_t4_EditingMode(self):
        self.page3_t4_Label.setText("page3_t4_Label")
        self.page3_t4_LineEdit.setPlaceholderText("page3_t4_LineEdit")
        self.page3_t4_PushButton.setText("page3_t4_PushButton")
        self.page3_t4_PushButton_2.setText("page3_t4_PushButton_2")
        self.page3_t4_PushButton_3.setText("page3_t4_PushButton_3")
        self.page3_t4_PushButton_4.setText("page3_t4_PushButton_4")
        self.page3_t4_PushButton_5.setText("page3_t4_PushButton_5")


# Page3_CHI = Page3_ClassHapusItem (untuk menghapus item dalam database)
class Page3_chi(Page3):
    def __init__(self, data):
        super(Page3_chi, self).__init__()
        self.Data = data
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setModal(True)
        self.Dialog.setWindowTitle('Konfirmasi Hapus')
        self.Page3_chi_Execution()
        self.Dialog.show()
        self.Dialog.exec_()

    def Page3_chi_Database(self):
        database = DatabaseProduk()
        self.page3_chi_DBConnection = sqlite3.connect(database)
        self.page3_chi_DBCursor = self.page3_chi_DBConnection.cursor()

    def Page3_chi_VBoxLayout(self):
        self.page3_chi_VBoxLayout = QtWidgets.QVBoxLayout(self.Dialog)

    def Page3_chi_Label(self):
        # Label Konfirmasi
        self.page3_chi_Label = QtWidgets.QLabel()
        self.page3_chi_VBoxLayout.addWidget(self.page3_chi_Label)

    def Page3_chi_SpacerItem(self):
        self.page3_chi_SpacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.page3_chi_VBoxLayout.addItem(self.page3_chi_SpacerItem)

    def Page3_chi_HBoxLayout(self):
        self.page3_chi_HBoxLayout = QtWidgets.QHBoxLayout()
        self.page3_chi_VBoxLayout.addLayout(self.page3_chi_HBoxLayout)

    def Page3_chi_SpacerItem_1(self):
        self.page3_chi_SpacerItem_1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.page3_chi_HBoxLayout.addItem(self.page3_chi_SpacerItem_1)

    def Page3_chi_PushButton(self):
        # Button Pilih
        self.page3_chi_PushButton = QtWidgets.QPushButton('Pilih')

    def Page3_chi_PushButton_1(self):
        # Button Ya
        self.page3_chi_PushButton_1 = QtWidgets.QPushButton('Ya')

    def Page3_chi_PushButton_2(self):
        # Button Tidak
        self.page3_chi_PushButton_2 = QtWidgets.QPushButton('Tidak')

    def Page3_chi_SpacerItem_2(self):
        self.page3_chi_SpacerItem_2 = self.page3_chi_SpacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

    '''
    TULIS PERINTAH DISINI :
    '''

    def Page3_chi_CekCurrentCell(self):
        try:
            self.page3_chi_posisiCellSekarang = self.Data.page3_tableWidget.item(self.Data.page3_tableWidget.currentRow(), 4).text()
        except:
            self.page3_chi_posisiCellSekarang = ''

    def Page3_chi_SetTextKonfirmasi(self):
        if self.page3_chi_posisiCellSekarang == '':
            self.page3_chi_Label.setText('Anda belum memilih data yang akan dihapus')
            self.page3_chi_HBoxLayout.addWidget(self.page3_chi_PushButton)
            self.page3_chi_HBoxLayout.addItem(self.page3_chi_SpacerItem_2)
        else:
            self.page3_chi_Label.setText('Apakah anda yakin ingin menghapus data {} ?\n\n'
                                         'Data yang telah dihapus tidak dapat dikembalikan'.format(self.page3_chi_posisiCellSekarang))
            self.page3_chi_HBoxLayout.addWidget(self.page3_chi_PushButton_1)
            self.page3_chi_HBoxLayout.addWidget(self.page3_chi_PushButton_2)
            self.page3_chi_HBoxLayout.addItem(self.page3_chi_SpacerItem_2)

    def Page3_chi_CloseDialogWithoutAnyAction(self):
        self.page3_chi_DBConnection.close()
        self.Dialog.close()

    def Page3_chi_CloseDialogWithDeleteItem(self):
        if self.page3_chi_posisiCellSekarang == '':
            pass
        else:
            self.page3_chi_DBCursor.execute('DELETE from Data_Produk_Master WHERE "Kode_Toko"="{}"'.format(self.page3_chi_posisiCellSekarang))
            self.page3_chi_DBConnection.commit()
            self.page3_chi_DBConnection.close()
            self.Dialog.close()
            self.Data.Page3_TableWidgetView()
            self.Data.page3_tableWidget.setCurrentCell(-1, -1)

    def Page3_chi_PERINTAH(self):
        self.page3_chi_PushButton.clicked.connect(self.Page3_chi_CloseDialogWithoutAnyAction)
        self.page3_chi_PushButton_1.clicked.connect(self.Page3_chi_CloseDialogWithDeleteItem)
        self.page3_chi_PushButton_2.clicked.connect(self.Page3_chi_CloseDialogWithoutAnyAction)
        pass

    def Page3_chi_Execution(self):
        self.Page3_chi_Database()
        self.Page3_chi_VBoxLayout()
        self.Page3_chi_Label()
        self.Page3_chi_SpacerItem()
        self.Page3_chi_HBoxLayout()
        self.Page3_chi_SpacerItem_1()
        self.Page3_chi_PushButton()
        self.Page3_chi_PushButton_1()
        self.Page3_chi_PushButton_2()
        self.Page3_chi_SpacerItem_2()
        self.Page3_chi_CekCurrentCell()
        self.Page3_chi_SetTextKonfirmasi()

        self.Page3_chi_PERINTAH()
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page3()
    objek.Page3_Execution('Admin Page 3', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
