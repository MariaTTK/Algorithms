def product_1_to_n(n):
    # we assume n >= 1
    return n * product_1_to_n(n-1) if n > 1 else 1

def product_1_to_n_NO_STACK_OVERFLOW(n):
    # we assume n >= 1
    result = 1
    for num in range(1, n+1):
        result *= num
    return result

print(product_1_to_n(2))  #  stack overflow error: if n >=999
                          # it builds up a call stack of size O(n)O(n)O(n),
                          # which makes our total memory cost O(n)O(n)O(n).

print(product_1_to_n_NO_STACK_OVERFLOW(2000))