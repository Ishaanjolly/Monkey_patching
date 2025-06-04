# 1. Import the 'random' module
# 2. Replace random.randint to always return a specific number
# 3. Test that the behavior is predictable now
# 4. Remember to restore the original function when done!

import random

original_randint = random.randint

def fixed_randint(a, b):
    return 42

random.randint = fixed_randint
   
result = random.randint(1, 100)

print(f"Result after monkey patching: {result}")  

random.randint = original_randint

result = random.randint(1, 100)
print(f"Result after restoring: {result}")  