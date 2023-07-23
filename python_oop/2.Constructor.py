######################################### Constructor, __init__ ###############################################

### To avoid hard code of all attributes each time whenever the class instance is created, we introduce constructor.
### It's __init__ method (a magic method) and it instantiates each time the class instance is created.
### quantity = 0 (default parameter)
### We can limit the argument type error with the colon defining argument type e.g., name: str.
### We don't need to define the type for the default parameter bcz it understands its type from its default value. e.g., quantity = 0.
### We can't validate the argument range or values this way. For this, we have assert command.
### Besides instance attributes (name,price,etc) , we have class attributes (e.g., pay_rate) which are global and shared across all instances.
### We don't need to instaantiate class object to access this class attribute.We can also access to claaa attributes from instance level.
### Actually , when program doesn't find attribute on instance level then he goes for class level attribute amd check that if it exists or not.
### Similarly, we can access to all class attributes or instance attributes through magic attribute __dict__.
### We have 2 types of usage of class attribute. First, is we overwrite our instance attribute price using pay rate on instance level using self.
### In this way, we can change our class attribute on instance level e.g. item2.pay_rate = 0.7.
### Second type of usage of class attribute is we can use it to overwrite the instance attribute on class level itself.
### hence, if we change our pay rate on instance level , there will be no effect of it . Pay rate will be 0.8 rather than 0.7.
### For example, we have overwrite quantity on class level using Item .
### One usage of class attribute is 'all' which is a list contining all instances of class Item.
### To represent the class objects more better format, we can use __repr__ magic method to represent them as a string.
### f you don't use __repr__ , it will not represent object that way.

class Item:
    pay_rate = 0.8   # The pay rate after 20% discount.
    all = []         # List containing all instances instantiated
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0 , f'Price {price} is not greater than or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Instances list appending
        Item.all.append(self)

    def calc_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        self.quantity = int(self.quantity * Item.pay_rate)
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

item1 = Item('Phone',100)
item2 = Item('Laptop',1000,3)

# item2.has_numpad = False                 ### We can instantiate attributes outside our class or init method

print(Item.pay_rate)             ### Accessing class attribute through class level
print(item1.pay_rate)            ### Accessing class attribute through instance level
print(item2.pay_rate)

print(Item.__dict__)              ### All attributes on class level
print(item1.__dict__)             ### All attributes on instance level

item1.apply_discount()
print(item1.price)            ### Overwriting instance attribute on instance level using class attribute pay rate
print(item1.quantity)         ### Overwriting instance attribute on class level using class attribute pay rate

item2.pay_rate = 0.7          ### This will affect only price not quantity due to class level overwriting .
item2.apply_discount()
print(item2.price)
print(item2.quantity)

print(item1.calc_total_price())
print(item2.calc_total_price())

item3 = Item('Cable',10,5)
item4 = Item('Mouse',50,5)
item5 = Item('Keyboard',75,5)
#
print(Item.all)                   ### Acccessing list on class level
print(item2.all)                  ### Acccessing list on instance level
print(item1.__repr__())

for instance in Item.all:
    print(instance.name)
