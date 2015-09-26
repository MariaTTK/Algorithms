__author__ = 'Maria'
import numpy as np
import time

x = np.random.randint(1,10,1000) # np.random.random_integers(low, high, size)
print(x)
# x = [28, 0, 3, 12]

def get_products_of_all_ints_except_at_index(int_array):

    # we make an array with the length of the input array to
    # hold our products
    products_of_all_ints_except_at_index = [1] * len(int_array)

    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product = 1
    i = 0
    while i < len(int_array):
        products_of_all_ints_except_at_index[i] = product
        product *= int_array[i]
        i += 1

    # for each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product = 1
    i = len(int_array) - 1
    while i >= 0:
        products_of_all_ints_except_at_index[i] *= product
        product *= int_array[i]
        i -= 1

    return products_of_all_ints_except_at_index

start = time.time()
print(get_products_of_all_ints_except_at_index(x))
end = time.time()
print("Time elapsed: ", end - start)
