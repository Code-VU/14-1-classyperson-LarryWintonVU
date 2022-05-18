'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''

class Person :
    name = ""
    age = 0

    def __init__(self, input_name, input_age) :
        self.name = input_name
        self.age = input_age
        print(self.name, self.age)

    def increase_age(self) :
        self.age = self.age + 1
        print(self.age)

    def say_greeting(self) :
        print('Hello world! My name is {0}!', self.name )

    def count_to_age(self) :
        print('do a loop to count from 1 to self.age')
        for num in range (1,self.age+1) :
            print(num)


# You won't need to call anything here.