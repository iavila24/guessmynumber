import tkinter as tk
from tkinter import messagebox

class GuessNumberGameGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Adivina usuario")

        self.label = tk.Label(self.window, text="Adivina el numero 🧐")
        self.label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.button = tk.Button(self.window, text="Guess", command=self.check_guess)
        self.button.pack()

        self.random_number = 42  # Número a adivinar

    def check_guess(self):
        guess = int(self.entry.get())

        if guess == self.random_number:
            messagebox.showinfo("Adivina usuario", "⭐¡Felicidades ! ¡Adivinaste el número!⭐")
            self.window.quit()
        elif guess < self.random_number:
            messagebox.showinfo("Adivina usuario", "El número es mayor. Sigue intentando.")
        else:
            messagebox.showinfo("Adivina usuario", "El número es menor. Sigue intentando.")

        self.entry.delete(0, tk.END)

    def run(self):
        self.window.mainloop()

game = GuessNumberGameGUI()
game.run()
