__author__ = 'Maria'

import numpy as np
import time
x = list(np.random.randint(1,10,10))
# x = [28, 0, 3, 12]
product = []


def product_of_indeges_without_current_index(a):
    for index in range(len(a)):
        temp = a[index]
        a[index] = 1
        product.append(np.prod(a))
        a[index] = temp
    return product

start = time.time()
print(product_of_indeges_without_current_index(x))
end = time.time()
print("Time elapsed: ", end - start)
