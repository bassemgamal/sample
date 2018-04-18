import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.ttk
import time

class Ekhnaton:
	def __init__ (self, count, buffet, ballroom_type, name="", cost=0, items={}):
		self.count = count
		self.buffet = buffet
		self.ballroom_type = ballroom_type
		self.name = name
		self.cost = cost
		self.items = items



	def delete_it(self):
		del self.name
		del self.count
		del self.buffet
		del self.ballroom_type
		del self.cost
		del self.items

	def check_out(self):
		print(self.name)
		print(self.count)
		print(self.buffet)
		print(self.ballroom_type)
		print(self.items)
		self.cost = sum(self.items.values())
		print("="* 30)
		print("items "+ (" "*14) + "cost")
		print("="* 30)
		for key in sorted(self.items.keys()):
			before = 20 - len(str(key))
			print(str(key) + (" "* before) + str(self.items[key]))
		print("_"* 30)
		print("total "+ (" "*14) + str(self.cost))
		return self.cost
#=================================================================

#========================================================================






			

		def add_sound(self):
			cost = 1000
			self.items["sound"]= cost
			self.cost = sum(self.items.values())
			
		def remove_sound(self):
			if "sound" in self.items.keys():
				self.items.pop("sound")
				

#=========================GUI PART=====================================
			
root = Tk()

a = Ekhnaton(count=250, buffet=1, ballroom_type="madany")

#=======================Root config========================

root.geometry("800x600+0+0")
root.title("BallRoom Calculator")
root.configure()
root.configure(cursor="dot")

#========================FRAMES==========================

Frame_Top = Frame(root, width=800)
Frame_Top.pack(side=TOP)

Frame1 = Frame(root, width=400,height=275,relief=SUNKEN)
Frame1.pack(side=TOP)

Frame2 = Frame(root, width=400,height=275,relief=SUNKEN)
Frame2.pack(side=BOTTOM)

#===========================Time============================

localtime = time.asctime(time.localtime(time.time()))

#==========================Info===========================

label_info= Label(Frame_Top, font=('arial', 15, 'bold'), text="Ballroom Calculator", fg="steel Blue", bd=10, anchor='w')
label_info.grid(row=0, column=0)
label_info= Label(Frame_Top, font=('arial', 15, 'bold'), text=localtime, fg="steel Blue", bd=10, anchor='w')
label_info.grid(row=1, column=0)

#============================labels and entries=====================
Name = StringVar()
Count = IntVar()
Buffet = IntVar()
Type= StringVar()
cost = 0
buffit_combovar = StringVar()
#buffit_combo['values'] = ('Romany', 'Ahlam', 'Omaraa')



#=======================getter func==============================


def get_info():
	get_Name = Name.get()
	print(get_Name)
	get_Count = int(Count.get())
	print(get_Count)
	get_Buffet = int(Buffet.get())
	print(get_Buffet)
	get_Type = Type.get()
	print(get_Type)
	create_obj(get_Count, get_Buffet, get_Type,get_Name)
	return

def create_obj( Count, Buffet, Type, Name):
	a = Ekhnaton(Count,Buffet,Type,Name)
	print(a.count)
	print(a.buffet)
	print(a.ballroom_type)
	print(a.name)
	print(a.bofeeh_cost())
	print(a.check_out())
	return a, a.count, a.buffet, a.ballroom_type, a.name


#=======================NAME func==============================


def set_name():
	a.name = Name.get()
	return a.name


#=======================Buffet Func==============================



"""
def set_Buffet():
	if chkButton == ON:
		Buffet = 1
		chkButton2 = OFF
		chkButton3 = OFF

def set_Buffet2():
	if chkButton2 == ON:
		Buffet = 2
		chkButton = OFF
		chkButton3 = OFF


def set_Buffet3():
	if chkButton2 == OFF and chkButton == OFF:
		Buffet = 3
		chkButton3 = ON
		chkButton = OFF
		chkButton3 = OFF
"""
def set_Type():
	if radioBtn1 == ON:
		Type = "officer"
	elif radioBtn2 == ON:
		Type = "madany"
	return





#=======================NAME ROW==============================

lblName = Label(Frame1, font=('arial', 10, 'bold'), text="Name:", anchor='w')
lblName.grid(row=0,column=0)

txtName = Entry(Frame1,width=30, font=('arial', 10, 'bold'), textvariable=Name, insertwidth=2,
					 bg="powder blue", justify="center")
txtName.grid(row=0,column=1,columnspan=2)


#=======================Count ROW==============================


lblCount = Label(Frame1, font=('arial', 10, 'bold'), text="Count:", anchor='w')
lblCount.grid(row=1,column=0)
txtReference = Entry(Frame1,width=30, font=('arial', 10, 'bold'), textvariable=Count, insertwidth=2,
					 bg="powder blue", justify="center")
txtReference.grid(row=1,column=1,columnspan=2)

#=======================Buffet ROW==============================

lblBuffet = Label(Frame1, font=('arial', 10, 'bold'), text="Buffet:", anchor='w')
lblBuffet.grid(row=2,column=0)
"""
chkButton = Checkbutton(Frame1,text="Romancy",width=10, font=('arial', 10, 'bold'),variable = Buffet, onvalue= 1, command=set_Buffet)
chkButton.grid(row=3,column=0, columnspan=1)

chkButton2 = Checkbutton(Frame1, text="Dreams",width=15, font=('arial', 10, 'bold'),variable = Buffet, onvalue= 2,command=set_Buffet2)
chkButton2.grid(row=4,column=0,columnspan=1 )

chkButton3 = Checkbutton(Frame1, text="Knites",width=20, font=('arial', 10, 'bold'),variable = Buffet, onvalue= 3,command=set_Buffet3)
chkButton3.grid(row=5,column=0,columnspan=1)"""


#=======================Type ROW==============================


lblType = Label(Frame1, font=('arial', 10, 'bold'), text="Type:", anchor='w')
lblType.grid(row=2,column=2)
radioBtn1 = Radiobutton(Frame1, font=('arial', 10, 'bold'), text="Officer",state=NORMAL,justify="left",variable = Type,value="officer",command=set_Type)
radioBtn1.grid(row=3,column=2)

radioBtn2 = Radiobutton(Frame1, font=('arial', 10, 'bold'), text="Madany",state=NORMAL, justify="left",variable = Type,value="madany", command=set_Type)
radioBtn2.grid(row=4,column=2)


#=======================test Buttons ROW==============================

Button3 = Button(Frame2)
Button3.place(relx=0.66, rely=0.4, height=24, width=107)
Button3.configure(activebackground="#d9d9d9")
Button3.configure(activeforeground="#000000")
Button3.configure(background="#d9d9d9")
Button3.configure(disabledforeground="#a3a3a3")
Button3.configure(foreground="#000000")
Button3.configure(highlightbackground="#d9d9d9")
Button3.configure(highlightcolor="black")
Button3.configure(pady="0")
Button3.configure(takefocus="0")
Button3.configure(text='''create''')
Button3.configure(command=a.check_out)

Button2 = Button(Frame2)
Button2.place(relx=0.66, rely=0.58, height=24, width=107)
Button2.configure(activebackground="#d9d9d9")
Button2.configure(activeforeground="#000000")
Button2.configure(background="#d9d9d9")
Button2.configure(disabledforeground="#a3a3a3")
Button2.configure(foreground="#000000")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(pady="0")
Button2.configure(takefocus="0")
Button2.configure(text='''submit''')
Button2.configure(command=set_name)



Button1 = Button(Frame2)
Button1.place(relx=0.33, rely=0.58, height=24, width=107)
Button1.configure(activebackground="#d9d9d9")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#d9d9d9")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(takefocus="0")
Button1.configure(text='''update''')
Button1.configure(command=get_info)

def buffet_checking():
	print(str(buffit_combovar.get()) + "  is the comobo var")
	if buffit_combovar.get() == 'Romancy':
		a.Buffet = 1
		print(str(buffit_combovar.get()) + "  is the comobo var after if")
		print(str(a.Buffet) + " is is actual Buffit")
		return a.Buffet
	elif buffit_combovar.get() == 'Ahlam':
		a.Buffet = 2
		Buffet = a.Buffet
		print(str(a.Buffet) + " is is actual Buffit")
		return a.Buffet, Buffet
	elif buffit_combovar.get() == 'Omaraa':
		a.Buffet = 3
		return a.Buffet


Button4 = Button(Frame2)
Button4.place(relx=0.15, rely=0.7, height=24, width=107)
Button4.configure(activebackground="#d9d9d9")
Button4.configure(activeforeground="#000000")
Button4.configure(background="#d9d9d9")
Button4.configure(disabledforeground="#a3a3a3")
Button4.configure(foreground="#000000")
Button4.configure(highlightbackground="#d9d9d9")
Button4.configure(highlightcolor="black")
Button4.configure(pady="0")
Button4.configure(takefocus="0")
Button4.configure(text='''Chair''')
Button4.configure(command=buffet_checking)


buffit_combo = ttk.Combobox(Frame1, textvariable=buffit_combovar)
buffit_combo['values'] = ('Romancy', 'Ahlam', 'Omaraa')
buffit_combo.bind('<<ComoboxSelected>>', buffet_checking)

buffit_combo.grid(column=6, row=6)




root.mainloop()