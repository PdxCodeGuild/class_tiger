import tkinter as tk
import requests
from PIL import Image, ImageDraw
from tkinter import font
import pyodbc



mw =  tk.Tk()
mw.title('SE Works: Youth Database')
mw.minsize(200, 200)
mw.maxsize(800, 300)
mw.geometry("2400x1567")
background_image = tk.PhotoImage(file="f949c8139770a539f056a8383ba04825.png")
background_label = tk.Label(mw, image=background_image).place(relwidth=1, relheight=1)

def report_table():
    report = tk.Toplevel(h)
    report.title("SE WORKS: Youth table report")

def intake_form():
    intake_entry = tk.Toplevel(a)
    intake_entry.title("SE WORKS: Intake form")

def view_edit():
    edit = tk.Toplevel(b)
    edit.title("SE WORKS: Edit or add Activities")

def youth_by_name(enter_name):
    print(f"This is a request to see basic data and latest activity",enter_name)

def format_response(result):
    try:  # in case wrong entry
        Name = result[0][0]
        Lastname = result[0][1]
        Status= result[0][4]
        last_activity = result[0][5]
        lines = result[0][3]
        last_comment = "\n".join(lines.strip().split("."))
        final_string = 'Name: {},{}\nStatus: {}\nlast_activity: {}\nlast_comment: {}'.format(Name, Lastname, Status,last_activity,last_comment)
    except:
        final_string = 'There was a problem retrieving that information'
    return final_string


def read():
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=.\SQLEXPRESS;"
        "Database=YDC_YCC;"
        "Trusted_Connection=yes;")
    cursor = conn.cursor()
    params2 = entry.get()
    cursor.execute("Execute [dbo].[Student] %s" % params2)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    label['text'] = format_response(result)


entry = tk.Entry(master=mw, font=('Courier', 14, 'bold'))
entry.place(relx=.125, rely=.05, relwidth=.50, relheight=.15)

button_view = tk.Button(master=mw, bg="#F2C0FF", text='Enter youth name', font=('Courier', 12, 'bold'),command=read)
button_view.place(relx=.63, rely=.05, relwidth=0.25, relheight=0.15)

label = tk.Label(master=mw, text='Active Youth Data wil display',bg= "white", justify="left", bd=4)
label.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.70,anchor='n')


def about():
    about_file = tk.Toplevel(mw)
    about_file.title("SE WORKS: Data Entry manual")

def say_ok():
    print('ok!')

main_menu= tk.Menu(mw)
premier = tk.Menu(main_menu,tearoff=0)

Intakemenu = tk.Menu(main_menu,tearoff=0)
a = Intakemenu.add_command(label="Start intake", command=intake_form)


editmenu = tk.Menu(main_menu,tearoff=0)
b=editmenu.add_command(label="Add activity", command=view_edit)
c=editmenu.add_separator()
d=editmenu.add_command(label="Add Education outcome", command=say_ok)
e=editmenu.add_command(label="Add Employment outcome", command=say_ok)
f=editmenu.add_command(label="Add Assessment", command=say_ok)
g=editmenu.add_command(label="Program Exit", command=say_ok)

reportsmenu = tk.Menu(main_menu,tearoff=0)
h=reportsmenu.add_command(label="PY counts", command=report_table)
i=reportsmenu.add_separator()
j=reportsmenu.add_command(label="Program outcomes", command=say_ok)
k=reportsmenu.add_command(label="Print list of active Youth", command=say_ok)


helpmenu = tk.Menu(main_menu, tearoff=0)
l=helpmenu.add_command(label="Data entry manual", command=say_ok)
m=helpmenu.add_command(label="About...", command=about)


main_menu.add_cascade(label="Intake",menu=Intakemenu )
main_menu.add_cascade(label="Edit record", menu=editmenu)
main_menu.add_cascade(label="Reports", menu=reportsmenu)
main_menu.add_cascade(label="Help", menu=helpmenu)
mw.config(menu=main_menu)


mw.mainloop()

# print(tk.font.families())


