from PandanArum import *
from MenuBar import *


class Page17(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page17, self).__init__()
        MenuBar.MenuBar_Execution(self)

    def Tab17(self):
        self.tab17 = QtWidgets.QWidget()
        self.tab17.setObjectName("Tab17")
        self.tab_UTAMA.addTab(self.tab17, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab17), "Page 10")

    def GridLayout_22(self):
        self.gridLayout_22 = QtWidgets.QGridLayout(self.tab17)
        self.gridLayout_22.setObjectName("gridLayout_22")

    def Tab_PAGE10_GridLayout(self):
        self.tab_PAGE10_GridLayout = QtWidgets.QGridLayout()
        self.tab_PAGE10_GridLayout.setObjectName("TAB_PAGE10_GridLayout")
        self.gridLayout_22.addLayout(self.tab_PAGE10_GridLayout, 0, 0, 1, 1)

    def Tab_PAGE10_TAB(self):
        self.tab_PAGE10_TAB = QtWidgets.QTabWidget(self.tab17)
        self.tab_PAGE10_TAB.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab_PAGE10_TAB.setFont(font)
        self.tab_PAGE10_TAB.setObjectName("TAB_PAGE10_TAB")
        self.tab_PAGE10_GridLayout.addWidget(self.tab_PAGE10_TAB, 0, 0, 1, 1)
        self.tab_PAGE10_TAB.setCurrentIndex(0)

    def Tab_PAGE10_TAB_Tab1(self):
        self.tab_PAGE10_TAB_Tab1 = QtWidgets.QWidget()
        self.tab_PAGE10_TAB_Tab1.setObjectName("TAB_PAGE10_TAB_Tab1")
        self.tab_PAGE10_TAB.addTab(self.tab_PAGE10_TAB_Tab1, "")
        self.tab_PAGE10_TAB.setTabText(self.tab_PAGE10_TAB.indexOf(self.tab_PAGE10_TAB_Tab1), "Tab 1")

    def Page17_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        # TAB 17
        self.Tab17()  # Page 17
        self.GridLayout_22()  # Page 17
        self.Tab_PAGE10_GridLayout()  # Page 17
        self.Tab_PAGE10_TAB()  # Page 17
        self.Tab_PAGE10_TAB_Tab1()  # Page 17


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page17()
    objek.Page17_Execution('Admin Page 17', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
