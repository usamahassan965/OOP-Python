######################################## OOP Principles ######################################################

#######################################  Encapsulation $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
### We have 4 OOP Principles to allow us write large programs which are : Enacpsulation, Abstraction, Inheritance, Polymorphism
### First, is Encapsulation. It is restricting the ability to override some attributes without using setter method
### This type of overriding is similar to class attribute pay_rate where we override price. But there we override public attribute but here in encapsulation, we override private attribute.




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
        self.__name1 = name
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

    @property
    ### Only Readable attribute   (Getter Method)
    def read_only_name(self):
        return 'AAA'

    @property
    ### Reading private attribute  (Getter Method)
    def set_name1(self):
        return self.__name1

    @set_name1.setter
    ### Writing to Private attribute   (Setter Method)
    def set_name1(self,Value):
        self.__name1 = Value


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

class Phone(Item):
    def __init__(self,name: str,price: float,quantity=0,broken_phones=0):
        ### Call to super function to access attributes / methods of parennt class
        super().__init__(name,price,quantity)

        assert broken_phones >= 0 , f'Broken Phones {broken_phones} is not > = 0.'

        self.broken_phones = broken_phones

phone1 = Phone('Phone1',100,5)
phone1.name = 'Phone3'
### phone1.read_only_name = 'BBB'                 ###n So this is not allowed
print(phone1.name)
print(phone1.read_only_name)
### print(phone1.name1)                           ### It will give error


phone1.set_name1 = 'Samsung'                     ### Now we can both read and write to private attribute
print(phone1.set_name1)

