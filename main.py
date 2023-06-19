import tkinter as tk
import math

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

def add_trig_table():
    trig_table = ""
    for angle in range(0, 91, 10):
        radian = math.radians(angle)
        sin_value = round(math.sin(radian), 4)
        cos_value = round(math.cos(radian), 4)
        tan_value = round(math.tan(radian), 4)
        trig_table += f"sin({angle}°) = {sin_value}\n"
        trig_table += f"cos({angle}°) = {cos_value}\n"
        trig_table += f"tan({angle}°) = {tan_value}\n"
        trig_table += "-" * 20 + "\n"

    entry.delete(0, tk.END)
    entry.insert(tk.END, trig_table)

def calculate_trig_ratio():
    expression = entry.get()
    result = eval(expression)
    result = round(math.degrees(result), 4)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Trig Calculator")

# Create the entry widget
entry = tk.Entry(window, width=25)
entry.grid(row=0, column=0, columnspan=4)

# Create the number buttons
button_1 = tk.Button(window, text="1", command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", command=lambda: button_click(0))

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)

# Create the operator buttons
button_add = tk.Button(window, text="+", command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", command=lambda: button_click("/"))

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

# Create the trigonometry buttons
button_sin = tk.Button(window, text="sin", command=lambda: button_click("sin("))
button_cos = tk.Button(window, text="cos", command=lambda: button_click("cos("))
button_tan = tk.Button(window, text="tan", command=lambda: button_click("tan("))

button_sin.grid(row=1, column=4)
button_cos.grid(row=2, column=4)
button_tan.grid(row=3, column=4)

# Create the other buttons
button_equal = tk.Button(window, text="=", command=button_equal)
button_clear = tk.Button(window, text="C", command=button_clear)
button_trig_table = tk.Button(window, text="Trig Table", command=add_trig_table)
button_trig_ratio = tk.Button(window, text="Trig Ratio", command=calculate_trig_ratio)

button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=1)
button_trig_table.grid(row=5, column=0, columnspan=2)
button_trig_ratio.grid(row=5, column=2, columnspan=2)

# Run the main loop
window.mainloop()
