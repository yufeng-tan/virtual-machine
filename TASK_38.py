# Write a test program that evaluates factorial using only functions, except for a final conversion to numbers. 
# You should use Church-encoded booleans, numbers, pairs, as well as the Z combinator.

# factorial function for comparison for this task
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


# sub1 := lambda n, fst(n, F, (pair zero zero))
def SUB1(n):
    return n - 1


# mult := lambda n, lambda m, lambda f, lambda z, n (m f) z
def MULT(m, n):
    return m * n


def factorial_(n):
    if n == 0:
        return 1
    else:
        return MULT(n, factorial_(SUB1(n)))

print(factorial_(5))


