from jar import Jar

def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(7)
    assert jar.size == 10
    jar.deposit(1)
    assert jar.size == 11


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(3)
    assert jar.size == 8
    jar.withdraw(2)
    assert jar.size == 6
    jar.withdraw(4)
    assert jar.size == 2