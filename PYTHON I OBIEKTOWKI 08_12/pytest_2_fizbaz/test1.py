from kod1 import fizzbuss

def test_fizzbuss_basic():
    assert fizzbuss(1) == 1
    assert fizzbuss(2) == 2

def test_fizzbuss_Fizz():
    assert fizzbuss(3) == 'Fizz'
    assert fizzbuss(9) == 'Fizz'
    assert fizzbuss(12) == 'Fizz'

def test_fizzbuss_Buzz():
    assert fizzbuss(5) == 'Buzz'
    assert fizzbuss(10) == 'Buzz'
    assert fizzbuss(35) == 'Buzz'

def test_fizzbuss_FizzBuzz():
    assert fizzbuss(15) == 'FizzBuzz'
    assert fizzbuss(45) == 'FizzBuzz'
    assert fizzbuss(150) == 'FizzBuzz'

def test_fizzbuzz_string():
    assert fizzbuss('Mama') == None

