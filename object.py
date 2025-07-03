class student:
    grade = 10
    print("Hi I am student of grade ", grade)
ob = student()


class Vehicle:
    def __init__(self, max_speed, mileage):  # Fixed: double underscores
        self.max_speed = max_speed
        self.mileage = mileage

model1 = Vehicle(240, 18)
print("Model max speed:", model1.max_speed)
print("Model mileage:", model1.mileage)





class Parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
blu = Parrot("Blu", 10)
woo = Parrot("Woo",15)
print("blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))
print("{} is {} years old ".format(blu.name, blu.age))
print("{} is {} mins old ".format(woo.name, woo.age))

