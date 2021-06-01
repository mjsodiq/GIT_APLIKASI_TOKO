from PandanArum import *
from MenuBar import *


class Page6(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page6, self).__init__()
        MenuBar.MenuBar_Execution(self)

    def Tab6(self):
        self.tab6 = QtWidgets.QWidget()
        self.tab6.setObjectName("Tab6")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/Tambah/align bottom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_UTAMA.addTab(self.tab6, icon18, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab6), "Analisis")

    def GridLayout_33(self):
        self.gridLayout_33 = QtWidgets.QGridLayout(self.tab6)
        self.gridLayout_33.setObjectName("gridLayout_33")

    def Tab_ANALISIS_GridLayout(self):
        self.tab_ANALISIS_GridLayout = QtWidgets.QGridLayout()
        self.tab_ANALISIS_GridLayout.setObjectName("TAB_ANALISIS_GridLayout")
        self.gridLayout_33.addLayout(self.tab_ANALISIS_GridLayout, 0, 0, 1, 1)

    def Tab_ANALISIS_TAB(self):
        self.tab_ANALISIS_TAB = QtWidgets.QTabWidget(self.tab6)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab_ANALISIS_TAB.setFont(font)
        self.tab_ANALISIS_TAB.setObjectName("TAB_ANALISIS_TAB")
        self.tab_ANALISIS_GridLayout.addWidget(self.tab_ANALISIS_TAB, 0, 0, 1, 1)
        self.tab_ANALISIS_TAB.setCurrentIndex(0)

    def Tab_ANALISIS_TAB_Tab1(self):
        self.tab_ANALISIS_TAB_Tab1 = QtWidgets.QWidget()
        self.tab_ANALISIS_TAB_Tab1.setObjectName("TAB_ANALISIS_TAB_Tab1")
        self.tab_ANALISIS_TAB.addTab(self.tab_ANALISIS_TAB_Tab1, "")
        self.tab_ANALISIS_TAB.setTabText(self.tab_ANALISIS_TAB.indexOf(self.tab_ANALISIS_TAB_Tab1), "Tab 1")

    def Page6_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        # TAB 6
        self.Tab6()  # Page 6
        self.GridLayout_33()  # Page 6
        self.Tab_ANALISIS_GridLayout()  # Page 6
        self.Tab_ANALISIS_TAB()  # Page 6
        self.Tab_ANALISIS_TAB_Tab1()  # Page 6


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page6()
    objek.Page6_Execution('Admin Page 6', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
