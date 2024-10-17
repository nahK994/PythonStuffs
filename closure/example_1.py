def make_multiplier(factor):
    def multiplier(number):
        return number * factor  # Accesses 'factor' from the outer function
    return multiplier  # Returns the inner function

multiply_by_2 = make_multiplier(2)
multiply_by_5 = make_multiplier(5)

print(multiply_by_2(10))
print(multiply_by_5(10))
