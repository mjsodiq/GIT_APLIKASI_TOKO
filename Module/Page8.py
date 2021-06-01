from PandanArum import *
from MenuBar import *


class Page8(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page8, self).__init__()
        MenuBar.MenuBar_Execution(self)

    def Tab8(self):
        self.tab8 = QtWidgets.QWidget()
        self.tab8.setObjectName("Tab8")
        self.tab_UTAMA.addTab(self.tab8, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab8), "Page 1")

    def GridLayout_31(self):
        self.gridLayout_31 = QtWidgets.QGridLayout(self.tab8)
        self.gridLayout_31.setObjectName("gridLayout_31")

    def Tab_PAGE1_GridLayout(self):
        self.tab_PAGE1_GridLayout = QtWidgets.QGridLayout()
        self.tab_PAGE1_GridLayout.setObjectName("TAB_PAGE1_GridLayout")
        self.gridLayout_31.addLayout(self.tab_PAGE1_GridLayout, 0, 0, 1, 1)

    def Tab_PAGE1_TAB(self):
        self.tab_PAGE1_TAB = QtWidgets.QTabWidget(self.tab8)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab_PAGE1_TAB.setFont(font)
        self.tab_PAGE1_TAB.setObjectName("TAB_PAGE1_TAB")
        self.tab_PAGE1_GridLayout.addWidget(self.tab_PAGE1_TAB, 0, 0, 1, 1)
        self.tab_PAGE1_TAB.setCurrentIndex(0)

    def Tab_PAGE1_TAB_Tab1(self):
        self.tab_PAGE1_TAB_Tab1 = QtWidgets.QWidget()
        self.tab_PAGE1_TAB_Tab1.setObjectName("TAB_PAGE1_TAB_Tab1")
        self.tab_PAGE1_TAB.addTab(self.tab_PAGE1_TAB_Tab1, "")
        self.tab_PAGE1_TAB.setTabText(self.tab_PAGE1_TAB.indexOf(self.tab_PAGE1_TAB_Tab1), "Tab 1")

    def Page8_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        # TAB 8
        self.Tab8()  # Page 8
        self.GridLayout_31()  # Page 8
        self.Tab_PAGE1_GridLayout()  # Page 8
        self.Tab_PAGE1_TAB()  # Page 8
        self.Tab_PAGE1_TAB_Tab1()  # Page 8


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page8()
    objek.Page8_Execution('Admin Page 8', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
