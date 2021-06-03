import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog,Text ,Toplevel
import time
import os
from shutil import copyfile
import prog

PATHNAME=""
ws = tk.Tk()
ws.title('Document Comparator')
ws.padx=10
pdfs=[]

def addFile():
    
    filename=filedialog.askopenfilename(initialdir="/home/tharikh",title="Select File",filetypes=(("text files","*.txt"),("all files","*.*")))
    pdfs.append(filename)
    print(filename)
    for widget in frame.winfo_children():
        widget.destroy()
    heading=tk.Label(frame,text="Documents",fg="black",bg="white",font=("Ubuntu", 20))
    heading.pack();
    i=1
    for pdf in pdfs:
        path=pdf.split("/")
        name=path[len(path) - 1]
        label=tk.Label(frame,text=str(i)+') '+name,padx=5,pady=5)
        label.pack()
        copyfile(pdf,os.getcwd()+ '/' + name)
        i=i+1


def process():
    inp=querytext.get(1.0,"end-1c")
    ranks=prog.nlpPart(inp)
    topwindow(ranks)



def topwindow(ranks):
    newWindow = Toplevel(ws)
    newcanvas=tk.Canvas(newWindow,height=700,width=1000,bg="#263D42")
    newcanvas.pack()
    newWindow.title("New Window")
    newframe=tk.Frame(newWindow,bg="white")
    newframe.place(relwidth=0.8,relheight=0.7,relx=0.1,rely=0.1)
    heading=tk.Label(newframe,text="Ranked Documents",fg="black",bg="white",font=("Ubuntu", 20))
    heading.pack();
    i=1
    for rank in ranks:
        label=tk.Label(newframe,text=str(i)+') '+rank,padx=5,pady=5)
        label.pack()
        i=i+1


canvas=tk.Canvas(ws,height=700,width=1000,bg="#263D42")
canvas.pack()


frame=tk.Frame(ws,bg="white")
frame.place(relwidth=0.8,relheight=0.7,relx=0.1,rely=0.1)

titlef=tk.Frame(ws,bg="#263D42")
titlef.place(relwidth=1,relheight=0.1,relx=0,rely=0)

title=tk.Label(titlef,text="DOCUMENT COMPARATOR", anchor="center",background="white",fg="black",font=("Ubuntu", 25))
title.pack()
title.place(rely=0.5,relx=0.35)

queryframe=tk.Frame(ws,bg="white")
queryframe.place(relwidth=0.8,relheight=0.1,relx=0.1,rely=0.8)
querylabel=tk.Label(queryframe,text="Enter Query", anchor="center",background="white",fg="black",font=("Ubuntu", 20))
querylabel.pack()
querytext=Text(queryframe,fg="black",width=100,font=("Ubuntu", 15))
querytext.pack();

upfile=tk.Button(ws,text="Upload File",padx=10,pady=5,fg="white",bg="#263D42",command=addFile)
upfile.pack()

runfile=tk.Button(ws,text="Run comparator",padx=10,pady=5,fg="white",bg="#263D42",command=process)
runfile.pack()

ws.mainloop()