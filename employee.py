class Employee:

    def __init__(self):
        print("The employee is created")

    def __del__(self):
        print("Delete is called")

def creating_obj():
    print("Creating the object")
    obj = Employee()
    print("Finding object")

obj = creating_obj()
print("program finished")





