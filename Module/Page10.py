from PandanArum import *
from MenuBar import *


class Page10(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page10, self).__init__()
        MenuBar.MenuBar_Execution(self)

    def Tab10(self):
        self.tab10 = QtWidgets.QWidget()
        self.tab10.setObjectName("Tab10")
        self.tab_UTAMA.addTab(self.tab10, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab10), "Page 3")

    def GridLayout_29(self):
        self.gridLayout_29 = QtWidgets.QGridLayout(self.tab10)
        self.gridLayout_29.setObjectName("gridLayout_29")

    def Tab_PAGE3_GridLayout(self):
        self.tab_PAGE3_GridLayout = QtWidgets.QGridLayout()
        self.tab_PAGE3_GridLayout.setObjectName("TAB_PAGE3_GridLayout")
        self.gridLayout_29.addLayout(self.tab_PAGE3_GridLayout, 0, 0, 1, 1)

    def Tab_PAGE3_TAB(self):
        self.tab_PAGE3_TAB = QtWidgets.QTabWidget(self.tab10)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab_PAGE3_TAB.setFont(font)
        self.tab_PAGE3_TAB.setObjectName("TAB_PAGE3_TAB")
        self.tab_PAGE3_GridLayout.addWidget(self.tab_PAGE3_TAB, 0, 0, 1, 1)
        self.tab_PAGE3_TAB.setCurrentIndex(0)

    def Tab_PAGE3_TAB_Tab1(self):
        self.tab_PAGE3_TAB_Tab1 = QtWidgets.QWidget()
        self.tab_PAGE3_TAB_Tab1.setObjectName("TAB_PAGE3_TAB_Tab1")
        self.tab_PAGE3_TAB.addTab(self.tab_PAGE3_TAB_Tab1, "")
        self.tab_PAGE3_TAB.setTabText(self.tab_PAGE3_TAB.indexOf(self.tab_PAGE3_TAB_Tab1), "Tab 1")

    def Page10_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        # TAB 10
        self.Tab10()  # Page 10
        self.GridLayout_29()  # Page 10
        self.Tab_PAGE3_GridLayout()  # Page 10
        self.Tab_PAGE3_TAB()  # Page 10
        self.Tab_PAGE3_TAB_Tab1()  # Page 10


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page10()
    objek.Page10_Execution('Admin Page 10', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
