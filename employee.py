class Employee:

    def __init__(self):
        print("Employee Created")

    def __del__(self):
        print("Destructor called")

print("Making object...")
obj = Employee()
print("Deleting object...")
del obj
print("Employee deleted")

print("\n\n\nThe object no longer exists, so when we call it we get:\n")
print(obj)