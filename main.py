from tkinter import *


def miles_to_km():
    km = 1.609 * float(input.get())
    result['text'] = km


window = Tk()
window.title("Convert miles to kilometers")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

# Entry
input = Entry(width=20)
input.grid(column=1, row=0)

mi_label = Label(text=" Miles", font=("Arial", 18, "bold"))
mi_label.grid(column=2, row=0)

equal_to_label = Label(text="Equal to: ", font=("Arial", 18, "bold"))
equal_to_label.grid(column=0, row=1)

result = Label(text="0", font=("Arial", 18, "bold"))
result.grid(column=1, row=1)

km_label = Label(text="km", font=("Arial", 18, "bold"))
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()
