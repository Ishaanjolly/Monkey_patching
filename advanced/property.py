class Person: 
    def __init__(self, first_name, last_name): 
        self.first_name = first_name 
        self.last_name = last_name 
        
def full_name_getter(self):
    return f"{self.first_name} {self.last_name}"

Person.full_name = property(full_name_getter)

person = Person("John", "Doe")
print(f"Full name: {person.full_name}")
print(f"First name: {person.first_name}") 
print(f"Last name: {person.last_name}")


