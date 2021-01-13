                                                                                          #""" Object """#
""" In our daily life we see a lot of 'things' like chair, table, a dog or our mom, dad or anything or anyone what ever we see around us everything is an object. In programming, both the living(dynamic) and static things are called object """

""" How do we call the objects? like you have a lot of friend how do you get to know them? They have own characteristics like name right! So from this characteristics we can say that everyone have their own attributes or properties. This unique attributes or properties differentiate one person from another. So we can say that every object in the world have own attributes. Most of the objects perform their own tasks like you eat, sleep or code as well as a car moves or drinks petrol or gasoline. """

""" Every objects in this universe 1) Has own attributes (characteristics) and 2) Perform tasks. """

""" You have to remember that when you are making objects you have to make a template to make sure that you don't make a lot of objects which do same tasks. Like you are the CEO of a mobile company and I ordered 1000 pieces of the same model with style, color and IMEI code what will you do? You will use your template or blueprint to make 1000 copies of the same phone right? Those phones have same attributes with different value like phones have same color, same style but the IMEI codes will be different. """

""" The template has a better name and it's called *Class*. A class is a category or a group of people/things that share similar attributes. Class is the template to make similar attributes. """

""" Declaring a class is easy. 1) write the keyword class 2) give the class a name (like cars :3) 3) use a colon (:) sign after the name (like cars: ). """

""" Attributes are just like variables that you declare inside a class. And you can give it an initial value """

""" To create an object from the class you will call the class like a function """

""" From a class you can create as many objects as you want """

class Phone:
      brand = ''
      price = ''
      apps = []

myPhone = Phone()

myPhone.brand = 'Samsung'
myPhone.price = '80,000 BDT'
myPhone.apps = ['Telegram', 'Programming Hero', 'Github']
print(myPhone.brand, myPhone.price, myPhone.apps)


herPhone = Phone()

herPhone.brand = 'Samsung'
herPhone.price = '10,2000 BDT'
herPhone.apps = ['Gmail', 'Instagram', 'Telegram']
print(herPhone.brand, herPhone.price, herPhone.apps)


momsPhone = Phone()

momsPhone.brand = 'Samsung'
momsPhone.price = '40,000 BDT'
momsPhone.apps = ['Phone Book', 'Messenger', 'Camera']
print(momsPhone.brand, momsPhone.price, momsPhone.apps)
print('\n\n')



                                                                                          #""" Method """#
""" If you write a function inside an Class you can call the function when ever you make a new Object of the class and it is called Method. To declare a method just write a function inside the class """

""" Whenever you are declaring a method you have to provide a parameter in the function. You may or may not use it, this parameter is called 'self' """

""" If you want to pass one or more parameters to a method you will write those parameters after the 'self' parameter. """

""" The first parameter of a function will be 'self' """

""" You can access the class from the method. You have to use the 'self' parameter for this. Just write self then a dot then the name of the attribute inside the mothod. like this, return self.account_balance """

""" You can access each and every attribute by using the self then dot sign then name of the attributes. """

class Student:
      name = ''
      id = ''
      bloodGroup = ''
      creditFee = '5500 BDT'
      def programName(self):
            program = 'Computer Science & Engineering'
            print('Program Name: ', program)

      def oop2Mark(self, code, obj):
            print('Mark of Object Oriented Programming 2: ', code + obj)

      def credit(self):
            print('Per Credit Fee: ', self.creditFee)

      def department(self, nameOfDept):
            return nameOfDept
      
      def deptMethodCall(self):
            print('Department Name: ', self.department('Faculty of Science & Engineering'))

firstStudent = Student()

firstStudent.name = 'Safkat Jaman'
firstStudent.id = '19-40286-1'
firstStudent.bloodGroup = 'O negative'
print('Student Name: ', firstStudent.name, '\nStudent ID: ', firstStudent.id, '\nStudent Blood Group: ', firstStudent.bloodGroup)
firstStudent.oop2Mark(60, 15)
firstStudent.programName()
firstStudent.deptMethodCall()
firstStudent.credit()
print('\n\n')



                                                                                          #""" Constructor """#
""" You can provide initial values in your class with a special method called Constructor. In Python it has a special name __init__. like this, def __init__(self) """

""" Explanation of below code: First of all we declared a class named Marks. Then we used the constructor method with that you can declare a attribute from the special method. Inside the constructor method we passed two parametes named 'self', 'subjectName'. Then by writing self.subjectName = subjectName we added an attribute in the class named Marks. We also declared another attribute named oldMarks in the method and we gave it a value like 50. We created another method named subjectMarks and passed two parametes named 'self' and 'newMarks' there. Inside this normal method we used the power of 'self' parameter. We called the oldMarks attribute. In the oldMarks attribute we tried to do a addition with the oldMarks of the constructor method and the newMarks parameter. After the end of the class we took a new variable called myMarks and called the class Marks (putted the value of it) for the variables value. Again we called the subjectMarks method of the Marks class and provide a value (35) to it. After all this processes we printed the output. That's it. """

class Marks:
      def __init__(self, subjectName):
            self.subjetName = subjectName
            self.oldMarks = 50
      def subjectMarks(self, newMarks):
            self.oldMarks = self.oldMarks + newMarks

myMarks = Marks('Object Oriented Analysis & Design')
myMarks.subjectMarks(35)

print('Subject Name:', myMarks.subjetName)
print('Marks Obtained:', myMarks.oldMarks)
print('\n\n')



                                                                                        #''' Advanced Class '''#
''' There is a problem in the below code. The second customer didn't add any T-shirt in his/her cart but still it's showing T-shit and Shoes in his/her cart. This thing is called class level attribute. These attributes are shared among all the objects created from the class '''

class Shopping:
      cart = []
      def add_to_cart(self, item):
            self.cart.append(item)

customer1 = Shopping()
customer1.add_to_cart('T-shirt')
print(customer1.cart)

customer2 = Shopping()
customer2.add_to_cart('Shoes')
print(customer2.cart)
print('\n\n')

''' To solve this problem we have to make a constructor in the class and create the cart attribute inside the constructor. Then, every object from this class will have a separate cart attribute. This is called an instance attribute. '''

class Shopping2:
      def __init__(self):
            self.cart = []

      def add_to_cart_2(self, item):
            self.cart.append(item)

customer01 = Shopping2()
customer01.add_to_cart_2('T-shirt')
print(customer01.cart)

customer02 = Shopping2()
customer02.add_to_cart_2('Shoes')
print(customer02.cart)
print('\n\n')



                                                                                       #''' Banking Software '''#
''' Class methods are functions you can add if-else, loop or any kind of calculation inside it. '''

class Bank:
      def __init__(self):
            self.balance = 10000
            self.minimum_balance = 1000
      
      def get_balance(self):
            return self.balance
      
      def withdraw(self, amount):
            if amount < self.minimum_balance:
                  print('Sorry! You can\'t withdraw less than 1000 BDT')
                  print('Account balance:', self.balance, 'BDT')

            elif amount > self.balance:
                  print('Sorry Sir/Mam! You have', self.balance, 'BDT.', 'You can\'t withdraw more than that from your account.')

            else:
                  print('Previous Balance:', self.balance, 'BDT')
                  print('Withdraw Amount:', amount, 'BDT')
                  self.balance = self.balance - amount
                  print('Current Balance:', self.balance, 'BDT')
                  return amount

myAccount = Bank()

myAccount.withdraw(20000)
print('\n\n')


                                                                                        #''' Inheritance '''#
''' Inheritance is easy to understand. Just think that Bill Gates is your father. If he dies you will get all of his wealth by inheritance. Another example is like, you are running a store where you sell smart phones, smart watches and tablets. '''
''' Smartphones: 1) brand name 2) price 3) video call 4) recharge battery ''' 
''' Smartwatches: 1) brand name 2) price 3) count walking steps 4) heart rate '''
''' tanlets: 1) brand name 2) price 3) can read books 4) play stupic games '''
''' These three smart devices have some attributes in common, like their brand name and price. '''

''' In the below code we created a class named SmartDevice because both the Phone2 and Watch class had a same method named recharge(). So we created the recharge method in the SmartDevice class and passed the SmartDevice through the parameter in the Phone class and Watch class. '''

''' The class you inherit from is called Parent Class and the class that is inheritting is called Child Class. Here SmartDevice is the parent class and Phone2 & Watch are the child classes. '''

class SmartDevice():
      def __init__(self, brand, price):
            self.brand = brand
            self.price = price
      def recharge(self):
            print('Eating electrons')
            print('Electrons are yummy!')

class Phone2(SmartDevice):
      video_call = True
      def __init__(self, brand, price, network):
            SmartDevice.__init__(self, brand, price)
            self.network = network

myPhone2 = Phone2('Samsung', 30000, 'Teletalk')
myPhone2.recharge()

print('\n')

class Watch(SmartDevice):
      def __init__(self, brand, price, has_gps):
            SmartDevice.__init__(self, brand, price)
            self.has_gps = has_gps

myWatch = Watch('Samsung', 20000, True)
myWatch.recharge()
print('\n\n')



                                                                                    #''' Encapsulation '''#
''' While coding you might want to protect some sensitive information from the user so that outsiders can't access or modify your private information. The act of protecting or encapsulating something is called Encapsulation '''

''' While creating a class if you create an attribute which starts with double underscores __ then the attribute will be private and no one will be able to access it from outside. '''

''' Though we can't access the attribute outside of the class but we can do it inside. Like below code, we are using the get_balance method to access the __balance attribute and showing it through the get_balance method '''

class Banking:
      def __init__(self):
            self.name = ''
            self.__balance = 1000
      def get_balance(self):
            return self.__balance
      
account = Banking()
account.name = 'Safkat Jaman'
balance = account.get_balance()
print(account.name, balance)
print('\n\n')



                                                                                    #''' Polymorphism '''#
''' When the code can take many forms. it's called polymorphism. The word poly means many and morph means a change of shape. Here the move method can take many forms. You are calling the move method. based on the class it's on, it calls the right method in the right class. '''

class Car:
      car_name = 'Mercedes'

      def move(self):
            print(self.car_name, 'is moving')

class Truck:
      truck_name = 'Cyber Truck'

      def move(self):
            print(self.truck_name, 'is moving')

class Bike:
      bike_name = 'R15'

      def move(self):
            print(self.bike_name, 'is moving')

vehicles = [Car(), Truck(), Bike()]
for moving in vehicles:
      moving.move()



                                                                                          #''' Summary '''#
''' Use Inheritance to reduce repetition of attributes and methods. To inherit, just pass the parent class to the child class. '''
''' Encapsulation is the process of protecting attributes from outsiders. To create private attributes you will need to use two underscores before the name of the attribute like this, __balance. '''
