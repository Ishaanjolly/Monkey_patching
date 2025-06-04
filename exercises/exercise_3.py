import numpy as np 

class Bugged: 
    def func(self, a,b): 
        a_arr = np.array(self.a)
        b_arr = np.array(self.b)
        return a_arr - b_arr 
    
def new_func(self, a,b): 
    return a + b 

Bugged.func = new_func

if __name__ == "__main__":
    bugged_instance = Bugged()
    result = bugged_instance.func(5, 3)
    print(f"Result after monkey patching: {result}")  
        
        