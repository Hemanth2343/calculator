import tkinter as tk

# Logic for button click
def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Setup window
root = tk.Tk()
root.title("🧮 Calculator")
root.geometry("300x400")

# Entry box
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10)

# Buttons layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        action = lambda x=btn_text: calculate() if x == '=' else button_click(x)
        tk.Button(root, text=btn_text, width=5, height=2, font=('Arial', 18), command=action).grid(row=i+1, column=j, padx=5, pady=5)

# Clear button
tk.Button(root, text="C", width=22, height=2, font=('Arial', 18), command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=10)

root.mainloop()
