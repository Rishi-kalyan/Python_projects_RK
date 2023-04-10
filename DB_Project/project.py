
import cx_Oracle
import tkinter as tk

dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
connection = cx_Oracle.connect('hr', 'hr', dsn)
cursor = connection.cursor()

def display_output():
    query = 'SELECT * FROM employees'
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        output.insert(tk.END, f"{row}\n")

window = tk.Tk()

# create the button and output widgets
button = tk.Button(window, text="Execute Query", command=display_output)
output = tk.Text(window)

# place the button and output widgets using the grid method
button.grid(row=0, column=0, padx=10, pady=10)
output.grid(row=1, column=0, padx=10, pady=10)

# run the Tkinter event loop
window.mainloop()