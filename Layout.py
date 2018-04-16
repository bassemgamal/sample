from tkinter import *
from tkinter import ttk
import time
from tkinter import messagebox
from tkinter import Checkbutton

#===================root Frame
root = Tk()
root.geometry("900x600")
root.title("Ballroom Calculator")



#=======================Tabs Func===================
rows = 0
while rows < 50:
    root.rowconfigure(rows, weight=1)
    root.columnconfigure(rows, weight=1)
    rows += 1

#=======================Functions========================
class obj:
    def __init__(self):
        self.count = IntVar()
        self.buffetvar = StringVar()
        self.buffet = IntVar()
        self.type = IntVar()
        self.chairsvar = StringVar()
        self.chairs = IntVar()
        self.add_drinks = IntVar()
        self.drinksvar = StringVar()
        self.drinks = IntVar()
        self.showfirevar = StringVar()
        self.showfire = IntVar()
        self.enteranceScreen = IntVar()
        self.catwalk = IntVar()
        self.lounge = IntVar()
        self.largeroundtabled = IntVar()
        self.largeCenterpeice = IntVar()
        self.enteranceguestbook = IntVar()
        self.guestbookB = IntVar()
        self.decorCorridor = IntVar()
        self.hightables = IntVar()

    def update_All(self, value):
        count = self.count
        count.set(value)
        print("you count to calculate is :  " + str(count.get()))
        print("Buffet number is : " + str(self.buffet.get()))
        print("Type number is : " + str(self.type.get()))
        print("your chairs option is " + str(self.chairs.get()))
        print("Add drinks  number is : " + str(self.add_drinks.get()))
        print("Drinks number is : " + str(self.drinks.get()))
        print("ShowFire number is : " + str(self.showfire.get()))
        print("EnternceLedScreen number is : " + str(self.enteranceScreen.get()))
        print("CatWalk number is : " + str(self.catwalk.get()))
        print("Lounge number is : " + str(self.lounge.get()))
        print("2 LargeRoundTable number is : " + str(self.largeroundtabled.get()))
        print("2 LargeRoundTableCenterpeice number is : " + str(self.largeCenterpeice.get()))
        print("Enterance GuestBook number is : " + str(self.enteranceguestbook.get()))
        print("GuestBook number is : " + str(self.guestbookB.get()))
        print("Decor Corridor number is : " + str(self.decorCorridor.get()))
        print("Hightables number is : " + str(self.hightables.get()))



    def update_count(self, value):
        count = self.count
        count.set(value)
        print(count.get())
        return count.get()

    def update_buffet(self, value):
        buffet = self.buffet
        buffetvar = self.buffetvar.get()
        if buffetvar == "Romancy":
            buffet.set(1)
            print(buffet.get())
            return buffet.get()
        elif buffetvar == "Ahlam":
            buffet.set(2)
            print(buffet.get())
            return buffet.get()
        elif buffetvar == "Omara":
            buffet.set(3)
            print(buffet.get())
            return buffet.get()
        else:
            buffet.set(1)
            print(buffet.get())

    def update_chairs(self, value):
        chairs = self.chairs
        chairsvar = self.chairsvar.get()
        if chairsvar == "Covers":
            chairs.set(1)
            print(chairs.get())
            return chairs.get()
        elif chairsvar == "VIP chairs":
            chairs.set(2)
            print(chairs.get())
            return chairs.get()
        else:
            chairs.set(1)
            print(chairs.get())


    def update_drinks(self, value):
        drinks = self.drinks
        drinksvar = self.drinksvar.get()
        temp = self.add_drinks.get()
        if temp == 0:
            self.drinksvar.set("")
            drinks.set(0)
            spinbox_drinks.configure(state=DISABLED)
        else:
            drinks = self.drinks
            drinksvar = self.drinksvar.get()
            if drinksvar == "Pepsi":
                drinks.set(1)
                print(drinks.get())
                return drinks.get()
            elif drinksvar == "Fresh Drinks":
                drinks.set(2)
                print(drinks.get())
                return drinks.get()
            elif drinksvar == "Open Buffet":
                drinks.set(3)
                print(drinks.get())
                return drinks.get()
            elif drinksvar == "":
                print(drinks.get())
                return drinks.get()
            else:
                drinks.set(0)
                print(drinks.get())

    def reset_drinks(self):
        drinks = self.drinks
        drinksvar = self.drinksvar.get()
        temp = self.add_drinks.get()
        if temp == 1:
            spinbox_drinks.configure(state=NORMAL)
            spinbox_drinks.configure(state="readonly")
        elif temp == 0:
            self.drinksvar.set("")
            drinks.set(0)
            spinbox_drinks.configure(state=DISABLED)

    def update_showfire(self, value):
        showfire = self.showfire
        showfirevar = self.showfirevar.get()
        if showfirevar == "Normal":
            showfire.set(1)
            print(showfire.get())
            return showfire.get()
        elif showfirevar == "The Rock":
            showfire.set(2)
            print(showfire.get())
            return showfire.get()
        elif showfirevar == "Dreams":
            showfire.set(3)
            print(showfire.get())
            return showfire.get()
        else:
            showfire.set(0)
            print(showfire.get())


    def update_largeRound(self, value):
        temp = self.largeroundtabled.get()
        if temp == 1:
            chkb_largeTables_centerPeice.configure(state=NORMAL)
        elif temp == 0:
            chkb_largeTables_centerPeice.configure(state=DISABLED)

    def update_GuestbookB(self):
        temp = self.enteranceguestbook.get()
        if temp > 0:
            chkb_Guestbook_book.configure(state=NORMAL)
        elif temp == 0:
            chkb_Guestbook_book.configure(state=DISABLED)




count = obj()

#================Variables=============================

countvar = IntVar()
typevar = IntVar()
buffetspinval = StringVar()
chairsspinvar = StringVar()
drinksspinvar = StringVar()
showfirespinvar = StringVar()
guestbookspinvar = StringVar()
hightablesspinvar = StringVar()
fireworksspinvar = StringVar()
bellydancerspinvar = StringVar()
ballerinaspinvar = StringVar()
videospinvar = StringVar()




#====================Tabs grid =========================
tabs = ttk.Notebook(root)
tabs.grid(column=0, row=1, columnspan=50, rowspan=49, sticky="NESW")

ekhnaton_frame = ttk.Frame(tabs)
ekhnaton_frame.grid()
isis_frame = ttk.Frame(tabs)
isis_frame.grid()
louts_frame = ttk.Frame(tabs)
louts_frame.grid()

localtime = time.asctime(time.localtime(time.time()))
time_info = ttk.Label(root,font=('arial', 10, 'bold'), text=localtime, anchor='w')
time_info.grid(row=1, column=45)

#==========================Row 2=====================================================

lblCount = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Count:", anchor='w')
lblCount.grid(row=2,column=1, padx=5, pady=5)
entry_count = Entry(ekhnaton_frame,width=19, font=('arial', 10, 'bold'),textvariable= count.count,bg="white", justify="center")
entry_count.grid(row=2,column=2,columnspan=1)
entry_count.focus()


lblbuffet = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Buffet:", anchor='w', justify="right")
lblbuffet.grid(row=2,column=4, pady=5)

count.update_buffet(1)
spinbox_buffet = Spinbox(ekhnaton_frame,from_=1,to=3,textvariable=count.buffetvar,font=('arial', 10, 'bold'), foreground="blue", values=("Romancy","Ahlam","Omara"), justify="center", state="readonly", command=lambda: count.update_buffet(count.buffet.get()))
spinbox_buffet.grid(row=2,column=5,columnspan=1)
spinbox_buffet.configure(state="readonly")
spinbox_buffet.tk_focusNext()




chkb_officer = Checkbutton(ekhnaton_frame,text="Officer",variable=count.type,font=('arial', 10, 'bold'),width=8, onvalue= 1,offvalue=0, justify="left", command=lambda: count.type.get())
chkb_officer.grid(row=2,column=6, columnspan=1, sticky="w")


#=======================================Row 3=========================================

lblChairs = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Chairs:", anchor='w')
lblChairs.grid(row=3,column=1, padx=5, pady=5)

count.update_chairs(1)
spinbox_chairs = Spinbox(ekhnaton_frame,from_=1,to=2 ,textvariable=count.chairsvar,font=('arial', 10, 'bold'), foreground="blue", values=("Covers", "VIP chairs"), justify="center", state="readonly", command=lambda: count.update_chairs(count.chairs.get()))
spinbox_chairs.grid(row=3,column=2,columnspan=1)
spinbox_chairs.configure(state="readonly")



chkb_drinks = Checkbutton(ekhnaton_frame, text="Add Drinks:",variable=count.add_drinks,font=('arial', 10, 'bold'), width=10, onvalue= 1, offvalue=0, justify="right", command=lambda: count.reset_drinks())
chkb_drinks.grid(row=3,column=4, columnspan=1)
chkb_drinks.select()

spinbox_drinks = Spinbox(ekhnaton_frame,from_=0,to=3 ,textvariable=count.drinksvar,font=('arial', 10, 'bold'), foreground="blue",background="#eff0f1", values=("","Pepsi","Fresh Drinks", "Open Buffet"), justify="center", state="readonly", command= lambda: count.update_drinks(count.drinks.get()))
spinbox_drinks.grid(row=3,column=5,columnspan=1)
spinbox_drinks.configure(state="readonly")

#======================================Row 4============================================

lblShowfire = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="ShowFire:", anchor='w')
lblShowfire.grid(row=4,column=1, padx=5, pady=5)

spinbox_showfire = Spinbox(ekhnaton_frame,from_=0,to=3 ,textvariable=count.showfirevar,font=('arial', 10, 'bold'), foreground="blue", values=("","Normal","The Rock", "Dreams"), justify="center", state="readonly", command=lambda :count.update_showfire(count.showfire.get()))
spinbox_showfire.grid(row=4,column=2,columnspan=1)
spinbox_showfire.configure(state="readonly")


lblSpecial_Entrance = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Special Entrance:", anchor='w')
lblSpecial_Entrance.grid(row=4,column=4, pady=5)


chkb_Entrence_led = Checkbutton(ekhnaton_frame, text="Entrance Screen",variable=count.enteranceScreen,font=('arial', 9, 'bold'), width=12, onvalue= 1, offvalue=0, justify="left")
chkb_Entrence_led.grid(row=4,column=5, columnspan=1, sticky="w")


chkb_Catwalk = Checkbutton(ekhnaton_frame, text="Cat Walk",variable=count.catwalk,font=('arial', 9, 'bold'), width=6, onvalue= 1, offvalue=0, justify="left")
chkb_Catwalk.grid(row=4,column=6, columnspan=1, sticky="w")


chkb_lounge = Checkbutton(ekhnaton_frame, text="Lounge",variable=count.lounge,font=('arial', 9, 'bold'), width=6, onvalue= 1, offvalue=0, justify="left", anchor="w")
chkb_lounge.grid(row=4,column=7, columnspan=1, sticky="w")

#====================================Row 5 ===============================

chkb_largeTables = Checkbutton(ekhnaton_frame, text="2 Large Round Tables",variable=count.largeroundtabled,font=('arial', 10, 'bold'), width=16, onvalue= 1, offvalue=0, justify="right",command=lambda: count.update_largeRound(count.largeroundtabled.get()))
chkb_largeTables.grid(row=5,column=1, columnspan=2)


chkb_corridor = Checkbutton(ekhnaton_frame, text="Decor Corridor",variable=count.decorCorridor,font=('arial', 10, 'bold'), width=11, onvalue= 1, offvalue=0, justify="right")
chkb_corridor.grid(row=5,column=6, columnspan=1, sticky="w")



lblSpecial_Entrance_gestbook = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Entrance Guest Book:", anchor='w')
lblSpecial_Entrance_gestbook.grid(row=5,column=4, pady=5)



spinbox_guestboot = Spinbox(ekhnaton_frame,from_=0,to=7 ,textvariable=count.enteranceguestbook,font=('arial', 10, 'bold'), foreground="blue", values=(0 ,400 ,450 ,600 ,650 ,700, 900, 1000), justify="center", state="readonly", command=lambda: count.update_GuestbookB())
spinbox_guestboot.grid(row=5,column=5,columnspan=1, padx=10)
spinbox_guestboot.configure(state="readonly")







#=====================================Row 6 ============================


chkb_largeTables_centerPeice = Checkbutton(ekhnaton_frame, text="With CenterPeice",variable=count.largeCenterpeice,state=DISABLED,font=('arial', 8, 'bold'), width=15, onvalue= 1, offvalue=0, justify="right")
chkb_largeTables_centerPeice.grid(row=6,column=2, columnspan=1)


chkb_Guestbook_book = Checkbutton(ekhnaton_frame, text="With Guest Book",state=DISABLED,variable=count.guestbookB,font=('arial', 8, 'bold'), width=15, onvalue= 1, offvalue=0, justify="right")
chkb_Guestbook_book.grid(row=6,column=4, columnspan=2)


tabs.add(ekhnaton_frame, text="Ekhnaton")
tabs.add(isis_frame, text="Isis")
tabs.add(louts_frame, text="Louts")

#==================================== Row 7 =================================


lblHigh_Tables = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="High Tables:", anchor='w')
lblHigh_Tables.grid(row=7,column=1, padx=10, pady=5)

spinbox_Hightables = Spinbox(ekhnaton_frame,from_=0,to=4 ,textvariable=count.hightables,font=('arial', 10, 'bold'), foreground="blue", values=(0 ,2 ,4 ,6 ,8), justify="center")
spinbox_Hightables.grid(row=7,column=2,columnspan=1)
spinbox_Hightables.configure(state="readonly")


lblFireworks = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Fireworks:", anchor='w')
lblFireworks.grid(row=7,column=4, pady=5)

spinbox_Hightables = Spinbox(ekhnaton_frame,from_=0,to=3 ,textvariable=fireworksspinvar,font=('arial', 10, 'bold'), foreground="blue", values=("" ,"4 on DanceFloor" ,"4 on Catwalk" ,"2 with CakeShow"), justify="center", state="readonly")
spinbox_Hightables.grid(row=7,column=5,columnspan=1)
spinbox_Hightables.configure(state="readonly")

#============================Row 8 =========================================


chkb_DanceFloor = Checkbutton(ekhnaton_frame, text="Dance Floor",font=('arial', 10, 'bold'), width=11, onvalue= 1, offvalue=0, justify="left")
chkb_DanceFloor.grid(row=8,column=2, columnspan=1, sticky="w")



lblBelly_dancers = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Belly Dancers:", anchor='w')
lblBelly_dancers.grid(row=8,column=4, pady=5)

spinboxBelly_dancers = Spinbox(ekhnaton_frame,from_=0,to=3 ,textvariable=bellydancerspinvar,font=('arial', 10, 'bold'), foreground="blue", values=(0 ,2 ,4 ,6), justify="center", state="readonly")
spinboxBelly_dancers.grid(row=8,column=5,columnspan=1)
spinboxBelly_dancers.configure(state="readonly")

#===============================Row 9 =================================================


chkb_Laser_show = Checkbutton(ekhnaton_frame, text="Laser_show",font=('arial', 10, 'bold'), width=11, onvalue= 1, offvalue=0, justify="left")
chkb_Laser_show.grid(row=9,column=2, columnspan=1, sticky="w")


lblBallerina = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Ballet Dancers:", anchor='w')
lblBallerina.grid(row=9,column=4, pady=5)

spinboxBallerina = Spinbox(ekhnaton_frame,from_=0,to=2 ,textvariable=ballerinaspinvar,font=('arial', 10, 'bold'), foreground="blue", values=(0 ,6 ,8), justify="center", state="readonly")
spinboxBallerina.grid(row=9,column=5,columnspan=1)
spinboxBallerina.configure(state="readonly")

#=================================== Row 10 ================================================

chkb_American_Cake = Checkbutton(ekhnaton_frame, text="American Cake",font=('arial', 10, 'bold'), width=14, onvalue= 1, offvalue=0, justify="left")
chkb_American_Cake.grid(row=10,column=2, columnspan=1, sticky="w")


lblVideo_Upgrade = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Video Upgrade:", anchor='w')
lblVideo_Upgrade.grid(row=10,column=4, pady=5)

spinboxVideo_Upgrade = Spinbox(ekhnaton_frame,from_=0,to=2 ,textvariable=videospinvar,font=('arial', 10, 'bold'), foreground="blue", values=("" ,"Full HD" ,"4K"), justify="center", state="readonly")
spinboxVideo_Upgrade.grid(row=10,column=5,columnspan=1)
spinboxVideo_Upgrade.configure(state="readonly")

#====================================Row 11 =========================================

chkb_Photo_Clip = Checkbutton(ekhnaton_frame, text="Photo Clip",font=('arial', 10, 'bold'), width=10, onvalue= 1, offvalue=0, justify="left")
chkb_Photo_Clip.grid(row=11,column=2, columnspan=1, sticky="w")


#=====================================Row 12 ==============================================

chkb_Bubbles = Checkbutton(ekhnaton_frame, text="Bubbles",font=('arial', 10, 'bold'), width=8, onvalue= 1, offvalue=0, justify="left")
chkb_Bubbles.grid(row=12,column=2, columnspan=1, sticky="w")

#=====================================Row 15==========================================

btnOK = ttk.Button(ekhnaton_frame, text="Submit", command=lambda: count.update_All(count.count.get()))
btnOK.grid(row=15, column=3)



root.mainloop()