# 1. Create a Calculator class with an 'add' method
# 2. Test the original method
# 3. Replace the 'add' method with a new version that multiplies instead
# 4. Verify the behavior has changed

class Calculator: 
    def __init__ (self, a,b):
        self.a = a 
        self.b = b 
    
    def add(self): 
        self.c = self.a + self.b
        return self.c 
    
def multiply(self): 
    """patching function"""
    self.c = self.a * self.b
    
    return self.c 

Calculator.add = multiply
    
    
if __name__ == "__main__": 
    a = 5 
    b = 3 
    c = Calculator(a, b).add()
   