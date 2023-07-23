########################################## getters and setters ####################################################

### We know that after instantiation of the object we can change attribute values like name,pric, etc.
### We can also define different type of attributes using property which couln't be changed later. eg., read_only_name in Item class
### Hence, with property decorator, we can read only but can't write.
### But if we define our attribute like self.__name1 , then we even can't access it . It will make this attribute private.
### We can read this private attribute through getter method (set_name1) having decorator property.
### We can write private attribute then through another setter method (set_name1) but this time with docorator name.setter.
### We must also pass some argument to setter method to change the attribute value e.g., Value in setter method.
### So Property Decorator = Read only attribute, functionname.setter Decorator = Read and Write only attribute

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

