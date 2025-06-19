

# Bonus
# Rewrite the previous function so that it returns the pattern as a string, then assign the result to a variables and print it.



def get_pattern(n):
    """
    This function takes a number `n` and returns a pattern string:
    For example, for n = 5:
    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1
    1
    """
    result = ""
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            result = result + str(j) + " " 
        result  = result + "\n"  
    return result

pattern = get_pattern(5)
print(pattern)
