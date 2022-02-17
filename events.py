import sys

import var


class Eventos():

    def Salir1(self):
        try:
            sys.exit()
        except Exception as error:
            print("Error %s" % str(error))

    def Salir(self):
        try:
            var.dlgsalir.show()
            if var.dlgsalir.exec():
                sys.exit()
            else:
                var.dlgsalir.hide()
        except Exception as error:
            print('Error en módulo salir', error)

    def letraDNI(self):
        try:
            dni = var.ui.lineDNI.text()
            var.ui.lineDNI.setText(dni.upper())
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            num = '1234567890'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in num]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblVal.setStyleSheet('QLabel {color: green;}')
                    var.ui.lblVal.setText('V')
                else:
                    var.ui.lblVal.setStyleSheet('QLabel {color: red;}')
                    var.ui.lblVal.setText('X')
            else:
                var.ui.lblVal.setStyleSheet('QLabel {color: red;}')
                var.ui.lblVal.setText('X')
        except Exception as error:
            print('Error al validar el DNI', error)

    def selSexo(self):
        try:
            if var.ui.rbtFemenino.isChecked():
                print('Marcado femenino')
            if var.ui.rbtMasculino.isChecked():
                print('Marcado masculino')
        except Exception as error:
            print('Error en módulo seleccionar sexo', error)

    def selPago(self):
        try:
            if var.ui.cbEfectivo.isChecked():
                print('Pagas con efectivo')
            if var.ui.cbTarjeta.isChecked():
                print('Pagas con tarjeta')
            if var.ui.cbTransferencia.isChecked():
                print('Pagas con transferencia')
        except Exception as error:
            print('Error: %' % str(error))

    def cargarProv(self):
        try:
            prov = ['A Coruña', 'Lugo', 'Ourense', 'Pontevedra']
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error: %' % str(error))

    def selProv(prov):
        try:
            print('Has seleccionado la provincia de ', prov)
        except Exception as error:
            print('Error: %' % str(error))
