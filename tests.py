# Special execution
# $ python -i filename.py

# RANGE and lists
numbers = list(range(1, 10))
contains_3 = 3 in numbers

# COPY LISTS by REFERENCE AND VALUE
copy_reference = numbers
copy_value = numbers[:]
copy_numbers = numbers.copy()

# COMPREHENSIONS
squares = []
for x in range(11):
    squares.append(x ** 2)

squares_com = [x ** 2 for x in range(11)]

# DICTIONARIES
alien = {
    'color': 'grenn',
    'age': '2022',
    'points': 5,
    'coords': [234, 534, 345]
}

# How to loop over a dictionary
for key, value in alien.items():
    print(f"{key} == {value}")
length = len(alien)

# ARRAYS => LISTS in Python
a1 = [1, 2, 3, 4, 5]
a2 = [[1, 2, 3], [4, 5, 6], 88]
a2_value = a2[1][2]


# Function
def my_func(a, b):
    c = a ** 2
    print(c)
    return a ** 2 + b

def second_function():
    print('This is a test message')
