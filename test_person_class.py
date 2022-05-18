from classy_person import Person

def test_person_class(capfd):
    chuck = Person(56, 'Charles R. Severance')
    print(chuck.age)

    chuck.increase_age()
    print(chuck.age)
    
    chuck.say_greeting()
    chuck.count_to_age()

    out, err = capfd.readouterr()
    assert "56" in out[0:3]
    assert "57" in out[3:5]
    assert "Hello world! My name is Charles R. Severance!" in out

    for num in range(1,58):
        assert str(num) in out