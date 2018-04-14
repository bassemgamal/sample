from tkinter import *
from tkinter import ttk
import time
from tkinter import messagebox
from tkinter import Checkbutton

#===================root Frame
root = Tk()
root.geometry("600x600")
root.title("Ballroom Calculator")



#=======================Tabs Func===================
rows = 0
while rows < 50:
    root.rowconfigure(rows, weight=1)
    root.columnconfigure(rows, weight=1)
    rows += 1

#=======================Functions========================
def check_add():
    if chkb_drinks.get() == 0:

        chkb_drinks.deselect()
    elif chkb_drinks.get() == 1:
        spinbox_drinks.config(state=NORMAL)
        chkb_drinks.select()







#================Variables=============================
buffetspinval = StringVar()
chairsspinvar = StringVar()
drinksspinvar = StringVar()






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
entry_count = ttk.Entry(ekhnaton_frame,width=19, font=('arial', 10, 'bold'), justify="center")
entry_count.grid(row=2,column=2,columnspan=1)
entry_count.focus()


lblbuffet = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Buffet:", anchor='w')
lblbuffet.grid(row=2,column=5, padx=5, pady=5)

spinbox_buffet = ttk.Spinbox(ekhnaton_frame,from_=1,to=3 ,textvariable=buffetspinval, values=("Romancy","Ahlam","Omara"), justify="center", state="readonly")
spinbox_buffet.grid(row=2,column=6,columnspan=1)
spinbox_buffet.configure(state="readonly")

chkb_officer = Checkbutton(ekhnaton_frame,text="Officer",font=('arial', 10, 'bold'),width=10, onvalue= 1)
chkb_officer.grid(row=2,column=7, columnspan=1, padx=10)

#=======================================Row 3=========================================

lblChairs = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Chairs:", anchor='w')
lblChairs.grid(row=3,column=1, padx=5, pady=5)

spinbox_chairs = ttk.Spinbox(ekhnaton_frame,from_=1,to=2 ,textvariable=chairsspinvar, values=("VIP chairs","Covers"), justify="center", state="readonly")
spinbox_chairs.grid(row=3,column=2,columnspan=1)
spinbox_chairs.configure(state="readonly")



chkb_drinks = Checkbutton(ekhnaton_frame, text="Add Drinks:",font=('arial', 10, 'bold'), width=10, onvalue= 1, offvalue=0)
chkb_drinks.grid(row=3,column=5, columnspan=1, padx=10)
chkb_drinks.select()

spinbox_drinks = ttk.Spinbox(ekhnaton_frame,from_=0,to=3 ,textvariable=drinksspinvar, values=("","Pepsi","Fresh Drinks", "Open Buffet"), justify="center", state="readonly")
spinbox_drinks.grid(row=3,column=6,columnspan=1)
spinbox_drinks.configure(state="readonly")







tabs.add(ekhnaton_frame, text="Ekhnaton")
tabs.add(isis_frame, text="Isis")
tabs.add(louts_frame, text="Louts")






root.mainloop()