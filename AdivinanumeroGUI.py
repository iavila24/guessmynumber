import random
from pygame import mixer
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton,QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5 import QtCore,QtWidgets
from PyQt5.uic import loadUi

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        mixer.init()
        mixer.music.load('music.mp3')
        mixer.music.play()

        super(VentanaPrincipal,self).__init__()
        loadUi('GUI/Interfaz.ui',self)

        self.setWindowTitle("Menu Principal")
        
        self.bt_menu_uno.clicked.connect(self.mover_menu)
        self.bt_menu_dos.clicked.connect(self.mover_menu)

        self.bt_restaurar.hide()
        self.bt_menu_dos.hide()

        self.sombra_frame(self.frame_superior)
        self.sombra_frame(self.bt_Numero)
        

        #Control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        #Eliminar barra de titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #SizeGrip
        self.gripSize=10
        self.grip= QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        #Mover Ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        self.Etiqueta.setText("Ingresa tu nombre: ") 
        self.Etiqueta_2.setText("Piensa en un número: ") 

        self.boton_verificar.clicked.connect(self.adivinar_numero)


    def adivinar_numero(self):
       name = self.entrada_nombre.text()
       
       x = int(self.entrada_numero.text())
       low = 1
       high = x
       guess = random.randint(low, high)
       
       
       
       if x==guess:
           self.etiqueta_resultado.setText(('He adivinado tu numero es ' + str(guess)).lower())
           with open('nombres.txt', 'a') as file:
                file.write(f'\nNombre: {name}')# Se corrigio el error de espacio en el codigo

           with open('nombres.txt', 'r') as file:
                lines = file.readlines()
                last_five_names = lines[-5:]
                print("\nÚltimos 5 nombres almacenados:")
                for name_line in last_five_names:
                    print(name_line.strip())
       else:
           self.etiqueta_resultado.setText(('Me equivoque tu numero es ' + str(guess)).lower())
           with open('nombres.txt', 'a') as file:
                file.write(f'\nNombre: {name}')# Se corrigio el error de espacio en el codigo

           with open('nombres.txt', 'r') as file:
                lines = file.readlines()
                last_five_names = lines[-5:]
                print("\nÚltimos 5 nombres almacenados:")
                for name_line in last_five_names:
                    print(name_line.strip())

    def control_bt_minimizar(self):
        self.showMinimized()

    def control_bt_normal(self):
        self.showNormal()
        self.bt_restaurar.hide()
        self.bt_maximizar.show()

    def control_bt_maximizar(self):
        self.showMaximized()
        self.bt_maximizar.hide()
        self.bt_restaurar.show()    

    #Metodo para sombras
    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)    
        sombra.setXOffset(8)
        sombra.setYOffset(8)
        sombra.setColor(QColor(20, 200, 220, 255))
        frame.setGraphicsEffect(sombra)

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    #Mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized()== False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=10:
            self.showMaximized()
            self.bt_restaurar.hide()
            self.bt_maximizar.show()
        else:
            self.showNormal()
            self.bt_restaurar.hide()
            self.bt_maximizar.show()    
                           
    def mover_menu(self):
        if True:
            width = self.menu_lateral.width()
            normal = 0
            if width==0:
                extender=300
                self.bt_menu_dos.hide()
                self.bt_menu_uno.show()
            else:
                self.bt_menu_dos.show()    
                self.bt_menu_uno.hide()
                extender = normal
            self.animacion = QPropertyAnimation(self.menu_lateral, b"maximumWidth")
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setDuration(500)
            self.animacion.setEasingCurve(QEasingCurve.OutInBack)
            self.animacion.start()               
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())
