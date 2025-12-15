# ---------------------------------------
import tkinter as tk
#m = tkinter.Tk()

root = tk.Tk()
root.title("F1 chatbot")

# Create a button with active background and foreground colors
button = tk.Button(root, text="Click Me to Enter", activebackground="blue", activeforeground="white")
button.pack()

# Create a label with background and foreground colors
label = tk.Label(root, text="Input question", bg="lightgray", fg="black")
label.pack()

# Create an Entry widget with selection colors
entry = tk.Entry(root, selectbackground="lightblue", selectforeground="black")
entry.pack()

root.mainloop()# creates main application window
# ---------------------------------------