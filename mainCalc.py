import tkinter as tk

# Button layout
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

# Colors
color_light_grey = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_grey = "#505050"
color_orange = "#FF9500"
color_white = "white"

row_count = len(button_values)
column_count = len(button_values[0])

# Window setup
window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)

# Frame Display
frame = tk.Frame(window, background=color_black)
frame.pack(expand=True, fill="both")

# Label display
label = tk.Label(frame, text="0", font=("Arial", 40),
                 background=color_black, foreground=color_white,
                 anchor="e", padx=10)
label.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Button click handler
def button_clicked(value):
    current = label.cget("text")

    if value == "AC":
        label.config(text="0")
        return

    elif value == "+/-":
        if current.startswith("-"):
            label.config(text=current[1:])
        else:
            label.config(text="-" + current)
        return

    elif value == "=":
        expression = current.replace("×", "*").replace("÷", "/")
        try:
            result = eval(expression)
            label.config(text=str(result))
        except:
            label.config(text="Error")
        return

    if current == "0":
        label.config(text=value)
    else:
        label.config(text=current + value)

# Buttons
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tk.Button(
            frame,
            text=value,
            font=('Arial', 20),
            bg=color_dark_grey if value not in ["÷", "×", "-", "+", "="] else color_orange,
            fg=color_white,
            borderwidth=0,
            command=lambda value=value: button_clicked(value)
        )
        button.grid(row=row+1, column=column, sticky="nsew")

# Configure grid scaling
for i in range(row_count + 1):
    frame.rowconfigure(i, weight=1)
for i in range(column_count):
    frame.columnconfigure(i, weight=1)

window.mainloop()
