from PandanArum import *
from MenuBar import *


class Page16(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page16, self).__init__()
        MenuBar.MenuBar_Execution(self)

    def Tab16(self):
        self.tab16 = QtWidgets.QWidget()
        self.tab16.setObjectName("Tab16")
        self.tab_UTAMA.addTab(self.tab16, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab16), "Page 9")

    def GridLayout_23(self):
        self.gridLayout_23 = QtWidgets.QGridLayout(self.tab16)
        self.gridLayout_23.setObjectName("gridLayout_23")

    def Tab_PAGE9_GridLayout(self):
        self.tab_PAGE9_GridLayout = QtWidgets.QGridLayout()
        self.tab_PAGE9_GridLayout.setObjectName("TAB_PAGE9_GridLayout")
        self.gridLayout_23.addLayout(self.tab_PAGE9_GridLayout, 0, 0, 1, 1)

    def Tab_PAGE9_TAB(self):
        self.tab_PAGE9_TAB = QtWidgets.QTabWidget(self.tab16)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab_PAGE9_TAB.setFont(font)
        self.tab_PAGE9_TAB.setObjectName("TAB_PAGE9_TAB")
        self.tab_PAGE9_GridLayout.addWidget(self.tab_PAGE9_TAB, 0, 0, 1, 1)
        self.tab_PAGE9_TAB.setCurrentIndex(0)

    def Tab_PAGE9_TAB_Tab1(self):
        self.tab_PAGE9_TAB_Tab1 = QtWidgets.QWidget()
        self.tab_PAGE9_TAB_Tab1.setObjectName("TAB_PAGE9_TAB_Tab1")
        self.tab_PAGE9_TAB.addTab(self.tab_PAGE9_TAB_Tab1, "")
        self.tab_PAGE9_TAB.setTabText(self.tab_PAGE9_TAB.indexOf(self.tab_PAGE9_TAB_Tab1), "Tab 1")

    def Page16_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        # TAB 16
        self.Tab16()  # Page 16
        self.GridLayout_23()  # Page 16
        self.Tab_PAGE9_GridLayout()  # Page 16
        self.Tab_PAGE9_TAB()  # Page 16
        self.Tab_PAGE9_TAB_Tab1()  # Page 16


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page16()
    objek.Page16_Execution('Admin Page 16', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
