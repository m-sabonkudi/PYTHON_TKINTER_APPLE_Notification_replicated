from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.config(pady=50, padx=50)
screen.title("")


def change_button():
    button1.config(image=clear_img)
    button1.config(command=work)


def work():
    canvas.itemconfig(greet, text="")
    del_love = messagebox.askyesno(title="DELETE CONFIRMATION", message="Do you also want to delete the love text?")
    if del_love:
        canvas.itemconfig(love, text="")
        button1.grid_forget()
        messagebox.showinfo(title="INFORMATION", message="Love text deleted successfully!")
    else:
        messagebox.showinfo(title="INFORMATION", message="Love text not deleted!")


with open("letter_1.txt") as file:
    data = file.read()


x_img = PhotoImage(file="wrong.png")
clear_img = PhotoImage(file="Clear.PNG")
img = PhotoImage(file="card_front.png")
canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
canvas.create_image(400, 263, image=img)
greet = canvas.create_text(400, 190, text=data, font=("Arial", 30))
love = canvas.create_text(400, 420, text="yours, most lovely ❤️", font=("Comic Sans MS", 30, "italic"))
canvas.grid(column=2, row=0)
button1 = Button(image=x_img, command=change_button, highlightthickness=0, bg="white")
button1.grid(column=2, row=1)







screen.mainloop()