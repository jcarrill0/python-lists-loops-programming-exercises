list_of_numbers = [4, 80, 85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(my_list):
    odd = []
    even = []
    conc = []
    
    for x in my_list:
        if x % 2 != 0:
            odd.append(x)
        else:
            even.append(x)
    conc.append(odd)
    conc.append(even)
    return conc

print(merge_two_list(list_of_numbers))

