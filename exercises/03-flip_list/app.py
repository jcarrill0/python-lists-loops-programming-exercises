arr = [45, 67, 87, 23, 5,  32, 60]
new_list = []
#your code below:
def inverse_list():
    largo = len(arr)
    for x in range(largo):
        largo-=1
        new_list.append(arr[largo])
    print("Initial list: ", arr)
    print("Final list: ", new_list)

inverse_list()