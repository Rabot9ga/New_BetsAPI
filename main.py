from getting_sports_time import Sports
import tkinter, tkinter.messagebox

root = tkinter.Tk()
root.geometry('500x200')

canvas = tkinter.Canvas(root, height=500, width=200)
canvas.pack()

frame = tkinter.Frame(root)
frame.place(relwidth=1, relheight=1)

title = tkinter.Label(frame, text='cookie: ', font=50)
title.place(x=10, y=10)

cookieField = tkinter.Entry(frame, bg='white', width=60)
cookieField.place(x=120, y=12)


def main():
    cookies = cookieField.get()
    for i in ['soccer', 'tennis', 'basketball']:
        sport = Sports(i, cookies)
        sport.sport_time()
        
    tkinter.messagebox.showinfo(title='Success', message='Time for tennis, basketball and soccer is created')


btn=tkinter.Button(frame, text='Create results', width=30, command=main)
btn.place(x=150, y=150)







root.mainloop()
