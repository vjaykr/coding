import tkinter as tk
from tkinter import messagebox

def generate_magic_square(n):
    if n % 2 == 0:
        messagebox.showerror("Error", "Only odd numbers are supported!")
        return None
    
    magic_square = [[0] * n for _ in range(n)]
    
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic_square[new_i][new_j]:
            i += 1
        else:
            i, j = new_i, new_j
    
    return magic_square

def display_magic_square():
    try:
        n = int(entry.get())
        if n % 2 == 0 or n < 1:
            messagebox.showerror("Error", "Please enter a positive odd number.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Enter an integer.")
        return
    
    magic_square = generate_magic_square(n)
    if magic_square:
        for widget in frame.winfo_children():
            widget.destroy()
        
        for i in range(n):
            for j in range(n):
                label = tk.Label(frame, text=str(magic_square[i][j]), font=("Arial", 14), width=5, height=2, borderwidth=2, relief="ridge")
                label.grid(row=i, column=j, padx=2, pady=2)

# GUI Setup
root = tk.Tk()
root.title("Magic Square Generator")

# Input Section
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter an odd number:", font=("Arial", 12)).pack(side=tk.LEFT)
entry = tk.Entry(input_frame, font=("Arial", 12), width=5)
entry.pack(side=tk.LEFT, padx=5)

tk.Button(input_frame, text="Generate", font=("Arial", 12), command=display_magic_square).pack(side=tk.LEFT)

# Display Frame
frame = tk.Frame(root)
frame.pack(pady=10)

root.mainloop()
