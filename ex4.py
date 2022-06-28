cars = 100 
space_in_a_car = 4.0 
drivers = 30
people = 90 
empty_cars = cars - drivers 
capacity = drivers * space_in_a_car
avg_people_per_car = people/drivers

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", empty_cars ,"empty cars today ")
print("we can transport", capacity ,"people today ")
print("we have",people , "to carpool today")
print("we need to put about",avg_people_per_car, "in each car")

'''
There will be x empty cars today 

we have x to carpool today 

'''