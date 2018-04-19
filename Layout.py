from tkinter import *
from tkinter import ttk
import time
from tkinter import messagebox
from tkinter import Checkbutton

#===================root Frame
root = Tk()
root.geometry("600x600")
root.minsize(width="1000",height="700")
root.title("Ballroom Calculator")



#=======================Tabs Func===================
rows = 0
while rows < 50:
    root.rowconfigure(rows, weight=1)
    root.columnconfigure(rows, weight=1)
    rows += 1

#=======================Functions========================
class obj_ekhnaton:
    def __init__(self):
        self.count = IntVar()
        self.buffetvar = StringVar()
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
        self.dancefloor = IntVar()
        self.fourfireoncatwalk = IntVar()
        self.twofiresoncake = IntVar()
        self.fourfiresondance = IntVar()
        self.bellydancer = IntVar()
        self.ballerina = IntVar()
        self.laser = IntVar()
        self.guestdisplay = IntVar()
        self.decorcatwalk = IntVar()
        self.americancake = IntVar()
        self.photclip = IntVar()
        self.bubbles = IntVar()
        self.video = IntVar()
        self.videovar = StringVar()
        self.sherbettray = IntVar()
        self.chocolatefountain = IntVar()
        self.projector = IntVar()
        self.spanishshow = IntVar()
        self.photographyout = IntVar()
        self.photographyin = IntVar()
        self.photographyinvalue = IntVar()
        self.nuts = IntVar()
        self.nutsvalue = IntVar()
        self.mazoon = IntVar()
        self.mazoonvalue = IntVar(())
        self.guestphoto = IntVar()
        self.centerpeiceromancy = IntVar()
        self.extradvd = IntVar()
        self.extraflash = IntVar()
        self.sound = IntVar()
        self.artistin1 = IntVar()
        self.artistin2 = IntVar()
        self.artistin3 = IntVar()
        self.artistout1 = IntVar()
        self.artistout2 = IntVar()
        self.artistout3 = IntVar()
        self.items = {}
        self.cost = IntVar()



    def check_out(self):
        countValue.set(account.count.get())
        print(" " * 41)
        print("#" * 41)
        print("=" * 15 + "  SUMMARY  " + "=" * 15)
        print("#" * 41)
        print(" " * 41)
        if account.chairs.get() == 1:
            account.remove_Vipchairs()
            account.add_chaircover()
            chairsValue.set(str(account.items["chairs"])+ " L.E.")
        elif account.chairs.get() == 2:
            account.remove_chaircover()
            account.add_vipchairs()
            chairsValue.set(str(account.items["VIPchairs"])+ " L.E.")
        if account.drinks.get() == 1:
            account.remove_open_drinks()
            account.remove_fresh_juice()
            account.add_pepsi()
            drinksValue.set(str(account.items["pepsi"])+ " L.E.")
        elif account.drinks.get() == 2:
            account.remove_pepsi()
            account.remove_open_drinks()
            account.add_fresh_juice()
            drinksValue.set(str(account.items["fresh juice"])+ " L.E.")
        elif account.drinks.get() == 3:
            account.remove_pepsi()
            account.remove_fresh_juice()
            account.add_open_drinks()
            drinksValue.set(str(account.items["open drinks"])+ " L.E.")
        elif account.drinks.get() == 0:
            account.remove_pepsi()
            account.remove_fresh_juice()
            account.remove_open_drinks()
            drinksValue.set(str(0)+ " L.E.")
        if account.showfire.get() == 0:
            showfireValue.set(str(0)+ " L.E.")
        elif account.showfire.get() == 1:
            account.add_showfire(1)
            showfireValue.set(str(account.items["showfire"]) + " L.E.")
        elif account.showfire.get() == 2:
            account.add_showfire(2)
            showfireValue.set(str(account.items["showfire"]) + " L.E.")
        elif account.showfire.get() == 3:
            account.add_showfire(3)
            showfireValue.set(str(account.items["showfire"]) + " L.E.")
        if account.dancefloor.get() == 1:
            account.add_dancefloor()
            dancefloorValue.set(str(account.items["dancefloor"]) + " L.E.")
        elif account.dancefloor.get() == 0:
            account.remove_dancefloor()
            dancefloorValue.set(str(0) + " L.E.")
        if account.fourfiresondance.get() == 1:
            account.add_firworks_on_df()
            fireondancefloorValue.set(str(account.items["4 fireworks on DF"])+" L.E.")
        elif account.fourfiresondance.get() == 0:
            account.remove_firworks_on_df()
            fireondancefloorValue.set(str(0) + " L.E.")
        if account.fourfireoncatwalk.get() == 1:
            account.add_firworks_on_cw()
            fireoncatwalkValue.set(str(account.items["4 fireworks on CW"]) + " L.E.")
        elif account.fourfireoncatwalk.get() == 0:
            account.remove_firworks_on_cw()
            fireoncatwalkValue.set(str(0) + " L.E.")
        if account.twofiresoncake.get() == 1:
            account.add_firworks_on_cake()
            fireoncakeValue.set(str(account.items["2 fireworks on cake"]) + " L.E.")
        elif account.twofiresoncake.get() == 0:
            account.remove_firworks_on_cake()
            fireoncakeValue.set(str(0) + " L.E.")
        if account.photclip.get() == 1:
            account.add_photo_clip()
            photoclipValue.set(str(account.items["photoclip"]) + " L.E.")
        elif account.photclip.get() == 0:
            account.remove_photo_clip()
            photoclipValue.set(str(0) + " L.E.")
        if account.video.get() == 1:
            account.add_fullHD()
            videoupgradeValue.set(str(account.items["fullHD"]) + " L.E.")
        elif account.video.get() == 2:
            account.add_4k()
            videoupgradeValue.set(str(account.items["4k"]) + " L.E.")
        elif account.video.get() == 0:
            account.remove_fullHD()
            account.remove_4k()
            videoupgradeValue.set(str(0) + " L.E.")
        if account.bellydancer.get() > 0:
            account.add_bellydancers(account.bellydancer.get())
            bellydancersValue.set(str(account.items["belly dancers"])+" L.E.")
        elif account.bellydancer.get() == 0:
            account.remove_bellydancers()
            bellydancersValue.set(str(0) + " L.E.")
        if account.ballerina.get() > 0:
            account.add_ballarena(account.ballerina.get())
            ballerinaValue.set(str(account.items["ballarena"]) + " L.E.")
        elif account.ballerina.get() == 0:
            account.remove_ballarena()
            ballerinaValue.set(str(0) + " L.E.")
        if account.enteranceguestbook.get() > 0:
            account.add_entrance_guestbook(account.enteranceguestbook.get())
            enteranceguestbookValue.set(str(account.items["entrance guestbook"])+" L.E.")
        elif account.ballerina.get() == 0:
            account.remove_entrance_guestbook()
            enteranceguestbookValue.set(str(0) + " L.E.")
        if account.guestbookB.get() > 0:
            account.add_guestbook()
            guestbookValue.set(str(account.items["guestbook"])+" L.E.")
        elif account.guestbookB.get() == 0:
            account.remove_guestbook()
            guestbookValue.set(str(0) + " L.E.")
        if account.decorCorridor.get() > 0:
            account.add_decore_corridoor()
            corridorValue.set(str(account.items["decore corridor"])+" L.E.")
        elif account.decorCorridor.get() == 0:
            account.remove_decore_corridoor()
            corridorValue.set(str(0) + " L.E.")
        if account.hightables.get() > 0:
            account.add_hightables(account.hightables.get())
            hightablesValue.set(str(account.items["hightables"])+" L.E.")
        elif account.hightables.get() == 0:
            account.remove_hightables()
            hightablesValue.set(str(0) + " L.E.")
        if account.laser.get() > 0:
            account.add_show_laser()
            lasershowValue.set(str(account.items["showlaser"])+" L.E.")
        elif account.laser.get() == 0:
            account.remove_show_laser()
            lasershowValue.set(str(0) + " L.E.")
        if account.bubbles.get() > 0:
            account.add_bubbles()
            bubblesValue.set(str(account.items["bubbles"])+" L.E.")
        elif account.bubbles.get() == 0:
            account.remove_bubbled()
            bubblesValue.set(str(0) + " L.E.")
        if account.americancake.get() > 0:
            account.add_american_cake()
            americancakeValue.set(str(account.items["american cake"])+" L.E.")
        elif account.americancake.get() == 0:
            account.remove_american_cake()
            americancakeValue.set(str(0) + " L.E.")
        if account.guestdisplay.get() > 0:
            account.add_guest_display()
            guestdisplayValue.set(str(account.items["Guest Display"])+" L.E.")
        elif account.guestdisplay.get() == 0:
            account.remove_guest_display()
            guestdisplayValue.set(str(0) + " L.E.")
        if account.decorcatwalk.get() > 0:
            account.add_decor_catwalk()
            decorcatwalkValue.set(str(account.items["Decor Catwalk"])+ " L.E.")
        elif account.decorcatwalk.get() == 0:
            account.remove_decor_catwalk()
            decorcatwalkValue.set(str(0) + " L.E.")
        if account.sherbettray.get() > 0:
            account.add_sherbet_tray()
            sherbettrayValue.set(str(account.items["Sherbet Tray"])+ " L.E.")
        elif account.sherbettray.get() == 0:
            account.remove_sherbet_tray()
            sherbettrayValue.set(str(0) + " L.E.")
        if account.chocolatefountain.get() > 0:
            account.add_chocolate_fountain()
            chocolatefountainValue.set(str(account.items["Chocolate Fountain"])+ " L.E.")
        elif account.chocolatefountain.get() == 0:
            account.remove_chocolate_fountain()
            chocolatefountainValue.set(str(0) + " L.E.")
        if account.projector.get() > 0:
            account.add_projector()
            projectorValue.set(str(account.items["Projector"])+ " L.E.")
        elif account.projector.get() == 0:
            account.remove_projector()
            projectorValue.set(str(0) + " L.E.")
        if account.spanishshow.get() > 0:
            account.add_spanish_show()
            spanishshowValue.set(str(account.items["Spanish Show"])+ " L.E.")
        elif account.spanishshow.get() == 0:
            account.remove_spanish_show()
            spanishshowValue.set(str(0) + " L.E.")
        if account.photographyout.get() > 0:
            account.add_premission_outer_photography()
            photographyoutValue.set(str(account.items["premission_outer_photography"]))
        elif account.photographyout.get() == 0:
            account.remove_premission_outer_photography()
            photographyoutValue.set(str(0) + " L.E.")
        if account.photographyin.get() > 0:
            account.add_photoghraphy(account.photographyinvalue.get())
            photographyinValue.set(str(account.items["photograghy"]))
        elif account.photographyin.get() == 0:
            account.remove_photoghraphy()
            photographyinValue.set(str(0) + " L.E.")
        if account.nuts.get() > 0:
            account.add_nuts(account.nutsvalue.get())
            nutsValue.set(str(account.items["Nuts"]))
        elif account.nuts.get() == 0:
            account.remove_nuts()
            nutsValue.set(str(0) + " L.E.")
        if account.mazoon.get() > 0:
            account.add_mazoon(account.mazoonvalue.get())
            mazoonValue.set(str(account.items["Mazoon"]))
        elif account.mazoon.get() == 0:
            account.remove_mazoon()
            mazoonValue.set(str(0) + " L.E.")
        if account.guestphoto.get() > 0:
            account.add_guest_photo(account.guestphoto.get())
            guestphotoValue.set(str(account.items["Guest Photo"]))
        elif account.guestphoto.get() == 0:
            account.remove_guest_photo()
            guestphotoValue.set(str(0) + " L.E.")
        if account.centerpeiceromancy.get() > 0:
            account.add_centerpeice_romancy()
            centerpeiceromancyValue.set(str(account.items["Centerpeice Romancy"])+ " L.E.")
        elif account.centerpeiceromancy.get() == 0:
            account.remove_centerpeice_romancy()
            centerpeiceromancyValue.set(str(0) + " L.E.")
        if account.extradvd.get() > 0:
            account.add_extra_dvd(account.extradvd.get())
            extradvdValue.set(str(account.items["Extra DVD"])+ " L.E.")
        elif account.extradvd.get() == 0:
            account.remove_extra_dvd()
            extradvdValue.set(str(0) + " L.E.")
        if account.extraflash.get() > 0:
            account.add_flash_video(account.extraflash.get())
            extraflashValue.set(str(account.items["Flash Video"])+ " L.E.")
        elif account.extraflash.get() == 0:
            account.remove_flash_video()
            extraflashValue.set(str(0) + " L.E.")
        if account.sound.get() > 0:
            account.add_sound()
            soundValue.set(str(account.items["Sound"]) + " L.E.")
        elif account.sound.get() == 0:
            account.remove_sound()
            soundValue.set(str(0) + " L.E.")
        if account.artistin1 != 0 or account.artistin2 != 0 or account.artistin3 != 0:
            account.update_artist_in(account.artistin1.get(), account.artistin2.get(), account.artistin3.get())
            artistinValue.set(str(account.items["Artists Inner"])+ " L.E.")
        if account.artistout1 != 0 or account.artistout2 != 0 or account.artistin3 != 0:
            account.update_artist_out(account.artistout1.get(), account.artistout2.get(), account.artistout3.get())
            artistoutValue.set(str(account.items["Artists Outter"])+ " L.E.")

        totalValue.set(account.cost)




        self.cost = sum(self.items.values())
        print("=" * 41)
        print("البيانات " + (" " * 20) + "التكلفة")
        print("=" * 41)
        for key in sorted(self.items.keys()):
            before = 31 - len(str(key))
            print(str(key) + (" " * before) + str(self.items[key]))
        print("_" * 41)
        print("الاجمالي " + (" " * 20) + str(self.cost))

    def update_All(self, value):
        count = self.count
        count.set(value)



    def buffet_cost(self):
        # madany type properity
        if self.type.get() == 0 :
            # romancy buffet for 250, less and more
            if  self.buffetvar.get() == "Romancy":
                # romancy buffet for 250 count
                if self.count.get() == 250:
                    self.items['بوفية'] = 68000
                    self.cost = sum(self.items.values())
                    print("بوفية رومانسي")
                    print("مدني")
                    print("العدد " + str(self.count.get()))
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
                # romancy buffet for more, less than 250
                elif self.count.get() > 250 and self.count.get() < 451:
                    rate = 140
                    extra = self.count.get() - 250
                    extra_cost = rate * extra
                    self.items['بوفية'] = 68000 + extra_cost
                    self.cost = sum(self.items.values())
                    print("بوفية رومانسي")
                    print("مدني")
                    print("العدد  " + str(self.count.get()))
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
                # for case out of capacity
                else:
                    print("استيعاب قاعة اخناتون من 250 الي 450")
                    print("تحقق من العدد مرة اخري")
                    self.items['بوفية'] = 0
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
            # ahlam buffet for more, less or 250 count
            elif self.buffetvar.get() == "Ahlam":
                # ahlam for 250 count
                if self.count.get() == 250:
                    self.items['بوفية'] = 72500
                    self.cost = sum(self.items.values())
                    print("بوفية احلام")
                    print("مدني")
                    print("العدد " + str(self.count.get()))
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
                # ahlam for more, less than 250
                elif self.count.get() > 250 and self.count.get() < 451:
                    rate = 160
                    extra = self.count.get() - 250
                    extra_cost = rate * extra
                    self.items['بوفية'] = 72500 + extra_cost
                    self.cost = sum(self.items.values())
                    print("الاحلام")
                    print("مدني")
                    print("العدد " + str(self.count.get()))
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
                # for out of capacity
                else:
                    print("استيعاب قاعة اخناتون من 250 الي 450")
                    print("تحقق من الرقم مرة اخري")
                    self.items['بوفية'] = 0
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
            # omaraa buffet for 250, less and more
            elif self.buffetvar.get() == "Omara":
                # omaraa for 250 count
                if self.count.get() == 250:
                    self.items['بوفية'] = 77000
                    self.cost = sum(self.items.values())
                    print("بوفية الامراء")
                    print("مدني")
                    print("العدد " + str(self.count.get()))
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
                # omaraa for less and more than 250
                elif self.count.get() > 250 and self.count.get() < 451:
                    rate = 180
                    extra = self.count.get() - 250
                    extra_cost = rate * extra
                    self.items['بوفية'] = 77000 + extra_cost
                    self.cost = sum(self.items.values())
                    print("بوفية الامراء")
                    print("مدني ")
                    print("العدد " + str(self.count.get()))
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
                # omara our of capacity
                else:
                    print("استيعاب القاعة من 250 الي 450")
                    print("تحقق من الرقم مرة اخري ")
                    self.items['بوفية'] = 0
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
                    return self.count
        elif self.type.get() == 1:
            if self.buffetvar.get() == "Romancy":
                if self.count.get() == 250:
                    self.items['بوفية'] = 56000
                    self.cost = sum(self.items.values())
                    print("بوفية رومانسي")
                    print("ضابط")
                    print("العدد " + str(self.count.get()))
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
                elif self.count.get() > 250 and self.count.get() < 451:
                    rate = 120
                    extra = self.count.get() - 250
                    extra_cost = rate * extra
                    self.items['بوفية'] = 56000 + extra_cost
                    self.cost = sum(self.items.values())
                    print("your selection on ROMANCY buffet")
                    print("ضابط")
                    print("العدد " + str(self.count.get()))
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
                else:
                    print("استيعاب القاعة من 250 الي 450")
                    print("تحقق من العدد مرة اخري")
                    self.items['بوفية'] = 0
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
            elif self.buffetvar.get() == "Ahlam":
                if self.count.get() == 250:
                    self.items['بوفية'] = 60500
                    self.cost = sum(self.items.values())
                    print("your selection on AHLAM buffet")
                    print("ضابط")
                    print("العدد " + str(self.count.get()))
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
                elif self.count.get() > 250 and self.count.get() < 451:
                    rate = 140
                    extra = self.count.get() - 250
                    extra_cost = rate * extra
                    self.items['بوفية'] = 60500 + extra_cost
                    self.cost = sum(self.items.values())
                    print("your selection on AHLAM buffet")
                    print("ضابط")
                    print("العدد " + str(self.count.get()))
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
                else:
                    print("استيعاب القاعة من 250 الي 450")
                    print("تحقق من العدد مرة اخري")
                    self.items['بوفية'] = 0
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
            elif self.buffetvar.get() == "Omara":
                if self.count.get() == 250:
                    self.items['بوفية'] = 65000
                    self.cost = sum(self.items.values())
                    print("بوفية الامراء")
                    print("ضابط")
                    print("العدد " + str(self.count.get()))
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
                elif self.count.get() > 250 and self.count.get() < 451:
                    rate = 160
                    extra = self.count.get() - 250
                    extra_cost = rate * extra
                    self.items['بوفية'] = 65000 + extra_cost
                    self.cost = sum(self.items.values())
                    print("بوفية الامراء")
                    print("ضابط")
                    print("العدد " + str(self.count.get()))
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")
                else:
                    print("استيعاب القاعة من 250 الي 450")
                    print("تحقق من العدد مرة اخري")
                    self.items['بوفية'] = 0
                    buffetValue.set(str(account.items["بوفية"]) + " L.E.")

    def add_chaircover(self):
        cost = self.count.get() * 10
        self.items["chairs"] = cost
        self.cost = sum(self.items.values())

    def remove_chaircover(self):
        if "chairs" in self.items.keys():
            self.items.pop("chairs")

    def add_vipchairs(self):
        if "chairs" in self.items.keys():
            self.items.pop("chairs")
            cost = self.count.get() * 20
            self.items["VIPchairs"] = cost
            self.cost = sum(self.items.values())
        else:
            cost = self.count.get() * 20
            self.items["VIPchairs"] = cost
            self.cost = sum(self.items.values())

    def remove_Vipchairs(self):
        if "VIPchairs" in self.items.keys():
            self.items.pop("VIPchairs")

    def add_pepsi(self):
        if "open drinks" in self.items.keys():
            self.items.pop("open drinks")
        cost = self.count.get() * 4
        self.items["pepsi"] = cost
        self.cost = sum(self.items.values())

    def remove_pepsi(self):
        if "pepsi" in self.items.keys():
            self.items.pop("pepsi")

    def add_fresh_juice(self):
        cost = self.count.get() * 10
        self.items["fresh juice"] = cost
        self.cost = sum(self.items.values())

    def remove_fresh_juice(self):
        if "fresh juice" in self.items.keys():
            self.items.pop("fresh juice")

    def add_open_drinks(self):
        if "pepsi" in self.items.keys():
            self.items.pop("pepsi")
        cost = self.count.get() * 15
        self.items["open drinks"] = cost
        self.cost = sum(self.items.values())

    def remove_open_drinks(self):
        if "open drinks" in self.items.keys():
            self.items.pop("open drinks")

    def add_showfire(self, category):
        if category == 1:
            cost = 6000
            self.items["showfire"] = cost
            self.cost = sum(self.items.values())
            print("you selected first one 6500")

        elif category == 2:
            cost = 9000
            self.items["showfire"] = cost
            self.cost = sum(self.items.values())
            print("you selected the rock show 9000")

        elif category == 3:
            cost = 11500
            self.items["showfire"] = cost
            self.cost = sum(self.items.values())
            print("you selected dreams show 11500")
        elif category == 0:
            "showfire" in self.items.keys()
            self.items.pop("showfire")
        else:
            print("sorry check your category from 1:3 available only")
            return category

    def remove_showfire(self):
        if "showfire" in self.items.keys():
            self.items.pop("showfire")

    def toggle_ledscreen(self):
        if account.enteranceScreen.get() == 1:
            self.items["انترانس ليد سكرين"] = 3000
            self.cost = sum(self.items.values())
            enteranceledValue.set(str(account.items["انترانس ليد سكرين"])+" L.E.")
        elif account.enteranceScreen.get() == 0:
            if "انترانس ليد سكرين" in self.items.keys():
                self.items.pop("انترانس ليد سكرين")
            enteranceledValue.set(str(0)+" L.E.")


    def toggle_catwalk(self):
        if account.catwalk.get() == 1:
            chkb_decorcatwalk.configure(state=NORMAL)
            self.items["كات ووك"] = 2400
            self.cost = sum(self.items.values())
            catwalkValue.set(str(account.items["كات ووك"])+" L.E.")
        elif account.catwalk.get() == 0:
            self.decorcatwalk.set(0)
            chkb_decorcatwalk.configure(state=DISABLED)
            if "كات ووك" in self.items.keys():
                self.items.pop("كات ووك")
            catwalkValue.set(str(0)+" L.E.")


    def toggle_lounge(self):
        if account.lounge.get() == 1:
            self.items["لاونج جلد"] = 2400
            self.cost = sum(self.items.values())
            loungeValue.set(str(account.items["لاونج جلد"])+" L.E.")
        elif account.lounge.get() == 0:
            if "لاونج جلد" in self.items.keys():
                self.items.pop("لاونج جلد")
            loungeValue.set(str(0)+" L.E.")


    def toggle_2_large_round_table(self):
        if account.largeroundtabled.get() == 1:
            chkb_largeTables_centerPeice.configure(state=NORMAL)
            self.items["2 ترابيزة كبيرة"] = 2000
            self.cost = sum(self.items.values())
            largetablesValue.set(str(account.items["2 ترابيزة كبيرة"])+" L.E.")
        elif account.largeroundtabled.get() == 0:
            self.largeCenterpeice.set(0)
            chkb_largeTables_centerPeice.configure(state=DISABLED)
            if "2 ترابيزة كبيرة" in self.items.keys():
                self.items.pop("2 ترابيزة كبيرة")
            largetablesValue.set(str(0)+" L.E.")

    def toggle_2_large_round_centerpiece(self):
        if account.largeCenterpeice.get() == 1:
            self.items["سنتر بيز راوند تابل"] = 600
            self.cost = sum(self.items.values())
            largetablescenterpeiceValue.set(str(account.items["سنتر بيز راوند تابل"])+" L.E.")
        elif account.largeCenterpeice.get() == 0:
            if "سنتر بيز راوند تابل" in self.items.keys():
                self.items.pop("سنتر بيز راوند تابل")
            largetablescenterpeiceValue.set(str(0)+" L.E.")

    def add_dancefloor(self):
        cost = 3500
        self.items["dancefloor"] = cost
        self.cost = sum(self.items.values())

    def remove_dancefloor(self):
        if "dancefloor" in self.items.keys():
            self.items.pop("dancefloor")

    def add_firworks_on_df(self):
        self.items["4 fireworks on DF"] = 1200
        self.cost = sum(self.items.values())

    def remove_firworks_on_df(self):
        if "4 fireworks on DF" in self.items.keys():
            self.items.pop("4 fireworks on DF")

    def add_firworks_on_cw(self):
        self.items["4 fireworks on CW"] = 1200
        self.cost = sum(self.items.values())

    def remove_firworks_on_cw(self):
        if "4 fireworks on CW" in self.items.keys():
            self.items.pop("4 fireworks on CW")

    def add_firworks_on_cake(self):
        self.items["2 fireworks on cake"] = 600
        self.cost = sum(self.items.values())

    def remove_firworks_on_cake(self):
        if "2 fireworks on cake" in self.items.keys():
            self.items.pop("2 fireworks on cake")

    def add_photo_clip(self):
        print("send your photos before 7 days of your wedding day.")
        self.items["photoclip"] = 300
        self.cost = sum(self.items.values())

    def remove_photo_clip(self):
        if "photoclip" in self.items.keys():
            self.items.pop("photoclip")

    def add_fullHD(self):
        if "4k" in self.items.keys():
            self.items.pop("4k")
        cost = 10000
        self.items["fullHD"] = cost
        self.cost = sum(self.items.values())

    def remove_fullHD(self):
        if "fullHD" in self.items.keys():
            self.items.pop("fullHD")

    def add_4k(self):
        if "fullHD" in self.items.keys():
            self.items.pop("fullHD")
        cost = 15000
        self.items["4k"] = cost
        self.cost = sum(self.items.values())

    def remove_4k(self):
        if "4k" in self.items.keys():
            self.items.pop("4k")

    def update_count(self, value):
        count = self.count
        count.set(value)
        countValue.set(self.count.get())
        print(count.get())
        return count.get()

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
        temp = self.add_drinks.get()
        if temp == 1:
            spinbox_drinks.configure(state=NORMAL)
            spinbox_drinks.configure(state="readonly")
        elif temp == 0:
            self.drinksvar.set("")
            drinks.set(0)
            spinbox_drinks.configure(state=DISABLED)

    def update_dancefloor(self, value):
        temp = self.dancefloor.get()
        fourfire = self.fourfiresondance
        if temp == 1:
            chkb_fireondance.configure(state=NORMAL)
        elif temp == 0:
            fourfire.set(0)
            chkb_fireondance.configure(state=DISABLED)

    def add_bellydancers(self, count):
        cost = (count /2)* 850
        self.items["belly dancers"] = cost
        self.cost = sum(self.items.values())

    def remove_bellydancers(self):
        if "belly dancer" in self.items.keys():
            self.items.pop("belly dancer")

    def add_ballarena(self, count):
        if count == 6:
            cost = 1000
            self.items["ballarena"] = cost
            self.cost = sum(self.items.values())
        elif count == 8:
            cost = 1200
            self.items["ballarena"] = cost
            self.cost = sum(self.items.values())
        else:
            print("sorry you can request 6 or 8 girls only")

    def remove_ballarena(self):
        if "ballarena" in self.items.keys():
            self.items.pop("ballarena")

    def update_GuestbookB(self):
        temp = self.enteranceguestbook.get()
        tempBook = self.guestbookB
        if temp > 0:
            chkb_Guestbook_book.configure(state=NORMAL)
        elif temp == 0:
            tempBook.set(0)
            chkb_Guestbook_book.configure(state=DISABLED)

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

    def update_videoQuality(self, value):
        video = self.video
        videovar = self.videovar.get()
        if videovar == "Full HD":
            video.set(1)
            print(video.get())
            return video.get()
        elif videovar == "4K":
            video.set(2)
            print(video.get())
            return video.get()
        else:
            video.set(0)
            print(video.get())

    def add_entrance_guestbook(self, cost):
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

    def add_decore_corridoor(self):
        cost = 2500
        self.items["decore corridor"] = cost
        self.cost = sum(self.items.values())

    def remove_decore_corridoor(self):
        if "decore corridor" in self.items.keys():
            self.items.pop("decore corridor")

    def add_hightables(self, count_to_add):
        if count_to_add <= 8:
            cost = (count_to_add * 150)
            self.items["hightables"] = cost
            self.cost = sum(self.items.values())

        else:
            print("sorry max number of tables to add is 8")
            return count_to_add

    def remove_hightables(self):
        if "hightables" in self.items.keys():
            self.items.pop("hightables")

    def add_bubbles(self):
        self.items["bubbles"] = 350
        self.cost = sum(self.items.values())

    def remove_bubbled(self):
        if "bubbles" in self.items.keys():
            self.items.pop("bubbles")

    def add_show_laser(self):
        self.items["showlaser"] = 2500
        self.cost = sum(self.items.values())

    def remove_show_laser(self):
        if "showlaser" in self.items.keys():
            self.items.pop("showlaser")

    def add_american_cake(self):
        cost = 500
        self.items["american cake"] = cost
        self.cost = sum(self.items.values())

    def remove_american_cake(self):
        if "american cake" in self.items.keys():
            self.items.pop("american cake")

    def add_guest_display(self):
        cost = 800
        self.items["Guest Display"] = cost
        self.cost = sum(self.items.values())

    def remove_guest_display(self):
        if "Guest Display" in self.items.keys():
            self.items.pop("Guest Display")

    def add_decor_catwalk(self):
        cost = 1000
        self.items["Decor Catwalk"] = cost
        self.cost = sum(self.items.values())

    def remove_decor_catwalk(self):
        if "Decor Catwalk" in self.items.keys():
            self.items.pop("Decor Catwalk")

    def add_sherbet_tray(self):
        cost = 150
        self.items["Sherbet Tray"] = cost
        self.cost = sum(self.items.values())

    def remove_sherbet_tray(self):
        if "Sherbet Tray" in self.items.keys():
            self.items.pop("Sherbet Tray")


    def add_chocolate_fountain(self):
        cost = 1500
        self.items["Chocolate Fountain"] = cost
        self.cost = sum(self.items.values())


    def remove_chocolate_fountain(self):
        if "Chocolate Fountain" in self.items.keys():
            self.items.pop("Chocolate Fountain")

    def add_projector(self):
        cost = 600
        self.items["Projector"] = cost
        self.cost = sum(self.items.values())

    def remove_projector(self):
        if "Projector" in self.items.keys():
            self.items.pop("Projector")

    def add_spanish_show(self):
        cost = 3000
        self.items["Spanish Show"] = cost
        self.cost = sum(self.items.values())

    def remove_spanish_show(self):
        if "Spanish Show" in self.items.keys():
            self.items.pop("Spanish Show")

    def add_photoghraphy(self, cost_to_add):
        self.items["photograghy"] = cost_to_add
        self.cost = sum(self.items.values())

    def remove_photoghraphy(self):
        if "photograghy"in self.items.keys():
            self.items.pop("photograghy")

    def add_premission_outer_photography(self):
        if self.type.get() == 0:
            cost = 2000
            self.items["premission_outer_photography"] = cost
            self.cost = sum(self.items.values())
        elif self.type.get() == 1:
            cost = 1000
            self.items["premission_outer_photography"] = cost
            self.cost = sum(self.items.values())
        else:
            print("check your ballroom_type madany or office no more choices")

    def remove_premission_outer_photography(self):
        if "premission outer photography" in self.items.keys():
            self.items.pop("premission outer photography")

    def update_photography_in(self, value):
        temp = self.photographyin.get()
        photoin = self.photographyout
        if temp == 1:
            photoin.set(0)
            chkb_photographyOut.configure(state=DISABLED)
        elif temp == 0:
            self.photographyinvalue.set(0)
            photographyinValue.set(str(0) + " L.E.")
            chkb_photographyOut.configure(state=NORMAL)

    def update_nuts(self, value):
        temp = self.nuts.get()
        nutsentry = self.nutsvalue
        if temp == 0:
            nutsentry.set(0)
            entry_nuts.configure(state=DISABLED)
        elif temp == 1:
            entry_nuts.configure(state=NORMAL)
            nutsentry.set(0)

    def add_nuts(self, count):
        cost = count * 25
        self.items["Nuts"] = cost
        self.cost = sum(self.items.values())

    def remove_nuts(self):
        if "Nuts" in self.items.keys():
            self.items.pop("Nuts")

    def update_mazoon(self, value):
        temp = self.mazoon.get()
        mazoonentry = self.mazoonvalue
        if temp == 0:
            mazoonentry.set(0)
            entry_mazoon.configure(state=DISABLED)
        elif temp == 1:
            entry_mazoon.configure(state=NORMAL)
            mazoonentry.set(0)

    def add_mazoon(self, value):
        if value <= 10000:
            cost = 600
            self.items["Mazoon"] = cost
            self.cost = sum(self.items.values())
        elif value <= 15000:
            cost = 750
            self.items["Mazoon"] = cost
            self.cost = sum(self.items.values())
        elif value <= 20000:
            cost = 900
            self.items["Mazoon"] = cost
            self.cost = sum(self.items.values())
        elif value <= 25000:
            cost = 950
            self.items["Mazoon"] = cost
            self.cost = sum(self.items.values())
        elif value <= 30000:
            cost = 1100
            self.items["Mazoon"] = cost
            self.cost = sum(self.items.values())
        elif value <= 40000:
            cost = 1350
            self.items["Mazoon"] = cost
            self.cost = sum(self.items.values())
        elif value <= 45000:
            cost = 1450
            self.items["Mazoon"] = cost
            self.cost = sum(self.items.values())
        elif value <= 50000:
            cost = 1700
            self.items["Mazoon"] = cost
            self.cost = sum(self.items.values())
        else:
            cost = int(((value*3.5)/100)) + 100
            self.items["Mazoon"] = cost
            self.cost = sum(self.items.values())

    def add_guest_photo(self, value):
        self.items["Guest Photo"] = value
        self.cost = sum(self.items.values())


    def remove_guest_photo(self):
        if "Guest Photo" in self.items.keys():
            self.items.pop("Guest Photo")

    def remove_mazoon(self):
        if "Mazoon" in self.items.keys():
            self.items.pop("Mazoon")

    def add_centerpeice_romancy(self):
        cost = 1500
        self.items["Centerpeice Romancy"] = cost
        self.cost = sum(self.items.values())

    def remove_centerpeice_romancy(self):
        if "Centerpeice Romancy" in self.items.keys():
            self.items.pop("Centerpeice Romancy")

    def add_extra_dvd(self, count):
        cost = count * 40
        self.items["Extra DVD"] = cost
        self.cost = sum(self.items.values())

    def remove_extra_dvd(self):
        if "Extra DVD" in self.items.keys():
            self.items.pop("Extra DVD")


    def add_flash_video(self, count):
        cost = count * 250
        self.items["Flash Video"] = cost
        self.cost = sum(self.items.values())

    def remove_flash_video(self):
        if "Flash Video" in self.items.keys():
            self.items.pop("Flash Video")

    def add_sound(self):
        cost = 1000
        self.items["Sound"] = cost
        self.cost = sum(self.items.values())

    def remove_sound(self):
        if "Sound" in self.items.keys():
            self.items.pop("Sound")

    def update_artist_in(self, value1, value2, value3):
        cost = value1 + value2 + value3
        self.items["Artists Inner"] = cost
        self.cost = sum(self.items.values())

    def update_artist_out(self, value1, value2, value3):
        cost = int(((value1 + value2 + value3) * 20)/100)
        self.items["Artists Outter"] = cost
        self.cost = sum(self.items.values())

account = obj_ekhnaton()

#================Variables=============================

countValue = IntVar()
buffetValue = IntVar()
chairsValue = IntVar()
drinksValue = IntVar()
showfireValue = IntVar()
enteranceledValue = IntVar()
catwalkValue = IntVar()
loungeValue = IntVar()
largetablesValue = IntVar()
largetablescenterpeiceValue = IntVar()
dancefloorValue = IntVar()
fireondancefloorValue = IntVar()
fireoncatwalkValue = IntVar()
fireoncakeValue = IntVar()
photoclipValue = IntVar()
videoupgradeValue = IntVar()
ballerinaValue = IntVar()
bellydancersValue = IntVar()
enteranceguestbookValue = IntVar()
guestbookValue = IntVar()
corridorValue = IntVar()
hightablesValue = IntVar()
lasershowValue = IntVar()
bubblesValue = IntVar()
americancakeValue = IntVar()
guestdisplayValue = IntVar()
decorcatwalkValue = IntVar()
sherbettrayValue = IntVar()
chocolatefountainValue = IntVar()
projectorValue = IntVar()
spanishshowValue = IntVar()
photographyoutValue = IntVar()
photographyinValue = IntVar()
nutsValue = IntVar()
mazoonValue = IntVar()
guestphotoValue = IntVar()
centerpeiceromancyValue = IntVar()
extradvdValue = IntVar()
extraflashValue = IntVar()
soundValue = IntVar()
artistinValue = IntVar()
artistoutValue = IntVar()
totalValue = StringVar()

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
tabs.grid(column=0, row=1, columnspan=55, rowspan=55, sticky="NESW")

ekhnaton_frame = ttk.Frame(tabs)
ekhnaton_frame.grid()
isis_frame = ttk.Frame(tabs)
isis_frame.grid()
louts_frame = ttk.Frame(tabs)
louts_frame.grid()

labelframe1 = ttk.LabelFrame(ekhnaton_frame, text="hi")
labelframe1.grid(row=25,column=6)

localtime = time.asctime(time.localtime(time.time()))
time_info = ttk.Label(root,font=('arial', 10, 'bold'), text=localtime, anchor='w')
time_info.grid(row=1, column=44)

#==========================Row 3=====================================================

lblCount = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Count:", anchor='w')
lblCount.grid(row=3,column=2, padx=5, pady=5)
entry_count = Entry(ekhnaton_frame,width=19, font=('arial', 10, 'bold'),textvariable= account.count,bg="white", justify="center")
entry_count.grid(row=3,column=3,columnspan=1)
entry_count.focus()
lblCountValue = ttk.Label(ekhnaton_frame,textvariable=countValue, font=('arial', 10, 'bold'),foreground="red", text="Count:", anchor='w')
lblCountValue.grid(row=3,column=4, padx=5, pady=5)


lblbuffet = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Buffet:", anchor='w')
lblbuffet.grid(row=3,column=5)
spinbox_buffet = Spinbox(ekhnaton_frame,from_=1,to=3,textvariable=account.buffetvar,font=('arial', 10, 'bold'),width=10, foreground="blue", values=("Romancy","Ahlam","Omara"), justify="center", state="readonly", command=lambda: account.buffet_cost())
spinbox_buffet.grid(row=3,column=6,columnspan=1)
spinbox_buffet.configure(state="readonly")
spinbox_buffet.tk_focusNext()
lblbuffetValue = ttk.Label(ekhnaton_frame,textvariable=buffetValue, font=('arial', 10, 'bold'),foreground="red", anchor='w', justify="right")
lblbuffetValue.grid(row=3,column=7, pady=5)


chkb_officer = Checkbutton(ekhnaton_frame,text="Officer",variable=account.type,font=('arial', 10, 'bold'),width=8, onvalue= 1,offvalue=0, justify="left", command=lambda: account.buffet_cost())
chkb_officer.grid(row=3,column=8, columnspan=1, sticky="w")


#=======================================Row 4=========================================

lblChairs = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Chairs:", anchor='w')
lblChairs.grid(row=4,column=2, padx=5, pady=5)
account.update_chairs(1)
spinbox_chairs = Spinbox(ekhnaton_frame,from_=1,to=2 ,textvariable=account.chairsvar,font=('arial', 10, 'bold'), foreground="blue", values=("Covers", "VIP chairs"), justify="center", state="readonly", command=lambda: account.update_chairs(account.chairs.get()))
spinbox_chairs.grid(row=4,column=3,columnspan=1)
spinbox_chairs.configure(state="readonly")
lblChairsValue = ttk.Label(ekhnaton_frame,textvariable=chairsValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblChairsValue.grid(row=4,column=4, padx=5, pady=5)



chkb_drinks = Checkbutton(ekhnaton_frame, text="Add Drinks:",variable=account.add_drinks,font=('arial', 10, 'bold'), width=15, onvalue= 1, offvalue=0, justify="center", command=lambda: account.reset_drinks())
chkb_drinks.grid(row=4,column=5)
chkb_drinks.select()
spinbox_drinks = Spinbox(ekhnaton_frame,from_=0,to=3 ,textvariable=account.drinksvar,font=('arial', 10, 'bold'), foreground="blue",background="#eff0f1", values=("","Pepsi","Fresh Drinks", "Open Buffet"), justify="center", state="readonly", command= lambda: account.update_drinks(account.drinks.get()))
spinbox_drinks.grid(row=4,column=6,columnspan=1)
spinbox_drinks.configure(state="readonly")
lbldrinksValue = ttk.Label(ekhnaton_frame,textvariable=drinksValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lbldrinksValue.grid(row=4,column=7, padx=5, pady=5)

#======================================Row 5============================================

lblShowfire = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="ShowFire:", anchor='w')
lblShowfire.grid(row=5,column=2, padx=5, pady=5)
spinbox_showfire = Spinbox(ekhnaton_frame,from_=0,to=3 ,textvariable=account.showfirevar,font=('arial', 10, 'bold'), foreground="blue", values=("","Normal","The Rock", "Dreams"), justify="center", state="readonly", command=lambda :account.update_showfire(account.showfire.get()))
spinbox_showfire.grid(row=5,column=3,columnspan=1)
spinbox_showfire.configure(state="readonly")
lblshowfireValue = ttk.Label(ekhnaton_frame,textvariable=showfireValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblshowfireValue.grid(row=5,column=4, padx=5, pady=5)

lblSpecial_Entrance = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Special Entrance:", anchor='w')
lblSpecial_Entrance.grid(row=5,column=5,columnspan=1, pady=5)
chkb_Entrence_led = Checkbutton(ekhnaton_frame, text="Entrance Screen",variable=account.enteranceScreen,font=('arial', 9, 'bold'), width=12, onvalue= 1, offvalue=0, justify="left",command=lambda :account.toggle_ledscreen())
chkb_Entrence_led.grid(row=5,column=6, sticky="we")
lblEntrence_ledValue = ttk.Label(ekhnaton_frame,textvariable=enteranceledValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblEntrence_ledValue.grid(row=5,column=7, padx=5, pady=5)


#====================================Row 6 ===============================


lbllarge_tables = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Additions:", anchor='w')
lbllarge_tables.grid(row=6,column=2, padx=5, pady=5)
chkb_largeTables = Checkbutton(ekhnaton_frame, text="2 Large VIP Tables",variable=account.largeroundtabled,font=('arial', 10, 'bold'), width=16, onvalue= 1, offvalue=0, justify="right",command=lambda: account.toggle_2_large_round_table())
chkb_largeTables.grid(row=6,column=3, columnspan=1)
lbllarge_tablesValue = ttk.Label(ekhnaton_frame,textvariable=largetablesValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lbllarge_tablesValue.grid(row=6,column=4)



chkb_Catwalk = Checkbutton(ekhnaton_frame, text="Cat Walk",variable=account.catwalk,font=('arial', 9, 'bold'), width=6, onvalue= 1, offvalue=0, justify="left",command=lambda: account.toggle_catwalk())
chkb_Catwalk.grid(row=6,column=6, columnspan=1, sticky="we")
lblCatwalkValue = ttk.Label(ekhnaton_frame,textvariable=catwalkValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblCatwalkValue.grid(row=6,column=7, padx=5, pady=5)


#=====================================Row 7 ============================


chkb_largeTables_centerPeice = Checkbutton(ekhnaton_frame, text="With CenterPeice",variable=account.largeCenterpeice,state=DISABLED,font=('arial', 10, 'bold'), width=15, onvalue= 1, offvalue=0, justify="right", anchor="w",command=lambda :account.toggle_2_large_round_centerpiece())
chkb_largeTables_centerPeice.grid(row=7,column=3,columnspan=1)
lbllargeTables_centerPeiceValue = ttk.Label(ekhnaton_frame,textvariable=largetablescenterpeiceValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lbllargeTables_centerPeiceValue.grid(row=7,column=4)

chkb_lounge = Checkbutton(ekhnaton_frame, text="Lounge",variable=account.lounge,font=('arial', 10, 'bold'), onvalue= 1, offvalue=0, justify="left",command=lambda :account.toggle_lounge())
chkb_lounge.grid(row=7,column=6, sticky="we")
lblloungeValue = ttk.Label(ekhnaton_frame,textvariable=loungeValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblloungeValue.grid(row=7,column=7, padx=5, pady=5)


tabs.add(ekhnaton_frame, text="Ekhnaton")
tabs.add(isis_frame, text="Isis")
tabs.add(louts_frame, text="Louts")

#==================================== Row 8 =================================


chkb_DanceFloor = Checkbutton(ekhnaton_frame, text="Dance Floor",variable=account.dancefloor,font=('arial', 10, 'bold'), width=11, onvalue= 1, offvalue=0, justify="left",command=lambda: account.update_dancefloor(account.dancefloor.get()))
chkb_DanceFloor.grid(row=8,column=3, columnspan=1, sticky="w")
lbldancefloorValue = ttk.Label(ekhnaton_frame,textvariable=dancefloorValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lbldancefloorValue.grid(row=8,column=4, padx=5, pady=5)

lblZaffaAddition = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Zaffa Addition:", anchor='w')
lblZaffaAddition.grid(row=8,column=5, columnspan=2)

#============================Row 9 =========================================

lblFireworks = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Fireworks:", anchor='w')
lblFireworks.grid(row=9,column=2, pady=5)
chkb_fireondance = Checkbutton(ekhnaton_frame, text="4 fires on Dance",variable=account.fourfiresondance,state=DISABLED,font=('arial', 10, 'bold'), width=12, onvalue= 1, offvalue=0, justify="left")
chkb_fireondance.grid(row=9,column=3, columnspan=1,padx=7, sticky="w")
lblfireondancefloorValue = ttk.Label(ekhnaton_frame,textvariable=fireondancefloorValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblfireondancefloorValue.grid(row=9,column=4, padx=5, pady=5)

lblBelly_dancers = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Belly Dancers:", anchor='w')
lblBelly_dancers.grid(row=9,column=6, pady=5)
spinboxBelly_dancers = Spinbox(ekhnaton_frame,from_=0,to=3 ,textvariable=account.bellydancer,font=('arial', 10, 'bold'), foreground="blue", values=(0 ,2 ,4 ,6), justify="center", state="readonly")
spinboxBelly_dancers.grid(row=9,column=7,columnspan=1)
spinboxBelly_dancers.configure(state="readonly")
lblbellydancersValue = ttk.Label(ekhnaton_frame,textvariable=bellydancersValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblbellydancersValue.grid(row=9,column=8, padx=5, pady=5)

#===============================Row 10 =================================================

chkb_fireoncatwalk = Checkbutton(ekhnaton_frame, text="4 fires on Catwalk",variable=account.fourfireoncatwalk,font=('arial', 10, 'bold'), width=13, onvalue= 1, offvalue=0, justify="left")
chkb_fireoncatwalk.grid(row=10,column=3, columnspan=1,padx=8, sticky="w")
lblfireoncatwalkValue = ttk.Label(ekhnaton_frame,textvariable=fireoncatwalkValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblfireoncatwalkValue.grid(row=10,column=4, padx=5, pady=5)

lblBallerina = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Ballet Dancers:", anchor='w')
lblBallerina.grid(row=10,column=6, pady=5)
spinboxBallerina = Spinbox(ekhnaton_frame,from_=0,to=2 ,textvariable=account.ballerina,font=('arial', 10, 'bold'), foreground="blue", values=(0 ,6 ,8), justify="center", state="readonly")
spinboxBallerina.grid(row=10,column=7,columnspan=1)
spinboxBallerina.configure(state="readonly")
lblballerinaValue = ttk.Label(ekhnaton_frame,textvariable=ballerinaValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblballerinaValue.grid(row=10,column=8, padx=5, pady=5)

#=================================== Row 11 ================================================

chkb_fireoncake = Checkbutton(ekhnaton_frame, text="2 fires on Cake",variable=account.twofiresoncake,font=('arial', 10, 'bold'), width=13, onvalue= 1, offvalue=0, justify="left")
chkb_fireoncake.grid(row=11,column=3, columnspan=1, sticky="w")
lblfireoncakeValue = ttk.Label(ekhnaton_frame,textvariable=fireoncakeValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblfireoncakeValue.grid(row=11,column=4, padx=5, pady=5)

lblmoredecoration = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Outside Decoration:", anchor='w')
lblmoredecoration.grid(row=11,column=5, columnspan=2)

#====================================Row 12 =========================================

lblVideo_addition = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Video Addition:", anchor='w')
lblVideo_addition.grid(row=12,column=2, padx=7)
chkb_Photo_Clip = Checkbutton(ekhnaton_frame, text="Photo Clip",variable= account.photclip,font=('arial', 10, 'bold'), width=10, onvalue= 1, offvalue=0, justify="left")
chkb_Photo_Clip.grid(row=12,column=3, columnspan=1, sticky="w")
lblphotoclipValue = ttk.Label(ekhnaton_frame,textvariable=photoclipValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblphotoclipValue.grid(row=12,column=4, padx=5, pady=5)

lblEntrance_gestbook = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Entrance Guest Book:", anchor='w')
lblEntrance_gestbook.grid(row=12,column=6, pady=5)
spinbox_guestboot = Spinbox(ekhnaton_frame,from_=0,to=7 ,textvariable=account.enteranceguestbook,font=('arial', 10, 'bold'), foreground="blue", values=(0 ,400 ,450 ,600 ,650 ,700, 900, 1000), justify="center", state="readonly", command=lambda: account.update_GuestbookB())
spinbox_guestboot.grid(row=12,column=7,columnspan=1, padx=10)
spinbox_guestboot.configure(state="readonly")
lblenteranceguestbookValue = ttk.Label(ekhnaton_frame,textvariable=enteranceguestbookValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblenteranceguestbookValue.grid(row=12,column=8, padx=5, pady=5)

#=====================================Row 13 ==============================================

lblVideo_Upgrade = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Video Upgrade:", anchor='w')
lblVideo_Upgrade.grid(row=13,column=2, pady=5)
spinboxVideo_Upgrade = Spinbox(ekhnaton_frame,from_=0,to=2 ,textvariable=account.videovar,font=('arial', 10, 'bold'), foreground="blue", values=("" ,"Full HD" ,"4K"), justify="center", state="readonly", command=lambda: account.update_videoQuality(account.videovar.get()))
spinboxVideo_Upgrade.grid(row=13,column=3,columnspan=1)
spinboxVideo_Upgrade.configure(state="readonly")
lblVideo_UpgradeValue = ttk.Label(ekhnaton_frame,textvariable=videoupgradeValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblVideo_UpgradeValue.grid(row=13,column=4, padx=5, pady=5)


chkb_Guestbook_book = Checkbutton(ekhnaton_frame, text="With Guest Book",state=DISABLED,variable=account.guestbookB,font=('arial', 10, 'bold'), width=15, onvalue= 1, offvalue=0, justify="right", anchor="w")
chkb_Guestbook_book.grid(row=13,column=6, columnspan=2)
lblguestbookValue = ttk.Label(ekhnaton_frame,textvariable=guestbookValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblguestbookValue.grid(row=13,column=8, padx=5, pady=5)

#====================================== Row 14 =================================================

lblHigh_Tables = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="High Tables:", anchor='w')
lblHigh_Tables.grid(row=14,column=2, padx=10, pady=5)
spinbox_Hightables = Spinbox(ekhnaton_frame,from_=0,to=4 ,textvariable=account.hightables,font=('arial', 10, 'bold'), foreground="blue", values=(0 ,2 ,4 ,6 ,8), justify="center")
spinbox_Hightables.grid(row=14,column=3,columnspan=1)
spinbox_Hightables.configure(state="readonly")
lblHightablesValue = ttk.Label(ekhnaton_frame,textvariable=hightablesValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblHightablesValue.grid(row=14,column=4, padx=5, pady=5)

chkb_corridor = Checkbutton(ekhnaton_frame, text="Decor Corridor",variable=account.decorCorridor,font=('arial', 10, 'bold'), width=11, onvalue= 1, offvalue=0, justify="right", anchor="w")
chkb_corridor.grid(row=14,column=7, columnspan=1, sticky="w")
lblcorridorValue = ttk.Label(ekhnaton_frame,textvariable=corridorValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblcorridorValue.grid(row=14,column=8, padx=5, pady=5)

#=====================================Row 15==========================================

lblOthers = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Others:", anchor='w')
lblOthers.grid(row=15,column=2, padx=10, pady=5)

#==================================== Row 16 ======================================

chkb_Laser_show = Checkbutton(ekhnaton_frame, text="Laser_show",variable=account.laser,font=('arial', 10, 'bold'), width=11, onvalue= 1, offvalue=0, justify="left")
chkb_Laser_show.grid(row=16,column=3, columnspan=1, sticky="w")
lbllasershowValue = ttk.Label(ekhnaton_frame,textvariable=lasershowValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lbllasershowValue.grid(row=16,column=4, padx=5, pady=5)


chkb_guestbookdisplay = Checkbutton(ekhnaton_frame, text="Guest Display",variable=account.guestdisplay,font=('arial', 10, 'bold'), width=11, onvalue= 1, offvalue=0, justify="left")
chkb_guestbookdisplay.grid(row=16,column=5, columnspan=1, sticky="w")
lblguestbookdisplayValue = ttk.Label(ekhnaton_frame,textvariable=guestdisplayValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblguestbookdisplayValue.grid(row=16,column=6, padx=5, pady=5)


chkb_chocolatefountain = Checkbutton(ekhnaton_frame, text="Chocolate Fountain",variable=account.chocolatefountain,font=('arial', 10, 'bold'), onvalue= 1, offvalue=0, justify="left")
chkb_chocolatefountain.grid(row=16,column=7, columnspan=1, sticky="w")
lblchocolatefountainValue = ttk.Label(ekhnaton_frame,textvariable=chocolatefountainValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblchocolatefountainValue.grid(row=16,column=8, padx=5, pady=5)



#===================================== Row 17 ====================================

chkb_Bubbles = Checkbutton(ekhnaton_frame, text="Bubbles",variable=account.bubbles,font=('arial', 10, 'bold'), width=8, onvalue= 1, offvalue=0, justify="left")
chkb_Bubbles.grid(row=17,column=3, columnspan=1, sticky="w")
lblbubblesValue = ttk.Label(ekhnaton_frame,textvariable=bubblesValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblbubblesValue.grid(row=17,column=4, padx=5, pady=5)


chkb_decorcatwalk = Checkbutton(ekhnaton_frame, text="Decor Catwalk",variable=account.decorcatwalk,state=DISABLED,font=('arial', 10, 'bold'), width=11, onvalue= 1, offvalue=0, justify="left", anchor="w")
chkb_decorcatwalk.grid(row=17,column=5, columnspan=1, sticky="w")
lbldecorcatwalkValue = ttk.Label(ekhnaton_frame,textvariable=decorcatwalkValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lbldecorcatwalkValue.grid(row=17,column=6, padx=5, pady=5)


chkb_projector = Checkbutton(ekhnaton_frame, text="Projector",variable=account.projector,font=('arial', 10, 'bold'), onvalue= 1, offvalue=0, justify="left")
chkb_projector.grid(row=17,column=7, columnspan=1, sticky="w")
lblprojectorValue = ttk.Label(ekhnaton_frame,textvariable=projectorValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblprojectorValue.grid(row=17,column=8, padx=5, pady=5)


#===================================== Row 18 ====================================

chkb_American_Cake = Checkbutton(ekhnaton_frame, text="American Cake",variable=account.americancake,font=('arial', 10, 'bold'), width=14, onvalue= 1, offvalue=0, justify="left")
chkb_American_Cake.grid(row=18,column=3, columnspan=1, sticky="w")
lblamericancakeValue = ttk.Label(ekhnaton_frame,textvariable=americancakeValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblamericancakeValue.grid(row=18,column=4, padx=5, pady=5)


chkb_sherbettray = Checkbutton(ekhnaton_frame, text="Sherbet's Tray",variable=account.sherbettray,font=('arial', 10, 'bold'), width=11, onvalue= 1, offvalue=0, justify="left", anchor="w")
chkb_sherbettray.grid(row=18,column=5, columnspan=1, sticky="w")
lblsherbettrayValue = ttk.Label(ekhnaton_frame,textvariable=sherbettrayValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblsherbettrayValue.grid(row=18,column=6, padx=5, pady=5)


chkb_spanishshow = Checkbutton(ekhnaton_frame, text="Spanish Show",variable=account.spanishshow,font=('arial', 10, 'bold'), onvalue= 1, offvalue=0, justify="left")
chkb_spanishshow.grid(row=18,column=7, columnspan=1, sticky="w")
lblspanishshowValue = ttk.Label(ekhnaton_frame,textvariable=spanishshowValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblspanishshowValue.grid(row=18,column=8, padx=5, pady=5)

#===================================== Row 19 ====================================

lblphotography = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Photography:", anchor='w')
lblphotography.grid(row=19,column=1,columnspan=2, pady=5)
chkb_photographyOut = Checkbutton(ekhnaton_frame, text=" Out ",variable=account.photographyout,font=('arial', 10, 'bold'), onvalue= 1, offvalue=0, justify="left",anchor="w")
chkb_photographyOut.grid(row=19,column=3, columnspan=1,padx=5, sticky="w")
lblphotographyOutValue = ttk.Label(ekhnaton_frame,textvariable=photographyoutValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblphotographyOutValue.grid(row=19,column=4, padx=5, pady=5)

chkb_nuts = Checkbutton(ekhnaton_frame, text=" Nuts ",variable=account.nuts,font=('arial', 10, 'bold'), onvalue= 1, offvalue=0, justify="left",anchor="w",command=lambda :account.update_nuts(account.nuts.get()))
chkb_nuts.grid(row=19,column=5, columnspan=1, sticky="w")

chkb_mazoon = Checkbutton(ekhnaton_frame, text=" Ma'zoon ",variable=account.mazoon,font=('arial', 10, 'bold'), onvalue= 1, offvalue=0, justify="left",anchor="w",command=lambda :account.update_mazoon(account.mazoon.get()))
chkb_mazoon.grid(row=19,column=7, columnspan=1, sticky="w")

#===================================== Row 20 ====================================

chkb_photographyin = Checkbutton(ekhnaton_frame, text=" In ",variable=account.photographyin,font=('arial', 10, 'bold'), onvalue= 1, offvalue=0, justify="left",anchor="e", command=lambda: account.update_photography_in(account.photographyin.get()))
chkb_photographyin.grid(row=20,column=2, columnspan=1,padx=5, sticky="e")
entry_photography = Entry(ekhnaton_frame,width=19, font=('arial', 10, 'bold'),textvariable= account.photographyinvalue,bg="white", justify="center")
entry_photography.grid(row=20,column=3,columnspan=1)
lblphotographyinValue = ttk.Label(ekhnaton_frame,textvariable=photographyinValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblphotographyinValue.grid(row=20,column=4, padx=5, pady=5)

entry_nuts = Entry(ekhnaton_frame,width=19, font=('arial', 10, 'bold'),textvariable= account.nutsvalue,bg="white", justify="center")
entry_nuts.grid(row=20,column=5,columnspan=1,padx=10)
lblnutsValue = ttk.Label(ekhnaton_frame,textvariable=nutsValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblnutsValue.grid(row=20,column=6, padx=5, pady=5)

entry_mazoon = Entry(ekhnaton_frame,width=19, font=('arial', 10, 'bold'),textvariable= account.mazoonvalue,bg="white", justify="center")
entry_mazoon.grid(row=20,column=7,columnspan=1,padx=10)
lblmazoonValue = ttk.Label(ekhnaton_frame,textvariable=mazoonValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblmazoonValue.grid(row=20,column=8, padx=5, pady=5)

#========================================= Row 21 ===================================

lblguestphoto = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Guest Photo:", anchor='w')
lblguestphoto.grid(row=21,column=1,columnspan=2, pady=5)
spinboxguestphoto = Spinbox(ekhnaton_frame,from_=0,to=2 ,textvariable=account.guestphoto,font=('arial', 10, 'bold'), foreground="blue", values=(0 ,1950 ,3500), justify="center", state="readonly")
spinboxguestphoto.grid(row=21,column=3,columnspan=1)
spinboxguestphoto.configure(state="readonly")
lblguestphotoValue = ttk.Label(ekhnaton_frame,textvariable=guestphotoValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblguestphotoValue.grid(row=21,column=4, padx=5, pady=5)

lblExtraflash = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Extra Flash:", anchor='w')
lblExtraflash.grid(row=21,column=5,columnspan=1, pady=5, sticky="w")


chkb_centerpeiceromancy = Checkbutton(ekhnaton_frame, text="Centerpeice Romancy",variable=account.centerpeiceromancy,font=('arial', 10, 'bold'), onvalue= 1, offvalue=0, justify="left",anchor="w", command=lambda: account.update_photography_in(account.photographyin.get()))
chkb_centerpeiceromancy.grid(row=21,column=7, columnspan=1, sticky="w")
lblcenterpeiceromancyValue = ttk.Label(ekhnaton_frame,textvariable=centerpeiceromancyValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblcenterpeiceromancyValue.grid(row=21,column=8, padx=5, pady=5)

 #============================================ Row 22 ===========================================

lblExtraDVD = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Extra DVD:", anchor='w')
lblExtraDVD.grid(row=22,column=2,columnspan=1, pady=5)
entry_extradvd = Entry(ekhnaton_frame,width=19, font=('arial', 10, 'bold'),textvariable= account.extradvd,bg="white", justify="center")
entry_extradvd.grid(row=22,column=3,columnspan=1,padx=10)
lblExtraDVDValue = ttk.Label(ekhnaton_frame,textvariable=extradvdValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblExtraDVDValue.grid(row=22,column=4, padx=5, pady=5)

entry_extraflash = Entry(ekhnaton_frame,width=19, font=('arial', 10, 'bold'),textvariable= account.extraflash,bg="white", justify="center")
entry_extraflash.grid(row=22,column=5,columnspan=1,padx=10)
lblExtraflashValue = ttk.Label(ekhnaton_frame,textvariable=extraflashValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblExtraflashValue.grid(row=22,column=6, padx=5, pady=5)

chkb_sound = Checkbutton(ekhnaton_frame, text=" Sound ",variable=account.sound,font=('arial', 10, 'bold'), onvalue= 1, offvalue=0, justify="left",anchor="w")
chkb_sound.grid(row=22,column=7, columnspan=1, sticky="w")
lblsoundValue = ttk.Label(ekhnaton_frame,textvariable=soundValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblsoundValue.grid(row=22,column=8, padx=5, pady=5)

# ============================================ Row 23 ===========================================

lblartistin = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Artists Inner:", anchor='w')
lblartistin.grid(row=23,column=2,columnspan=1, pady=5)
entry_artistin1 = Entry(ekhnaton_frame,width=19, font=('arial', 10, 'bold'),textvariable= account.artistin1,bg="white", justify="center")
entry_artistin1.grid(row=23,column=3,columnspan=1,padx=10)
entry_artistin2 = Entry(ekhnaton_frame,width=19, font=('arial', 10, 'bold'),textvariable= account.artistin2,bg="white", justify="center")
entry_artistin2.grid(row=23,column=4,columnspan=1,padx=10)
entry_artistin3 = Entry(ekhnaton_frame,width=19, font=('arial', 10, 'bold'),textvariable= account.artistin3,bg="white", justify="center")
entry_artistin3.grid(row=23,column=5,columnspan=1,padx=10)
lblExtraDVDValue = ttk.Label(ekhnaton_frame,textvariable=artistinValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblExtraDVDValue.grid(row=23,column=6, padx=5, pady=5)

lblTotal = ttk.Label(ekhnaton_frame,foreground="red",text="=====TOTAL=====", font=('arial', 10, 'bold'), anchor='w')
lblTotal.grid(row=23,column=7,columnspan = 2, padx=5, pady=5)

#====================================================Row 24 =========================================


lblartistout = ttk.Label(ekhnaton_frame, font=('arial', 10, 'bold'), text="Artists Outer:", anchor='w')
lblartistout.grid(row=24,column=2,columnspan=1, pady=5)
entry_artistout1 = Entry(ekhnaton_frame,width=19, font=('arial', 10, 'bold'),textvariable= account.artistout1,bg="white", justify="center")
entry_artistout1.grid(row=24,column=3,columnspan=1,padx=10)
entry_artistout2 = Entry(ekhnaton_frame,width=19, font=('arial', 10, 'bold'),textvariable= account.artistout2,bg="white", justify="center")
entry_artistout2.grid(row=24,column=4,columnspan=1,padx=10)
entry_artistout3 = Entry(ekhnaton_frame,width=19, font=('arial', 10, 'bold'),textvariable= account.artistout3,bg="white", justify="center")
entry_artistout3.grid(row=24,column=5,columnspan=1,padx=10)
lblExtraDVDValue = ttk.Label(ekhnaton_frame,textvariable=artistoutValue,foreground="red", font=('arial', 10, 'bold'), anchor='w')
lblExtraDVDValue.grid(row=24,column=6, padx=5, pady=5)

lblTotal = ttk.Label(ekhnaton_frame,foreground="Purple",textvariable=totalValue, font=('arial', 10, 'bold'), anchor='w')
lblTotal.grid(row=24,column=7,columnspan = 2, padx=5, pady=5)

#===================================================Row 25 ===========================================


btnOK = ttk.Button(ekhnaton_frame, text="Submit", command=lambda: account.update_All(account.count.get()))
btnOK.grid(row=25, column=4)

btnChkOut = ttk.Button(ekhnaton_frame, text="Done?!" ,command=lambda: account.check_out())
btnChkOut.grid(row=25, column=4,columnspan=2,sticky="we")



ekhnaton_frame.columnconfigure(0, weight=1)
ekhnaton_frame.columnconfigure(1, weight=2)
ekhnaton_frame.columnconfigure(2, weight=2)
ekhnaton_frame.columnconfigure(3, weight=2)
ekhnaton_frame.columnconfigure(4, weight=2)
ekhnaton_frame.columnconfigure(5, weight=2)
ekhnaton_frame.columnconfigure(6, weight=2)
ekhnaton_frame.columnconfigure(7, weight=2)
ekhnaton_frame.columnconfigure(8, weight=2)
ekhnaton_frame.columnconfigure(9, weight=1)

ekhnaton_frame.rowconfigure(0, weight=1)
ekhnaton_frame.rowconfigure(1, weight=1)
ekhnaton_frame.rowconfigure(2, weight=1)
ekhnaton_frame.rowconfigure(3, weight=1)
ekhnaton_frame.rowconfigure(4, weight=1)
ekhnaton_frame.rowconfigure(5, weight=1)
ekhnaton_frame.rowconfigure(6, weight=1)
ekhnaton_frame.rowconfigure(7, weight=1)
ekhnaton_frame.rowconfigure(8, weight=1)
ekhnaton_frame.rowconfigure(9, weight=1)
ekhnaton_frame.rowconfigure(10, weight=1)
ekhnaton_frame.rowconfigure(11, weight=1)
ekhnaton_frame.rowconfigure(12, weight=1)
ekhnaton_frame.rowconfigure(13, weight=1)
ekhnaton_frame.rowconfigure(14, weight=1)
ekhnaton_frame.rowconfigure(15, weight=1)
ekhnaton_frame.rowconfigure(16, weight=1)
ekhnaton_frame.rowconfigure(17, weight=1)
ekhnaton_frame.rowconfigure(18, weight=1)
ekhnaton_frame.rowconfigure(19, weight=1)
ekhnaton_frame.rowconfigure(20, weight=1)
ekhnaton_frame.rowconfigure(21, weight=1)
ekhnaton_frame.rowconfigure(22, weight=1)
ekhnaton_frame.rowconfigure(23, weight=1)
ekhnaton_frame.rowconfigure(24, weight=1)
ekhnaton_frame.rowconfigure(25, weight=1)
ekhnaton_frame.rowconfigure(26, weight=1)






root.mainloop()
