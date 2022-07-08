
import functools

def process(x):
    return (x[1], x[2] )

def collect_companies(dict, input):
    if input[0] not in dict:
        dict[input[0]] = [input[1]]
    else:
        dict[input[0]].append(input[1])
    return dict

def avg_item(item):
    return (item[0], functools.reduce(lambda x, y: int(x)+int(y), item[1]))

def get_higher_avg(left, right):
    # print(left, right)
    if left[1] > right[1]:
        return left
    else:
        return right    

def get_highest_mean_score(data):
    nonames = list(map( process, data))
    # print (nonames)
    hash = functools.reduce(collect_companies, nonames, {})
    # print(hash)
    avg = dict(map(avg_item, hash.items()))

    print (avg)

    highest = functools.reduce( get_higher_avg, avg.items())
    return highest[0]