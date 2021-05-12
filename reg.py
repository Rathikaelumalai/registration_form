from tkinter import *
#from tkinter import tk
import sqlite3

root = Tk()
root.geometry("600x500")
root.title("Registration form")
#root["bg"] = ""


Authorname = StringVar()
Publisheddate = IntVar()
Bookname = StringVar()
Bookprice = IntVar()
Time = IntVar()


def database():
    authorname = Authorname.get()
    publisheddate = Publisheddate.get()
    bookname = Bookname.get()
    bookprice = Bookprice.get()
    time = Time.get()
    conn = sqlite3.connect('reg.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Book(Atuhorname Text,Publisheddate INTEGER,Bookname TEXT,Bookprice INTEGER,Time INTEGER)')
    cursor.execute('INSERT INTO Book(Atuhorname,Publisheddate,Bookname,Bookprice,Time) VALUES(?,?,?,?,?)',(authorname,publisheddate,bookname,bookprice,time,))
    conn.commit()



label_1 = Label(root, text = "Registration Form", width=20, font=("bold",20))
label_1.place(x=90,y=53)

label_2 = Label(root, text = "Author Name", width=20, font=("bold",10))
label_2.place(x=90,y=130)

entry_2 = Entry(root, textvar=Authorname)
entry_2.place(x=240,y=130)

label_3 = Label(root, text = "Published date", width=20, font=("bold",10))
label_3.place(x=70,y=230)

entry_3 = Entry(root, textvar=Authorname)
entry_3.place(x=240,y=230)

label_4 = Label(root, text = "Book Name", width=20, font=("bold",10))
label_4.place(x=68,y=180)

entry_4 = Entry(root, textvar=Bookname)
entry_4.place(x=240,y=180)

label_5 = Label(root, text = "Book price", width=20, font=("bold",10))
label_5.place(x=70,y=280)

entry_5 = Entry(root, textvar=Authorname)
entry_5.place(x=240,y=280)

label_6 = Label(root, text = "Time", width=20, font=("bold",10))
label_6.place(x=85,y=330)

entry_6 = Entry(root, textvar=Authorname)
entry_6.place(x=240,y=330)

Button(root, text="Submit", width=20, bg="brown", fg="white", command=database).place(x=180,y=380)
root.mainloop()







