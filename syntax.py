'''
******* For noting some useful syntax in python ***********
'''

# ***************************** zip function **************************************
friends = ["Jane", "Alice", "Bob", "Ham"]
age = [23, 30, 25, 27, 29]

combined_list = list(zip(friends, age))   # output will be [('Jane', 23), ('Alice', 30), ('Bob', 25), ('Ham', 27)]
friends_info = dict(zip(friends, age))  # output will be a dictionary


# ****************************************** lambda function ***************************************************

def divide(x, y):
    return x/y

#   this can be rewritten using lambda function like;

divide = lambda x,y: x/y


# ***************************** First class and Higher order function **************************************

def before_and_after(func):
    print("Before..")
    func()
    print("After..")


def hello():
    print("Hello, World")


#   before_and_after is a higher order function it takes another function as an argument)
#   while hello is a first class function, before_and_after is also a first class function

#   application

operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": sum,
    "top": max
}

students = [
    {"name": "jake", "grades":(67, 55, 75, 98)},
    {"name": "Ken", "grades": (97, 85, 60, 100)},
    {"name": "Jane", "grades": (88, 99, 70, 94)},
    {"name": "Bob", "grades": (80, 100, 92, 90)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top': ")

    result = operations[operation](grades)
    print(result)