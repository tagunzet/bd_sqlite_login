import sqlite3
import tkinter
from tkinter import *
#from one import Connect, Create , Check_database
#from two import *
from one import Connect, Create , Check_database

def addItem():
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master;")
    conn.commit()
    rows = cursor.fetchall()
    lbox.delete(0, END)
    for row in rows:

        lbox.insert(END, row)



def delList():
    creates = Create("создание базы данных")
    creates.create_db(entry.get())


def saveList():
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    sqlzap = "DROP TABLE "+entry.get()+";"
    print("удалено")
    cursor.execute(sqlzap)
    conn.commit()
    rows = cursor.fetchall()
    lbox.delete(0, END)
    for row in rows:
        lbox.insert(END, row)





def new_frame():
    global entrylogin
    global entrypassword
    global base
    listFrame = tkinter.Frame(root, width=350)
    listFrame.pack(side="top", fill="both")
    base = Entry(listFrame)
    base.pack(anchor=N)
    entrylogin = Entry(listFrame)
    entrylogin.pack(anchor=N)
    entrypassword = Entry(listFrame)
    entrypassword.pack(anchor=N)
    buttonframe = tkinter.Button(listFrame, text="Войти",command=login_base)
    buttonframe.pack(side="bottom")


def login_base():
    print(entrylogin.get())
    abba = entrylogin.get()

    print(entrypassword.get())
    print('base=' + base.get())
    eee = "password LIKE " + "'%"+ abba + "%';"
    #eee = 'login LIKE "' +abba+'%";'
    print(eee)

    try:
        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()
        #qlzap = "SELECT * FROM " + base.get() +" WHERE login =?" , (login,))
        #print(sqlzap)
        sqlzapp = "SELECT login FROM " + base.get() +" WHERE " + eee
        #sqlzapp = "SELECT * FROM " + base.get() + ";"
        print(sqlzapp)
        cursor.execute(sqlzapp)
        rows = cursor.fetchall()
        #conn.commit()
        for rowg in rows:
            lboxxx.insert(END, rowg)
            print(rowg)


    except sqlite3.OperationalError:
        print('Такой таблицы нету в базе , возможно создать ')


root = Tk()


lbox = Listbox(selectmode=EXTENDED)
lbox.pack(side=LEFT)
scroll = Scrollbar(command=lbox.yview)
scroll.pack(side=LEFT, fill=Y)
lbox.config(yscrollcommand=scroll.set)

f = Frame()
f.pack(side=LEFT, padx=10)
entry = Entry(f)
entry.pack(anchor=N)
badd = Button(f, text="Список пользователей", command=addItem)
badd.pack(fill=X)
bdel = Button(f, text="Добавить пользователя", command=delList)
bdel.pack(fill=X)
bsave = Button(f, text="Удалить пользователя", command=saveList)
bsave.pack(fill=X)
bsave = Button(f, text="Войти", command=new_frame)
bsave.pack(fill=X)
listFrame = tkinter.Frame(root, width=350)
listFrame.pack(side="top", fill="both")
lboxxx = Listbox(listFrame, selectmode=EXTENDED)
lboxxx.pack(side=LEFT)
root.mainloop()