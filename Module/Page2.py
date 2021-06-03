from PandanArum import *
from MenuBar import *


class Page2(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page2, self).__init__()

    def Page2_Tab2(self):
        self.Page2_tab2 = QtWidgets.QWidget()
        self.Page2_tab2.setObjectName("Tab2")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Tambah/User_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_UTAMA.addTab(self.Page2_tab2, icon12, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.Page2_tab2), "Atur Pengguna")

    def Page2_GridLayout(self):
        self.page2_gridLayout = QtWidgets.QGridLayout(self.Page2_tab2)
        self.page2_gridLayout.setObjectName("gridLayout_36")

    def Page2_TabWidget(self):
        self.page2_TabWidget = QtWidgets.QTabWidget()
        self.page2_gridLayout.addWidget(self.page2_TabWidget, 0, 0)

    def Page2_Execution(self, username, kelas):
        self.Page2_Tab2()
        self.Page2_GridLayout()
        self.Page2_TabWidget()
        objek1 = Page2_Tab1(self)


class Page2_Tab1(Page2):
    def __init__(self, Data):
        self.Data = Data
        super(Page2_Tab1, self).__init__()

        # Inisialisasi tabel staf
        self.Page2_TableWidget_Kolom_to_Database_Dict = {
                                                            'No': 'No',
                                                            'Nama': 'Nama',
                                                            'Otorisasi': 'kelas',
                                                            'Username': 'username',
                                                            'Password': 'password',
                                                            'Email': 'email',
                                                            'Nomor HP': 'No_HP',
                                                            'NIK': 'NIK',
                                                            'Foto KTP': 'Foto_KTP',
                                                            'Foto Diri': 'Foto_Diri',
                                                            'Outlet': 'Outlet',
                                                            'Aksi': 'Aksi'
                                                        }
        self.Page2_TableWidget_Kolom = list(self.Page2_TableWidget_Kolom_to_Database_Dict.keys())
        self.Page2_TableWidget_Kolom_to_Ignore = ['Password']
        self.Page2_TableWidget_Kolom_to_Index = {}
        for item in range(len(self.Page2_TableWidget_Kolom)):
            Page2_TableWidget_Kolom_Dict = {self.Page2_TableWidget_Kolom[item]: item}
            self.Page2_TableWidget_Kolom_to_Index.update(Page2_TableWidget_Kolom_Dict)

        # Exekusi Gui untuk Page2_Tab1
        self.Page2_Tab1_Inisialisasi_Tab()  # Page 2
        self.Page2_Tab1_GridLayout()
        self.Page2_Tab1_Label()
        self.Page2_Tab1_HBoxLayout()
        self.Page2_Tab1_Label2()
        self.Page2_Tab1_LineEdit()
        self.Page2_Tab1_PushButton()
        self.Page2_Tab1_TableWidget()
        self.Page2_Tab1_Operasi_TableWidget()

        # Perintah

    def Page2_Tab1_Inisialisasi_Tab(self):
        self.page2_Tab1 = QtWidgets.QWidget()
        icon = QtGui.QIcon()
        self.Data.page2_TabWidget.addTab(self.page2_Tab1, icon, '')
        self.Data.page2_TabWidget.setTabText(self.Data.page2_TabWidget.indexOf(self.page2_Tab1), 'Kelola Staf')

    def Page2_Tab1_GridLayout(self):
        self.page2_Tab1_GridLayout = QtWidgets.QGridLayout(self.page2_Tab1)

    def Page2_Tab1_Label(self):
        self.page2_Tab1_Label = QtWidgets.QLabel('Daftar Staf : ')
        self.page2_Tab1_Label.setFont(Font(9, True))
        self.page2_Tab1_GridLayout.addWidget(self.page2_Tab1_Label, 0, 0)

    def Page2_Tab1_HBoxLayout(self):
        self.page2_Tab1_HBoxLayout = QtWidgets.QHBoxLayout()
        self.page2_Tab1_GridLayout.addLayout(self.page2_Tab1_HBoxLayout, 1, 0)

    def Page2_Tab1_Label2(self):
        self.page2_Tab1_Label2 = QtWidgets.QLabel('Cari Staf : ')
        self.page2_Tab1_HBoxLayout.addWidget(self.page2_Tab1_Label2)

    def Page2_Tab1_LineEdit(self):
        self.page2_Tab1_LineEdit = QtWidgets.QLineEdit()
        self.page2_Tab1_HBoxLayout.addWidget(self.page2_Tab1_LineEdit)

    def Page2_Tab1_PushButton(self):
        self.page2_Tab1_PushButton = QtWidgets.QPushButton('Cari')
        self.page2_Tab1_HBoxLayout.addWidget(self.page2_Tab1_PushButton)

    def Page2_Tab1_TableWidget(self):
        self.page2_Tab1_TableWidget = QtWidgets.QTableWidget()
        self.page2_Tab1_TableWidget.setFont(Font(9, False))
        self.page2_Tab1_GridLayout.addWidget(self.page2_Tab1_TableWidget, 2, 0, 1, 1)

    def Page2_Tab1_Operasi_TableWidget(self):
        conn = sqlite3.connect(self.UserDatabase)
        curr = conn.cursor()
        Data = curr.execute('select * from user').fetchall()
        No = curr.execute("select No from user").fetchall()
        Header = list(map(lambda x: x[0], curr.description))
        self.page2_Tab1_TableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.page2_Tab1_TableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.page2_Tab1_TableWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.page2_Tab1_TableWidget.setAlternatingRowColors(True)
        self.page2_Tab1_TableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.page2_Tab1_TableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.page2_Tab1_TableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.page2_Tab1_TableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.page2_Tab1_TableWidget.verticalHeader().hide()
        self.page2_Tab1_TableWidget.setObjectName("tableWidget_3")
        self.page2_Tab1_TableWidget.setColumnCount(len(self.Page2_TableWidget_Kolom))
        for item in self.Page2_TableWidget_Kolom:
            self.page2_Tab1_TableWidget.setHorizontalHeaderItem(self.Page2_TableWidget_Kolom_to_Index[item], QtWidgets.QTableWidgetItem(item))
            self.page2_Tab1_TableWidget.horizontalHeader().setSectionResizeMode(self.Page2_TableWidget_Kolom_to_Index[item], QtWidgets.QHeaderView.ResizeToContents)

        self.page2_Tab1_TableWidget.horizontalHeader().setSectionResizeMode(self.Page2_TableWidget_Kolom_to_Index['Nama'], QtWidgets.QHeaderView.Stretch)

        JumlahBaris = len(Data)
        self.page2_Tab1_TableWidget.setRowCount(JumlahBaris)

        for row in range(JumlahBaris):
            No = row
            for key in self.Page2_TableWidget_Kolom:
                if key not in self.Page2_TableWidget_Kolom_to_Ignore:
                    try:
                        self.page2_Tab1_TableWidget.setItem(No, self.Page2_TableWidget_Kolom_to_Index[key], QtWidgets.QTableWidgetItem(str(curr.execute("select {} from user where No='{}'".format(self.Page2_TableWidget_Kolom_to_Database_Dict[key], No+1)).fetchone()[0])))
                    except:
                        pass
                else:
                    pass



        # Menambahkan Tombol 'Minta Password' pada kolom 'Password'
        for row in range(JumlahBaris):
            Widget1 = QtWidgets.QWidget()

            HBoxLayout = QtWidgets.QHBoxLayout(Widget1)
            HBoxLayout.setAlignment(QtCore.Qt.AlignHCenter)
            HBoxLayout.setContentsMargins(5, 0, 5, 0)
            HBoxLayout.setSpacing(5)

            TombolMintaPassword = QtWidgets.QPushButton("MintaPassword")
            TombolMintaPassword.clicked.connect(lambda: self.Page2_Tab1_TombolMintaPassword_clicked())
            HBoxLayout.addWidget(TombolMintaPassword)

            self.page2_Tab1_TableWidget.setCellWidget(row, self.Page2_TableWidget_Kolom_to_Index["Password"], Widget1)

        # Menambahkan Tombol pada Kolom Aksi
        for row in range(JumlahBaris):
            Widget2 = QtWidgets.QWidget()

            HBoxLayout = QtWidgets.QHBoxLayout(Widget2)
            HBoxLayout.setAlignment(QtCore.Qt.AlignHCenter)
            HBoxLayout.setContentsMargins(5, 0, 5, 0)
            HBoxLayout.setSpacing(5)

            TombolHapus = QtWidgets.QPushButton("Hapus Staf")
            TombolHapus.clicked.connect(self.Page2_Tab1_TombolHapusStaf_clicked)
            HBoxLayout.addWidget(TombolHapus)

            TombolUbah = QtWidgets.QPushButton("Ubah")
            TombolUbah.clicked.connect(self.Page2_Tab1_TombolUbah_clicked)
            HBoxLayout.addWidget(TombolUbah)

            self.page2_Tab1_TableWidget.setCellWidget(row, self.Page2_TableWidget_Kolom_to_Index["Aksi"], Widget2)

        conn.close()

    def Page2_Tab1_TombolMintaPassword_clicked(self):
        print("tombol Minta Password telah diklik")

    def Page2_Tab1_TombolHapusStaf_clicked(self):
        print("tombol Hapus Staf telah diklik")

    def Page2_Tab1_TombolUbah_clicked(self):
        print("tombol Ubah telah diklik")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page2()
    objek.Page2_Execution('Admin Page 2', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
