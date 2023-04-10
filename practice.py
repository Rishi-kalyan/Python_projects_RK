import tkinter as tk

window = tk.Tk()

# Create the Entry widget
entry = tk.Entry(window)

# Place the Entry widget in the window
entry.pack()

# Create a Label widget to display the data
label = tk.Label(window, text="")
label.pack()

# Function to get the data from the Entry widget and update the label
def get_data():
    data = entry.get()
    label.config(text="Data entered: " + data)

# Create a button to retrieve the data
button = tk.Button(window, text="Get Data", command=get_data)
button.pack()

window.mainloop()