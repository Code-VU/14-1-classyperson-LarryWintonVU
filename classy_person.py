'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''

class Person:
    name = ""
    age = 0

    def __init__(self, input_age: int, input_name: str) :
        self.age = int(input_age)
        self.name = input_name

    def increase_age(self) :
        self.age += 1

    def say_greeting(self) :
        print('Hello world! My name is {0}!'.format(self.name))

    def count_to_age(self) :
        # print numbers 1 to the current age of the object 
        for num in range (1, self.age+1) :
            print(num)


# You won't need to call anything here.
