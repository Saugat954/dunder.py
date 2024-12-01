class Employee:
    def __init__(self, name):
        self.name = name 

    # __str__ is used for a human-readable string representation
    def __str__(self):
        return f"Employee Name: {self.name}"

    # __repr__ is used for an unambiguous string representation, useful for debugging
    def __repr__(self):
        return f"Employee('{self.name}')"
    
    # __call__ allows the object to be called like a function
    def __call__(self, new_name):
        self.name = new_name
        print(f"Employee's name has been changed to: {self.name}")

# Create an instance of Employee
e = Employee("Saugat")

# Using __str__ when printing the object
print(e)  # This uses the __str__ method

# Using __repr__ when using repr() or in the interactive shell
print(repr(e))  # This uses the __repr__ method

# Using __call__ to change the employee's name
e("John")  # This calls the __call__ method
print(e)  # Print again to see the updated name