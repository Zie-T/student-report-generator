#fruits = ["apple", "banana", "mango", "orange", "grape"]
#print(fruits[2])
#fruits.append("strawberry")
#print(fruits)
#fruits.remove("banana")
#print(fruits)
#fruits.reverse()
#print(len(fruits))

# coordinates = (10, 20, 30, 40, 50)
# print(coordinates[0])
# print(coordinates[-1])
# print(len(coordinates))
# print(30 in coordinates)
# coordinates[1] = 99 #"object does not support item assignement"

# user = {
#     "name": "John",
#     "age": 25,
#     "email": "john@gmail.com",
#     "city": "Cape Town"
# }
# print(user["name"])
# user["age" ] = 26
# user["country"] = "South Africa"
# del user["email"]
# print(user.keys())
# print(user)

#SETS


#list comprehension

# names = ["alice", "bob", "charlie", "diana", "eve"]

# upper_names = [n.upper() for n in names]
# print(upper_names)

# long_names = [n for n in names if len(n) > 3]
# print(long_names)

# products = {
#     "bread": 15,
#     "shoes": 450,
#     "phone": 2500,
#     "milk": 22,
#     "headphones": 350
# }
# for product, price in products.items():
#     if  price > 200 :
#         print(product, price)

#2
# tudents = {
#     "Zee": 85,
#     "John": 42,
#     "Lebo": 91,
#     "Mike": 38,
#     "Sara": 67
# }

# total_passed = 0
# for name, mark in students.items():
#     if mark >= 50:
#         total_passed += 1
#         print(f"{name} passed with {mark}%")

# print(f"\nTotal students passed: {total_passed}")s

# students = {
#     "Zee": 85,
#     "John": 42,
#     "Lebo": 91,
#     "Mike": 38,
#     "Sara": 67
# }

# passed = [name for name, mark in students.items() if mark >= 50]
# print(passed)