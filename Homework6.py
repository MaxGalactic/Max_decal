import numpy as np

# Star Temperature Prime Number 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def containsPrimes(arr):
    return np.array([row for row in arr if any(is_prime(x) for x in row)])

arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
print(containsPrimes(arr))

#2.1 Lets Play Checkers

def checkerboard():
    return np.zeros((8, 8), dtype=int)

print(checkerboard())

#2.2 

def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    for row in range(0, 8, 2):  # even rows only (0, 2, 4, 6)
        board[row, ::2] = 1     # set 1s in alternating pattern
    return board

print(checkerboard())

#2.3 

def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    for row in range(8):
        board[row] = [ (row + col) % 2 for col in range(8) ]
    return board

#2.4

def reverse_checkerboard():
    return np.fromfunction(lambda i, j: (i + j + 1) % 2, (8, 8), dtype=int)

print(checkerboard())


#3.1

def expansion(arr, num_spaces):
    spacer = ' ' * num_spaces
    expanded = [spacer.join(list(word)) for word in arr]
    return np.array(expanded)

universe = np.array(['galaxy', 'clusters'])
print(expansion(universe, 1))

#4.1

def secondDimmest(stars):
    return np.sort(stars, axis=0)[1]
np.random.seed(123)
stars = np.random.randint(500, 2000, (5, 5))
print(stars)
print(secondDimmest(stars))



