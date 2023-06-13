from plates import is_valid

def main():
    test_valid1()
    test_valid2()
    test_valid3()
    test_valid4()


def test_valid1():
    assert is_valid("a") == False
    assert is_valid("Hello, World") == False
    assert is_valid("Harvard") == False
    assert is_valid("CS50") == True

def test_valid2():
    assert is_valid("123") == False
    assert is_valid("CS50") == True

def test_valid3():
    assert is_valid("cs.,12") == False
    assert is_valid("CS50") == True

def test_valid4():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False