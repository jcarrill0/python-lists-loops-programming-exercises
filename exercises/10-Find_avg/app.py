my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:
def avg_list():
    avg = 0
    for num in my_list:
        avg+=num
    return avg / len(my_list)


print(avg_list())

