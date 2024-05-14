from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QTableWidgetItem, QWidget
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QMovie

#CSV
import csv
lista_clientes = []

#Función para guardar datos en el CSV
def guardar_datos_csv(datos, nombre_archivo):
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        for cliente in datos:
            escritor.writerow([cliente.apellido, cliente.nombre, cliente.dni,cliente.origen, cliente.destino])

#Ventana que muestra la lista de clientes
class ListaClientes(QDialog):
  def __init__(self):
    super().__init__()
    uic.loadUi("listaclientes.ui", self)
    self.setWindowTitle("Lista de clientes")
    self.setWindowIcon(QtGui.QIcon('media\windowIcon.png'))
    self.cargar_datos.clicked.connect(self.on_cargar_datos_actuales)
    self.guardar_datos.clicked.connect(self.on_guardar_datos)
    self.cargar_datos_guardados.clicked.connect(self.on_cargar_datos_guardados)
    self.guardar_datos.setEnabled(False)
    
  def on_cargar_datos_actuales(self):  
    for cliente in lista_clientes:
        filas = self.tabla.rowCount()
        self.tabla.insertRow(filas)
        self.tabla.setItem(filas, 0, QTableWidgetItem(cliente.apellido))
        self.tabla.setItem(filas, 1, QTableWidgetItem(cliente.nombre))
        self.tabla.setItem(filas, 2, QTableWidgetItem(cliente.dni))
        self.tabla.setItem(filas, 3, QTableWidgetItem(cliente.origen))
        self.tabla.setItem(filas, 4, QTableWidgetItem(cliente.destino))

    if self.tabla.rowCount() != 0:
        self.guardar_datos.setEnabled(True)   
        
  def on_guardar_datos(self):
      guardar_datos_csv(lista_clientes, "datos.csv")
      
  def on_cargar_datos_guardados(self):
    cuenta_filas = self.tabla.rowCount()
    archivo = open('datos.csv')

    filas = csv.reader(archivo, delimiter=',', quotechar='"')

    for fila in filas:
        self.tabla.insertRow(cuenta_filas)
        self.tabla.setItem(cuenta_filas, 0, QTableWidgetItem(fila[0]))
        self.tabla.setItem(cuenta_filas, 1, QTableWidgetItem(fila[1]))
        self.tabla.setItem(cuenta_filas, 2, QTableWidgetItem(fila[2]))
        self.tabla.setItem(cuenta_filas, 3, QTableWidgetItem(fila[3]))
        self.tabla.setItem(cuenta_filas, 4, QTableWidgetItem(fila[4]))
        
    if self.tabla.rowCount() != 0:
        self.guardar_datos.setEnabled(True)

#Clase cliente
class Cliente():
  def __init__(self, apellido, nombre, dni, origen, destino):
    self.apellido = apellido
    self.nombre = nombre
    self.dni = dni
    self.origen = origen
    self.destino = destino
    
  def __str__(self):
    return f'{self.apellido}, {self.nombre}, {self.dni}'

#Ventana principal
class menuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("menu.ui", self)
        self.catamarca_cordoba = reservarAsientos(self)
        self.catamarca_larioja = reservarAsientos(self)
        self.catamarca_tucuman = reservarAsientos(self)
        self.cordoba_catamarca = reservarAsientos(self)
        self.cordoba_larioja = reservarAsientos(self)
        self.cordoba_tucuman = reservarAsientos(self)
        self.larioja_catamarca = reservarAsientos(self)
        self.larioja_cordoba = reservarAsientos(self)
        self.larioja_tucuman = reservarAsientos(self)
        self.tucuman_catamarca = reservarAsientos(self)
        self.tucuman_cordoba = reservarAsientos(self)
        self.tucuman_larioja = reservarAsientos(self)
        self.setWindowTitle("Menú principal")
        self.setWindowIcon(QtGui.QIcon('media\windowIcon.png'))
        self.verViajesDisponibles.clicked.connect(self.on_verViajesDisponibles)
        self.verListaClientes.clicked.connect(self.on_verListaClientes)
              
    def on_verViajesDisponibles(self):
        if self.listaOrigen.currentIndex() == self.listaDestino.currentIndex():
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon('media\windowIcon.png'))
            msg.setText("El origen y el destino no pueden ser iguales")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
        else:
            if self.listaOrigen.currentText() == "Catamarca" and self.listaDestino.currentText() == "Córdoba":
                self.catamarca_cordoba.show()
            if self.listaOrigen.currentText() == "Catamarca" and self.listaDestino.currentText() == "La Rioja":
                self.catamarca_larioja.show()
            if self.listaOrigen.currentText() == "Catamarca" and self.listaDestino.currentText() == "Tucumán":
                self.catamarca_tucuman.show()
            if self.listaOrigen.currentText() == "Córdoba" and self.listaDestino.currentText() == "Catamarca":
                self.cordoba_catamarca.show()
            if self.listaOrigen.currentText() == "Córdoba" and self.listaDestino.currentText() == "La Rioja":
                self.cordoba_larioja.show()
            if self.listaOrigen.currentText() == "Córdoba" and self.listaDestino.currentText() == "Tucumán":
                self.cordoba_tucuman.show()
            if self.listaOrigen.currentText() == "La Rioja" and self.listaDestino.currentText() == "Catamarca":
                self.larioja_catamarca.show()
            if self.listaOrigen.currentText() == "La Rioja" and self.listaDestino.currentText() == "Córdoba":
                self.larioja_cordoba.show()
            if self.listaOrigen.currentText() == "La Rioja" and self.listaDestino.currentText() == "Tucumán":
                self.larioja_tucuman.show()
            if self.listaOrigen.currentText() == "Tucumán" and self.listaDestino.currentText() == "Catamarca":
                self.tucuman_catamarca.show()
            if self.listaOrigen.currentText() == "Tucumán" and self.listaDestino.currentText() == "Córdoba":
                self.tucuman_cordoba.show()
            if self.listaOrigen.currentText() == "Tucumán" and self.listaDestino.currentText() == "La Rioja":
                self.tucuman_larioja.show()
    
    def on_verListaClientes(self):
        lista = ListaClientes()
        lista.exec()

    def on_listaOrigen(self):
        origen = self.listaOrigen.currentText()  
        return origen
    
    def on_listaDestino(self):
        destino = self.listaDestino.currentText()  
        return destino

#Segunda ventana - Ver colectivos y reservar asientos
class reservarAsientos(QMainWindow):
    def __init__(self, ventanaPadre):
        super().__init__()
        uic.loadUi("reservarAsiento.ui", self)
        self.setWindowIcon(QtGui.QIcon('media\windowIcon.png'))    
        self.ventanaPadre = ventanaPadre
        self.setWindowTitle("Reservar asiento")
        self.iniciarViaje = iniciarViaje()
        self.aceptar.clicked.connect(self.on_aceptar)
        self.A1.clicked.connect(lambda: self.on_reservar("A1"))
        self.A2.clicked.connect(lambda: self.on_reservar("A2"))
        self.A3.clicked.connect(lambda: self.on_reservar("A3"))
        self.A4.clicked.connect(lambda: self.on_reservar("A4"))
        self.A5.clicked.connect(lambda: self.on_reservar("A5"))
        self.A6.clicked.connect(lambda: self.on_reservar("A6"))
        self.A7.clicked.connect(lambda: self.on_reservar("A7"))
        self.A8.clicked.connect(lambda: self.on_reservar("A8"))
        self.A9.clicked.connect(lambda: self.on_reservar("A9"))
        self.A10.clicked.connect(lambda: self.on_reservar("A10"))
        self.A11.clicked.connect(lambda: self.on_reservar("A11"))
        self.B1.clicked.connect(lambda: self.on_reservar("B1"))
        self.B2.clicked.connect(lambda: self.on_reservar("B2"))
        self.B3.clicked.connect(lambda: self.on_reservar("B3"))
        self.B4.clicked.connect(lambda: self.on_reservar("B4"))
        self.B5.clicked.connect(lambda: self.on_reservar("B5"))
        self.B6.clicked.connect(lambda: self.on_reservar("B6"))
        self.B7.clicked.connect(lambda: self.on_reservar("B7"))
        self.B8.clicked.connect(lambda: self.on_reservar("B8"))
        self.B9.clicked.connect(lambda: self.on_reservar("B9"))
        self.B10.clicked.connect(lambda: self.on_reservar("B10"))
        self.B11.clicked.connect(lambda: self.on_reservar("B11"))
        self.botonIniciarViaje.clicked.connect(self.on_botonIniciarViaje)

    def on_botonIniciarViaje(self):
        listaAsientos = [self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7, self.A8, self.A9, self.A10, self.A11, self.B1, self.B2, self.B3, self.B4, self.B5, self.B6, self.B7, self.B8, self.B9, self.B10, self.B11]
        for asiento in listaAsientos:
            asiento.setText("Libre")
            asiento.setStyleSheet('QPushButton {background-color: #0c9c18; border-radius: 10%; color: #ffffff;}')
            asiento.setStyleSheet('QPushButton::hover {background-color: #075c0e;}')
        self.hide()
        self.iniciarViaje.show()

    def on_aceptar(self):
        self.hide()
        self.ventanaPadre.show()

    def on_reservar(self, asiento):
        boton = getattr(self, asiento)
        if boton.text() == "Libre":
            crear_dialogo(boton)
        elif boton.text() == "X" :
            cancelar_reserva(boton)

#Formulario que toma los datos del pasajero
class Formulario(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("formulario.ui", self)
        self.setWindowTitle("Ingresar datos")
        self.setWindowIcon(QtGui.QIcon('media\windowIcon.png'))
    
    def getCliente(self):
        dni = self.dni.text()
        apellido = self.apellido.text()
        nombre = self.nombre.text()
        origen = mainMenu.on_listaOrigen()
        destino = mainMenu.on_listaDestino()
        if dni != None or apellido == "" or nombre == "" or origen == "" or destino == "":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Question)
            msgBox.setText("Tienes que llenar todos los campos")
            msgBox.setWindowTitle("Warning")
            msgBox.setWindowIcon(QtGui.QIcon('media\windowIcon.png'))
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        else:    
            return Cliente(apellido, nombre, dni, origen, destino)

#Función utilizada para reservar un asiento
def crear_dialogo(boton):
   formulario = Formulario()
   if (formulario.exec()):
       boton.setText("X")
       boton.setStyleSheet('QPushButton {background-color: #82150d;}')
       cliente = formulario.getCliente()
       lista_clientes.append(cliente)

# Cancelar asiento reservado
def cancelar_reserva(boton):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Icon.Question)
    msgBox.setText("¿Estás seguro de que quieres cancelar la reserva de este asiento?")
    msgBox.setWindowTitle("Cancelar reservas")
    msgBox.setWindowIcon(QtGui.QIcon('media\windowIcon.png'))
    msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    opcion = msgBox.exec()

    if opcion == QMessageBox.StandardButton.Yes:
        boton.setText("Libre")
        boton.setStyleSheet('QPushButton {background-color: #0c9c18; border-radius: 10%; color: #ffffff;}')
        boton.setStyleSheet('QPushButton::hover {background-color: #075c0e;}') 

#Ventana que indica que ha partido un colectivo
class iniciarViaje(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("iniciarViaje.ui", self)
        self.setWindowTitle("Viaje iniciado")
        self.setWindowIcon(QtGui.QIcon('media\windowIcon.png'))
        self.movie = QMovie("media\iniciarViaje.gif")
        self.label.setMovie(self.movie)
        self.movie.start() 

#------------------------#
app = QApplication([])
mainMenu = menuPrincipal()
mainMenu.show()
app.exec()