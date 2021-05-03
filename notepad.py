from tkinter import *
from tkinter.messagebox import *
import tkinter.filedialog as filesdialog
from tkinter.ttk import Combobox
import os


def ers():
    global textpart
    textpart = Text(root)
    textpart.grid(sticky=N + E + S + W)

    Menubar = Menu(root)

    # file part
    root.config(menu=Menubar)
    filescetion = Menu(Menubar, tearoff=0)
    filescetion.add_command(label="New                                  Ctrl+N", command=new)
    filescetion.add_command(label="New Window        Ctrl+Shift+N")
    filescetion.add_command(label="Open...                              Ctrl+O",command=openfile)
    filescetion.add_command(label="Save                                   Ctrl+S",command=savefile)
    filescetion.add_command(label="Save As...                Ctrl+Shift+S", command=saveasfile)
    filescetion.add_separator()
    filescetion.add_command(label="Page Setup", command=page_setup)
    filescetion.add_command(label="Print                                  Ctrl+P", command=print)
    filescetion.add_separator()
    filescetion.add_command(label="Exit", command=root.quit)
    Menubar.add_cascade(label="File", menu=filescetion)

    # Edit part
    root.config(menu=Menubar)
    editsecetion = Menu(Menubar, tearoff=0)
    editsecetion.add_command(label="Undo")
    editsecetion.add_separator()
    editsecetion.add_command(label="Cut")
    editsecetion.add_command(label="Copy")
    editsecetion.add_command(label="Paste")
    editsecetion.add_command(label="Delete")
    editsecetion.add_separator()
    editsecetion.add_command(label="Search for Bing...")
    editsecetion.add_command(label="Find")
    editsecetion.add_command(label="Find Next")
    editsecetion.add_command(label="Find Previous")
    editsecetion.add_command(label="Replace")
    editsecetion.add_command(label="Go To")
    editsecetion.add_separator()
    editsecetion.add_command(label="Select All")
    editsecetion.add_command(label="Time/Date")
    Menubar.add_cascade(label="Edit", menu=editsecetion)

    # Format part
    root.config(menu=Menubar)
    formatsecetion = Menu(Menubar, tearoff=0)
    formatsecetion.add_command(label="Word Warp")
    formatsecetion.add_command(label="Font...")
    Menubar.add_cascade(label="Format", menu=formatsecetion)

    # View part

    root.config(menu=Menubar)
    viwesecetion = Menu(Menubar, tearoff=0)
    viwesecetion.add_command(label="Zoom")
    viwesecetion.add_command(label="Status Bar")
    Menubar.add_cascade(label="View", menu=viwesecetion)

    # Help part
    root.config(menu=Menubar)
    helpsecetion = Menu(Menubar, tearoff=0)
    helpsecetion.add_command(label="View Help")
    helpsecetion.add_command(label="Send Feedback")
    helpsecetion.add_separator()
    helpsecetion.add_command(label="About Notepad")
    Menubar.add_cascade(label="Help", menu=helpsecetion)
    root.config(menu=Menubar)


def print():
    from printer import prin


def new():
    global textpart
    root.title("Untitled - Notepad")
    file = None
    textpart.delete(1.0, END)


def openfile():
    global textpart
    root.title("Untitled - Notepad")
    file = filesdialog.askopenfile(defaultextension=".txt",
                                   filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
    file = file.name

    if file=="":
        file = None
    else:
        root.title((os.path.basename(file) + "-Notepad"))
        textpart.delete(1.0, END)
        file = open(file,"rb")
        textpart.insert(1.0,file.read())
        file.close()

def savefile():
    global textpart, file
    if file == None:
        file = filesdialog.asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
                                   filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
        if file == None:
            file=None
        else:
            file=open(file,"w")
            text=str(textpart.get(1.0, END))
            file.write(text)
            file.close()
            file = file.name
            root.title(os.path.basename(file) + " - Notepad")
    else:
        file = open(file, "w")
        text=str(textpart.get(1.0, END))
        file.write(text)
        file.close()


def saveasfile():
    global textpart, file1
    if file1 == None:
        file1 = filesdialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                             filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
        if file1 == None:
            file1 = None
        else:
            file1 = open(file1, "w")
            text = str(textpart.get(1.0, END))
            file1.write(text)
            file1.close()
            file1 = file1.name
            root.title(os.path.basename(file1) + " - Notepad")
def page_setup():
    root1 = Tk()
    root1.title("Page Setup")
    root1.geometry("535x320")
    root1.resizable(0, 0)
    root1.iconbitmap()
    var=IntVar()
    frame=LabelFrame(root1, text="Paper")
    frame.place(x=15, y=8, height=100, width=330)
    label1=Label(frame, text="Size:")
    label1.place(x=10, y=8)
    compo=Combobox(frame,value=["letter", "A4", "A3", "A2"])
    compo.place(x=80, y=8, width=240)
    compo.current(3)
    label2=Label(frame, text="Source:")
    label2.place(x=10, y=38)
    compo1 = Combobox(frame)
    compo1.place(x=80, y=38, width=240)
    frame1=LabelFrame(root1,text="Orientation")
    frame1.place(x=15, y=115, height=100, width=100)
    radio=Radiobutton(frame1, text="Portrait", variable=var, value=1)
    radio.place(x=10,y=8)
    radio1=Radiobutton(frame1, text="Landscape", variable=var, value=2)
    radio1.place(x=10, y=40)
    frame2=LabelFrame(root1, text="Margin(inches)")
    frame2.place(x=125, y=115, height=100, width=220)
    label3=Label(frame2, text="Left:")
    label3.place(x=10, y=8)
    entryb=Entry(frame2)
    entryb.place(x=60, y=8, width=40)
    label4=Label(frame2,text="Right:")
    label4.place(x=110, y=8, width=40)
    entryb1=Entry(frame2)
    entryb1.place(x=160,y=8,width=40)
    label5=Label(frame2,text="Top:")
    label5.place(x=10, y=38)
    entryb2 = Entry(frame2)
    entryb2.place(x=60, y=38, width=40)
    label6 = Label(frame2, text="Bottom:")
    label6.place(x=110, y=38, width=40)
    entryb3 = Entry(frame2)
    entryb3.place(x=160, y=38, width=40)
    label6=Label(root1,text="Header")
    label6.place(x=15,y=220)
    entryb4=Entry(root1)
    entryb4.place(x=80,y=220,width=210)
    label7=Label(root1,text="Footer")
    label7.place(x=15,y=260)
    entryb5=Entry(root1)
    entryb5.place(x=80,y=260, width=210)

# Main code part

root = Tk()
root.iconbitmap(r'notepad.ico')
root.title("Untitled - NotePad")
file = None
file1 = None
ers()
root.mainloop()