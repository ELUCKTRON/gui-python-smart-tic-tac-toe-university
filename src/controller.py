from ui import GameBoardUI
from logic import TicTacToe
from PySide6.QtWidgets import QApplication
import sys


class GameController:
    def __init__(self):
        self.ui = GameBoardUI()
        self.game = TicTacToe()

        self.xScore = 0
        self.oScore = 0

        self.update_score_label()
        self.ui.status_label.setText("Status: X's turn")

        for row in range(3):
            for col in range(3):
                self.ui.buttons[row][col].clicked.connect(
                    lambda _, r=row, c=col: self.make_move(r, c)
                )

        self.ui.next_game_button.clicked.connect(self.next_game)
        self.ui.reset_button.clicked.connect(self.reset_scores)
        self.ui.exit_button.clicked.connect(self.exit_game)

        self.ui.show()

    def update_score_label(self):
        self.ui.x_score_label.setText(f"X: {self.xScore}")
        self.ui.o_score_label.setText(f"O: {self.oScore}")

    def make_move(self, r, c):
        if not self.game.status:
            return

        current_player = self.game.playerTurn()
        self.ui.buttons[r][c].setText(current_player)
        self.ui.buttons[r][c].setEnabled(False)
        self.game.matrix[r][c] = current_player

        if self.game.isWon(current_player):
            self.ui.status_label.setText(f"Status: {current_player} wins!")
            self.game.status = False
            if current_player == "X":
                self.xScore += 1
            else:
                self.oScore += 1
            self.update_score_label()
            self.disable_board()
            return

        elif self.game.isDraw():
            self.ui.status_label.setText("Status: It's a draw!")
            self.game.status = False
            return

        self.game.turn += 1
        self.ui.status_label.setText("Status: O (AI) is thinking...")
        QApplication.processEvents()  # Force UI update

        # ---- AI MOVE ----
        move = self.game.aiPlay()
        r_ai, c_ai = int(move[0]), int(move[1])
        self.ui.buttons[r_ai][c_ai].setText("O")
        self.ui.buttons[r_ai][c_ai].setEnabled(False)
        self.game.matrix[r_ai][c_ai] = "O"

        if self.game.isWon("O"):
            self.ui.status_label.setText("Status: O wins!")
            self.game.status = False
            self.oScore += 1
            self.update_score_label()
            self.disable_board()
        elif self.game.isDraw():
            self.ui.status_label.setText("Status: It's a draw!")
            self.game.status = False
        else:
            self.game.turn += 1
            self.ui.status_label.setText("Status: X's turn")

    def next_game(self):
        self.game = TicTacToe()
        self.ui.reset()
        self.ui.status_label.setText("Status: X's turn")

    def reset_scores(self):
        self.xScore = 0
        self.oScore = 0
        self.update_score_label()
        self.next_game()

    def disable_board(self):
        for row in range(3):
            for col in range(3):
                self.ui.buttons[row][col].setEnabled(False)

    def exit_game(self):
        self.ui.close()

