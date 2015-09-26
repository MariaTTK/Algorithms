import numpy as np
import time


def max_product_real(x):
    prod_seq_lists = [[x[0], x[1]]]  # Start assuming the first 2 elements have max product and save them in a list
    product_result = []  # Contains the product of each list


    for e in x[2:]:  # Start for loop from 3rd element
        if x[0] == 0 or x[1] == 0 or e == 0:  # Raise error if there's a 0
            raise IndexError('Found 0')

        temp_b = np.prod(prod_seq_lists[-1])  # Calculate the product of the last list in max_prod_seq
        temp_a = temp_b * e  # Multiply the new_element

        if temp_a >= temp_b:  # If last_list*new_element >= last_list
            prod_seq_lists[-1].append(e)  # Append the new_element in your last_list

            if e == x[-1]:
                product_result.append(temp_a)  # Save the product of the last list

        else:
            product_result.append(temp_b)  # Save the product of each list
            prod_seq_lists.append([e])  # Else, append append the new element in a new_list


    print("Your array: ", prod_seq_lists)
    print("The list with max product of consecutive elements: ", prod_seq_lists[np.argmax(product_result)])  # Get index of the maximum product and print that list
    print("The max product of consecutive elements: ", max(product_result))

def max_product_real_2 (x):
    if len(x) <= 0:
        raise IndexError('Array length <=0')

    max_at = x[0]
    min_at = x[0]
    max_value = max_at

    for element in x:
        prev_max_at = max_at
        prev_min_at = min_at
        max_at = max(element, element * prev_min_at, element * prev_max_at)
        min_at = min(element, element * prev_min_at, element * prev_max_at)
        max_value = max(max_value,max_at)

    return max_value


def max_product_n_ints(x, n):
    if len(x) < n:
        raise IndexError("Array length < n")

    highest = max(x[0], x[1])
    lowest = min(x[0], x[1])

    highest_product_of_previous = []
    lowest_product_of_previous = []
    highest_product_of_n = np.product([x[j] for j in range(1, n)])
    #  [product_of_n-1_elemnts,product_of_n-2_elemnts,....,product_of_2_elemnts]
    for i in range(n-1):
        highest_product_of_previous.append(np.product([x[j] for j in range(1, n-i)]))
        lowest_product_of_previous.append(np.product([x[j] for j in range(1, n-i)]))
        print("highest_product_of_previous: ", highest_product_of_previous)
        print("lowest_product_of_previous: ", lowest_product_of_previous)
    for element in x[2:]:
        for i in range(1,n+1):
            highest_product_of_n = max(highest_product_of_n,
                                       element * highest_product_of_previous[1],
                                       element * lowest_product_of_previous[1])
            highest_product_of_previous[i] = max(highest_product_of_previous[i],
                                              element * highest_product_of_previous[i-1],
                                              element * lowest_product_of_previous[i-1])
            lowest_product_of_previous[i] = (min(lowest_product_of_previous[i],
                                             element * highest_product_of_previous[i-1],
                                             element * lowest_product_of_previous[i-1]))
        highest = max(highest, element * highest)
        lowest = min(lowest, element * lowest)

        print("highest_product_of_n :", highest_product_of_n)
        print("highest: ", highest)
        print("lowest: ", lowest)
    return highest_product_of_n


def max_product_3_positive_ints(x):
    if len(x) < 3:
        raise IndexError("Array length < 3")

    max_elements = [x[0], x[1], x[2]]
    for element in x[3:]:
      if element > max_elements[0] or element > max_elements[1] or element > max_elements[2]:
        max_elements[np.argmin(max_elements)] = element
    return max_elements


def max_product_3_ints(x):
    if len(x) < 3:
        raise IndexError("Array length < 3")
    max_positve = [0,0,0]
    max_negative = [0,0]
    for element in x:
        if element >= 0:
            if element > max_positve[0] or element > max_positve[1] or element > max_positve[2]:
                max_positve[np.argmin(max_positve)] = element

        else:
            if element < max_positve[0] or element < max_positve[1]:
                max_negative[np.argmax(max_negative)] = element

    if np.product(max_negative) * max(max_positve) > np.product(max_positve):
        max_product = np.product(max_negative) * max(max_positve)
        # max_elements = [max_negative,max(max_positve)]
    else:
        max_product = np.product(max_positve)
        # max_elements = max_positve

    return max_product


def max_product_3_ints_2(array_of_ints):
    if len(array_of_ints) < 3:
        raise Exception('Less than 3 items!')

    # We're going to start at the 3rd item (at index 2)
    # so pre-populate highests and lowests based on the first 2 items.
    # The alternative is starting these as None and checking below if they're set
    # I think this is a little cleaner, but it's debatable.
    highest = max(array_of_ints[0], array_of_ints[1])
    lowest =  min(array_of_ints[0], array_of_ints[1])

    highest_product_of_2 = array_of_ints[0] * array_of_ints[1]
    lowest_product_of_2  = array_of_ints[0] * array_of_ints[1]

    # Except this one--we pre-populate it for the first /3/ items.
    # This means in our first pass it'll check against itself, which is fine.
    highest_product_of_three = array_of_ints[0] * array_of_ints[1] * array_of_ints[2]

    #print ("1: ", highest_product_of_three," 2: ", highest_product_of_2," 3: ", lowest_product_of_2," 4: ", highest," 5: ", lowest)
    # walk through items, starting at index 2
    for current in x[2:]:

        # do we have a new highest product of 3?
        # it's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_three = max(
            highest_product_of_three,
            current * highest_product_of_2,
            current * lowest_product_of_2)

        # do we have a new highest product of two?
        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new lowest product of two?
        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest)

        # do we have a new highest?
        highest = max(highest, current)

        # do we have a new lowest?
        lowest = min(lowest, current)


        #print ("1: ", highest_product_of_three," 2: ", highest_product_of_2," 3: ", lowest_product_of_2," 4: ", highest," 5: ", lowest)

    return highest_product_of_three
'''
# Find the max product of 3 integers >=0
positvive_integers = np.random.uniform(-1000,1000, size=5000000)
print(max_product_3_positive_ints(positvive_integers))

# Find the max product of 3 integers negative and positive
array_of_ints = np.random.uniform(0,1000, size=5000000)
start = time.time()
print(max_product_3_ints(array_of_ints))
end = time.time()
print("Time elapsed: ",end - start)
print(max_product_3_ints_2(array_of_ints))

# Find the max product of consecutive elements
real_numbers = [-50,-40,20,0.1,-100,20,-10,90,1000]
max_product_real(real_numbers)
max_product_real_2(real_numbers)
'''
# Find the max product of n integers negative and positive
array=[1,2,3,20,10]
print(max_product_n_ints(array, 3))

