from calculator.operations import add, subtract, multiply, divide

class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def get_result(self):

        return self.operation(self.a, self.b)
    
class Calculator: 
    @staticmethod
    def add(a,b):
        calculation = Calculation(a, b, add)
        return calculation.get_result()
    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a, b, subtract)
        return calculation.get_result()
    @staticmethod
    def multiply (a,b):
        calculation = Calculation(a, b, multiply)
        return calculation.get_result()
    @staticmethod
    def divide(a,b):
        calculation = Calculation(a, b, divide)
        return calculation.get_result()