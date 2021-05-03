from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Combobox
from os import *
from sys import *
print(__name__)
class frame1:
    def __init__(self, root):
        self.root = root
        frame1 = LabelFrame(root, bg="light gray")
        frame1.place(x=0, y=0, height=80, width=753)
        fra1_la1 = Label(frame1, text="Printer:", bg="light gray")
        fra1_la1.place(x=10, y=10)
        ent = Entry(frame1)
        ent.place(x=54, y=10)
        fra1_la2 = Label(frame1, text="Copies:", bg="light gray")
        fra1_la2.place(x=10, y=45)
        number_Copy = Spinbox(frame1, from_=0, to=100, width=5)
        number_Copy.place(x=52, y=47)
        fra_btn = Button(frame1, text="Properties", bg="light gray", bd=1, activebackground="light gray", command=selet)
        fra_btn.place(x=200, y=10)
        fra_btn2 = Button(frame1, text="Advanced", bg="light gray", bd=1, activebackground="light gray", command=selet1)
        fra_btn2.place(x=280, y=10)
        fra_btn_ = Checkbutton(frame1, text="Print in grayscale(black and white)", bg="light gray",
                               activebackground="light gray")
        fra_btn_.place(x=270, y=47)
        fra_btn_1 = Checkbutton(frame1, text="Save ink/toner", bg="light gray", activebackground="light gray")
        fra_btn_1.place(x=490, y=47)
        help_btn = Button(frame1, text="Help", bd=0, bg="light gray", fg="blue", activebackground="light gray")
        help_btn.place(x=650, y=10)


def selet():
    root = Tk()
    root.title("Printer Name")
    root.geometry("550x430")
    root.resizable(0, 0)
    frame_lab = LabelFrame(root, text="Layout", bg="white")
    frame_lab.place(x=10, y=10, height=370, width=520)
    frame_lab_label = Label(frame_lab, text="Orientations :", bg="white")
    frame_lab_label.place(x=10, y=20)
    frame_lab_entry = Entry(frame_lab, bd=6)
    frame_lab_entry.place(x=10, y=60)
    frame_lab_btn = Button(frame_lab, text="Advanced", bg="light gray", activebackground="light gray",
                           command=Prsetting)
    frame_lab_btn.place(x=440, y=310)
    btn1 = Button(root, text="OK", width=12, bg="light gray", command=root.destroy)
    btn1.place(x=320, y=390)
    btn1 = Button(root, text="Cancel", width=12, bg="light gray", command=root.destroy)
    btn1.place(x=430, y=390)


def Prsetting():
    showinfo("Printer setting", "Adjustment the page setup ")

def selet1():
    root = Tk()
    root.title("Advanced print setup")
    root.geometry("380x450")
    fra_lab = LabelFrame(root, text="PostScript Options")
    fra_lab.place(x=20, y=20, height=150, width=350)
    fra_lab_lab1 = Label(fra_lab, text="Language")
    fra_lab_lab1.place(x=10, y=10)
    fra_lab_ent = Entry(fra_lab)
    fra_lab_ent.place(x=70, y=10)
    fra_lab_lab2 = Label(fra_lab, text="Font and Resource Policy")
    fra_lab_lab2.place(x=10, y=50)
    fra_lab_ent2 = Entry(fra_lab, show="Send By Rang")
    fra_lab_ent2.place(x=160, y=50)
    fra_lab_btn = Checkbutton(fra_lab, text="Download Asian Fonts")
    fra_lab_btn.place(x=20, y=80)
    fra_lab_btn = Checkbutton(fra_lab, text="Discolored Background correction")
    fra_lab_btn.place(x=20, y=100)
    fra_lab1 = LabelFrame(root, text="Colour Management")
    fra_lab1.place(x=20, y=180, height=120, width=250)
    cha1 = Checkbutton(fra_lab1, text="Let printer determine color")
    cha1.place(x=20, y=10)
    cha2 = Checkbutton(fra_lab1, text="Tread grays as K-only grays")
    cha2.place(x=20, y=30)
    cha3 = Checkbutton(fra_lab1, text="Preserve Black")
    cha3.place(x=20, y=50)
    cha4 = Checkbutton(fra_lab1, text="Preserve CMYK Primaries")
    cha4.place(x=20, y=70)
    cha5 = Checkbutton(root, text="Print As Image")
    cha5.place(x=20, y=310)
    cha6 = Checkbutton(root, text="Simulate Overprinting")
    cha6.place(x=20, y=330)
    cha7 = Checkbutton(root, text="Print to file")
    cha7.place(x=20, y=350)
    btn1 = Button(root, text="OK", width=12, bg="light gray", command=root.destroy)
    btn1.place(x=170, y=390)
    btn1 = Button(root, text="Cancel", width=12, bg="light gray", command=root.destroy)
    btn1.place(x=280, y=390)


class frame2:
    def __init__(self, root, var):
        frame2 = LabelFrame(root, bg="light gray")
        frame2.place(x=0, y=81, height=90, width=753)
        fra2_la_ = Label(frame2, text="Pages to print:", bg="light gray")
        fra2_la_.place(x=10, y=0)
        fra2_btn_ = Radiobutton(frame2, text="All", bg="light gray", variable=var, value=1)
        fra2_btn_.place(x=10, y=30)
        fra2_btn_1 = Radiobutton(frame2, text="Current ", bg="light gray", variable=var, value=2)
        fra2_btn_1.place(x=95, y=30)
        fra2_btn_2 = Radiobutton(frame2, text="Pages", bg="light gray", variable=var, value=3)
        fra2_btn_2.place(x=210, y=30)
        fra2_ent = Entry(frame2)
        fra2_ent.place(x=290, y=30)


class frame3:
    def __init__(self, root,var2):
        frame3 = LabelFrame(root, bg="light gray")
        frame3.place(x=0, y=172, height=150, width=753)
        fra3_la_ = Label(frame3, text="Page Sizing & Handing:", bg="light gray")
        fra3_la_.place(x=10, y=0)
        fra3_btn = Button(frame3, text="Size", bg="light gray", activebackground="light gray", bd=1, width=12)
        fra3_btn.place(x=10, y=25)
        fra3_btn1 = Button(frame3, text="Poster", activebackground="light gray", bg="light gray", bd=1, width=12)
        fra3_btn1.place(x=110, y=25)
        fra3_btn2 = Button(frame3, text="Multiple", activebackground="light gray", bg="light gray", bd=1, width=12)
        fra3_btn2.place(x=210, y=25)
        fra3_btn3 = Button(frame3, text="Booklet", activebackground="light gray", bg="light gray", bd=1, width=12)
        fra3_btn3.place(x=310, y=25)
class frame4:
    def __init__(self, root, var1):
        frame4 = LabelFrame(root, bg="light gray")
        frame4.place(x=0, y=323, height=60, width=753)
        fra4_la = Label(frame4, text="Orientation:", bg="light gray")
        fra4_la.place(x=10, y=0)
        fra4_btn_ = Radiobutton(frame4, text="Auto", bg="light gray", variable=var1, value=1)
        fra4_btn_.place(x=10, y=20)
        fra4_btn_1 = Radiobutton(frame4, text="Portrait", bg="light gray", variable=var1, value=2)
        fra4_btn_1.place(x=110, y=20)
        fra4_btn_2 = Radiobutton(frame4, text="Landscape", bg="light gray", variable=var1, value=3)
        fra4_btn_2.place(x=210, y=20)


class frame5:
    def __init__(self, root):
        frame5 = LabelFrame(root, bg="light gray")
        frame5.place(x=0, y=384, height=90, width=753)
        fra5_la = Label(frame5, text="Comments & Forms:", bg="light gray")
        fra5_la.place(x=10, y=0)
        fra5_ent = Entry(frame5, width=30)
        fra5_ent.place(x=10, y=25)
        fra5_btn = Button(frame5, text="summarize comments", bg="light gray", bd=1, activebackground="light gray")
        fra5_btn.place(x=220, y=25)


class end:
    def __init__(self, root):
        btn = Button(root, text="Page Setup")
        btn.place(x=10, y=480)
        btn1 = Button(root, text="Print", command=root.quit)
        btn1.place(x=610, y=480, width=50)
        btn2 = Button(root, text="Cancel", command=root.destroy)
        btn2.place(x=680, y=480, width=50)


root = Tk()
var = IntVar()
var1 = IntVar()
var2 = IntVar()
obj1 = frame1(root)
obj2 = frame2(root, var)
obj3 = frame3(root,var2)
obj4 = frame4(root, var1)
obj5 = frame5(root)
obj6 = end(root)
root.title("Print")
root.geometry("753x520+100+50")
root.resizable(0, 0)
root["bg"] = "gray"
root.mainloop()
