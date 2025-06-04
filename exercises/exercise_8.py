""" 
pandas monkey patching test
"""

import pandas as pd
import numpy as np


df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'salary': [50000, 60000, 70000, 55000],
    'department': ['Engineering', 'Marketing', 'Engineering', 'Sales']
})

def new_info(self):
    """Get a quick summary of the DataFrame"""
    return pd.Series({
        'shape': self.shape,
        'columns': list(self.columns),
        'missing_values': self.isnull().sum().sum(),
        'memory_usage': f"{self.memory_usage(deep=True).sum() / 1024:.2f} KB"
    })

pd.DataFrame.info = new_info

def safe_monkey_patch(cls, method_name, method):
    """Safely add a method to a class"""
    if hasattr(cls, method_name):
        print(f"Warning: Method '{method_name}' already exists in {cls.__name__}")
        return False
    else:
        setattr(cls, method_name, method)
        print(f"Successfully added '{method_name}' to {cls.__name__}")
        return True

def custom_describe(self):
    """Custom describe method"""
    return f"Custom description: {self.shape[0]} rows, {self.shape[1]} columns"


safe_monkey_patch(pd.DataFrame, 'custom_describe', custom_describe)

