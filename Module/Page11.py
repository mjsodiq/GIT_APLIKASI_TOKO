from PandanArum import *
from MenuBar import *


class Page11(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page11, self).__init__()
        MenuBar.MenuBar_Execution(self)

    def Tab11(self):
        self.tab11 = QtWidgets.QWidget()
        self.tab11.setObjectName("Tab11")
        self.tab_UTAMA.addTab(self.tab11, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab11), "Page 4")

    def GridLayout_28(self):
        self.gridLayout_28 = QtWidgets.QGridLayout(self.tab11)
        self.gridLayout_28.setObjectName("gridLayout_28")

    def Tab_PAGE4_GridLayout(self):
        self.tab_PAGE4_GridLayout = QtWidgets.QGridLayout()
        self.tab_PAGE4_GridLayout.setObjectName("TAB_PAGE4_GridLayout")
        self.gridLayout_28.addLayout(self.tab_PAGE4_GridLayout, 0, 0, 1, 1)

    def Tab_PAGE4_TAB(self):
        self.tab_PAGE4_TAB = QtWidgets.QTabWidget(self.tab11)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab_PAGE4_TAB.setFont(font)
        self.tab_PAGE4_TAB.setObjectName("TAB_PAGE4_TAB")
        self.tab_PAGE4_GridLayout.addWidget(self.tab_PAGE4_TAB, 0, 0, 1, 1)
        self.tab_PAGE4_TAB.setCurrentIndex(0)

    def Tab_PAGE4_TAB_Tab1(self):
        self.tab_PAGE4_TAB_Tab1 = QtWidgets.QWidget()
        self.tab_PAGE4_TAB_Tab1.setObjectName("TAB_PAGE4_TAB_Tab1")
        self.tab_PAGE4_TAB.addTab(self.tab_PAGE4_TAB_Tab1, "")
        self.tab_PAGE4_TAB.setTabText(self.tab_PAGE4_TAB.indexOf(self.tab_PAGE4_TAB_Tab1), "Tab 1")

    def Page11_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        # TAB 11
        self.Tab11()  # Page 11
        self.GridLayout_28()  # Page 11
        self.Tab_PAGE4_GridLayout()  # Page 11
        self.Tab_PAGE4_TAB()  # Page 11
        self.Tab_PAGE4_TAB_Tab1()  # Page 12


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page11()
    objek.Page11_Execution('Admin Page 11', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
