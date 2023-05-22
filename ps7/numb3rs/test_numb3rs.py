import sys
from numb3rs import validate


def main():
    test_validate()


def test_validate():
    try:
        assert validate("1.2.3.4") == True
        assert validate("1.4") == False
        assert validate("1.2.300.4") == False
        assert validate("1.2.3.4.2") == False

    except AssertionError:
        sys.exit(-1)


if __name__ == "__main__":
    main()