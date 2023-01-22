from tkinter import*
from tkinter import ttk
from pafy import new
from tkinter import filedialog
from pytube import YouTube
root = Tk()
root.title("Download vidoe(3.2)")
root.geometry("650x410+340+10")
root.resizable(False,False)
Folder_name = ""
def fil():
    global Folder_name
    Folder_name = filedialog.askdirectory()
    if (len(Folder_name) > 1) :
        lb1.config(text = Folder_name , fg = "green")
def down():
#try:
    choice = ytdchoices.get()
    url = ydtEntry.get()
    if(len(url) > 1):
        if(choice == choice[0]):
            url = ydtEntry.get()
            video = new(url)
            dl = video.getbest()
            dl.download(Folder_name)
            locationError.config(text="تم الأنتهاء من التحميل", fg="green")

        elif(choice == choice[1]):
            urlu = ydtEntry.get()
            audio = new(urlu)
            dl = audio.audiostreams
            dl[0].download()
            locationError.config(text="تم الأنتهاء من التحميل", fg="green")

        else:
            locationError.config(text="حاول ان تدخل الرابط مجددا", fg="red")
    #except:
        #if ydtEntry.get()== "":
            #locationError.config(text = "الرجاء ادخال الرابط ")
        #else:
            #locationError.config(text = "")

f1 = Frame(root,width=580,height=100,bg = "whitesmoke",bd=3,relief=GROOVE)
f1.place(x=30,y=130)
f2 = Frame(root,width=580,height=55,bg='whitesmoke',bd=3,relief=GROOVE)
f2.place(x=30 ,y=250)


t = Label(root,text = "برنامج تحميل الفيديوهات والأغاني ",bg = "red", fg = "white")
t.pack(fill = X)
ytdLabel = Label(root,text = "قم بادخال الرابط هنا ")
ytdLabel.pack()


ydtEntry = Entry(root,width=70,justify = "center",fg = "blue")
ytdEntryVar = StringVar()
ydtEntry.pack()

ytdError = Label(root,text = "ملاحضات التحميل",fg = "red")
ytdError.pack()


saveLabel = Label(root,text = "أختر مكان الحفظ")
saveLabel.place(x=390 ,y=140)

saveEntry = Button(f1,width=20,font = ("Tajawal",15),bg = "red",fg = "white",text ="مسار الحفظ",command = fil)
saveEntry.place(x=340 , y=30)


locationError = Label(root,text = " لا يوجد ",bg = "whitesmoke",fg = "red")
locationError.pack()

lb1 = Label(f1,text = "",bg = "whitesmoke",font = ("Tajawal",10,"bold"))
lb1.place(x =10 , y= 40)

ytdQuality = Label(root,text = "أختر جودة الفيديو")
ytdQuality.place(x=430 ,y=255)



choices = ["فيديو","صوت فقط"]
ytdchoices = ttk.Combobox(root,value = choices,state = 'readonly')
ytdchoices.current(0)
ytdchoices.place(x=260,y=265)


downloabtn = Button(root,text ="بدء التحميل",width = 20,command = down)
downloabtn.place(x=40,y=255)


root.mainloop()