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

	def bofeeh_cost(self):
		# madany type properity
		if self.ballroom_type == "madany":
			# romancy buffet for 250, less and more
			if self.buffet == 1:
				# romancy buffet for 250 count
				if self.count == 250:
					self.items['buffet'] = 68000
					self.cost = sum(self.items.values())
					print("your selection on ROMANCY buffet")
					print("your ballroom_type is Madany")
					print("your count is " + str(self.count))
				# romancy buffet for more, less than 250
				elif self.count > 250 and self.count < 451:
					rate = 140
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['buffet'] = 68000 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on ROMANCY buffet")
					print("your ballroom_type is Madany")
					print("your count is " + str(self.count))
				# for case out of capacity
				else:
					print("sorry ekhnaton capacity is from 250 to 450")
					print ("check your count again")
					return self.count
			# ahlam buffet for more, less or 250 count
			elif self.buffet == 2:
				# ahlam for 250 count
				if self.count == 250:
					self.items['buffet'] = 72500
					self.cost = sum(self.items.values())
					print("your selection on ALAHALM buffet")
					print("your ballroom_type is Madany")
					print("your count is " + str(self.count))
				# ahlam for more, less than 250
				elif self.count > 250 and self.count < 451:
					rate = 160
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['buffet'] = 72500 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on ALAHALM buffet")
					print("your ballroom_type is Madany")
					print("your count is " + str(self.count))
				# for out of capacity
				else:
					print("sorry ekhnaton capacity is from 250 to 450")
					print ("check your count again")
					return self.count
			# omaraa buffet for 250, less and more
			elif self.buffet == 3:
				# omaraa for 250 count
				if self.count == 250:
					self.items['buffet'] = 77000
					self.cost = sum(self.items.values())
					print("your selection on OMARA' buffet")
					print("your ballroom_type is Madany")
					print("your count is " + str(self.count))
				# omaraa for less and more than 250
				elif self.count > 250 and self.count < 451:
					rate = 180
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['buffet'] = 77000 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on OMARA' buffet")
					print("your ballroom_type is Madany")
					print("your count is " + str(self.count))
				# omara our of capacity
				else:
					print("sorry ekhnaton capacity is from 250 to 450")
					print ("check your count again")
					return self.count
		elif self.ballroom_type == "officer":
			if self.buffet == 1:
				if self.count == 250:
					self.items['buffet'] = 56000
					self.cost = sum(self.items.values())
					print("your selection on ROMANCY buffet")
					print("your ballroom_type is Officer")
					print("your count is " + str(self.count))
				elif self.count > 250 and self.count < 451:
					rate = 120
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['buffet'] = 56000 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on ROMANCY buffet")
					print("your ballroom_type is Officer")
					print("your count is " + str(self.count))
				else:
					print("sorry ekhnaton capacity is from 250 to 450")
					print ("check your count again")
					return self.count
			elif self.buffet == 2:
				if self.count == 250:
					self.items['buffet'] = 60500
					self.cost = sum(self.items.values())
					print("your selection on AHLAM buffet")
					print("your ballroom_type is Officer")
					print("your count is " + str(self.count))
				elif self.count > 250 and self.count < 451:
					rate = 140
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['buffet'] = 60500 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on AHLAM buffet")
					print("your ballroom_type is Officer")
					print("your count is " + str(self.count))
				else:
					print("sorry ekhnaton capacity is from 250 to 450")
					print ("check your count again")
					return self.count
			elif self.buffet == 3:
				if self.count == 250:
					self.items['buffet'] = 65000
					self.cost = sum(self.items.values())
					print("your selection on OMARAA' buffet")
					print("your ballroom_type is Officer")
					print("your count is " + str(self.count))
				elif self.count > 250 and self.count < 451:
					rate = 160
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['buffet'] = 65000 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on OMARAA' buffet")
					print("your ballroom_type is Officer")
					print("your count is " + str(self.count))
				else:
					print("sorry ekhnaton capacity is from 250 to 450")
					print ("check your count again")
					return self.count

	def add_chaircover(self):
		cost = self.count * 10
		self.items["chairs"]= cost
		self.cost = sum(self.items.values())

	def remove_chaircover(self):
		if "chairs" in self.items.keys():
			self.items.pop("chairs")

	def add_vipchairs(self):
		if "chairs" in self.items.keys():
			self.items.pop("chairs")
			cost = self.count * 20
			self.items["VIPchairs"]= cost
			self.cost = sum(self.items.values())
		else:
			cost = self.count * 20
			self.items["VIPchairs"]= cost
			self.cost = sum(self.items.values())

	def remove_Vipchairs(self):
		if "VIPchairs" in self.items.keys():
			self.items.pop("VIPchairs")



	def add_dancefloor(self):
		cost = 3500
		self.items["dancefloor"]= cost
		self.cost = sum(self.items.values())

	def remove_dancefloor(self):
		if "dancefloor" in self.items.keys():
			self.items.pop("dancefloor")


	def add_hightables(self, count_to_add):
		if count_to_add <= 8:
			cost = (count_to_add * 150)
			self.items["hightables"]= cost
			self.cost = sum(self.items.values())

		else:
			print("sorry max number of tables to add is 8")
			return count_to_add


	def remove_hightables(self):
		if "hightables" in self.items.keys():
			self.items.pop("hightables")

	def add_catwalk(self):
		self.items["catwalk"]= 2400
		self.cost = sum(self.items.values())

	def remove_catwalk(self):
		if "catwalk" in self.items.keys():
			self.items.pop("catwalk")


	def add_ledscreen(self):
		self.items["ledscreen"]= 3000
		self.cost = sum(self.items.values())

	def remove_ledscreen(self):
		if "ledscreen" in self.items.keys():
			self.items.pop("ledscreen")


	def add_launge(self, count_to_add):
		if count_to_add <= 4:
			cost = (count_to_add * 600)
			self.items["launge"]= cost
			self.cost = sum(self.items.values())

		else:
			print("sorry max number of tables to add is 4")
			return count_to_add

	def remove_launge(self):
		if "launge" in self.items.keys():
			self.items.pop("launge")

	def add_photoghraphy(self, cost_to_add):
		self.items["photograghy"]= cost_to_add
		self.cost = sum(self.items.values())

	def remove_photography(self):
		if "photograghy" in self.items.keys():
			self.items.pop("photograghy")

	def add_showfire(self, category):
		if category == 1:
			cost = 6000
			self.items["showfire"]= cost
			self.cost = sum(self.items.values())
			print("you selected first one 6500")

		elif category == 2:
			cost = 9000
			self.items["showfire"]= cost
			self.cost = sum(self.items.values())
			print("you selected the rock show 9000")

		elif category == 3:
			cost = 11500
			self.items["showfire"]= cost
			self.cost = sum(self.items.values())
			print("you selected dreams show 11500")

		else:
			print("sorry check your category from 1:3 available only")
			return category

	def remove_showfire(self):
		if "showfire" in self.items.keys():
			self.items.pop("showfire")

	def add_bubbles(self):
		self.items["bubbles"]= 350
		self.cost = sum(self.items.values())

	def remove_bubbled(self):
		if "bubbles" in self.items.keys():
			self.items.pop("bubbles")

	def add_firworks_on_df(self):
		self.items["4 fireworks on DF"]= 1200
		self.cost = sum(self.items.values())

	def remove_firworks_on_df(self):
		if "4 fireworks on DF" in self.items.keys():
			self.items.pop("4 fireworks on DF")

	def add_firworks_on_cw(self):
		self.items["4 fireworks on CW"]= 1200
		self.cost = sum(self.items.values())

	def remove_firworks_on_cw(self):
		if "4 fireworks on CW" in self.items.keys():
			self.items.pop("4 fireworks on CW")

	def add_firworks_on_cake(self):
		self.items["2 fireworks on cake"]= 600
		self.cost = sum(self.items.values())

	def remove_firworks_on_cake(self):
		if "2 fireworks on cake" in self.items.keys():
			self.items.pop("2 fireworks on cake")

	def add_dancers(self, count):
		cost = (count /2) * 850
		self.items["dancers"]= cost
		self.cost = sum(self.items.values())

	def remove_dancers(self):
		if "dancers" in self.items.keys():
			self.items.pop("dancers")

	def add_ballarena(self, count):
		if count == 6:
			cost = 1000
			self.items["ballarena"]= cost
			self.cost = sum(self.items.values())
		elif count == 8:
			cost = 1200
			self.items["ballarena"]= cost
			self.cost = sum(self.items.values())
		else:
			print("sorry you can request 6 or 8 girls only")


	def remove_ballarena(self):
		if "ballarena" in self.items.keys():
			self.items.pop("ballarena")

	def add_photo_clip(self):
		print("send your photos before 7 days of your wedding day.")
		self.items["photoclip"]= 300
		self.cost = sum(self.items.values())

	def remove_photo_clip(self):
		if "photoclip" in self.items.keys():
			self.items.pop("photoclip")

	def add_show_laser(self):
		self.items["showlaser"]= 2500
		self.cost = sum(self.items.values())

	def remove_show_laser(self):
		if "showlaser" in self.items.keys():
			self.items.pop("showlaser")

	def add_pepsi(self):
		if "open drinks" in self.items.keys():
			self.items.pop("open drinks")
		cost = self.count * 4
		self.items["pepsi"] = cost
		self.cost = sum(self.items.values())


	def remove_pepsi(self):
		if "pepsi" in self.items.keys():
			self.items.pop("pepsi")

	def add_fresh_juice(self):
		cost = self.count * 10
		self.items["fresh juice"] = cost
		self.cost = sum(self.items.values())


	def remove_fresh_juice(self):
		if "fresh juice" in self.items.keys():
			self.items.pop("fresh juice")

	def add_open_drinks(self):
		if "pepsi" in self.items.keys():
			self.items.pop("pepsi")
		cost = self.count * 15
		self.items["open drinks"] = cost
		self.cost = sum(self.items.values())


	def remove_open_drinks(self):
		if "open drinks" in self.items.keys():
			self.items.pop("open drinks")

	def add_mazoon(self,m=1000):
		if m <= 10000:
			cost = 600
			self.items["mazoon"] = cost
			self.cost = sum(self.items.values())
		elif m != 0 and m > 10000:
			cost = (m* (3.5/100)) + 100
			self.items["mazoon"] = cost
			self.cost = sum(self.items.values())
		else:
			print("check moaphar amount to get you right cost")

	def remove_mazoon(self):
		if "mazoon" in self.items.keys():
			self.items.pop("mazoon")
			
	def add_nuts(self):
		cost = self.count * 25
		self.items["nuts"] = cost
		self.cost= sum(self.items.values())
			
	def remove_nuts(self):
		if "nuts" in self.items.keys():
			self.items.pop("nuts")
			
	def add_american_cake(self):
		cost = 500
		self.items["american cake"]= cost
		self.cost = sum(self.items.values())
		
	def remove_american_cake(self):
		if "american cake" in self.items.keys():
			self.items.pop("american cake")
			
	def add_fullHD(self):
		if "4k" in self.items.keys():
			self.items.pop("4k")
		cost = 10000
		self.items["fullHD"]= cost
		self.cost = sum(self.items.values())
		
	def remove_fullHD(self):
		if "fullHD" in self.items.keys():
			self.items.pop("fullHD")
		
	def add_4k(self):
		if "fullHD" in self.items.keys():
			self.items.pop("fullHD")
		cost = 15000
		self.items["4k"]= cost
		self.cost = sum(self.items.values())
		
	def remove_4k(self):
		if "4k" in self.items.keys():
			self.items.pop("4k")
			
	def add_decore_corridoor(self):
		cost = 2500
		self.items["decore corridor"] = cost
		self.cost = sum(self.items.values())
		
	def remove_decore_corridoor(self):
		if "decore corridor" in self.items.keys():
			self.items.pop("decore corridor")
			
	def add_entrance_guestbook(self):
		cost = 600
		self.items["entrance guestbook"] = cost
		self.cost = sum(self.items.values())
		
	def remove_entrance_guestbook(self):
		if "entrance guestbook" in self.items.keys():
			self.items.pop("entrance guestbook")
			
	def add_guestbook(self):
		cost = 300
		self.items["guestbook"] = cost
		self.cost = sum(self.items.values())
		
	def remove_guestbook(self):
		if "guestbook" in self.items.keys():
			self.items.pop("guestbook")
			
	def add_merriage_cups(self):
		cost = 150
		self.items["merriage_cups"] = cost
		self.cost = sum(self.items.values())
	
	def remove_merriage_cups(self):
		if "merriage_cups" in self.items.keys():
			self.items.pop("merriage_cups")
		
	def add_2_large_round_table(self):
		cost = 2000
		self.items["2_large_round_table"] = cost
		self.cost = sum(self.items.values())
		
	def remove_2_large_round_table(self):
		if "2_large_round_table" in self.items.keys():
			self.items.pop("2_large_round_table")
			
	def add_premission_outer_photography(self):
		if self.ballroom_type == "madany":
			cost = 2000
			self.items["premission_outer_photography"] = cost
			self.cost = sum(self.items.values())
		elif self.ballroom_type == "officer":
			cost = 1000
			self.items["premission_outer_photography"] = cost
			self.cost = sum(self.items.values())
		else:
			print("check your ballroom_type madany or office no more choices")
			
	def remove_premission_outer_photography(self):
		if "premission_outer_photography" in self.items.keys():
			self.items.pop("premission_outer_photography")
			
			
	def add_chocolate_fountine(self):
		cost = 1500
		self.items["chocolate_fountine"] = cost
		self.cost = sum(self.items.values())
		
	def remove_chocolate_fountine(self):
		if "chocolate_fountine" in self.items.keys():
			self.items.pop("chocolate_fountine")
			
		def add_sound(self):
			cost = 1000
			self.items["sound"]= cost
			self.cost = sum(self.items.values())
			
		def remove_sound(self):
			if "sound" in self.items.keys():
				self.items.pop("sound")
				
				
		def add_extra_dvd(self, count):
			cost = count * 40
			self.items["extra_dvd"]= cost
			self.cost = sum(self.items.values())
			
		def remove_extra_dvd(self):
			if "extra_dvd" in self.items.keys():
				self.items.pop("extra_dvd")
				
		def add_flash_video(self, count=1):
			cost = count * 250
			self.items["flash_video"]= cost
			self.cost = sum(self.items.values())
			
		def remove_flash_video(self):
			if "flash_video" in self.items.keys():
				self.items.pop("flash_video")

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

def

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