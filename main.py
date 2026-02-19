import numpy as np
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = Figure()
        super().__init__(fig)
        self.ax = fig.add_subplot(111)

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Direction Field App")
window.resize(750, 750)

central_widget = QWidget()
layout = QVBoxLayout(central_widget)

canvas = MplCanvas()
layout.addWidget(canvas)
def f(x, y):
    return x - y

density = 30
x = np.linspace(-10, 10, density)
y = np.linspace(-10, 10, density)

X, Y = np.meshgrid(x, y)

DY = f(X, Y)
DX = np.ones_like(DY)

magnitude = np.sqrt(DX**2 + DY**2)
DX = DX / magnitude
DY = DY / magnitude
canvas.ax.set_aspect("equal")

canvas.ax.quiver(X, Y, DX, DY)
canvas.draw()
window.setCentralWidget(central_widget)
window.show()

sys.exit(app.exec())
