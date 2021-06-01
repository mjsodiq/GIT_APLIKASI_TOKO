from PandanArum import *
from MenuBar import *


class Page13(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page13, self).__init__()
        MenuBar.MenuBar_Execution(self)

    def Tab13(self):
        self.tab13 = QtWidgets.QWidget()
        self.tab13.setObjectName("Tab13")
        self.tab_UTAMA.addTab(self.tab13, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab13), "Page6")

    def GridLayout_26(self):
        self.gridLayout_26 = QtWidgets.QGridLayout(self.tab13)
        self.gridLayout_26.setObjectName("gridLayout_26")

    def Tab_PAGE6_GridLayout(self):
        self.tab_PAGE6_GridLayout = QtWidgets.QGridLayout()
        self.tab_PAGE6_GridLayout.setObjectName("TAB_PAGE6_GridLayout")
        self.gridLayout_26.addLayout(self.tab_PAGE6_GridLayout, 0, 0, 1, 1)

    def Tab_PAGE6_TAB(self):
        self.tab_PAGE6_TAB = QtWidgets.QTabWidget(self.tab13)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab_PAGE6_TAB.setFont(font)
        self.tab_PAGE6_TAB.setObjectName("TAB_PAGE6_TAB")
        self.tab_PAGE6_GridLayout.addWidget(self.tab_PAGE6_TAB, 0, 0, 1, 1)
        self.tab_PAGE6_TAB.setCurrentIndex(0)

    def Tab_PAGE6_TAB_Tab1(self):
        self.tab_PAGE6_TAB_Tab1 = QtWidgets.QWidget()
        self.tab_PAGE6_TAB_Tab1.setObjectName("TAB_PAGE6_TAB_Tab1")
        self.tab_PAGE6_TAB.addTab(self.tab_PAGE6_TAB_Tab1, "")
        self.tab_PAGE6_TAB.setTabText(self.tab_PAGE6_TAB.indexOf(self.tab_PAGE6_TAB_Tab1), "Tab 1")

    def Page13_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        # TAB 13
        self.Tab13()  # Page 13
        self.GridLayout_26()  # Page 13
        self.Tab_PAGE6_GridLayout()  # Page 13
        self.Tab_PAGE6_TAB()  # Page 13
        self.Tab_PAGE6_TAB_Tab1()  # Page 13


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page13()
    objek.Page13_Execution('Admin Page 13', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
