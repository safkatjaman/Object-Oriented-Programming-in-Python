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