'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''

import unittest
import io
import sys

class Person:
    name = ""
    age = 0

    def __init__(self, input_age: int, input_name: str) :
        try :
            self.age = int(input_age)
        except :
            print('Age input was not an integer number.')
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
class TestPersonMethods(unittest.TestCase) :
    def test_age(self):
        larry = Person(10, 'Larry Winton')
        self.assertEqual(larry.age, 10)

    def test_age_nan(self):
        larry = Person('NaN', 'Larry Winton')
        self.assertNotEqual(larry.age, 'NaN')

    def test_increase_age(self) :
        larry = Person(10, 'Larry Winton')
        larry.increase_age()
        self.assertEqual(larry.age, 11)

    def test_say_greeting(self) :
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        larry = Person(10, 'Larry Winton')
        larry.say_greeting()
        sys.stdout = sys.__stdout__
        self.assertTrue('Larry Winton' in capturedOutput.getvalue())

    def test_count_to_age(self) :
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        larry = Person(10, 'Larry Winton')
        larry.count_to_age()
        sys.stdout = sys.__stdout__
        self.assertTrue('10' in capturedOutput.getvalue())        

# comment out for submission to class assignment
# if __name__ == '__main__' :
#     unittest.main()