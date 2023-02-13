class Date:
    def __init__(self,y,m,d):
        self.y = y
        self.m = m
        self.d = d

    def show(self):
        print(self.y,"/",self.m,"/",self.d)    

    def get_mounth_name(self):
        if self.m == 1:
            print("Farvardin")

        elif self.m == 2:
            print("Ordibehesht")

        elif self.m == 3: 
            print("Khordaad")

        elif self.m == 4: 
            print("Tir")

        elif self.m == 5: 
            print("Mordaad")

        elif self.m == 6: 
            print("Shahrivar")

        elif self.m == 7: 
            print("Mehr")

        elif self.m == 8: 
            print("Abaan")

        elif self.m == 9: 
            print("Azar")

        elif self.m == 10: 
            print("Dey")  

        elif self.m == 11: 
            print("Bahman")

        elif self.m == 12: 
            print("Esfand")                                   

    def is_valid_date(self):
        if not 1 <= self.d <= 30 or not 1 <= self.m <= 12 or not 1 <= self.y <= 9999: 
            print(False)
        else:
            print(True)
            

date1 = Date(1392,13,24)
date1.show()
date1.get_mounth_name()
date1.is_valid_date()


date2 = Date(1400,4,21)
date2.show()
date2.get_mounth_name()
date2.is_valid_date()
