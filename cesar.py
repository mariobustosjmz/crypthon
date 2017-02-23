#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
import script

#Main
#Interfaz Grafica usando Qt4

class Interfaz(QtGui.QWidget):
    
    def __init__(self):
        super(Interfaz, self).__init__()
        self.initUI()
        
    
        
    def initUI(self):      

        #Boton con estilos embebidos para la accion de Cifrar
        self.btn = QtGui.QPushButton('Cifrar', self)
        self.btn.move(20, 20)
        self.btn.setStyleSheet("background-color: grey;color:white;width:200px;height:50px;margin:auto;font-weight:bold;font-size:20px; ")
        self.btn.clicked.connect(self.dialogcifrar)
               
        #Boton con estilos embebidos para la accion de Descifrar
        self.btn = QtGui.QPushButton('Descifrar', self)
        self.btn.move(20, 130)
        self.btn.setStyleSheet("background-color: grey;color:white;width:200px;height:50px;margin:auto;font-weight:bold;font-size:20px; ")
        self.btn.clicked.connect(self.dialogdescifrar)
        
        
        
        #Panel donde estaran los botones
        self.setGeometry(400, 400, 300, 300)
     	resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))


        self.setWindowTitle('CIFRADO CESAR ::PYTHON::')
        self.show()
   
   
    #Funcion que pregunta y captura el texto a cifrar
    # y la llave para usarla en el script principal
    def dialogcifrar(self):
        
        vmensajec, okc = QtGui.QInputDialog.getText(self, 'Cifrar', 
            'Introduce el Mensaje:')
        vllavec, okc2 = QtGui.QInputDialog.getText(self, 'Cifrar', 
            'Introduce la Llave')
        
        encriptado = script.crypt(str(vmensajec),int(vllavec))
    	textc = encriptado    

        if okc and okc2:
            QtGui.QMessageBox.information(self, "Texto Cifrado", textc)

        
           
    #Funcion que pregunta y captura el texto a descifrar
    # y la llave para usarla en el script principal 
    def dialogdescifrar(self):
        
        vmensajed, okd = QtGui.QInputDialog.getText(self, 'Descifrar', 
            'Introduce el Mensaje:')
            
        vllaved, okd2 = QtGui.QInputDialog.getText(self, 'Descifrar', 
            'Introduce la Llave:')
   		
        desencriptado = script.decrypt(str(vmensajed),int(vllaved))
        textd = desencriptado
        
        if okd and okd2:
            QtGui.QMessageBox.information(self, "Texto Descifrado", textd)
        
                                          
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Interfaz()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()