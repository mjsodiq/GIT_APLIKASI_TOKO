from PandanArum import *
from MenuBar import *


class Page14(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page14, self).__init__()
        MenuBar.MenuBar_Execution(self)

    def Tab14(self):
        self.tab14 = QtWidgets.QWidget()
        self.tab14.setObjectName("Tab14")
        self.tab_UTAMA.addTab(self.tab14, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab14), "Page 7")

    def GridLayout_25(self):
        self.gridLayout_25 = QtWidgets.QGridLayout(self.tab14)
        self.gridLayout_25.setObjectName("gridLayout_25")

    def Tab_PAGE7_GridLayout(self):
        self.tab_PAGE7_GridLayout = QtWidgets.QGridLayout()
        self.tab_PAGE7_GridLayout.setObjectName("TAB_PAGE7_GridLayout")
        self.gridLayout_25.addLayout(self.tab_PAGE7_GridLayout, 0, 0, 1, 1)

    def Tab_PAGE7_TAB(self):
        self.tab_PAGE7_TAB = QtWidgets.QTabWidget(self.tab14)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab_PAGE7_TAB.setFont(font)
        self.tab_PAGE7_TAB.setObjectName("TAB_PAGE7_TAB")
        self.tab_PAGE7_GridLayout.addWidget(self.tab_PAGE7_TAB, 0, 0, 1, 1)
        self.tab_PAGE7_TAB.setCurrentIndex(0)

    def Tab_PAGE7_TAB_Tab1(self):
        self.tab_PAGE7_TAB_Tab1 = QtWidgets.QWidget()
        self.tab_PAGE7_TAB_Tab1.setObjectName("TAB_PAGE7_TAB_Tab1")
        self.tab_PAGE7_TAB.addTab(self.tab_PAGE7_TAB_Tab1, "")
        self.tab_PAGE7_TAB.setTabText(self.tab_PAGE7_TAB.indexOf(self.tab_PAGE7_TAB_Tab1), "Tab 1")

    def Page14_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        # TAB 14
        self.Tab14()  # Page 14
        self.GridLayout_25()  # Page 14
        self.Tab_PAGE7_GridLayout()  # Page 14
        self.Tab_PAGE7_TAB()  # Page 14
        self.Tab_PAGE7_TAB_Tab1()  # Page 14


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page14()
    objek.Page14_Execution('Admin Page 14', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
