from Calculator import Calculator

# tests addition method in calculator 
def test_add():
    x, y = 1,2
    calc = Calculator(1,2)
    
    assert calc.add() == x + y, "Error in add method"

# tests subtract method 
def test_subtract():
    x,y = 1,2 
    calc = Calculator(1,2)
    
    assert calc.subtract() == x-y, "Error in subtract method"
    
