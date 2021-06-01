from PandanArum import *
from MenuBar import *


class Page9(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page9, self).__init__()
        MenuBar.MenuBar_Execution(self)

    def Tab9(self):
        self.tab9 = QtWidgets.QWidget()
        self.tab9.setObjectName("Tab9")
        self.tab_UTAMA.addTab(self.tab9, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab9), "Page 2")

    def GridLayout_30(self):
        self.gridLayout_30 = QtWidgets.QGridLayout(self.tab9)
        self.gridLayout_30.setObjectName("gridLayout_30")

    def Tab_PAGE2_GridLayout(self):
        self.tab_PAGE2_GridLayout = QtWidgets.QGridLayout()
        self.tab_PAGE2_GridLayout.setObjectName("TAB_PAGE2_GridLayout")
        self.gridLayout_30.addLayout(self.tab_PAGE2_GridLayout, 0, 0, 1, 1)

    def Tab_PAGE2_TAB(self):
        self.tab_PAGE2_TAB = QtWidgets.QTabWidget(self.tab9)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab_PAGE2_TAB.setFont(font)
        self.tab_PAGE2_TAB.setObjectName("TAB_PAGE2_TAB")
        self.tab_PAGE2_GridLayout.addWidget(self.tab_PAGE2_TAB, 0, 0, 1, 1)
        self.tab_PAGE2_TAB.setCurrentIndex(0)

    def Tab_PAGE2_TAB_Tab1(self):
        self.tab_PAGE2_TAB_Tab1 = QtWidgets.QWidget()
        self.tab_PAGE2_TAB_Tab1.setObjectName("TAB_PAGE2_TAB_Tab1")
        self.tab_PAGE2_TAB.addTab(self.tab_PAGE2_TAB_Tab1, "")
        self.tab_PAGE2_TAB.setTabText(self.tab_PAGE2_TAB.indexOf(self.tab_PAGE2_TAB_Tab1), "Tab 1")

    def Page9_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        # TAB 9
        self.Tab9()  # Page 9
        self.GridLayout_30()  # Page 9
        self.Tab_PAGE2_GridLayout()  # Page 9
        self.Tab_PAGE2_TAB()  # Page 9
        self.Tab_PAGE2_TAB_Tab1()  # Page 9


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page9()
    objek.Page9_Execution('Admin Page 9', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
