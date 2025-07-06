from PySide6.QtWidgets import (
    QWidget, QPushButton, QLabel, QGridLayout,
    QVBoxLayout, QHBoxLayout, QSizePolicy
)
from PySide6.QtCore import Qt


class GameBoardUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Tic Tac Toe")
        self.setFixedSize(300, 420)  

        # ---- Main vertical layout ----
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(5, 5, 5, 5)
        self.main_layout.setSpacing(10)
        self.setLayout(self.main_layout)

        # ---- Score display ----
        self.score_layout = QHBoxLayout()
        self.x_score_label = QLabel("X: 0")
        self.o_score_label = QLabel("O: 0")
        self.score_layout.addWidget(self.x_score_label)
        self.score_layout.addStretch()
        self.score_layout.addWidget(self.o_score_label)
        self.main_layout.addLayout(self.score_layout)

        # ---- Status label ----
        self.status_label = QLabel("Status: X's turn")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.status_label)

        # ---- Grid layout for game board ----
        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setAlignment(Qt.AlignCenter)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for row in range(3):
            for col in range(3):
                button = QPushButton("-")
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                button.setStyleSheet("padding: 0px; margin: 0px; border: 1px solid black;")
                self.grid.addWidget(button, row, col)
                self.buttons[row][col] = button

        self.main_layout.addLayout(self.grid)

        # ---- Control buttons ----
        self.control_layout = QHBoxLayout()
        self.control_layout.setSpacing(10)

        self.next_game_button = QPushButton("Next Game")
        self.reset_button = QPushButton("Reset")
        self.exit_button = QPushButton("Exit")

        self.control_layout.addWidget(self.next_game_button)
        self.control_layout.addWidget(self.reset_button)
        self.control_layout.addWidget(self.exit_button)

        self.main_layout.addLayout(self.control_layout)

    def reset(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText("-")
                self.buttons[row][col].setEnabled(True)
