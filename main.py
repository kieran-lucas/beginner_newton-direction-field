import numpy as np
import sympy as sp
import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLineEdit, QPushButton,
    QHBoxLayout
)
from PySide6.QtGui import QFont

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = Figure()
        super().__init__(fig)
        self.ax = fig.add_subplot(111)


class DirectionFieldApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Direction Field App")
        self.resize(750, 750)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout(central_widget)

        input_layout = QHBoxLayout()

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Enter dy/dx = f(x,y)")

        font = QFont("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        self.input_box.setFont(font)

        self.plot_button = QPushButton("Plot")
        self.plot_button.setFont(font)

        input_layout.addStretch()
        input_layout.addWidget(self.input_box)
        input_layout.addWidget(self.plot_button)
        input_layout.addStretch()

        self.layout.addLayout(input_layout)

        self.canvas = MplCanvas()
        self.layout.addWidget(self.canvas)

        self.plot_button.clicked.connect(self.handle_plot)

        self.x_sym, self.y_sym = sp.symbols("x y")


    def handle_plot(self):
        expr_text = self.input_box.text()

        if not expr_text:
            return

        try:
            expr = sp.sympify(expr_text)

            f = sp.lambdify((self.x_sym, self.y_sym), expr, "numpy")

            density = 28
            x = np.linspace(-10, 10, density)
            y = np.linspace(-10, 10, density)
            X, Y = np.meshgrid(x, y)

            DY = f(X, Y)
            DX = np.ones_like(DY)

            magnitude = np.sqrt(DX**2 + DY**2)
            DX = DX / magnitude
            DY = DY / magnitude

            self.canvas.ax.clear()
            self.canvas.ax.set_aspect("equal")


            self.canvas.ax.quiver(X, Y, DX, DY)
            self.canvas.draw()

        except Exception as e:
            print("Error:", e)

# Run
app = QApplication(sys.argv)
window = DirectionFieldApp()
window.show()
sys.exit(app.exec())
