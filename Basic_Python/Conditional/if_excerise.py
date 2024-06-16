# Write a program to find even or odd:

# n = input("Enter Your Number: ")
# n = int(n)
#
# if n % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

#if-elif

# indian = ['samosa', 'poha', 'jalebi']
# italian = ['pasta', 'pizza', 'risotto']
# mexican = ['french fries', 'toco', 'burger']
#
# dish = input("Enter your dish name: ")
#
# if dish in indian:
#     print(f"{dish} is indian")
# elif dish in italian:
#     print(f"{dish} is italian")
# elif dish in mexican:
#     print(f"{dish} is mexican")
# else:
#     print("I dont know this cusine:")

#Even Odd Using Tenary Operator -

# n = input("Enter Your Number: ")
# n = int(n)
#
# message = "Number is Even" if n % 2 == 0 else "Number is Odd"
# print(message)

# BMI - Category -

# height = input("Enter your height in meter: ")
# weight = input("Enter your weight in KG: ")
# height = int(height)
# weight = float(weight)
#
# BMI = weight / (height**2)
# print(BMI)
#
# if BMI > 30:
#     print("Obesity")
# elif BMI > 25 and BMI < 29:
#     print("Overweight")
# elif BMI > 18 and BMI < 25.5:
#     print("Normal")
# elif BMI > 18.5:
#     print("Underweight")

#
# India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
# USA = ["New York","Chicago","Las Vegas", "San Francisco"]
# UK = ["London", "Manchester", "Liverpool", "Nottingham"]
#
# city = input("Enter your first city name: ")
# city_one = input("Enter your second city name: ")
#
# if city in India and city_one in India:
#     print(f"{city} and {city_one}Both are in same city")
# elif city in USA and city_one in USA:
#     print(f"{city} and {city_one}Both are in same city")
# elif city in UK and city_one in UK:
#     print(f"{city} and {city_one}Both are in same city")
# else:
#     print("Both city are not same")