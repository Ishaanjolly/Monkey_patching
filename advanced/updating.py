"""
updating built in attributes such as list, dict, etc are not possible using 
monkey patching 
"""
import time 
original_list_append = list.append

def timing_append(self, item):
    """Wrapper that times list.append operations"""
    start_time = time.time()
    result = original_list_append(self, item)
    end_time = time.time()
    print(f"Time taken to append {item}: {end_time - start_time:.6f} seconds")
    return result


list.append = timing_append

for i in range(5):
    my_list = []
    my_list.append(i)


## This would not work!

