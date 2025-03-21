#HW 5 - Review

#1 HW1/HW2 Review: Terminal + Command Line + Git

#1.1 - You would use the command "pwd" meaning print working diretory.
#1.2 - You would use the command "ls".
#1.3 - You would cd to python_decal then cd to Brianna_repo where the howmwork is at. Then, you pull these changes from git hub to your computer using git pull origin main.
#1.4 - You copy/clone the updated file (cp) and then move (mv) the homework through the correct path.Then you do the commands git add, git commit, git push origin main/master which will save the changes to your repository.
#1.5 - You would use the command cat along with the name of the file
#1.6 - You would use nano to edit the contents of homewokr.py in your terminal.
#1.7 - You do git add, git commit, git push origin main/master (which pushes the changes you made to the file to git)
#1.8 - You would do git pull origin main, potentially if there are any conflicts do git add and then git commit, finally do git push origin main.
#1.9 - It would just be the command cd then its aboslute path.

#2 HW3 Review; Data Types + Functions + Conditionals + Loops 

#2.1 - Data Types

def checkDataType(value):
    return type(value).__name__

print(checkDataType(3.14))
print(checkDataType(True))

#2.2 - Conditonals 
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "odd"

#3 Loops 

def sumWithLoop(numbers):
    total = 0 
    for num in numbers:
        total += num
    return total
numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))

#4 HW4 Review: Lists 

#4.1 Lists

def duplicateList(input_list):
    result = []
    for item in input_list:
        result.append(item)
        result.append(item)
    return result

test_list = ['a', 'b', 'c']
print(duplicateList(test_list))

#4.2 Debugging 

def square(num):
    return num * num

num = 2
print(square(num))


