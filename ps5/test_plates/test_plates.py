import sys
from plates import is_valid

def main():
    test_valid()


def test_valid():
    try:
        assert is_valid("ABC12") == True
        assert is_valid("ABCDEFGHIJK") == False
        assert is_valid("F") == False
        assert is_valid("ADE45A") == False
        assert is_valid("ABCD") == True
        assert is_valid("zz055") == False
        assert is_valid("xyz.5") == False
        assert is_valid("A1234") == False

    except AssertionError:
        sys.exit(-1)


if __name__ == "__main__":
    main()