from PandanArum import *
from MenuBar import *


class Page12(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page12, self).__init__()
        MenuBar.MenuBar_Execution(self)

    def Tab12(self):
        self.tab12 = QtWidgets.QWidget()
        self.tab12.setObjectName("Tab12")
        self.tab_UTAMA.addTab(self.tab12, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab12), "Page 5")

    def GridLayout_27(self):
        self.gridLayout_27 = QtWidgets.QGridLayout(self.tab12)
        self.gridLayout_27.setObjectName("gridLayout_27")

    def Tab_PAGE5_GridLayout(self):
        self.tab_PAGE5_GridLayout = QtWidgets.QGridLayout()
        self.tab_PAGE5_GridLayout.setObjectName("TAB_PAGE5_GridLayout")
        self.gridLayout_27.addLayout(self.tab_PAGE5_GridLayout, 0, 0, 1, 1)

    def Tab_PAGE5_TAB(self):
        self.tab_PAGE5_TAB = QtWidgets.QTabWidget(self.tab12)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab_PAGE5_TAB.setFont(font)
        self.tab_PAGE5_TAB.setObjectName("TAB_PAGE5_TAB")
        self.tab_PAGE5_GridLayout.addWidget(self.tab_PAGE5_TAB, 0, 0, 1, 1)
        self.tab_PAGE5_TAB.setCurrentIndex(0)

    def Tab_PAGE5_TAB_Tab1(self):
        self.tab_PAGE5_TAB_Tab1 = QtWidgets.QWidget()
        self.tab_PAGE5_TAB_Tab1.setObjectName("TAB_PAGE5_TAB_Tab1")
        self.tab_PAGE5_TAB.addTab(self.tab_PAGE5_TAB_Tab1, "")
        self.tab_PAGE5_TAB.setTabText(self.tab_PAGE5_TAB.indexOf(self.tab_PAGE5_TAB_Tab1), "Tab 1")

    def Page12_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        # TAB 12
        self.Tab12()  # Page 12
        self.GridLayout_27()  # Page 12
        self.Tab_PAGE5_GridLayout()  # Page 12
        self.Tab_PAGE5_TAB()  # Page 12
        self.Tab_PAGE5_TAB_Tab1()  # Page 12


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page12()
    objek.Page12_Execution('Admin Page 12', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
