from PySide6.QtWidgets import QApplication
from controller import GameController
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = GameController()
    controller.ui.show()
    sys.exit(app.exec())
