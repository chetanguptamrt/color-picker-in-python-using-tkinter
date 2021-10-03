from tkinter import *
from tkinter.messagebox import showinfo,showerror,askyesno
from tkinter.ttk import Notebook
from pyperclip import copy
from tkinter.colorchooser import askcolor
import pickle
import os 
#pickle object & class
class color_dat:
    def __init__(self,color):
        self.color=color
class frame_dat:
    def __init__(self,color_option_frame,color_option):
        self.color_option_frame=color_option_frame
        self.color_option=color_option
#default & backup
def default_setting():
    reset=askyesno("Default setting")
    print(reset)
    if reset==True:
        file=os.listdir("color bin")
        for i in file:
            if os.path.exists(f"color bin\\{i}"):
                os.remove(f"color bin\\{i}")
        if os.path.exists("Frame\\notebook_frame.dat"):
            os.remove("Frame\\notebook_frame.dat")
        color1=["#E44236","#B83227","#D63031","#E84342","#FF3031","#BA2F16","#EC4849","#FF3E4D","#E71C23","#EA425C","#E8290B",
        "#AE1438","#E83350","#FF4848","#FF362E",'#3498DB','#2475B0','#74B9FF','#4834DF','#0A79DF','#30336B','#487EB0','#192A56',
        '#6A89CC','#0A3D62','#4BCFFA','#0ABDE3','#25CCF7','#67E6DC','#3C40C6','#2ECC72','#26AE60','#6AB04C','#6AB04A','#BADC57',
        '#43BE31','#45CE30','#10A881','#1BCA9B','#7CEC9F','#019031','#A3CB37','#75DA8B','#53E0BC','#218F76','#EEC213','#F5C469',
        '#F4C724','#F0DF87','#DFAF2B','#FAC42F','#F3B63A','#FBD28B','#F3B431','#FAD02E','#E5B143','#F3CC79','#F9DDA4','#FFF222',
        '#E1DA00','#7B8788','#99AAAB','#2C3335','#616C6F','#DAE0E2','#535C68','#333945','#2F363F','#586776','#8395A7','#A4B0BD',
        '#777E8B','#758AA2','#47535E','#4C4B4B','#EAF0F1','#E74292','#01CBC6','#BB2CD9','#8B78E6','#00CCCD','#1287A5','#EA7773',
        '#2B2B52','#F5BCBA','#FFFFFF']
        #pickling
        with open(f'color bin\\all_color.dat',mode="wb") as f:
            stu1=color_dat(color1)
            pickle.dump(stu1,f)
        #unpickling
        with open(f'color bin\\all_color.dat',mode="rb") as f:
            obj1=pickle.load(f)
            print(obj1.color)
        #color maker, choose all color
        color_maker=[[["#E44236","#B83227","#D63031","#E84342","#FF3031","#BA2F16","#EC4849"],["#FF3E4D","#E71C23","#EA425C","#E8290B","#AE1438","#E83350","#FF4848"],
                    ["#FF362E"]],[['#3498DB','#2475B0','#74B9FF','#4834DF','#0A79DF','#30336B','#487EB0'],['#192A56','#6A89CC','#0A3D62','#4BCFFA','#0ABDE3','#25CCF7','#67E6DC'],
                    ['#3C40C6']],[['#2ECC72','#26AE60','#6AB04C','#6AB04A','#BADC57','#43BE31','#45CE30'],['#10A881','#1BCA9B','#7CEC9F','#019031','#A3CB37','#75DA8B','#53E0BC'],
                    ['#218F76']],[['#EEC213','#F5C469','#F4C724','#F0DF87','#DFAF2B','#FAC42F','#F3B63A'],['#FBD28B','#F3B431','#FAD02E','#E5B143','#F3CC79','#F9DDA4','#FFF222'],
                    ['#E1DA00']],[['#7B8788','#99AAAB','#2C3335','#616C6F','#DAE0E2','#535C68','#333945'],['#2F363F','#586776','#8395A7','#A4B0BD','#777E8B','#758AA2','#47535E'],
                    ['#4C4B4B']],[['#EAF0F1','#E74292','#01CBC6','#BB2CD9','#8B78E6','#00CCCD','#1287A5'],['#EA7773','#2B2B52','#F5BCBA','#FFFFFF']]]
        #pickling
        for i in range(len(color_maker)):
            with open(f'color bin\\color_{i+1}.dat',mode="wb") as f:
                stu1=color_dat(color_maker[i])
                pickle.dump(stu1,f)
        #unpickling
        for i in range(len(color_maker)):
            with open(f'color bin\\color_{i+1}.dat',mode="rb") as f:
                obj=pickle.load(f)
                print(obj.color)
        color_option_frame=["Rocking Red","Beautiful Blue","Golf Green","Fresh Yellow","old Grey","Might Be Great  "]
        color_option=[["Rocking Red","Beautiful Blue","Golf Green","Fresh Yellow","old Grey"],["Might Be Great  "]]
        #pickling
        with open("frame\\notebook_frame.dat",mode="wb") as f:
            frame=frame_dat(color_option_frame,color_option)
            pickle.dump(frame,f)
        #unpickling 
        with open("frame\\notebook_frame.dat",mode="rb") as f:
            obj=pickle.load(f)
            print(obj.color_option_frame,obj.color_option)
        des()
        main()
def restore_backup():
    pass
def upload_backup():
    pass
#add frame
def add_frame():
    global new_frame,notebook_2
    if len(notebook_2)<10:
        if len(new_frame.get())<=16 and len(new_frame.get())>=4:
            with open("frame\\notebook_frame.dat",mode="rb") as f:
                obj=pickle.load(f)
                temp_all_frame=obj.color_option_frame
                temp_all=obj.color_option
            name=new_frame.get()
            temp_all_frame.append(name)
            temp_all[1].append(name)
            #pickle all color, update and unpickle
            with open(f'color bin\\all_color.dat',mode="rb") as f:
                obj=pickle.load(f)
                temp_all_color=obj.color
            temp_all_color.append([])
            with open(f'color bin\\all_color.dat',mode="wb") as f:
                stu1=color_dat(temp_all_color)
                pickle.dump(stu1,f)
            
            with open(f"color bin\\color_{len(temp_all_frame)}.dat",mode='wb') as f:
                stu1=color_dat([[]])
                pickle.dump(stu1,f)
            with open("frame\\notebook_frame.dat",mode="wb") as f:          
                frame=frame_dat(temp_all_frame,temp_all)
                pickle.dump(frame,f)
            des()
            main()
        else:
            showerror("Frame name","Length of frame name can be 4 to 16 character.")
    else:
        showerror("Max frame error","Error, You can not add more than 10 frame.")

def ask_color():
    global choosecolor,writecolor
    clr=askcolor(title="Select color")
    clr1=""
    for i in clr[1]:
        if i.islower():
            clr1+=i.upper()
        else:
            clr1+=i
    choosecolor.set(clr1)
    writecolor.set("")
def write_color():
    global choosecolor,writecolor,notebook_8_frame3_write
    try:
        clr1=""
        for i in writecolor.get():
            if i.islower():
                clr1+=i.upper()
            else:
                clr1+=i
        writecolor.set(clr1)
        notebook_8_frame3_write.config(bg=writecolor.get())
    except:
        showerror("Error","please write valid color")
    choosecolor.set("")
def add_color():
    global choosecolor,writecolor,notebook_8_frame3_write,autocolor,temp_all_color
    if autocolor.get()==0:
        pass
    elif choosecolor.get()!="" or writecolor.get()!="":
        if choosecolor.get()!="":
            clr=choosecolor.get()
        elif writecolor.get()!="":
            clr=writecolor.get()
        #check color already exist or not
        if clr in temp_all_color:
            temp_all=0
            showinfo("Already exist","color is already exist\nplease try another color")
        else:
            temp_all=1
            print("clr is add in all_color")
        choosecolor.set("")    
        writecolor.set("")
        temp=[]
        if temp_all==1:
            temp_all=0
            #update and pickle new all_color.dat file
            temp_all_color.append(clr)
            with open(f'color bin\\all_color.dat',mode='wb') as f:
                temp_all_color2=color_dat(temp_all_color)
                pickle.dump(temp_all_color2,f)

            #unpickle and add new object then pickle updated file
            with open(f'color bin\\color_{autocolor.get()}.dat',mode="rb") as f:
                obj=pickle.load(f)
                temp=obj.color

            #now update color list
            a=len(temp)
            if a!=0:
                b=len(temp[a-1])
            else:
                b=len(temp[a])
            print(a,b)
            if a*b==28:
                showerror("Warning","Warning!\nYou can not add color in this,\nplease choose another one.")
            else:
                if b<7:
                    temp[a-1].append(clr)
                elif b==7:
                    a+=2
                    temp.append([clr])
                with open(f'color bin\\color_{autocolor.get()}.dat',mode="wb") as f:
                    temp_file=color_dat(temp)
                    pickle.dump(temp_file,f)
                des()
                main()
    else:
        showerror("Error","Please choose color or frame")
def choose_color(event):
    copy(event.widget.cget("text"))
#help and contact
def viewhelp():
    showinfo("Help","press any button to choose color\ncolor will be automatically copied when you press button")
def viewabout():
    showinfo("About","This application made by Chetan Gupta\nVersion - 1.0.1")
def viewcontact():
    showinfo("Contact us","Contact me on -\nFacebook - chetanguptamrt\nInstagram - chetanguptamrt\nTwitter - chetanguptamrt")
#quit
def des():
    global root
    root.destroy()

def main():
    global root,autocolor,choosecolor,writecolor,notebook_8_frame3_write,autocolor,temp_all_color,new_frame,notebook_2
    try:
        #unpickle all_color for check color already exist or not
        with open(f'color bin\\all_color.dat',mode="rb") as f:
            obj=pickle.load(f)
            temp_all_color=obj.color
        root=Tk()
        root.geometry("1300x660+20+10")
        root.minsize(1300,660)
        root.resizable(0,0)
        root.title("Color picker Made by chetan")
        root.iconbitmap("icon\\color.ico")
        #------------------------------------Menu-----------------------------------------
        mainmenubar=Menu(root)
        m1=Menu(mainmenubar,tearoff=0)
        m1.add_command(label="Exit",command=des)
        mainmenubar.add_cascade(label="File",menu=m1)
        m2=Menu(mainmenubar,tearoff=0)
        m2.add_command(label="Help",command=viewhelp)
        m2.add_command(label="About",command=viewabout)
        m2.add_command(label="Contact us",command=viewcontact)
        mainmenubar.add_cascade(label="Help",menu=m2)
        root.config(menu=mainmenubar)
        #------------------------------------Frame-------------------------------------------
        frame=Frame(root,bd=6,relief='ridge',width=1290,height=650)
        frame.pack(padx=5,pady=5)
        #-----------------------------------notebook--------------------------------------------
        notebook=Notebook(frame,width=1284,height=644,)
        notebook.pack(pady=3,padx=3)
        notebook_1=Frame(notebook)
        notebook_2=[]
        with open("frame\\notebook_frame.dat",mode="rb") as f:
            obj=pickle.load(f)
            for i in range(len(obj.color_option_frame)):
                notebook_2.append(Frame(notebook))
        notebook_8=Frame(notebook)
        notebook.add(notebook_1,text="Welcome Note",padding=5)
        with open("frame\\notebook_frame.dat",mode="rb") as f:
            obj=pickle.load(f)
            for i in range(len(obj.color_option_frame)):
                notebook.add(notebook_2[i],text=obj.color_option_frame[i],padding=5)
        notebook.add(notebook_8,text="Add Color & Frame",padding=5)
        #-----------------------------------welcome-----------------------------------------
        notebook_1_sbr=Scrollbar(notebook_1)
        notebook_1_sbr.pack(fill="y",side=RIGHT)
        notebook_1_text=Text(notebook_1,font="Arial 16",wrap=WORD,bd=3,selectbackground='#0A79DF')
        notebook_1_text.pack(fill="both")
        """""""""  Write welcome note of color picker  """""""""
        notebook_1_text.config(state="disabled")
        notebook_1_sbr.config(command=notebook_1_text.yview)
        notebook_1_text.config(yscrollcommand=notebook_1_sbr.set)
        #--------------------------------notebook 2----------------------------------------
        for k in range(len(notebook_2)):
            try:
                with open(f'color bin\\color_{k+1}.dat',mode="rb") as f:
                    obj=pickle.load(f)
                    print(obj.color)
                    for i in range(4):
                        for j in range(7):
                            try:
                                Button(notebook_2[k],text=obj.color[i][j],padx=36,pady=45,bg=obj.color[i][j],font=("times","13","bold")).grid(row=i,column=j,padx=12,pady=10)
                            except:
                                pass
            except:
                pass
        #---------------------------------add color---------------------------------------
        autocolor=IntVar()
        choosecolor=StringVar()
        writecolor=StringVar()
        choosecolor.set("")
        writecolor.set("")
        notebook_8_frame1=Frame(notebook_8,bd=7,relief="groove",width=550,height=560,bg="#ffffff")
        notebook_8_frame1.pack(side=LEFT,padx=10,pady=10)
        notebook_8_frame2=Frame(notebook_8,bd=7,relief="groove",width=700,height=560)
        notebook_8_frame2.pack(side=RIGHT,padx=(0,10),pady=10)

        #Label(notebook_8_frame1,text="Add color",font="Times 36 bold underline",bg="#ffffff",width=18,height=6).pack()

        notebook_8_frame3=LabelFrame(notebook_8_frame2,text="Write manualy",width=150,height=250)
        notebook_8_frame3.place(x=10,y=10)
        notebook_8_frame4=LabelFrame(notebook_8_frame2,text="Automatically",width=150,height=250)
        notebook_8_frame4.place(x=170,y=10)
        notebook_8_frame5=LabelFrame(notebook_8_frame2,text="Add color",width=320,height=250)
        notebook_8_frame5.place(x=330,y=10)
        notebook_8_frame6=LabelFrame(notebook_8_frame2,text="Add New Frame",width=640,height=120)
        notebook_8_frame6.place(x=10,y=270)
        notebook_8_frame7=LabelFrame(notebook_8_frame2,text="Default & Backup",width=640,height=125)
        notebook_8_frame7.place(x=10,y=400)
        notebook_8_frame3_write=Frame(notebook_8_frame3,bd=3,width=60,height=25,relief="raised")
        notebook_8_frame3_write.grid(row=0,column=0,pady=(45,10))
        Entry(notebook_8_frame3,textvariable=writecolor,width=8,relief="sunken",font="times 16").grid(row=1,column=0,pady=10,padx=27)
        Button(notebook_8_frame3,text="Ok",font="arial 13",bg="#0A79DF",padx=30,command=write_color).grid(row=2,column=0,pady=(10,60),padx=27)
        Label(notebook_8_frame4,textvariable=choosecolor,width=8,relief="sunken",font="times 16").grid(row=0,column=0,pady=(70,10),padx=18)
        Button(notebook_8_frame4,text="Choose color",font="arial 13",bg="#0A79DF",command=ask_color).grid(row=1,column=0,pady=(20,70),padx=18)
        for_temp_radio_button_in_frame8=1
        with open("frame\\notebook_frame.dat",mode="rb") as f:
            obj=pickle.load(f)
            temp_all=obj.color_option
        # temp_all_frame=obj.color_option_frame
            for i in range(len(temp_all)): 
                for j in range(len(temp_all[i])):
                    Radiobutton(notebook_8_frame5,text=temp_all[i][j],font="arial 13",value=for_temp_radio_button_in_frame8,variable=autocolor).grid(row=j,column=i,padx=10,sticky="w")
                    for_temp_radio_button_in_frame8+=1
        Button(notebook_8_frame5,text="Add Color",font="arial 10",bg="#0A79DF",padx=10,pady=5,command=add_color).grid(row=5,column=1,padx=10,pady=23)
        new_frame=StringVar()
        Label(notebook_8_frame6,text="Frame name - ",font="arial 14").grid(row=0,column=0,pady=30,padx=(60,10))
        Entry(notebook_8_frame6,textvariable=new_frame,font="arial 14",width=17).grid(row=0,column=1,pady=30,padx=(14,40))
        Button(notebook_8_frame6,text="Add frame",padx=10,pady=4,font="arial 14",bg="#0A79DF",command=add_frame).grid(row=0,column=2,pady=30,padx=(10,60))
        Button(notebook_8_frame7,text="Default Setting",font="arial 14",bg="#0A79DF",command=default_setting).grid(row=0,column=0,pady=30,padx=(60,20))
        Button(notebook_8_frame7,text="Upload Backup",font="arial 14",bg="#0A79DF",command=upload_backup).grid(row=0,column=1,pady=30,padx=19)
        Button(notebook_8_frame7,text="Restore Backup",font="arial 14",bg="#0A79DF",command=restore_backup).grid(row=0,column=2,pady=30,padx=(20,60))
        root.mainloop()
    except:
        showerror("Error","May be some file has corrupt or missing\nNow, Application will start at default setting.")
        default_setting()
if __name__ == "__main__":
    main()