# Name: Yilun Dai
import math
import random
# hw3.py

##### Template for Homework 3, exercises 1 -  ######


# ********** Exercise 1 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####
def is_divisible(m, n):
    if n != 0:
        result = m % n
        answer = result == 0
    else:
        answer = "division by 0"
    return answer




# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print(is_divisible(10, 5))  # This should return True
print(is_divisible(18, 7))  # This should return False
print(is_divisible(42, 0)) # What should this return?

# ********** Exercise 2 ********** 

# Define not_equal function here
##### YOUR CODE HERE #####
def not_equal(a, b):
    if a == b:
        return False
    else:
        return True


# Test cases for not_equal
##### YOUR CODE HERE #####
print(not_equal(1018, 1121))
print(not_equal(95, 95))
print(not_equal('tiger', 'cat'))
print(not_equal('cat', 'cat'))
print(not_equal([0, 2, 4, 6], [0, 2, 4]))
print(not_equal([0, 1], [0, 1]))
print(not_equal([], []))

# ********** Exercise 3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####
def multadd(a, b, c):
    result = a * b + c
    return result

## 2 - Equations
##### YOUR CODE HERE #####
angle_test = multadd(math.cos(math.pi / 4.0), 0.5, math.sin(math.pi / 4.0))
ceiling_test = multadd(math.log(12, 7), 2, math.ceil(276/19))

# Test Cases
angle_test = multadd(math.cos(math.pi / 4.0), 0.5, math.sin(math.pi / 4.0))
print("sin(pi/4) + cos(pi/4)/2 is:")
print(angle_test)

ceiling_test = multadd(math.log(12, 7), 2, math.ceil(276/19))
print("ceiling(276/19) + 2 log_7(12) is:")
print(ceiling_test)


# ********** Exercise 4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
def rand_divis_3():
    random_number = random.randint(0,100)
    print("The number generated is: ", random_number)
    result = random_number % 3
    answer = result == 0
    return answer

# Test Cases
##### YOUR CODE HERE #####

print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())
