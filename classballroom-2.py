#import tkinter
#from tkinter import *


class ballroom():
	def __init__(self, name, count):
		self.name = name
		self.count = count


class ekhnaton(ballroom):
	def __init__ (self, name, count, buffet, type, cost=0, items={}):
		ballroom.__init__(self, name, count)
		self.type = type
		self.buffet = buffet
		self.cost = cost
		self.items = items


	def delete_it(self):
		del self.name
		del self.count
		del self.buffet
		del self.type
		del self.cost
		del self.items

	def check_out(self):
		self.cost = sum(self.items.values())
		print("="* 30)
		print("items "+ (" "*14) + "cost")
		print("="* 30)
		for key in sorted(self.items.keys()):
			before = 20 - len(str(key))
			print(str(key) + (" "* before) + str(self.items[key]))
		print("_"* 30)
		print("total "+ (" "*14) + str(self.cost))

	def bofeeh_cost(self):
		# madany type properity
		if self.type == "madany":
			# romancy buffet for 250, less and more
			if self.buffet == 1:
				# romancy buffet for 250 count
				if self.count == 250:
					self.items['buffet'] = 68000
					self.cost = sum(self.items.values())
					print("your selection on ROMANCY buffet")
					print("your Type is Madany")
					print("your count is " + str(self.count))
				# romancy buffet for more, less than 250
				elif self.count > 250 and self.count < 451:
					rate = 140
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['buffet'] = 68000 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on ROMANCY buffet")
					print("your Type is Madany")
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
					print("your Type is Madany")
					print("your count is " + str(self.count))
				# ahlam for more, less than 250
				elif self.count > 250 and self.count < 451:
					rate = 160
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['buffet'] = 72500 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on ALAHALM buffet")
					print("your Type is Madany")
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
					print("your Type is Madany")
					print("your count is " + str(self.count))
				# omaraa for less and more than 250
				elif self.count > 250 and self.count < 451:
					rate = 180
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['buffet'] = 77000 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on OMARA' buffet")
					print("your Type is Madany")
					print("your count is " + str(self.count))
				# omara our of capacity
				else:
					print("sorry ekhnaton capacity is from 250 to 450")
					print ("check your count again")
					return self.count
		elif self.type == "officer":
			if self.buffet == 1:
				if self.count == 250:
					self.items['buffet'] = 56000
					self.cost = sum(self.items.values())
					print("your selection on ROMANCY buffet")
					print("your Type is Officer")
					print("your count is " + str(self.count))
				elif self.count > 250 and self.count < 451:
					rate = 120
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['buffet'] = 56000 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on ROMANCY buffet")
					print("your Type is Officer")
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
					print("your Type is Officer")
					print("your count is " + str(self.count))
				elif self.count > 250 and self.count < 451:
					rate = 140
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['buffet'] = 60500 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on AHLAM buffet")
					print("your Type is Officer")
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
					print("your Type is Officer")
					print("your count is " + str(self.count))
				elif self.count > 250 and self.count < 451:
					rate = 160
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['buffet'] = 65000 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on OMARAA' buffet")
					print("your Type is Officer")
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
		if self.type == "madany":
			cost = 2000
			self.items["premission_outer_photography"] = cost
			self.cost = sum(self.items.values())
		elif self.type == "officer":
			cost = 1000
			self.items["premission_outer_photography"] = cost
			self.cost = sum(self.items.values())
		else:
			print("check your type madany or office no more choices")
			
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
				
		
		
			
			
			
##	root = Tk()
##	main_frame = Frame(root,height = 900, width = 1800)
##	main_frame.pack()
##	
##	label_topframe = LabelFrame(root, text="main3 frame")
##	label_topframe.pack(fill="both", expand="yes") 
##
##	
##	label_bottomframe = LabelFrame(label_topframe, text="main2 frame")
##	label_bottomframe.pack(expand="yes")
##
##	name = StringVar()
##	name_label = Label(label_topframe, bd= 3, textvariable=name, relief=RAISED)
##	name.set("Name:")
##	name_label.pack(side = TOP)
##	
##	greenbutton = Button(main_frame, text="Brown", fg="brown")
##	greenbutton.pack( side = LEFT )
##	bluebutton = Button(main_frame, text="Blue", fg="blue")
##	bluebutton.pack( side = LEFT )
##	#blackbutton = Button(bottomframe, text="Black", fg="black")
##	#blackbutton.pack( side = BOTTOM)
##	root.mainloop()