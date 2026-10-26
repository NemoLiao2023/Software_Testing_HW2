class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def pow(self, a, b):
        if a == 0 and b == 0:
            raise ValueError("0 to the power of 0 is undefined")
        return a ** b
