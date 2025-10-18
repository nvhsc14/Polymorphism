class Vehicle:
    def describe(self):
        print("This is a generic vehicle.")

class Car(Vehicle):
    print("This is a sporty car.")

class Motorcycle(Vehicle):
    def describe(self):
        print("This is a fast motorcycle.")

#Make objects from each class
v = Vehicle()
cr = Car()
mcycle = Motorcycle()

# Call the describe method on different objects
v.describe()
cr.describe()
mcycle.describe()
