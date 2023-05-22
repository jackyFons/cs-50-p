import sys
from bank import value

def main():
    test_value()


def test_value():
    try:
        assert value("hello") == 0
        assert value("Hello Bank") == 0
        assert value("hey") == 20
        assert value("This greeting doesn't start with h") == 100
    except AssertionError:
        sys.exit(-1)


if __name__ == "__main__":
    main()