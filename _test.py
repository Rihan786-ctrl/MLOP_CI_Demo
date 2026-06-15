import pytest

# Function to test square

def square(number):
    return number ** 2

# fun to test cube

def cube(number):
    return number ** 3

# fun to test fourth power

def fourth_power(number):
    return number ** 4

# Test sq fun
def test_square():
    assert square(2) == 4, "Test Failed: Square of 2 should be 4"
    assert square(3) == 9, "Test Failed: Square of 3 should be 9"

# Test cube fun 
def test_cube():
    assert cube(2) == 8, "Test Failed: Cube of 2 should be 8"
    assert cube(3) == 27, "Test Failed: Cube of 3 should be 27"

# Test fourth power fun
def test_fourth_power():
    assert fourth_power(2) == 16, "Test Failed: Fourth power of 2 should be 16"
    assert fourth_power(3) == 81, "Test Failed: Fourth power of 3 should be 81"


# test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("a")
    with pytest.raises(TypeError):
        cube("a")
    with pytest.raises(TypeError):
        fourth_power("a")


