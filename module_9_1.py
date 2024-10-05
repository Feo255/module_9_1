

def apply_all_func(int_list, *functions):
    dict_ = {}
    for function in functions:
        result = function(int_list)
        dict_[function.__name__] = result
    return dict_
def max(int_list):
    maximum = int_list[0]
    for k in int_list:
        if k > maximum:
            maximum =k
    return maximum

def min(int_list):
    minimum = int_list[0]
    for k in int_list:
        if k < minimum:
            minimum = k
    return minimum

def len(int_list):
    length = 0
    for k in int_list:
        length += 1
    return length

def sum(int_list):
    summ = 0
    for k in int_list:
        summ += k
    return summ

def sorted(int_list):
    int_list.sort()

    return int_list






print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))