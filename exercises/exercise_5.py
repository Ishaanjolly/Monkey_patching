# 1. Write a context manager class called 'TemporaryMonkeyPatch'
# 2. The context manager should apply a patch when entering
# 3. It should restore the original when exiting
# 4. Test it with a simple class and method
from contextlib import contextmanager
from functools import wraps
import inspect
import logging
logging.basicConfig(level=logging.INFO)     


def log_method_call(method):        
    """
    Decorator to log method calls.
    
    Args:
        method: The method to log.
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling method {method.__name__} with args: {args}, kwargs: {kwargs}")
        return method(*args, **kwargs)
    
    return wrapper

        
class SimpleClass:
    """
    A simple class with a method to demonstrate monkey patching.
    """
    
    @log_method_call
    def original_method(self, x):
        return x * 2
    @log_method_call
    def another_method(self, y):
        return y + 3
    
    
def new_method(self, x):
    """
    New method to replace the original method.
    """
    return x * 3 
       
if __name__ == "__main__":  
    # Create an instance of the class
    instance = SimpleClass()
    
    # Call the original method
    result = instance.original_method(5)
    logging.info(f"Original method result: {result}")
    
    
    
    