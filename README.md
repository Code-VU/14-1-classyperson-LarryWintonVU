# Object Oriented Programming

You've learned how to make a Python class that has its own values, methods and initializes its values.

## Assignment:

### Build a class called `Person`
This class should have a constructor that takes in a name and age and sets its values accordingly.

This class should have 4 methods:
1. `__init__` method that passed name and age to itself.
2. `increase_age` method that increases the object's age by 1
3. `say_greeting` method that prints out:
    ```Hello world! My name is { objects_name }!```
4. `count_to_age` method that prints 1 to the current age of the object as a loop.


### Expected output
I'll be construction an object with your class. If the object I made is `nathan = Person(32, "Nathan")` I would expect:

print(nathan.age)
```
32
```


nathan.say_greeting()
```
Hello world! My name is Nathan!
```


nathan.increase_age()

print(nathan.age)
```
33
```


nathan.count_to_age()
```
1
2
... (numbers 3-32)
33
```