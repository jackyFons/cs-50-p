import sys
from seasons import validate, num_to_words
import pytest


def main():
    test_num_to_words()


def test_num_to_words():
    try:
        assert num_to_words(100) == "One hundred"
    except AssertionError:
        sys.exit(-1)


if __name__ == "__main__":
    main()