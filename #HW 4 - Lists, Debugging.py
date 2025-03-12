#HW 4 - Lists, Debugging

#2 Sliding and Striding

#2.1 - making a list variable
Radioheads = list(range(21))
print(Radioheads)

#2.2 - working with list elements 

Radioheads = list(range(21))

def square_list(numbers):
    return [num **2 for num in numbers]
Radioheads = list(range(21))
Radioheads_squared = square_list(Radioheads)
print(Radioheads_squared)
# I received the error square_list() was not defined, so i fixed it by defining sqare list relative to Radioheads

#2.3 - slicing 

def first_15_elements(numbers):
    return numbers[:15]
first_15 = first_15_elements(Radioheads_squared)
print(first_15)

#2.4 - striding

def every_5th_element(numbers):
    return numbers[4::5]
every_5th = every_5th_element(Radioheads_squared)
print(every_5th)
# I encountered an error at first as I started from 0, not from  16, which is the 4th number in the list

#2.5 - slicing and striding 

def every_third_element(numbers):
    return numbers [3:][::-3]
Radioheads_every_three = every_third_element(Radioheads_squared)
print(Radioheads_every_three)

#3 - 2D lists

#3.1 - creating a 5x5 list

def create_2d_list():
    return [[col + row * 5 + 1 for col in range(5)] for row in range(5)]
matrix = create_2d_list()
for row in matrix:
    print(row)

#3.2 - Replacing a 2D List with Multiples of 3

def modified_2d_list(matrix):
    return [["?" if num % 3 == 0 else num for num in row] for row in matrix]
modified_matrix = modified_2d_list(matrix)
for row in modified_matrix:
    print(row)
#The error i recieved was that I did not def midified_2d_list relative to the matrix I made in 3.1

#3.3 - Summing None-'?' elements

def sum_non_question_elements(matrix):
    return sum(num for row in matrix for num in row if num != "?")
total_sum = sum_non_question_elements(modified_matrix)

print(total_sum)


      





