import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

def press(num):
    current_expression = expression_var.get()
    expression_var.set(current_expression + str(num))

def delete():
    current_expression = expression_var.get()
    expression_var.set(current_expression[:-1])

def evaluate():
    try:
        current_expression = expression_var.get()
        result = str(eval(current_expression))
        operation_label.config(text=current_expression)
        expression_var.set(result)
    except Exception as e:
        expression_var.set("Error")

def clear():
    expression_var.set("")
    operation_label.config(text="")

def create_button(gui, text, row, col, command, width=8):
    btn = ttk.Button(gui, text=text, style='CalculatorButton.TButton', command=command)
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    btn.config(width=width)

def run_calculator():
    global expression_var, operation_label
    gui = tk.Tk()
    gui.title("Modern Calculator")
    gui.geometry("383x290")
    gui.configure(bg="white")

    style = ttk.Style()
    style.theme_use("default")

    expression_var = tk.StringVar()
    expression_entry = ttk.Entry(gui, textvariable=expression_var, font=("Helvetica", 24), justify="right")
    expression_entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

    operation_label = ttk.Label(gui, text="", font=("Helvetica", 12))
    operation_label.grid(row=1, column=0, columnspan=4, pady=(0, 5))

    buttons = [
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('/', 3, 3),
        ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('*', 4, 3),
        ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('-', 5, 3),
        ('0', 6, 0), ('.', 6, 1), ('=', 6, 2), ('+', 6, 3)
    ]

    for (text, row, col) in buttons:
        if text == '=':
            create_button(gui, text, row, col, evaluate, width=16)
        elif text == 'del':
            create_button(gui, text, row, col, delete, width=16)
        else:
            create_button(gui, text, row, col, lambda num=text: press(num), width=8)


    gui.mainloop()

if __name__ == "__main__":
    run_calculator()
