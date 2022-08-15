def factorial_r1(n):
    """Calculate the factorial of (n) recursively by checking the ending condition."""
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_r1(n - 1)


def factorial_r2(n):
    """Calculate the factorial of (n) recursively by checking the continuation condition."""
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_r1(n - 1)


def factorial_loop(n):
    """Calculate the factorial of (n) by means of a while loop."""
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


# ============== #
# The main code  #
# ============== #

n = input("Enter an Natural number to find its factorial: ")
n = int(n)
print("Recursvive method 1: {}".format(factorial_r1(n)))
print("Recursvive method 2: {}".format(factorial_r2(n)))
print("Loop method: {}".format(factorial_loop(n)))
