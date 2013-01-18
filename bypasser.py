#Date:11/8/2011
#Made by:Strangegeorge
#Contact:strangegeorge2@gmail.com
#Donate in Paypal:strangegeorge2@gmail.com

#! /usr/bin/python

from Tkinter import *
import tkMessageBox
import urllib2
    
def  aboutMe():
    tkMessageBox.showinfo(title="Ads Bypasser", message="AdfBypasser:\nCreated by Strangegeorge.\nThe author of this software cant be held responsible for any damage or illegal usage you may experience.")
    return

def  Contact():
     tkMessageBox.showinfo(title="Ads Bypasser", message="Contact: Strangegeorge\nEmail: strangegeorge2@gmail.com")
     return
     
def  GetResults():
    websitevalue1 = Websitein1.get()
    websitevalue2 = Websitein2.get()
    websitevalue3 = Websitein3.get()
    websitethen1 = websitevalue1[7:]
    websitethen2 = websitevalue2[7:]
    websitethen3 = websitevalue3[7:]
    website1 = "http://www." + websitethen1
    website2 = "http://www." + websitethen2
    website3 = "http://www." + websitethen3
    allvalues = [website1, website2, website3]
    for value in allvalues:
        connection = urllib2.urlopen(value)
        html_code = connection.read()
        start_point = html_code.find('var url = ')
        end_point = html_code.find('skip_ad1 = true;')
        scores = html_code[start_point : end_point]
        delete = scores[11:]
        delete_end = delete.find("'")
        delete_after = delete[:delete_end]
        Output.insert(END, delete_after)
        return
        
def  Saveresults():
    saves = Output.get(1.0, END)
    savesfile = open("results.txt", "w")
    savesfile.write(saves)
    savesfile.close
    tkMessageBox.showinfo(title="Ads Bypasser", message="Save Completed!")
    return
    
    
app = Tk()
app.title("Ads Bypasser by Strangegeorge")
app.geometry("400x300+200+200")


menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_cascade(label="Quit", command=app.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_cascade(label="About Me", command=aboutMe)
helpmenu.add_cascade(label="Contact", command=Contact)
menubar.add_cascade(label="Help", menu=helpmenu)

app.config(menu=menubar)

labelText1 = StringVar()
labelText1.set("Shortened URLs:")
label1 = Label(app, textvariable=labelText1, height=1).pack(anchor=W)

Websitein1 = StringVar(None)
Websiteinput1 = Entry(app, textvariable=Websitein1)
Websiteinput1.pack(anchor=W)

Websitein2 = StringVar(None)
Websiteinput2 = Entry(app, textvariable=Websitein2)
Websiteinput2.pack(anchor=W)

Websitein3 = StringVar(None)
Websiteinput3 = Entry(app, textvariable=Websitein3)
Websiteinput3.pack(anchor=W)

getbutton = Button(app, text="Get Real URLs", width=20, command=GetResults)
getbutton.pack(padx=15, pady=15)

Output = Text(app, height=5)
Output.pack()

savebutton = Button(app, text="Save Results", width=20, command=Saveresults)
savebutton.pack()

app.mainloop()

