import counting_pages
import getting_sports_time
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
    header = {
        'cookie': cookies,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'upgrade-insecure-requests': '1'
    }
    pages_soccer_number: int = counting_pages.pages_counting(header, 'soccer')
    pages_tennis_number: int = counting_pages.pages_counting(header, 'tennis')
    getting_sports_time.sport_time(pages_soccer_number, header, 'soccer')
    getting_sports_time.sport_time(pages_tennis_number, header, 'tennis')
    tkinter.messagebox.showinfo(title='Success', message='Time for tennis and soccer is created')


btn=tkinter.Button(frame, text='Create results', width=30, command=main)
btn.place(x=150, y=150)







root.mainloop()
