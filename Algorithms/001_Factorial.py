import timeit


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


def fun_timer(fun, n):
    """Measure the running time of "fun" with an input argument n."""
    tic = timeit.default_timer()
    n_fac = fun(n)
    toc = timeit.default_timer()
    return n_fac, toc - tic


# ============== #
# The main code  #
# ============== #

n = input("Enter an Natural number to find its factorial: ")
n = int(n)

fac_r1 = fun_timer(factorial_r1, n)
fac_r2 = fun_timer(factorial_r2, n)
fac_loop = fun_timer(factorial_loop, n)

print("Recursive method 1: {}, \t sec elapsed {}".format(fac_r1[0], fac_r1[1]))
print("Recursive method 2: {}, \t sec elapsed {}".format(fac_r2[0], fac_r2[1]))
print("Loop method: {}, \t sec elapsed {}".format(fac_loop[0], fac_loop[1]))
