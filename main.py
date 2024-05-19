import sys
import math as m
from PyQt5 import QtWidgets
from interfaz import Ui_MainWindow

def pitagoras(x, y):
    xmax = m.sqrt(x**2 + y**2)
    return round(xmax, 2)

def angulobase(pit, y):
    ab = m.asin(y / pit)
    return ab

def angulocompas(pit):
    results = []
    for i in range(45, 91):
        compa = round((5.3**2 * m.sin(2 * m.radians(i))) / 9.8, 2)
        results.append((i, compa))
    return results

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Calcular.clicked.connect(self.calculate)
        self.delete_2.clicked.connect(self.clear)

    def calculate(self):
        try:
            x = float(self.line1.text()) / 100  # convertir de cm a metros
            y = float(self.line2.text()) / 100  # convertir de cm a metros
            pit = pitagoras(x, y)
            base_angle = angulobase(pit, y)
            compas_results = angulocompas(pit)

            self.value1.clear()  # Limpiar las listas antes de agregar nuevos resultados
            self.value2.clear()

            self.value1.addItem(f"El objetivo está a: {pit} metros.")
            self.value1.addItem(f"El ángulo de la base es de {base_angle:.2f} radianes.")
            
            self.value2.addItem("Ángulos de elevación (grados y distancia):")
            for angle, dist in compas_results:
                self.value2.addItem(f"{angle}° = {dist} m")
        except ValueError:
            self.value1.clear()
            self.value2.clear()
            self.value1.addItem("Por favor ingrese valores numéricos válidos.")

    def clear(self):
        self.line1.clear()
        self.line2.clear()
        self.value1.clear()
        self.value2.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
