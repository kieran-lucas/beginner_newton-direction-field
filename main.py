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
window.resize(800, 600)

central_widget = QWidget()
layout = QVBoxLayout(central_widget)

canvas = MplCanvas()
layout.addWidget(canvas)

window.setCentralWidget(central_widget)
window.show()

sys.exit(app.exec())
