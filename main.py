# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import events
from ejercicioCuatro import *
from windowaviso import *

import sys
import var


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)

        var.ui.actionSalir.triggered.connect(events.Eventos.Salir1)
        var.ui.btnAceptar.clicked.connect(events.Eventos.letraDNI)
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)

        var.ui.buttonGroup.buttonClicked.connect(events.Eventos.selSexo)

        var.ui.cbEfectivo.stateChanged.connect(events.Eventos.selPago)
        var.ui.cbTarjeta.stateChanged.connect(events.Eventos.selPago)
        var.ui.cbTarnsferencia.stateChanged.connect(events.Eventos.selPago)

        events.Eventos.cargarProv(self)
        var.ui.cmbProv.activated[str].connect(events.Eventos.selProv)


class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgsalir = Ui_Dialog()
        var.dlgsalir.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgsalir = DialogSalir()
    window.show()
    sys.exit(app.exec())
