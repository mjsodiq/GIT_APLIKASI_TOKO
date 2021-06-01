from PandanArum import *
from MenuBar import *


class Page5(MenuBar, Ui_ProgramAplikasiToko):
    def __init__(self):
        super(Page5, self).__init__()
        MenuBar.MenuBar_Execution(self)

    def Tab5(self):
        self.tab5 = QtWidgets.QWidget()
        self.tab5.setObjectName("Tab5")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/Tambah/Archive_256x256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_UTAMA.addTab(self.tab5, icon17, "")
        self.tab_UTAMA.setTabText(self.tab_UTAMA.indexOf(self.tab5), "LOG")

    def GridLayout_34(self):
        self.gridLayout_34 = QtWidgets.QGridLayout(self.tab5)
        self.gridLayout_34.setObjectName("gridLayout_34")

    def Tab_LOG_GridLayout(self):
        self.tab_LOG_GridLayout = QtWidgets.QGridLayout()
        self.tab_LOG_GridLayout.setObjectName("TAB_LOG_GridLayout")
        self.gridLayout_34.addLayout(self.tab_LOG_GridLayout, 0, 0, 1, 1)

    def Tab_LOG_TAB(self):
        self.tab_LOG_TAB = QtWidgets.QTabWidget(self.tab5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.tab_LOG_TAB.setFont(font)
        self.tab_LOG_TAB.setObjectName("TAB_LOG_TAB")
        self.tab_LOG_GridLayout.addWidget(self.tab_LOG_TAB, 0, 0, 1, 1)
        self.tab_LOG_TAB.setCurrentIndex(0)

    def Tab_LOG_TAB_Tab1(self):
        self.tab_LOG_TAB_Tab1 = QtWidgets.QWidget()
        self.tab_LOG_TAB_Tab1.setObjectName("TAB_LOG_TAB_Tab1")
        self.tab_LOG_TAB.addTab(self.tab_LOG_TAB_Tab1, "")
        self.tab_LOG_TAB.setTabText(self.tab_LOG_TAB.indexOf(self.tab_LOG_TAB_Tab1), "Tab 1")

    def Page5_Execution(self, username, kelas):
        self.username = username
        self.kelas = kelas
        # TAB 5
        self.Tab5()  # Page 5
        self.GridLayout_34()  # Page 5
        self.Tab_LOG_GridLayout()  # Page 5
        self.Tab_LOG_TAB()  # Page 5
        self.Tab_LOG_TAB_Tab1()  # Page 5


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    objek = Page5()
    objek.Page5_Execution('Admin Page 5', 'super')
    objek.programAplikasiToko.showMaximized()
    sys.exit(app.exec_())
