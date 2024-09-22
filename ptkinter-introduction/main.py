import tkinter

window = tkinter.Tk()


window.title("My first GUI program")
window.minsize(height=300, width=500)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left", expand=True)










window.mainloop()