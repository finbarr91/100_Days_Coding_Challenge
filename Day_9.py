from os import system, name
# # programming_dictionary = {
# #     "Bug": "An error in a program that prevents the program from running as excepted.",
# #     "Function" : "A piece of code that you can easily call over and over again.",
# # }
# #
# # # retrieving items from a dictionary
# # print(programming_dictionary["Bug"])
# # programming_dictionary["Loop"] = "The action of doing something over and over again"
# # print(programming_dictionary)
# #
# # # create an empty dictionary
# # # empty_dictionary = {}
# #
# # # # Wipe an existing dictionary
# # # programming_dictionary ={}
# # # print(programming_dictionary)
# #
# # # Edit an item in a dictionary:
# # programming_dictionary["Bug"] = "A moth in your computer"
# # print(programming_dictionary)
# #
# # # Loop through a dictionary
# # for key in programming_dictionary:
# #     print(key)
# #     print(programming_dictionary[key])
#
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# # TODO-1: Create an empty dictionary called student_grades.
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
# #
# # Scores 91 - 100: Grade = "Outstanding"
# #
# # Scores 81 - 90: Grade = "Exceeds Expectations"
# #
# # Scores 71 - 80: Grade = "Acceptable"
# #
# # Scores 70 or lower: Grade = "Fail"
#
#
# student_grade ={}
#
# # for student in student_scores:
# #     score = student_scores[student]
# #     if score > 90:
# #         student_grade[student] ="Outstanding"
# #     elif score>80:
# #         student_grade[student] = "Exceeds Expectations"
# #     elif score>70:
# #         student_grade[student] = "Acceptable"
# #     else:
# #         student_grade[student] = "Fail"
# # print(student_grade)
#
# # scores = [j for i,j in student_scores.items()]
# # print(scores)
# # students = [i for i,j in student_scores.items()]
# # print(students)
# #
# # for student in students:
# #     score = student_scores[student]
# #     if score >90:
# #         student_grade[student] ="Outstanding"
# #     elif score>80:
# #         student_grade[student] = "Exceeds Expectations"
# #     elif score>70:
# #         student_grade[student] = "Acceptable"
# #     else:
# #         student_grade[student] = "Fail"
# # print(student_grade)
#
# # # Nesting
# # capitals = {
# #     "France":"Paris",
# #     "Germany" : "Berlin"
# #             }
# #
# # # Nesting a list in a Dictionary
# # travel_log = {
# #     "France" : ["Paris", "Lille", "Dijon"],
# #     "Germany" : ["Berlin", "Hamburg", "Stuttgart"]
# # }
# #
# # # Nesting a Dictionary in a Dictionary
# # destination_log = { "France" : {"citiest_visited":["Paris", "Lille", "Dijon"], "total_visit": 12},
# #                     "Germany" : {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visit":5}
# #               }
# #
# # # Nesting a Dictionary in a list
# #
# # travel_log_EU =[
# #     {"country":"France",
# #      "cities_visited":["Paris", "Lille", "Dijon"],
# #      "total_visit": 12},
# #
# # {"country" : "Germany",
# #  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
# #  "total_visit":5},
# # ]
# # print(travel_log_EU)
#
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
#
# def add_new_country(country_visited,times_visited,cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)
#
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
#

# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')

# Then, whenever you want to clear the screen, just use this clear function as:
x= 4+5
print(x)

clear()

y = 2+3
print(y)
