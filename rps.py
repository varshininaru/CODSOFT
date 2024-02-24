import tkinter as tk
from tkinter import messagebox
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("300x200")
        
        self.player_score = 0
        self.comp_score = 0
        
        self.label = tk.Label(root, text="Choose: Rock, Paper, or Scissors", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()
        
        self.rock_btn = tk.Button(self.buttons_frame, text="Rock", command=lambda: self.check_winner("rock"))
        self.rock_btn.grid(row=0, column=0, padx=5)
        
        self.paper_btn = tk.Button(self.buttons_frame, text="Paper", command=lambda: self.check_winner("paper"))
        self.paper_btn.grid(row=0, column=1, padx=5)
        
        self.scissors_btn = tk.Button(self.buttons_frame, text="Scissors", command=lambda: self.check_winner("scissors"))
        self.scissors_btn.grid(row=0, column=2, padx=5)
        
        self.score_label = tk.Label(root, text=f"Score: Player - {self.player_score}, Computer - {self.comp_score}")
        self.score_label.pack(pady=5)
        
        self.play_again_btn = tk.Button(root, text="Play Again", command=self.reset_game)
        self.play_again_btn.pack(pady=5)
        
    def check_winner(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        comp_choice = random.choice(choices)
        
        if player_choice == comp_choice:
            result = "It's a tie!"
        elif (player_choice == "rock" and comp_choice == "scissors") or \
             (player_choice == "paper" and comp_choice == "rock") or \
             (player_choice == "scissors" and comp_choice == "paper"):
            result = "You win!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.comp_score += 1
        
        messagebox.showinfo("Result", f"Player's choice: {player_choice}\nComputer's choice: {comp_choice}\n{result}")
        self.update_score_label()
        
    def update_score_label(self):
        self.score_label.config(text=f"Score: Player - {self.player_score}, Computer - {self.comp_score}")
        
    def reset_game(self):
        self.player_score = 0
        self.comp_score = 0
        self.update_score_label()

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSGame(root)
    root.mainloop()
