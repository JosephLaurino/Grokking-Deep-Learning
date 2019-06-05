def elementwise_multiplication(vec_a, vec_b):
    assert(len(vec_a)==len(vec_b))
    result = [0] * len(vec_a)
    for i in range(len(vec_a)):
        result[i] = vec_a[i]*vec_b[i]
    return result

def elementwise_addition(vec_a, vec_b):
    assert(len(vec_a)==len(vec_b))
    result = [0] * len(vec_a)
    for i in range(len(vec_a)):
        result[i] = vec_a[i]+vec_b[i]
    return result

def vector_sum(vec_a):
    result = 0
    for i in range(len(vec_a)):
        result += vec_a[i]
    return result

def vector_average(vec_a):
    result = 0
    for i in range(len(vec_a)):
        result += vec_a[i]
    result /= len(vec_a)
    return result

def vector_dot_product(vec_a, vec_b):
    assert(len(vec_a)==len(vec_b))
    mul_result = elementwise_multiplication(vec_a, vec_b)
    return vector_sum(mul_result)

array_0 = [1,10,100]
array_1 = [.5,.5,.5]
array_2 = [1,1,1]

array_result = elementwise_multiplication(array_0, array_1)
print(array_result)

array_result = elementwise_multiplication(array_0, array_2)
print(array_result)

array_result = elementwise_addition(array_0, array_1)
print(array_result)

result = vector_sum(array_0)
print(result)

result = vector_average(array_1)
print(result)


weights = [0.1, 0.2, 0]
toes =  [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wlrec[0], nfans[0]]

def neural_network(input, weights):
    pred = vector_dot_product(input,weights)
    return pred

input = [toes[0], wlrec[0], nfans[0]]
pred = neural_network(input, weights)
print(pred)

