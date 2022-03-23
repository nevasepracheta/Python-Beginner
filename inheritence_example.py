##Chef Class
class Chef:
    def make_chicken(self):
        print("Chef can make chicken")

    def make_salad(self):
        print("Chef can make a salad")

    def make_special_dish(self):
        print("Chef's special is Chicken Wings!")
#########################################################
##Chinese Chef
from chef import Chef 

class chinese_chef(Chef): # Inheriting Chef to chinese_chef class

    def make_special_dish(self): # Overriding function from inherited class Chef
        print("Chef's special is Orange Chicken")

    def make_fried_rice(self):
        print("Chef can make fried rice")
#########################################################
from chef import Chef
from chinese_chef import chinese_chef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = chinese_chef()
myChineseChef.make_special_dish()
