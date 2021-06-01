from PandanArum import *
from PandanArum import *
from MenuBar import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import requests
import json
from datetime import datetime
from pprint import pprint
import time
from xml.etree import ElementTree

class Page4(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page4, self).__init__()
        MenuBar.MenuBar_Execution(self)

    def Tab4(self):
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("Tab4")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/Tambah/Globe_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_UTAMA.addTab(self.tab4, icon16, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab4), "Marketplace")

    def GridLayout_35(self):
        self.gridLayout_35 = QtWidgets.QGridLayout(self.tab4)
        self.gridLayout_35.setObjectName("gridLayout_35")

    def Tab_MARKETPLACE_GridLayout(self):
        self.tab_MARKETPLACE_GridLayout = QtWidgets.QGridLayout()
        self.tab_MARKETPLACE_GridLayout.setObjectName("TAB_MARKETPLACE_GridLayout")
        self.gridLayout_35.addLayout(self.tab_MARKETPLACE_GridLayout, 0, 0, 1, 1)

    def Tab_MARKETPLACE_TAB(self):
        self.tab_MARKETPLACE_TAB = QtWidgets.QTabWidget(self.tab4)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab_MARKETPLACE_TAB.setFont(font)
        self.tab_MARKETPLACE_TAB.setTabBarAutoHide(False)
        self.tab_MARKETPLACE_TAB.setObjectName("TAB_MARKETPLACE_TAB")
        self.tab_MARKETPLACE_GridLayout.addWidget(self.tab_MARKETPLACE_TAB, 0, 0, 1, 1)
        self.tab_MARKETPLACE_TAB.setCurrentIndex(0)

    def Tab_MARKETPLACE_TAB_Tab1(self):
        self.tab_MARKETPLACE_TAB_Tab1 = QtWidgets.QWidget()
        self.tab_MARKETPLACE_TAB_Tab1.setObjectName("TAB_MARKETPLACE_TAB_Tab1")
        self.tab_MARKETPLACE_TAB.addTab(self.tab_MARKETPLACE_TAB_Tab1, "")
        self.tab_MARKETPLACE_TAB.setTabText(self.tab_MARKETPLACE_TAB.indexOf(self.tab_MARKETPLACE_TAB_Tab1), "Tab 1")

    def GridLayout_6(self):
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_MARKETPLACE_TAB_Tab1)
        self.gridLayout_6.setObjectName("gridLayout_6")

    def Frame_5(self):
        self.frame_5 = QtWidgets.QFrame(self.tab_MARKETPLACE_TAB_Tab1)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_6.addWidget(self.frame_5, 0, 0, 1, 1)

    def GridLayout_8(self):
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_8.setObjectName("gridLayout_8")

    def PushButton_16(self):
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_16.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.setText("Bukalapak")
        self.gridLayout_8.addWidget(self.pushButton_16, 4, 1, 1, 1)

    def SpacerItem9(self):
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem9, 6, 0, 1, 1)

    def PushButton_17(self):
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_17.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.setText("JD.ID")
        self.gridLayout_8.addWidget(self.pushButton_17, 5, 0, 1, 1)

    def PushButton_18(self):
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.setText("BliBli")
        self.gridLayout_8.addWidget(self.pushButton_18, 5, 1, 1, 1)

    def Label_2(self):
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_2.setText('Pilih Marketplace : ')

    def PushButton_12(self):
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 70))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../../../../PICTURES/LOGO - LOGO/images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon15)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setText("Tokopedia")
        self.gridLayout_8.addWidget(self.pushButton_12, 2, 0, 1, 1)

    def PushButton_15(self):
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_15.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.setText("Lazada")
        self.gridLayout_8.addWidget(self.pushButton_15, 4, 0, 1, 1)

    def SpacerItem10(self):
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem10, 1, 0, 1, 2)

    def PushButton_14(self):
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.setText("Shopee")
        self.gridLayout_8.addWidget(self.pushButton_14, 2, 1, 1, 1)

    def Page4_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        # TAB 4
        self.Tab4()  # Page 4
        self.GridLayout_35()  # Page 4
        self.Tab_MARKETPLACE_GridLayout()  # Page 4
        self.Tab_MARKETPLACE_TAB()  # Page 4
        self.Tab_MARKETPLACE_TAB_Tab1()  # Page 4
        self.GridLayout_6()  # Page 4
        self.Frame_5()  # Page 4
        self.GridLayout_8()  # Page 4
        self.PushButton_16()  # Page 4
        self.SpacerItem9()  # Page 4
        self.PushButton_17()  # Page 4
        self.PushButton_18()  # Page 4
        self.Label_2()  # Page 4
        self.PushButton_12()  # Page 4
        self.PushButton_15()  # Page 4
        self.SpacerItem10()  # Page 4
        self.PushButton_14()  # Page 4
        self.Page4_Perintah()
    def Page4_PushButton_14_clicked(self):
        Shopee()

    def Page4_Perintah(self):
        self.pushButton_14.clicked.connect(self.Page4_PushButton_14_clicked)


class Shopee(QtCore.QObject):
    def __init__(self):
        super(Shopee, self).__init__()
        self.Page4_Shopee_Dialog = QtWidgets.QDialog()
        self.Page4_Shopee_Dialog.setWindowTitle("Shopee Area")
        self.Page4_Shopee_Dialog.setModal(True)
        self.Page4_Shopee_Layout = QtWidgets.QGridLayout(self.Page4_Shopee_Dialog)
        self.Page4_Shopee_ShopID = "332679464"

        # Definisikan Kolom Alias
        self.Page4_Shopee_Kolom1 = "No"
        self.Page4_Shopee_Kolom2 = "Nama Produk"
        self.Page4_Shopee_Kolom3 = "Barcode"
        self.Page4_Shopee_Kolom4 = "Kode Toko"
        self.Page4_Shopee_Kolom5 = "Status Upload"
        self.Page4_Shopee_Kolom6 = "SKU di Shopee"
        self.Page4_Shopee_Kolom7 = "Kode Produk di Shopee"
        self.Page4_Shopee_Kolom8 = "Kode Variasi di Shopee"
        self.Page4_Shopee_Kolom9 = "Stok di Toko"
        self.Page4_Shopee_Kolom10 = "Stok di Shopee"
        self.Page4_Shopee_Kolom11 = "Kolom 1"
        self.Page4_Shopee_Kolom12 = "Kolom 2"
        self.Page4_Shopee_Kolom13 = "Kolom 3"
        self.Page4_Shopee_Kolom14 = "Kolom 4"
        self.Page4_Shopee_Kolom15 = "Kolom 5"
        self.Page4_Shopee_Kolom16 = "Kolom 6"
        self.Page4_Shopee_Kolom17 = "Kolom 7"
        self.Page4_Shopee_Kolom18 = "Kolom 8"
        self.Page4_Shopee_Kolom19 = "Kolom 9"
        self.Page4_Shopee_Kolom20 = "Kolom 10"
        self.Page4_Shopee_TableWidget_Kolom = [self.Page4_Shopee_Kolom1,
                                               self.Page4_Shopee_Kolom2,
                                               self.Page4_Shopee_Kolom3,
                                               self.Page4_Shopee_Kolom4,
                                               self.Page4_Shopee_Kolom5,
                                               self.Page4_Shopee_Kolom6,
                                               self.Page4_Shopee_Kolom7,
                                               self.Page4_Shopee_Kolom8,
                                               self.Page4_Shopee_Kolom9,
                                               self.Page4_Shopee_Kolom10,
                                               # self.Page4_Shopee_Kolom11,
                                               # self.Page4_Shopee_Kolom12,
                                               # self.Page4_Shopee_Kolom13,
                                               # self.Page4_Shopee_Kolom14,
                                               # self.Page4_Shopee_Kolom15,
                                               # self.Page4_Shopee_Kolom16,
                                               # self.Page4_Shopee_Kolom17,
                                               # self.Page4_Shopee_Kolom18,

                                               ]

        # Definisikan Index Kolom
        self.Page4_Shopee_TableWidget_Kolom_to_Index = {}
        for item in range(len(self.Page4_Shopee_TableWidget_Kolom)):
            Kolom_To_Index_Dict = {self.Page4_Shopee_TableWidget_Kolom[item]: item}
            self.Page4_Shopee_TableWidget_Kolom_to_Index.update(Kolom_To_Index_Dict)


        self.Page4_Shopee_Label()
        self.Page4_Shopee_Label2()
        self.Page4_Shopee_TableWidget()
        self.Page4_Shopee_PushButton1()

        #PERINTAH
        self.page4_Shopee_PushButton1.clicked.connect(self.Page4_Shopee_PushButton1_clicked)

        self.Page4_Shopee_Dialog.showMaximized()
        self.Page4_Shopee_Dialog.exec_()

    def Page4_Shopee_Label(self):
        self.page4_Shopee_Label = QtWidgets.QLabel("Shopee Area")
        self.page4_Shopee_Label.setAlignment(QtCore.Qt.AlignHCenter)
        self.page4_Shopee_Label.setFont(Font(14, True))
        self.Page4_Shopee_Layout.addWidget(self.page4_Shopee_Label, 0, 0)

    def Page4_Shopee_Label2(self):
        self.page4_Shopee_Label2 = QtWidgets.QLabel("Shop ID = {}".format(self.Page4_Shopee_ShopID))
        self.page4_Shopee_Label2.setAlignment(QtCore.Qt.AlignHCenter)
        self.Page4_Shopee_Layout.addWidget(self.page4_Shopee_Label2, 1, 0)

    def Page4_Shopee_TableWidget(self):
        self.page4_Shopee_TableWidget = QtWidgets.QTableWidget()
        self.Page4_Shopee_Layout.addWidget(self.page4_Shopee_TableWidget, 2, 0)

        def LoadDataJSONProduk(url, KodeProduk):
            my_referer = "https://shopee.co.id/"
            s = requests.Session()
            s.cookies.get_dict()
            s.headers.update({'referer': my_referer})
            headers = {
                'access - control - allow - credentials': 'true',
                'Referer': 'https://shopee.co.id/product-i.332679464.9913523055',
                'Content-Type': 'application/json; charset=utf-8',
                'Content - Length': '11000',
                'User-Agent': 'pandanarum',
            }
            text2 = s.get(url, headers=headers).json()
            print(text2)
            # pprint(text2)


            # return pprint(text)

        def inisialisasiTabel():
            # Inisialisasi Kolom
            self.page4_Shopee_TableWidget.setColumnCount(len(self.Page4_Shopee_TableWidget_Kolom))
            for item in range(len(self.Page4_Shopee_TableWidget_Kolom)):
                self.page4_Shopee_TableWidget.setHorizontalHeaderItem(item, QtWidgets.QTableWidgetItem(str(self.Page4_Shopee_TableWidget_Kolom[item])))

            # Inisialisasi Baris
            Barcode = []
            conn = sqlite3.connect(DatabaseProduk())
            curr = conn.cursor()

            conn2 = sqlite3.connect(DatabaseShopee())
            curr2 = conn2.cursor()

            Data = curr.execute("select name from sqlite_master where type = 'table'").fetchall()
            DataShopee = curr2.execute("select SKU_Shopee from UploadedShopee").fetchall()
            ProdukTerupload = [item[0] for item in DataShopee]

            for item2 in range(len(Data)):
                if Data[item2][0] != "Data_Produk_Master":
                    Barcode.append(str(Data[item2][0]))
                else:
                    pass
            self.page4_Shopee_TableWidget.setRowCount(len(Barcode))
            for item3 in range(len(Barcode)):
                self.page4_Shopee_TableWidget.setItem(item3, self.Page4_Shopee_TableWidget_Kolom_to_Index[self.Page4_Shopee_Kolom1], QtWidgets.QTableWidgetItem(str(item3 + 1)))
                self.page4_Shopee_TableWidget.setItem(item3, self.Page4_Shopee_TableWidget_Kolom_to_Index[self.Page4_Shopee_Kolom3], QtWidgets.QTableWidgetItem(str(Barcode[item3])))

                NamaProduk = curr.execute("select Nama_Produk from '{}'".format(Barcode[item3])).fetchone()[0]
                self.page4_Shopee_TableWidget.setItem(item3, self.Page4_Shopee_TableWidget_Kolom_to_Index[self.Page4_Shopee_Kolom2], QtWidgets.QTableWidgetItem(str(NamaProduk)))

                KodeToko = curr.execute("select Kode_Toko from '{}'".format(Barcode[item3])).fetchone()[0]
                self.page4_Shopee_TableWidget.setItem(item3, self.Page4_Shopee_TableWidget_Kolom_to_Index[self.Page4_Shopee_Kolom4], QtWidgets.QTableWidgetItem(str(KodeToko)))

                if KodeToko in ProdukTerupload:
                    StatusUpload = "Sudah Upload"
                    self.page4_Shopee_TableWidget.setItem(item3, self.Page4_Shopee_TableWidget_Kolom_to_Index[self.Page4_Shopee_Kolom5], QtWidgets.QTableWidgetItem(str(StatusUpload)))

                    SKU_di_Shopee = KodeToko
                    self.page4_Shopee_TableWidget.setItem(item3, self.Page4_Shopee_TableWidget_Kolom_to_Index[self.Page4_Shopee_Kolom6], QtWidgets.QTableWidgetItem(str(SKU_di_Shopee)))

                    KodeProduk = curr2.execute("select Kode_Produk_Shopee from UploadedShopee where SKU_Shopee='{}'".format(SKU_di_Shopee)).fetchone()[0]
                    self.page4_Shopee_TableWidget.setItem(item3, self.Page4_Shopee_TableWidget_Kolom_to_Index[self.Page4_Shopee_Kolom7], QtWidgets.QTableWidgetItem(str(KodeProduk)))

                    KodeVariasi = curr2.execute("select Kode_Variasi_Shopee from UploadedShopee where SKU_Shopee='{}'".format(SKU_di_Shopee)).fetchone()[0]
                    self.page4_Shopee_TableWidget.setItem(item3, self.Page4_Shopee_TableWidget_Kolom_to_Index[self.Page4_Shopee_Kolom8], QtWidgets.QTableWidgetItem(str(KodeVariasi)))

                    url = r"https://shopee.co.id/api/v2/item/get?itemid={}&shopid={}".format(KodeProduk, self.Page4_Shopee_ShopID)
                    # url = r"https://shopee.co.id/product-i.332679464.9913523055".format(self.Page4_Shopee_ShopID, KodeProduk)

                    stok = LoadDataJSONProduk(url, str(KodeProduk))
                    print(url)
                    print("data ke {} selesai diunduh".format(item3))
                    print(stok)
                    self.page4_Shopee_TableWidget.setItem(item3, self.Page4_Shopee_TableWidget_Kolom_to_Index[self.Page4_Shopee_Kolom10], QtWidgets.QTableWidgetItem(str(stok)))

                else:
                    pass

                BanyakTransaksi = curr.execute("select No,Total_Stok_Sekarang from '{}'".format(Barcode[item3])).fetchall()
                TotalStok = 0
                for item in range(len(BanyakTransaksi)):
                    Stok = BanyakTransaksi[item][1]
                    TotalStok += int(Stok)
                self.page4_Shopee_TableWidget.setItem(item3, self.Page4_Shopee_TableWidget_Kolom_to_Index[self.Page4_Shopee_Kolom9], QtWidgets.QTableWidgetItem(str(TotalStok)))

            conn.close()
            conn2.close()
            #

        def LoadJumlahHalamanProduk(idtoko):

            url = "https://shopee.co.id/api/v4/search/search_items?by=ctime&limit=30&match_id={}&newest=0&order=desc&page_type=shop&scenario=PAGE_OTHERS&version=2".format(idtoko)
            my_referer = "https://shopee.co.id/"
            s = requests.Session()
            s.headers.update({'referer': my_referer})
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                'From': 'youremail@domain.com'  # This is another valid field
            }
            text = s.get(url, headers=headers).json()
            jumlahProduk = text["total_count"]
            print(jumlahProduk)

        inisialisasiTabel()
        LoadJumlahHalamanProduk("332679464")
        # LoadDataJSONProduk("https://shopee.co.id/api/v2/item/get?itemid=2819848861&shopid=332679464")

    def Page4_Shopee_PushButton1(self):
        self.page4_Shopee_PushButton1 = QtWidgets.QPushButton("Test Sync Stok")
        self.Page4_Shopee_Layout.addWidget(self.page4_Shopee_PushButton1, 30, 0)

    def Page4_Shopee_PushButton1_clicked(self):
        print("Shopee PushButton 1 clicked")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page4()
    objek.Page4_Execution('Admin Page 4', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
