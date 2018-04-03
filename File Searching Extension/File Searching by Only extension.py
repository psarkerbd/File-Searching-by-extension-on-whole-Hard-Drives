"""
@Author: Pranta Sarker
Institute: North East University Bangladesh
Language: Python
Version: 3.x
Platfrom: Pycharm Community Version
"""

# -------------- Packages importing -----------
from tkinter import *;
from PIL import ImageTk, Image;
from tkinter import messagebox;
import os;
#--------x x x x x -------------------------

def searchPerform2(master, extension):
    directory = ["C:\\", "D:\\", "E:\\", "F:\\", "G:\\", "H:\\", "I:\\"];
    reply = "";
    f = False;


    filelist = [];

    listbox = Listbox(master);

    listbox.delete(0, END);

    scrollbar = Scrollbar(master);

    for rootpath in directory:
        for root, dirnames, filenames in os.walk(rootpath):
            for name in filenames:
                if name.endswith(extension):
                    f = True;
                    total = str(root) + str(dirnames) + name;
                    filelist.append(total);
                        #break;
                #if(f==True):
                    #break;
            #if(f==True):
                #break;
        #if(f==True):
            #break;

    listbox.delete(0, END);

    if (f == False):
        no(master);
    else:
        cnt = 0;
        listbox.delete(0, END);
        listbox.config(fg='green', yscrollcommand=scrollbar.set, justify='left')
        scrollbar.config(command=listbox.yview);
        for filename in filelist:
            cnt += 1;
            reply = str(cnt) + '. ' + filename
            listbox.insert(END, reply);
            listbox.pack(side=LEFT, fill=BOTH, expand=1);
            scrollbar.pack(side=RIGHT, fill=Y);

def allDiskButtonAction():
    master = Tk();
    master.title("File Searching on all drives");
    master.geometry("300x300+200+250");

    ufLabel = Label(master, text="Enter extension");
    ufLabel.place(relx=0.5, rely=0.1, anchor="center")

    ufEntry = Entry(master);
    ufEntry.place(relx=0.5, rely=0.2, anchor="center");

    ufEntry.insert(0, "give extension");
    ufEntry.bind("<Button-1>", lambda event: clear(ufEntry, master));

    submitButton = Button(master, text="Submit", bg="black", fg="white", command=lambda: searchPerform2(master, ufEntry.get()));
    submitButton.place(relx=0.5, rely=0.3, anchor="center");

    master.resizable(True, True);
    master.mainloop();

def no(listbox):
    reply = 'Did not find';
    listbox.config(justify = 'center', fg = 'red')
    listbox.insert(END, reply);
    listbox.pack(side=LEFT, fill=BOTH, expand=1);

def searchPerform1(master, extension, var):
    #directory = ["C:\\", "D:\\", "E:\\", "F:\\", "G:\\", "H:\\", "I:\\"];
    if(var == 1):
        rootpath = "C:\\";
    elif(var == 2):
        rootpath = "D:\\";
    elif(var == 3):
        rootpath = "E:\\";
    elif(var == 4):
        rootpath = "F:\\";
    elif(var == 5):
        rootpath = "G:\\";
    elif(var == 6):
        rootpath = "H:\\";
    elif(var == 7):
        rootpath = "I:\\";

    reply = "";

    listbox = Listbox(master);

    listbox.delete(0, END);

    scrollbar = Scrollbar(master);

    f = False;
    #print("%s %s" % (ufilename, rootpath));

    #print("%s %s" % (filename, extantion));

    filelist = [];

    for root, dirnames, filenames in os.walk(rootpath):
        for name in filenames:
            if name.endswith(extension):
                #print("Found !!!");
                f=True;
                all = str(root) + str(dirnames) + str(name);
                filelist.append(all);

    listbox.delete(0, END);

    if (f == False):
        no(listbox);
    else:
        cnt = 0;
        listbox.delete(0, END);
        listbox.config(fg='green', yscrollcommand=scrollbar.set, justify='left')
        scrollbar.config(command=listbox.yview);

        for filename in filelist:
            cnt += 1;
            reply = str(cnt) + '. ' + filename;
            listbox.insert(END, reply);
            listbox.pack(side=LEFT, fill=BOTH, expand=TRUE);
            scrollbar.pack(side=RIGHT, fill=Y);


def clear(event, master):
    event.delete(0, END);

def action(var):
    #directory = ["C:\\", "D:\\", "E:\\", "F:\\", "G:\\", "H:\\", "I:\\"];
    master = Tk();
    master.title("File Name");
    master.geometry("450x300+200+250");

    ufLabel = Label(master, text="Enter extension");
    ufLabel.place(relx=0.5, rely=0.1, anchor = "center")

    ufEntry = Entry(master);
    ufEntry.insert(0, "give extension");
    ufEntry.bind("<Button-1>", lambda event: clear(ufEntry, master));
    ufEntry.place(relx=0.5, rely=0.2, anchor = "center");

    submitButton = Button(master, text="Submit", bg="black", fg="white", command = lambda : searchPerform1(master, ufEntry.get(), var));
    submitButton.place(relx = 0.5, rely= 0.3, anchor = "center");

    master.resizable(True, True);
    master.mainloop();

#------------ exit button working ---------------

def exitButtonAction(root):
    if messagebox.askokcancel("Exit", "Do you want to Exit?"):
        root.quit();
        root.destroy();
#------------------x x x x x --------------------

# ------------------- show main window ----------
def show_main_window(master):
    master.withdraw();
    master.destroy();
    temp = Toplevel(mainWindow);
    temp.destroy();
    mainWindow.iconify();
    mainWindow.deiconify();
# -------x x x x x x x x -----------------------

# ----- hide the main window after go to another window--------
def hide_main_window(master):
    print("on the hide main window function");
    master.withdraw();
    master.quit();
# ----------------- x x  x x x x -----------------------

# ------ Back button of Specific search file Window ------
def backButton(sDisk):
    print("on the back button function");
    theButton = Button(sDisk, text="Back", width = 5, bg="black", fg="white", command = lambda : show_main_window(sDisk));
    theButton.place(relx=0.0, rely=0.0);
# --------------x x x x x---------------------------------

#----------- second button on the first window which is specific drive file searching ----------------
def specificDiskAction(master):
    hide_main_window(master);
    sDisk = Tk();
    sDisk.config(bg="black")
    sDisk.geometry("300x300+200+250")
    sDisk.title("File Search on a Specific Drive");
    backButton(sDisk);
    #exitButton = Button(sDisk, text="X", bg="red", fg="black", width=5, command= lambda: exitButtonAction(sDisk));
    #exitButton.place(relx=0.85, rely=0.0);

    #------- Radio button working -------------

    var = IntVar();
    #var.set(1);

    Cdrive = Radiobutton(sDisk, text="C", variable=var, bg="white", fg="black", value=1, tristatevalue=0, command=lambda: action(1));
    Cdrive.place(relx=0.5, rely=0.1, anchor="center");

    Ddrive = Radiobutton(sDisk, text="D", variable=var, bg="white", fg="black", value=2, tristatevalue=0, command=lambda: action(2));
    Ddrive.place(relx=0.5, rely=0.2, anchor="center");

    Edrive = Radiobutton(sDisk, text="E", variable=var, bg="white", fg="black", value=3, tristatevalue=0, command=lambda: action(3));
    Edrive.place(relx=0.5, rely=0.3, anchor="center");

    Fdrive = Radiobutton(sDisk, text="F", variable=var, bg="white", fg="black", value=4, tristatevalue=0, command=lambda: action(4));
    Fdrive.place(relx=0.5, rely=0.4, anchor="center");

    Gdrive = Radiobutton(sDisk, text="G", variable=var, bg="white", fg="black", value=5, tristatevalue=0, command=lambda: action(5));
    Gdrive.place(relx=0.5, rely=0.5, anchor="center");

    Hdrive = Radiobutton(sDisk, text="H", variable=var, bg="white", fg="black", value=6, tristatevalue=0, command=lambda: action(6));
    Hdrive.place(relx=0.5, rely=0.6, anchor="center");

    Idrive = Radiobutton(sDisk, text=" I ", variable=var, bg="white", fg="black", value=7, tristatevalue=0, command=lambda: action(7));
    Idrive.place(relx=0.5, rely=0.7, anchor="center");

    #----------x x x x x x x x x x ------------

    sDisk.resizable(False, False);
    sDisk.mainloop();
#-------------------x x x x x x x x x x ------------------------------------------------

mainWindow = Tk();
mainWindow.config(bg="gray");
mainWindow.title("File Searching");
mainWindow.geometry("300x300+200+250");

# ------- image insertion code -----------
img = Image.open("files.jpg");
photo = ImageTk.PhotoImage(img);
imageLabel = Label(mainWindow, image=photo);
imageLabel.place(relx=0.5, rely=0.5, anchor="center");
# ------------ image insertion code ------

fileSearchingAllDiskButton = Button(mainWindow, text="Search a file on all Disks", width=25, font="arial 10 bold", bg="black", fg="white", command = allDiskButtonAction);
fileSearchingAllDiskButton.place(relx=0.5, rely=0.4, anchor="center");
fileSearchingSpecificDiskButton = Button(mainWindow, text="Search a file on a specific Disk", font="arial 10 bold", bg="black", fg="white", command = lambda : specificDiskAction(mainWindow))
fileSearchingSpecificDiskButton.place(relx=0.5, rely=0.55, anchor="center");
exitButton = Button(mainWindow, text="X", bg="red", fg="black", width = 5, command=lambda : exitButtonAction(mainWindow));
exitButton.place(relx=0.85, rely=0.0);
mainWindow.resizable(False, False);
mainWindow.mainloop();