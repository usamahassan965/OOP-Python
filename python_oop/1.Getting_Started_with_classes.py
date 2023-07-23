################################# Getting Started with Classes #########################################

### Classes do have attributes and methods . e.g., class 'str' has methods upper , lower , etc.
### Argument 'self' is representing the object itself.

class Item:
    def calc_total_price(self,x,y):
        return x*y

item1 = Item()
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5
print(item1.calc_total_price(item1.price,item1.quantity))

print(type(item1))              ### instance of class 'Item'
print(type(item1.name))         ### instance of class 'str' (Item attribute)
print(type(item1.price))        ### instance of class 'int' (Item attribute)
print(type(item1.quantity))     ### instance of class 'int' (Item attribute)