# LAB_FUNCTIONS_101

## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

# **Example Output for `5`**
# ```
# 5 4 3 2 1   
# 4 3 2 1   
# 3 2 1   
# 2 1   
# 1   
# ```

#### Document the newly created function. describe what it does, then print the documentation. 


# Bonus
# Rewrite the previous function so that it returns the pattern as a string, then assign the result to a variables and print it.


def print_pattern(n: int):
    """
    This function takes an integer number and prints a pattern.
    For example, if the number is = 5, it prints:
    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1
    1
    """
    n = 5
    for i in range(n, 0, -1):
        line = ""  
        for j in range(i, 0, -1):
            line = line + str(j) + " " 
        print(line) 
print(print_pattern.__doc__)

print_pattern(5)

