import tkinter as tk

# Main calculator window
root = tk.Tk()
root.title("🧮 Real Calculator")
root.geometry("510x600")
root.resizable(False, False)

expression = ""

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Evaluate the expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Clear all
def clear():
    global expression
    expression = ""
    equation.set("")

# Delete last character
def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# Toggle positive/negative
def toggle_sign():
    global expression
    if expression.startswith('-'):
        expression = expression[1:]
    else:
        expression = '-' + expression
    equation.set(expression)

# Apply percentage
def apply_percentage():
    global expression
    try:
        value = float(expression)
        value /= 100
        expression = str(value)
        equation.set(expression)
    except:
        equation.set("Error")
        expression = ""

# Create input field
equation = tk.StringVar()
input_field = tk.Entry(root, textvariable=equation, font=('Arial', 24), bd=10, relief='ridge', justify='right')
input_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, pady=20)

# Button layout
buttons = [
    ('C', 1, 0), ('⌫', 1, 1), ('%', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('+/-', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3),
]

# Create buttons with real logic
for (text, row, col) in buttons:
    if text == '=':
        action = equalpress
    elif text == 'C':
        action = clear
    elif text == '⌫':
        action = backspace
    elif text == '+/-':
        action = toggle_sign
    elif text == '%':
        action = apply_percentage
    else:
        action = lambda x=text: press(x)

    tk.Button(root, text=text, width=9, height=3, font=('Arial', 16), command=action)\
        .grid(row=row, column=col, padx=5, pady=5)

root.mainloop()