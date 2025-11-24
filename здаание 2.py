# a= input("Введите число:")
# a_numbers = a.split()
# numbers = []
# for s in a_numbers:
#     numbers.append(int(s))
# unique_sorted = sorted(set(numbers))
# print ("toto",unique_sorted )
    
    
student = [
    {"name": "Aleksei", "age":"20","ocenki" : [5,5,5]},
    {"name": "Vadim", "age":"21","ocenki" : [5,4,5]},
    {"name": "AleElenaksei", "age":"22","ocenki" : [5,5,3]},
]
print ("список", student)
for s in student:
    print (f"{student['name']}, возраст: {student['age']}, оценки: {student['ocenki']}") 