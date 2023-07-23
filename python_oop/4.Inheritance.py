####################################333 Inheritance ###########################################################

### We can create child classes from Item class which is parent class to add more features which are specific to the child classes.
### Like here , we have made class Phone , child class of parent class Item , have extra feature broken phones.
### We must pass parent class name in child class definition e.g., phone(Item).
### To inertt all attributes / methods from parent class , we use super function.
### We also changed repr function using magic attribute __class__.__name__ to print corresponding instance (child or parent)


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
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

class Phone(Item):
    def __init__(self,name: str,price: float,quantity=0,broken_phones=0):
        ### Call to super function to access attributes / methods of parennt class
        super().__init__(name,price,quantity)

        assert broken_phones >= 0 , f'Broken Phones {broken_phones} is not > = 0.'

        self.broken_phones = broken_phones

phone1 = Phone('Phone1',100,5)
phone1.broken_phones = 5
phone2 = Item('Phone2',100,6)

print(phone1.calc_total_price())
print(Item.all)
print(Phone.all)
