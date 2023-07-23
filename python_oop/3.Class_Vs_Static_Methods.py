############################################## Class Vs Static Methods #########################################

### We need to add more features in it. We will separate the data from the code. We will use csv file for this.
### To instantiate data from the method itself, we need to define a class method like class attribute to perform operation on class level
### That's why, we made instantiate_from_csv to accompalish it.
### Also, we use decorator @classmethod to define it and pass cls (class reference) in the class method argument.
### Decorator changes the behavior of a function.
### We use DictReader function to read in list of dictionaries format.


import csv
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

    @classmethod
    def instantiate_from_csv(cls):
        with open('data.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )                       ### Accesing attributes on class level  (List of dictionaries)

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

Item.instantiate_from_csv()
print(Item.all)


################################################ Static Method ##################################################

### We define staticmethods with a decorator like class methods. But it works like a regular function and doesn't require self argument.
### We access the static methods like class methods. We can access them both on class level or instance level.
### We use static methods as they should do something that has a relationship with a class but not something that must be unique per instance.
### Like in function Is_integer , we are just checking if a number num is insteger or not. it is like a regular function we use without class.
### while class methods are used for instantiating instances from some structure data that you own , to maintain data like we have done with csv



import csv
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

    @classmethod
    def instantiate_from_csv(cls):
        with open('data.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )                       ### Accesing attributes on class level  (List of dictionaries)

    @staticmethod
    def Is_integer(num):
        ## We'll count those floats which are point zero e.g., 5.0 , 10.0 etc
        if isinstance(num,float):
            return num.is_integer()                 ### returning false if float
        elif isinstance(num,int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

print(Item.Is_integer(7.0))

