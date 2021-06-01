from PandanArum import *
from MenuBar import *


class Page7(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page7, self).__init__()
        MenuBar.MenuBar_Execution(self)

    def Tab7(self):
        self.tab7 = QtWidgets.QWidget()
        self.tab7.setObjectName("Tab7")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/Tambah/Settings_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_UTAMA.addTab(self.tab7, icon19, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab7), "Pengaturan")

    def GridLayout_32(self):
        self.gridLayout_32 = QtWidgets.QGridLayout(self.tab7)
        self.gridLayout_32.setObjectName("gridLayout_32")

    def Tab_PENGATURAN_GridLayout(self):
        self.tab_PENGATURAN_GridLayout = QtWidgets.QGridLayout()
        self.tab_PENGATURAN_GridLayout.setObjectName("TAB_PENGATURAN_GridLayout")
        self.gridLayout_32.addLayout(self.tab_PENGATURAN_GridLayout, 0, 0, 1, 1)

    def Tab_PENGATURAN_TAB(self):
        self.tab_PENGATURAN_TAB = QtWidgets.QTabWidget(self.tab7)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab_PENGATURAN_TAB.setFont(font)
        self.tab_PENGATURAN_TAB.setObjectName("TAB_PENGATURAN_TAB")
        self.tab_PENGATURAN_GridLayout.addWidget(self.tab_PENGATURAN_TAB, 0, 0, 1, 1)
        self.tab_PENGATURAN_TAB.setCurrentIndex(0)

    def Tab_PENGATURAN_TAB_Tab1(self):
        self.tab_PENGATURAN_TAB_Tab1 = QtWidgets.QWidget()
        self.tab_PENGATURAN_TAB_Tab1.setObjectName("TAB_PENGATURAN_TAB_Tab1")
        self.tab_PENGATURAN_TAB.addTab(self.tab_PENGATURAN_TAB_Tab1, "")
        self.tab_PENGATURAN_TAB.setTabText(self.tab_PENGATURAN_TAB.indexOf(self.tab_PENGATURAN_TAB_Tab1), "Tab 1")

    def Page7_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        # TAB 7
        self.Tab7()  # Page 7
        self.GridLayout_32()  # Page 7
        self.Tab_PENGATURAN_GridLayout()  # Page 7
        self.Tab_PENGATURAN_TAB()  # Page 7
        self.Tab_PENGATURAN_TAB_Tab1()  # Page 7


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page7()
    objek.Page7_Execution('Admin Page 7', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
