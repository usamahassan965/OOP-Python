################################# Getting Started with Classes #########################################

### Classes do have attributes and methods . e.g., class 'str' has methods upper , lower , etc.
### Argument 'self' is representing the object itself.

# class Item:
#     def calc_total_price(self,x,y):
#         return x*y
#
# item1 = Item()
# item1.name = 'Phone'
# item1.price = 100
# item1.quantity = 5
# print(item1.calc_total_price(item1.price,item1.quantity))
#
# print(type(item1))              ### instance of class 'Item'
# print(type(item1.name))         ### instance of class 'str' (Item attribute)
# print(type(item1.price))        ### instance of class 'int' (Item attribute)
# print(type(item1.quantity))     ### instance of class 'int' (Item attribute)


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

# class Item:
#     pay_rate = 0.8   # The pay rate after 20% discount.
#     all = []         # List containing all instances instantiated
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validations to the received arguments
#         assert price >= 0 , f'Price {price} is not greater than or equal to zero!'
#         assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'
#
#         # Assign to self object
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#         # Instances list appending
#         Item.all.append(self)
#
#     def calc_total_price(self):
#         return self.price * self.quantity
#
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
#         self.quantity = int(self.quantity * Item.pay_rate)
#     def __repr__(self):
#         return f"Item('{self.name}',{self.price},{self.quantity})"

# item1 = Item('Phone',100)
# item2 = Item('Laptop',1000,3)

## item2.has_numpad = False                 ### We can instantiate attributes outside our class or init method

# print(Item.pay_rate)             ### Accessing class attribute through class level
# print(item1.pay_rate)            ### Accessing class attribute through instance level
# print(item2.pay_rate)
#
# print(Item.__dict__)              ### All attributes on class level
# print(item1.__dict__)             ### All attributes on instance level
#
# item1.apply_discount()
# print(item1.price)            ### Overwriting instance attribute on instance level using class attribute pay rate
# print(item1.quantity)         ### Overwriting instance attribute on class level using class attribute pay rate
#
# item2.pay_rate = 0.7          ### This will affect only price not quantity due to class level overwriting .
# item2.apply_discount()
# print(item2.price)
# print(item2.quantity)
#
# print(item1.calc_total_price())
# print(item2.calc_total_price())

# item3 = Item('Cable',10,5)
# item4 = Item('Mouse',50,5)
# item5 = Item('Keyboard',75,5)
# #
# print(Item.all)                   ### Acccessing list on class level
# print(item2.all)                  ### Acccessing list on instance level
# print(item1.__repr__())

# for instance in Item.all:
#     print(instance.name)


############################################## Class Vs Static Methods #########################################

### We need to add more features in it. We will separate the data from the code. We will use csv file for this.
### To instantiate data from the method itself, we need to define a class method like class attribute to perform operation on class level
### That's why, we made instantiate_from_csv to accompalish it.
### Also, we use decorator @classmethod to define it and pass cls (class reference) in the class method argument.
### Decorator changes the behavior of a function.
### We use DictReader function to read in list of dictionaries format.


# import csv
# class Item:
#     pay_rate = 0.8   # The pay rate after 20% discount.
#     all = []         # List containing all instances instantiated
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validations to the received arguments
#         assert price >= 0 , f'Price {price} is not greater than or equal to zero!'
#         assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'
#
#         # Assign to self object
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#         # Instances list appending
#         Item.all.append(self)
#
#     def calc_total_price(self):
#         return self.price * self.quantity
#
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
#         self.quantity = int(self.quantity * Item.pay_rate)
#
#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('data.csv','r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)
#         for item in items:
#             Item(
#                 name = item.get('name'),
#                 price = float(item.get('price')),
#                 quantity = int(item.get('quantity'))
#             )                       ### Accesing attributes on class level  (List of dictionaries)
#
#     def __repr__(self):
#         return f"Item('{self.name}',{self.price},{self.quantity})"
#
# Item.instantiate_from_csv()
# print(Item.all)


################################################ Static Method ##################################################

### We define staticmethods with a decorator like class methods. But it works like a regular function and doesn't require self argument.
### We access the static methods like class methods. We can access them both on class level or instance level.
### We use static methods as they should do something that has a relationship with a class but not something that must be unique per instance.
### Like in function Is_integer , we are just checking if a number num is insteger or not. it is like a regular function we use without class.
### while class methods are used for instantiating instances from some structure data that you own , to maintain data like we have done with csv



# import csv
# class Item:
#     pay_rate = 0.8   # The pay rate after 20% discount.
#     all = []         # List containing all instances instantiated
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validations to the received arguments
#         assert price >= 0 , f'Price {price} is not greater than or equal to zero!'
#         assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'
#
#         # Assign to self object
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#         # Instances list appending
#         Item.all.append(self)
#
#     def calc_total_price(self):
#         return self.price * self.quantity
#
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
#         self.quantity = int(self.quantity * Item.pay_rate)
#
#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('data.csv','r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)
#         for item in items:
#             Item(
#                 name = item.get('name'),
#                 price = float(item.get('price')),
#                 quantity = int(item.get('quantity'))
#             )                       ### Accesing attributes on class level  (List of dictionaries)
#
#     @staticmethod
#     def Is_integer(num):
#         ## We'll count those floats which are point zero e.g., 5.0 , 10.0 etc
#         if isinstance(num,float):
#             return num.is_integer()                 ### returning false if float
#         elif isinstance(num,int):
#             return True
#         else:
#             return False
#
#     def __repr__(self):
#         return f"Item('{self.name}',{self.price},{self.quantity})"
#
# print(Item.Is_integer(7.0))



####################################333 Inheritance ###########################################################

### We can create child classes from Item class which is parent class to add more features which are specific to the child classes.
### Like here , we have made class Phone , child class of parent class Item , have extra feature broken phones.
### We must pass parent class name in child class definition e.g., phone(Item).
### To inertt all attributes / methods from parent class , we use super function.
### We also changed repr function using magic attribute __class__.__name__ to print corresponding instance (child or parent)


# import csv
# class Item:
#     pay_rate = 0.8   # The pay rate after 20% discount.
#     all = []         # List containing all instances instantiated
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validations to the received arguments
#         assert price >= 0 , f'Price {price} is not greater than or equal to zero!'
#         assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'
#
#         # Assign to self object
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#         # Instances list appending
#         Item.all.append(self)
#
#     def calc_total_price(self):
#         return self.price * self.quantity
#
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
#         self.quantity = int(self.quantity * Item.pay_rate)
#
#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('data.csv','r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)
#         for item in items:
#             Item(
#                 name = item.get('name'),
#                 price = float(item.get('price')),
#                 quantity = int(item.get('quantity'))
#             )                       ### Accesing attributes on class level  (List of dictionaries)
#
#     @staticmethod
#     def Is_integer(num):
#         ## We'll count those floats which are point zero e.g., 5.0 , 10.0 etc
#         if isinstance(num,float):
#             return num.is_integer()                 ### returning false if float
#         elif isinstance(num,int):
#             return True
#         else:
#             return False
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
#
# class Phone(Item):
#     def __init__(self,name: str,price: float,quantity=0,broken_phones=0):
#         ### Call to super function to access attributes / methods of parennt class
#         super().__init__(name,price,quantity)
#
#         assert broken_phones >= 0 , f'Broken Phones {broken_phones} is not > = 0.'
#
#         self.broken_phones = broken_phones
#
# phone1 = Phone('Phone1',100,5)
# phone1.broken_phones = 5
# phone2 = Item('Phone2',100,6)
#
# print(phone1.calc_total_price())
# print(Item.all)
# print(Phone.all)

########################################## getters and setters ####################################################

### We know that after instantiation of the object we can change attribute values like name,pric, etc.
### We can also define different type of attributes using property which couln't be changed later. eg., read_only_name in Item class
### Hence, with property decorator, we can read only but can't write.
### But if we define our attribute like self.__name1 , then we even can't access it . It will make this attribute private.
### We can read this private attribute through getter method (set_name1) having decorator property.
### We can write private attribute then through another setter method (set_name1) but this time with docorator name.setter.
### We must also pass some argument to setter method to change the attribute value e.g., Value in setter method.
### So Property Decorator = Read only attribute, functionname.setter Decorator = Read and Write only attribute

# import csv
# class Item:
#     pay_rate = 0.8   # The pay rate after 20% discount.
#     all = []         # List containing all instances instantiated
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validations to the received arguments
#         assert price >= 0 , f'Price {price} is not greater than or equal to zero!'
#         assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'
#
#         # Assign to self object
#         self.name = name
#         self.__name1 = name
#         self.price = price
#         self.quantity = quantity
#
#         # Instances list appending
#         Item.all.append(self)
#
#     def calc_total_price(self):
#         return self.price * self.quantity
#
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
#         self.quantity = int(self.quantity * Item.pay_rate)
#
#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('data.csv','r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)
#         for item in items:
#             Item(
#                 name = item.get('name'),
#                 price = float(item.get('price')),
#                 quantity = int(item.get('quantity'))
#             )                       ### Accesing attributes on class level  (List of dictionaries)
#
#     @staticmethod
#     def Is_integer(num):
#         ## We'll count those floats which are point zero e.g., 5.0 , 10.0 etc
#         if isinstance(num,float):
#             return num.is_integer()                 ### returning false if float
#         elif isinstance(num,int):
#             return True
#         else:
#             return False
#
#     @property
#     ### Only Readable attribute   (Getter Method)
#     def read_only_name(self):
#         return 'AAA'
#
#     @property
#     ### Reading private attribute  (Getter Method)
#     def set_name1(self):
#         return self.__name1
#
#     @set_name1.setter
#     ### Writing to Private attribute   (Setter Method)
#     def set_name1(self,Value):
#         self.__name1 = Value
#
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
#
# class Phone(Item):
#     def __init__(self,name: str,price: float,quantity=0,broken_phones=0):
#         ### Call to super function to access attributes / methods of parennt class
#         super().__init__(name,price,quantity)
#
#         assert broken_phones >= 0 , f'Broken Phones {broken_phones} is not > = 0.'
#
#         self.broken_phones = broken_phones
#
# phone1 = Phone('Phone1',100,5)
# phone1.name = 'Phone3'
# ### phone1.read_only_name = 'BBB'                 ###n So this is not allowed
# print(phone1.name)
# print(phone1.read_only_name)
# ### print(phone1.name1)                           ### It will give error
#
#
# phone1.set_name1 = 'Samsung'                     ### Now we can both read and write to private attribute
# print(phone1.set_name1)



######################################## OOP Principles ######################################################

#######################################  Encapsulation $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
### We have 4 OOP Principles to allow us write large programs which are : Enacpsulation, Abstraction, Inheritance, Polymorphism
### First, is Encapsulation. It is restricting the ability to override some attributes without using setter method
### This type of overriding is similar to class attribute pay_rate where we override price. But there we override public attribute but here in encapsulation, we override private attribute.




# import csv
# class Item:
#     pay_rate = 0.8   # The pay rate after 20% discount.
#     all = []         # List containing all instances instantiated
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validations to the received arguments
#         assert price >= 0 , f'Price {price} is not greater than or equal to zero!'
#         assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'
#
#         # Assign to self object
#         self.name = name
#         self.__name1 = name
#         self.price = price
#         self.quantity = quantity
#
#         # Instances list appending
#         Item.all.append(self)
#
#     def calc_total_price(self):
#         return self.price * self.quantity
#
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
#         self.quantity = int(self.quantity * Item.pay_rate)
#
#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('data.csv','r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)
#         for item in items:
#             Item(
#                 name = item.get('name'),
#                 price = float(item.get('price')),
#                 quantity = int(item.get('quantity'))
#             )                       ### Accesing attributes on class level  (List of dictionaries)
#
#     @staticmethod
#     def Is_integer(num):
#         ## We'll count those floats which are point zero e.g., 5.0 , 10.0 etc
#         if isinstance(num,float):
#             return num.is_integer()                 ### returning false if float
#         elif isinstance(num,int):
#             return True
#         else:
#             return False
#
#     @property
#     ### Only Readable attribute   (Getter Method)
#     def read_only_name(self):
#         return 'AAA'
#
#     @property
#     ### Reading private attribute  (Getter Method)
#     def set_name1(self):
#         return self.__name1
#
#     @set_name1.setter
#     ### Writing to Private attribute   (Setter Method)
#     def set_name1(self,Value):
#         self.__name1 = Value
#
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
#
# class Phone(Item):
#     def __init__(self,name: str,price: float,quantity=0,broken_phones=0):
#         ### Call to super function to access attributes / methods of parennt class
#         super().__init__(name,price,quantity)
#
#         assert broken_phones >= 0 , f'Broken Phones {broken_phones} is not > = 0.'
#
#         self.broken_phones = broken_phones
#
# phone1 = Phone('Phone1',100,5)
# phone1.name = 'Phone3'
# ### phone1.read_only_name = 'BBB'                 ###n So this is not allowed
# print(phone1.name)
# print(phone1.read_only_name)
# ### print(phone1.name1)                           ### It will give error
#
#
# phone1.set_name1 = 'Samsung'                     ### Now we can both read and write to private attribute
# print(phone1.set_name1)



######################################  Abstraction ##########################################################

### Used for hiding unnecsaary information from the user. Shows only necessary attributes.
### Like if we want to make a function send_email then we have to make functions for connecting to smpt server , prepare body , send.
### But the user actually need to access only send_email, not other functions which are used under send_email.
### Thus, to hide those functions, we make them private functions using __ like __send , __ preapare_body , etc.

# import csv
# class Item:
#     pay_rate = 0.8   # The pay rate after 20% discount.
#     all = []         # List containing all instances instantiated
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validations to the received arguments
#         assert price >= 0 , f'Price {price} is not greater than or equal to zero!'
#         assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'
#
#         # Assign to self object
#         self.name = name
#         self.__name1 = name
#         self.price = price
#         self.quantity = quantity
#
#         # Instances list appending
#         Item.all.append(self)
#
#     def calc_total_price(self):
#         return self.price * self.quantity
#
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
#         self.quantity = int(self.quantity * Item.pay_rate)
#
#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('data.csv','r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)
#         for item in items:
#             Item(
#                 name = item.get('name'),
#                 price = float(item.get('price')),
#                 quantity = int(item.get('quantity'))
#             )                       ### Accesing attributes on class level  (List of dictionaries)
#
#     @staticmethod
#     def Is_integer(num):
#         ## We'll count those floats which are point zero e.g., 5.0 , 10.0 etc
#         if isinstance(num,float):
#             return num.is_integer()                 ### returning false if float
#         elif isinstance(num,int):
#             return True
#         else:
#             return False
#
#     @property
#     ### Only Readable attribute   (Getter Method)
#     def read_only_name(self):
#         return 'AAA'
#
#     @property
#     ### Reading private attribute  (Getter Method)
#     def set_name1(self):
#         return self.__name1
#
#     @set_name1.setter
#     ### Writing to Private attribute   (Setter Method)
#     def set_name1(self,Value):
#         self.__name1 = Value
#
#     def __connect_smpt_server(self):
#         pass
#     def __prepare_body(self):
#         return f"""
#                 Hello , we have {self.name} {self.quantity} times.
#                 Regards,
#                 Usama Hassan """
#     def __send(self):
#         pass
#
#     def send_email(self):
#         self.__connect_smpt_server()
#         self.__prepare_body()
#         self.__send()
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
#
# class Phone(Item):
#     def __init__(self,name: str,price: float,quantity=0,broken_phones=0):
#         ### Call to super function to access attributes / methods of parennt class
#         super().__init__(name,price,quantity)
#
#         assert broken_phones >= 0 , f'Broken Phones {broken_phones} is not > = 0.'
#
#         self.broken_phones = broken_phones
#
# phone1 = Phone('Phone1',100,5)
# phone1.name = 'Phone3'
# ### phone1.read_only_name = 'BBB'                 ###n So this is not allowed
# print(phone1.name)
# print(phone1.read_only_name)
# ### print(phone1.name1)                           ### It will give error




# phone1.set_name1 = 'Samsung'                     ### Now we can both read and write to private attribute
# print(phone1.set_name1)
# print(phone1.send_email())
# #print(phone1.__connect)                         #### Will give error due to private function



################################  Polymorphism ###############################################################

### Use same entity to represent different types of entities for different usecases (Many forms).
### Any function could be entity. We have built in function len() which works for multiple types like strings , list , etc.
### here we have over rided pay rate value from Item class (0.8) to Phone class (0.7).
### which means if we instantiate object of Phone class we will get pay rate 0.7 but if we have other child classes we will get pay rate of 0.8.
### Hence, we have 2 forms of using pay rate.

# import csv
# class Item:
#     pay_rate = 0.8   # The pay rate after 20% discount.
#     all = []         # List containing all instances instantiated
#     def __init__(self, name: str, price: float, quantity=0):
#         # Run validations to the received arguments
#         assert price >= 0 , f'Price {price} is not greater than or equal to zero!'
#         assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'
#
#         # Assign to self object
#         self.name = name
#         self.__name1 = name
#         self.price = price
#         self.quantity = quantity
#
#         # Instances list appending
#         Item.all.append(self)
#
#     def calc_total_price(self):
#         return self.price * self.quantity
#
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
#         self.quantity = int(self.quantity * Item.pay_rate)
#
#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('data.csv','r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)
#         for item in items:
#             Item(
#                 name = item.get('name'),
#                 price = float(item.get('price')),
#                 quantity = int(item.get('quantity'))
#             )                       ### Accesing attributes on class level  (List of dictionaries)
#
#     @staticmethod
#     def Is_integer(num):
#         ## We'll count those floats which are point zero e.g., 5.0 , 10.0 etc
#         if isinstance(num,float):
#             return num.is_integer()                 ### returning false if float
#         elif isinstance(num,int):
#             return True
#         else:
#             return False
#
#     @property
#     ### Only Readable attribute   (Getter Method)
#     def read_only_name(self):
#         return 'AAA'
#
#     @property
#     ### Reading private attribute  (Getter Method)
#     def set_name1(self):
#         return self.__name1
#
#     @set_name1.setter
#     ### Writing to Private attribute   (Setter Method)
#     def set_name1(self,Value):
#         self.__name1 = Value
#
#     def __connect_smpt_server(self):
#         pass
#     def __prepare_body(self):
#         return f"""
#                 Hello , we have {self.name} {self.quantity} times.
#                 Regards,
#                 Usama Hassan """
#     def __send(self):
#         pass
#
#     def send_email(self):
#         self.__connect_smpt_server()
#         self.__prepare_body()
#         self.__send()
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
#
# class Phone(Item):
#     pay_rate = 0.7
#     def __init__(self,name: str,price: float,quantity=0,broken_phones=0):
#         ### Call to super function to access attributes / methods of parennt class
#         super().__init__(name,price,quantity)
#
#         assert broken_phones >= 0 , f'Broken Phones {broken_phones} is not > = 0.'
#
#         self.broken_phones = broken_phones
#
# phone1 = Phone('Phone1',400,5,7)
# item1 = Item('Item1',400,5)
# 
# phone1.apply_discount()
# item1.apply_discount()
#
# print(phone1.price)
# print(item1.price)

