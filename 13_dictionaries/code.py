# Dictionaries
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

friend_ages['Bob'] = 20 #crea o actualiza

print(friend_ages['Adam']) #get [key,value]

print(friend_ages)

friend = [
    {"name": "Rolf", "age": 30},
    {"name": "Adam", "age": 40},
]

print(friend[0])
print(friend[0]["name"])

student_attendance = {"Pedro": 96, "Juan": 80, "Diego": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")
    
for item1, item2 in student_attendance.items(): #destructurar
    print(f"{item1}: {item2}")
    
    
if "Juan" in student_attendance:
    print("existe")
else:
    print("No existe en este listado")
    
    
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))

#Quiz
my_dictionary = {'a': 1, 'b': 2, 'c': 3}
items = list(my_dictionary.items())
print(items)