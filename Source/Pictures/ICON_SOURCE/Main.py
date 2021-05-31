import sys
from PyQt5 import QtWidgets


class HitungTPdanStopOrder(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('TP dan Stop Order')
        self.resize(600, 400)
        self.Layout1 = QtWidgets.QFormLayout()

        # WIDGETS
        self.CheckBox_Buy = QtWidgets.QCheckBox('Mode Buy')
        self.CheckBox_Sell = QtWidgets.QCheckBox('Mode Sell')
        self.input_HargaAtas = QtWidgets.QLineEdit('0')
        self.input_HargaBawah = QtWidgets.QLineEdit('0')
        self.input_Spread = QtWidgets.QLineEdit('30')
        self.input_Lot = QtWidgets.QLineEdit('0.02')
        self.input_BiayaSwap = QtWidgets.QLineEdit('0')
        self.input_TP = QtWidgets.QLineEdit('0')
        self.input_TP.setReadOnly(True)
        self.input_BuyStopOrder = QtWidgets.QLineEdit('0')
        self.input_BuyStopOrder.setReadOnly(True)
        self.input_SellStopOrder = QtWidgets.QLineEdit('0')
        self.input_SellStopOrder.setReadOnly(True)
        self.spacer = QtWidgets.QSpacerItem(100, 50)

        # LAYOUT MANAGEMENT
        # ----CHECKBOX LAYOUT---
        self.CheckBox_Widget = QtWidgets.QWidget()
        self.CheckBox_Widget.setLayout(QtWidgets.QHBoxLayout())
        self.CheckBox_Widget.layout().addWidget(self.CheckBox_Buy)
        self.CheckBox_Widget.layout().addWidget(self.CheckBox_Sell)

        # ----Lot & Swap-----
        self.LotSwap = QtWidgets.QHBoxLayout()
        self.Lot = QtWidgets.QFormLayout()
        self.Lot.addRow('Lot : ', self.input_Lot)
        self.LotSwap.layout().addItem(self.Lot)
        self.Swap = QtWidgets.QFormLayout()
        self.Swap.addRow('Biaya Swap : ', self.input_BiayaSwap)
        self.LotSwap.layout().addItem(self.Swap)

        # ----Layout1 -----
        self.Layout1.addRow('', self.CheckBox_Widget)
        self.Layout1.addRow('Harga Atas : ', self.input_HargaAtas)
        self.Layout1.addRow('Harga Bawah : ', self.input_HargaBawah)
        self.Layout1.addRow('Spread : ', self.input_Spread)
        self.Layout1.addRow('', self.LotSwap)
        self.Layout1.addItem(self.spacer)
        self.Layout1.addRow('TP : ', self.input_TP)
        self.Layout1.addRow('Buy Stop at : ', self.input_BuyStopOrder)
        self.Layout1.addRow('Sell Stop at : ', self.input_SellStopOrder)

        # SIGNAL executed
        self.input_HargaAtas.textChanged.connect(self.BuyMode)
        self.input_HargaAtas.textChanged.connect(self.SellMode)
        self.input_HargaBawah.textChanged.connect(self.BuyMode)
        self.input_HargaBawah.textChanged.connect(self.SellMode)
        self.input_Spread.textChanged.connect(self.BuyMode)
        self.input_Spread.textChanged.connect(self.SellMode)
        self.CheckBox_Buy.stateChanged.connect(self.BuyMode)
        self.CheckBox_Sell.stateChanged.connect(self.SellMode)
        self.input_Lot.textChanged.connect(self.BuyMode)
        self.input_Lot.textChanged.connect(self.SellMode)
        self.input_BiayaSwap.textChanged.connect(self.BuyMode)
        self.input_BiayaSwap.textChanged.connect(self.SellMode)


        self.setLayout(self.Layout1)
        self.show()

    def BuyMode(self):
        if self.CheckBox_Buy.isChecked():
            self.CheckBox_Sell.setChecked(False)
            self.input_SellStopOrder.setDisabled(True)
            self.hitungBuyStopOrder()

        else:
            if self.CheckBox_Sell.isChecked():
                self.input_BuyStopOrder.setText('0')
                self.input_SellStopOrder.setEnabled(True)
                self.hitungSellStopOrder()
            else:
                self.input_TP.setText('0')
                self.input_BuyStopOrder.setText('0')
                self.input_SellStopOrder.setEnabled(True)
                self.hitungSellStopOrder()

    def SellMode(self):
        if self.CheckBox_Sell.isChecked():
            self.CheckBox_Buy.setChecked(False)
            self.input_BuyStopOrder.setDisabled(True)
            self.hitungSellStopOrder()
        else:
            if self.CheckBox_Buy.isChecked():
                self.input_SellStopOrder.setText('0')
                self.input_BuyStopOrder.setEnabled(True)
                self.hitungSellStopOrder()
            else:
                self.input_TP.setText('0')
                self.input_SellStopOrder.setText('0')
                self.input_BuyStopOrder.setEnabled(True)
                self.hitungSellStopOrder()

    def hitungBuyStopOrder(self):
        a = self.CheckBox_Buy.checkState()
        b = self.CheckBox_Sell.checkState()
        try:
            HargaBawah = int(self.input_HargaBawah.text())
        except:
            HargaBawah = 0
        try:
            HargaAtas = int(self.input_HargaAtas.text())
        except:
            HargaAtas = 0
        try:
            Spread = int(self.input_Spread.text())
        except:
            Spread = 0
        try:
            Lot = float(self.input_Lot.text())
        except:
            Lot = 0.01
        try:
            Swap = float(self.input_BiayaSwap.text()) + 0.5
        except:
            Swap = 0
        try:
            BiayaSwap = int(Swap/Lot)
        except:
            BiayaSwap = 0
        try:
            TitikTengah = int((HargaAtas - HargaBawah) / 2)
        except:
            TitikTengah = 0

        if a > 0:
            try:
                if (HargaAtas < HargaBawah):
                    self.input_TP.setText('Harga atas dan bawah salah')
                    self.input_BuyStopOrder.setText('Harga atas dan bawah salah')
                else:
                    BuyStop = (HargaBawah + TitikTengah + BiayaSwap) + Spread
                    TP = (HargaBawah + TitikTengah + BiayaSwap)
                    self.input_BuyStopOrder.setText(str(int(BuyStop)))
                    self.input_TP.setText(str(TP))
                    if int(self.input_HargaAtas.text()) < int(BuyStop):
                        self.input_BuyStopOrder.setText('{} (Anda akan rugi)'.format(int(BuyStop)))
                    else:
                        pass
            except ValueError:
                self.input_BuyStopOrder.setText('0')
        else:
            self.input_BuyStopOrder.setText('0')

    def hitungSellStopOrder(self):
        a = self.CheckBox_Buy.checkState()
        b = self.CheckBox_Sell.checkState()
        try:
            HargaBawah = int(self.input_HargaBawah.text())
        except:
            HargaBawah = 0
        try:
            HargaAtas = int(self.input_HargaAtas.text())
        except:
            HargaAtas = 0
        try:
            Spread = int(self.input_Spread.text())
        except:
            Spread = 0
        try:
            Lot = float(self.input_Lot.text())
        except:
            Lot = 0.01
        try:
            Swap = float(self.input_BiayaSwap.text()) + 0.5
        except:
            Swap = 0
        try:
            BiayaSwap = int(Swap/Lot)
        except:
            BiayaSwap = 0
        try:
            TitikTengah = int((HargaAtas - HargaBawah) / 2)
        except:
            TitikTengah = 0
        if b > 0:
            try:
                if (int(self.input_HargaAtas.text()) < int(self.input_HargaBawah.text())):
                    self.input_TP.setText('Harga atas dan bawah salah')
                    self.input_SellStopOrder.setText('Harga atas dan bawah salah')
                else:
                    SellStop = (HargaBawah + TitikTengah - BiayaSwap) - Spread
                    TP = HargaBawah + TitikTengah - BiayaSwap
                    self.input_SellStopOrder.setText(str(int(SellStop)))
                    self.input_TP.setText(str(TP))
                    if int(self.input_HargaBawah.text()) > int(SellStop):
                        self.input_SellStopOrder.setText('{} (Anda akan rugi)'.format(int(SellStop)))
                    else:
                        pass
            except ValueError:
                self.input_SellStopOrder.setText('0')
        else:
            self.input_SellStopOrder.setText('0')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    objek = HitungTPdanStopOrder()
    sys.exit(app.exec_())
