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
