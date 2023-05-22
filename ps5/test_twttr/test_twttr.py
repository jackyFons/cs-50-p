from twttr import shorten
import sys


def main():
    tests()


def tests():
    try:
        assert shorten("twitter") == "twttr"
        assert shorten("test cAse") == "tst cs"
        assert shorten("Hello world") == "Hll wrld"
        assert shorten("this is. cs50") == "ths s. cs50"
    except AssertionError:
        sys.exit(-1)


if __name__ == "__main__":
    main()