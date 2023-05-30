import tkinter as tk
from tkinter import messagebox
import random

class GuessingGameGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Adivina la computadora")

        self.target_number = None
        self.min_value = 1
        self.max_value = 100

        self.label = tk.Label(self.window, text="Ingresa un número:")
        self.label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.start_button = tk.Button(self.window, text="Comenzar", command=self.start_game)
        self.start_button.pack()

        self.guess_button = tk.Button(self.window, text="¡Es correcto!", command=self.correct_guess, state=tk.DISABLED)
        self.guess_button.pack()

        self.higher_button = tk.Button(self.window, text="El número es mayor", command=self.number_is_higher, state=tk.DISABLED)
        self.higher_button.pack()

        self.lower_button = tk.Button(self.window, text="El número es menor", command=self.number_is_lower, state=tk.DISABLED)
        self.lower_button.pack()

        self.computer_guess_label = tk.Label(self.window, text="")
        self.computer_guess_label.pack()

        self.is_guess_correct = False

    def start_game(self):
        try:
            self.target_number = int(self.entry.get())
            self.entry.config(state=tk.DISABLED)
            self.start_button.config(state=tk.DISABLED)
            self.guess_button.config(state=tk.NORMAL)
            self.higher_button.config(state=tk.NORMAL)
            self.lower_button.config(state=tk.NORMAL)
            self.guess_number()
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido.")

    def guess_number(self):
        if self.min_value <= self.max_value:
            guess = random.randint(self.min_value, self.max_value)
            self.computer_guess_label.config(text=f"Intento de la computadora: {guess}")
            if guess == self.target_number:
                self.is_guess_correct = True
            elif guess < self.target_number:
                self.min_value = guess + 1
            else:
                self.max_value = guess - 1
        else:
            messagebox.showerror("Error", "Algo salió mal. Reinicia el juego.")
            self.reset_game()

    def correct_guess(self):
        if self.is_guess_correct:
            messagebox.showinfo("¡Adiviné!", "¡Ouyeah, soy la mejor computadora! 😎👌")
        else:
            messagebox.showinfo("Mensaje", "Presiona este botón solo si la computadora adivinó el número.")
        self.reset_game()

    def number_is_higher(self):
        self.min_value += 1
        self.guess_number()

    def number_is_lower(self):
        self.max_value -= 1
        self.guess_number()

    def reset_game(self):
        self.target_number = None
        self.min_value = 1
        self.max_value = 100
        self.entry.delete(0, tk.END)
        self.entry.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.DISABLED)
        self.higher_button.config(state=tk.DISABLED)
        self.lower_button.config(state=tk.DISABLED)
        self.computer_guess_label.config(text="")
        self.is_guess_correct = False

    def run(self):
        self.window.mainloop()

game = GuessingGameGUI()
game.run()
