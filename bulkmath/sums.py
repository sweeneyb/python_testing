def sum(a, b):
    return a + b

def sum_tuple(a):
    return a[0]+a[1]

def sum_tuples(tuples):
    result = []
    for (x,y) in tuples:
        result.append(sum(x,y))

    return result

def map_sum_tuples(tuples):

    return list(map(sum_tuple, tuples))