class Food(object):
    def __init__(self,name,price):
       self.name = name
       self.price = price
    def get_name_and_price(self):
        return self.name + " " + self.price

    def  get_price_name(self):
        message = "The food name and price is"
        message += self.get_name_and_price()
        return message
    def get_intro(self):
        message = "the food name is"
        message += self.name
        message += "price is" + self.price + "."
        return message     
baozi = Food(name="baozi",price="111")
print(baozi.get_intro())
