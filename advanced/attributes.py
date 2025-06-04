class MathOperations:
    def __init__(self, value):
        self.value = value

# Dynamically add mathematical operations
operations = {
    'add': lambda self, x: self.value + x,
    'subtract': lambda self, x: self.value - x,
    'multiply': lambda self, x: self.value * x,
    'divide': lambda self, x: self.value / x if x != 0 else float('inf'),
    'power': lambda self, x: self.value ** x,
    'modulo': lambda self, x: self.value % x if x != 0 else 0
}

for op_name, op_func in operations.items():
    setattr(MathOperations, op_name, op_func)
    
math_obj = MathOperations(10)
print(f"10 + 5 = {math_obj.add(5)}")
print(f"10 * 3 = {math_obj.multiply(3)}")
print(f"10 ** 2 = {math_obj.power(2)}")