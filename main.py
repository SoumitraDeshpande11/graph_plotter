import tkinter as tk
from tkinter import messagebox
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def plot_user_equation(equation_str):

    x, y = sp.symbols('x y')

    try:

        if '=' not in equation_str:
            raise ValueError("Please include an '=' sign in the equation (e.g., 'y = x**2').")

        left_side, right_side = equation_str.split('=')
        left_side = left_side.strip()
        right_side = right_side.strip()


        expr = sp.sympify(right_side)

        if left_side == 'y':

            equation_func = sp.lambdify(x, expr, "numpy")
            x_values = np.linspace(-10, 10, 1000)
            y_values = equation_func(x_values)

            # Plot the function
            plt.figure(figsize=(8, 6))
            plt.plot(x_values, y_values, label=f"{equation_str}")
            plt.xlabel("x")
            plt.ylabel("y")

        elif left_side == 'x':

            x_value = float(expr)
            y_values = np.linspace(-10, 10, 1000)
            x_values = np.full_like(y_values, x_value)


            plt.figure(figsize=(8, 6))
            plt.plot(x_values, y_values, label=f"{equation_str}")
            plt.xlabel("x")
            plt.ylabel("y")

        else:
            raise ValueError("Only 'x' or 'y' can be on the left side of the equation.")

        plt.title("Graph of the equation")
        plt.grid(True)
        plt.legend()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Invalid equation! Please check the format.\n\nDetails: {e}")


def on_plot_button_click():
    equation_str = equation_entry.get()
    if equation_str.strip():
        plot_user_equation(equation_str)
    else:
        messagebox.showwarning("Input Required", "Please enter an equation to plot.")



root = tk.Tk()
root.title("Equation Plotter")
root.geometry("400x200")


label = tk.Label(root, text="Enter an equation (e.g., 'y = x**2 - 3*x + 2' or 'x = 5'):")
label.pack(pady=10)

equation_entry = tk.Entry(root, width=40)
equation_entry.pack(pady=10)

plot_button = tk.Button(root, text="Plot Equation", command=on_plot_button_click)
plot_button.pack(pady=10)


root.mainloop()
