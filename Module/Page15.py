from PandanArum import *
from MenuBar import *


class Page15(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page15, self).__init__()
        MenuBar.MenuBar_Execution(self)

    def Tab15(self):
        self.tab15 = QtWidgets.QWidget()
        self.tab15.setObjectName("Tab15")
        self.tab_UTAMA.addTab(self.tab15, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab15), "Page 8")

    def GridLayout_24(self):
        self.gridLayout_24 = QtWidgets.QGridLayout(self.tab15)
        self.gridLayout_24.setObjectName("gridLayout_24")

    def Tab_PAGE8_GridLayout(self):
        self.tab_PAGE8_GridLayout = QtWidgets.QGridLayout()
        self.tab_PAGE8_GridLayout.setObjectName("TAB_PAGE8_GridLayout")
        self.gridLayout_24.addLayout(self.tab_PAGE8_GridLayout, 0, 0, 1, 1)

    def Tab_PAGE8_TAB(self):
        self.tab_PAGE8_TAB = QtWidgets.QTabWidget(self.tab15)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab_PAGE8_TAB.setFont(font)
        self.tab_PAGE8_TAB.setObjectName("TAB_PAGE8_TAB")
        self.tab_PAGE8_GridLayout.addWidget(self.tab_PAGE8_TAB, 0, 0, 1, 1)
        self.tab_PAGE8_TAB.setCurrentIndex(0)

    def Tab_PAGE8_TAB_Tab1(self):
        self.tab_PAGE8_TAB_Tab1 = QtWidgets.QWidget()
        self.tab_PAGE8_TAB_Tab1.setObjectName("TAB_PAGE8_TAB_Tab1")
        self.tab_PAGE8_TAB.addTab(self.tab_PAGE8_TAB_Tab1, "")
        self.tab_PAGE8_TAB.setTabText(self.tab_PAGE8_TAB.indexOf(self.tab_PAGE8_TAB_Tab1), "Tab 1")

    def Page15_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        # TAB 15
        self.Tab15()  # Page 15
        self.GridLayout_24()  # Page 15
        self.Tab_PAGE8_GridLayout()  # Page 15
        self.Tab_PAGE8_TAB()  # Page 15
        self.Tab_PAGE8_TAB_Tab1()  # Page 15


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page15()
    objek.Page15_Execution('Admin Page 15', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
