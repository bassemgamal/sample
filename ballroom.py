class ballroom():
	def __init__(self, name, count):
		self.name = name
		self.count = count
		

class ekhnaton(ballroom):
	def __init__ (self, name, count, bofeeh, type, cost=0, items={}):
		ballroom.__init__(self, name, count)
		self.type = type
		self.bofeeh = bofeeh
		self.cost = cost
		self.items = items
	
	
	def delete_it(self):
		del self.name
		del self.count
		del self.bofeeh
		del self.type
		del self.cost
		del self.items
		del self
		
	def check_out(self):
		self.cost = sum(self.items.values())
		print("="* 30)
		print("items "+ (" "*14) + "cost")
		print("="* 30)
		for i in self.items:
			before = 20 - len(str(i))
			print(str(i) + (" "* before) + str(self.items[i]))
		print("_"* 30)
		print("total "+ (" "*14) + str(self.cost))
		
	def bofeeh_cost(self):
		# madany type properity
		if self.type == "madany":
			# romancy bofeeh for 250, less and more
			if self.bofeeh == 1:
				# romancy bofeeh for 250 count
				if self.count == 250:
					self.items['bofeeh'] = 68000
					self.cost = sum(self.items.values())
					print("your selection on romancy")
					print("your count is " + str(self.count))
					return self.cost, self.items
				# romancy bofeeh for more, less than 250
				elif self.count > 250 and self.count < 451:
					rate = 140
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['bofeeh'] = 68000 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on romancy")
					print("your count is " + str(self.count))
					return self.cost, self.items
				# for case out of capacity
				else:
					print("sorry ekhnaton capacity is from 250 to 450")
					print ("check your count again")
					return self.count
			# ahlam bofeeh for more, less or 250 count
			elif self.bofeeh == 2:
				# ahlam for 250 count
				if self.count == 250:
					self.items['bofeeh'] = 72500
					self.cost = sum(self.items.values())
					print("your selection on ahlam")
					print("your count is " + str(self.count))
					return self.cost, self.items
				# ahlam for more, less than 250
				elif self.count > 250 and self.count < 451:
					rate = 160
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['bofeeh'] = 72500 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on ahlam")
					print("your count is " + str(self.count))
					return self.cost, self.items
				# for out of capacity
				else:
					print("sorry ekhnaton capacity is from 250 to 450")
					print ("check your count again")
					return self.count
			# omaraa bofeeh for 250, less and more
			elif self.bofeeh == 3:
				# omaraa for 250 count
				if self.count == 250:
					self.items['bofeeh'] = 77000
					self.cost = sum(self.items.values())
					print("your selection on omaraa")
					print("your count is " + str(self.count))
					return self.cost, self.items
				# omaraa for less and more than 250
				elif self.count > 250 and self.count < 451:
					rate = 180
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['bofeeh'] = 77000 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on omaraa")
					print("your count is " + str(self.count))
					return self.cost, self.items
				# omara our of capacity
				else:
					print("sorry ekhnaton capacity is from 250 to 450")
					print ("check your count again")
					return self.count
		elif self.type == "officer":
			if self.bofeeh == 1:
				if self.count == 250:
					self.items['bofeeh'] = 56000
					self.cost = sum(self.items.values())
					print("your selection on romancy")
					print("your count is " + str(self.count))
					return self.cost, self.items
				elif self.count > 250 and self.count < 451:
					rate = 120
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['bofeeh'] = 56000 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on romancy")
					print("your count is " + str(self.count))
					return self.cost, self.items
				else:
					print("sorry ekhnaton capacity is from 250 to 450")
					print ("check your count again")
					return self.count
			elif self.bofeeh == 2:
				if self.count == 250:
					self.items['bofeeh'] = 60500
					self.cost = sum(self.items.values())
					print("your selection on ahlam")
					print("your count is " + str(self.count))
					return self.cost, self.items
				elif self.count > 250 and self.count < 451:
					rate = 140
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['bofeeh'] = 60500 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on ahlam")
					print("your count is " + str(self.count))
					return self.cost, self.items
				else:
					print("sorry ekhnaton capacity is from 250 to 450")
					print ("check your count again")
					return self.count
			elif self.bofeeh == 3:
				if self.count == 250:
					self.items['bofeeh'] = 65000
					self.cost = sum(self.items.values())
					print("your selection on omaraa")
					print("your count is " + str(self.count))
					return self.cost, self.items
				elif self.count > 250 and self.count < 451:
					rate = 160
					extra = self.count - 250
					extra_cost = rate * extra
					self.items['bofeeh'] = 65000 + extra_cost
					self.cost = sum(self.items.values())
					print("your selection on omaraa")
					print("your count is " + str(self.count))
					return self.cost, self.items
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
