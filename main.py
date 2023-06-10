from tkinter import *


def miles_to_km():
    miles = float(entry_field.get())
    km = miles * 1.609
    results_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometres Conversion")
window.config(padx=20, pady=20)

entry_field = Entry()
entry_field.grid(column=1, row=0)
miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)
isEqual_label = Label(text='is equal to')
isEqual_label.grid(column=0, row=1)
results_label = Label(text='0')
results_label.grid(column=1, row=1)
kilometres_label = Label(text='Kilometres')
kilometres_label.grid(column=2, row=1)
calculate_button = Button(text='calculate', command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
