# Creating a file with a a test funcion to test another function functionality

# add function
def add(a,b):
    return a+b

# test function for testing
def test_add():
    assert add(2,3) == 5 # assert keyword