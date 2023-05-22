import pytest
from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("4/4") == 100
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("a/b")


def test_gauge():
    assert gauge(40) == "40%"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"


if __name__ == "__main__":
    main()