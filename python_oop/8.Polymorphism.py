
################################  Polymorphism ###############################################################

### Use same entity to represent different types of entities for different usecases (Many forms).
### Any function could be entity. We have built in function len() which works for multiple types like strings , list , etc.
### here we have over rided pay rate value from Item class (0.8) to Phone class (0.7).
### which means if we instantiate object of Phone class we will get pay rate 0.7 but if we have other child classes we will get pay rate of 0.8.
### Hence, we have 2 forms of using pay rate.

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

    def __connect_smpt_server(self):
        pass
    def __prepare_body(self):
        return f"""
                Hello , we have {self.name} {self.quantity} times.
                Regards,
                Usama Hassan """
    def __send(self):
        pass

    def send_email(self):
        self.__connect_smpt_server()
        self.__prepare_body()
        self.__send()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

class Phone(Item):
    pay_rate = 0.7
    def __init__(self,name: str,price: float,quantity=0,broken_phones=0):
        ### Call to super function to access attributes / methods of parennt class
        super().__init__(name,price,quantity)

        assert broken_phones >= 0 , f'Broken Phones {broken_phones} is not > = 0.'

        self.broken_phones = broken_phones

phone1 = Phone('Phone1',400,5,7)
item1 = Item('Item1',400,5)

phone1.apply_discount()
item1.apply_discount()

print(phone1.price)
print(item1.price)

