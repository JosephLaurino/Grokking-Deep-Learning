def elementwise_multiplication(vec_a, vec_b):
    assert(len(vec_a)==len(vec_b))
    result = [0] * len(vec_a)
    for i in range(len(vec_a)):
        result[i] = vec_a[i]*vec_b[i]
    return result

array_0 = [1,10,100]
array_1 = [.5,.5,.5]

array_result = elementwise_multiplication(array_0, array_1)

print(array_result)