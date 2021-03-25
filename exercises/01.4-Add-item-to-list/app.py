#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
def add_element():
    my_list.append(random.randint(1, 100))
    print(my_list)
add_element()
add_element()
add_element()
add_element()
add_element()
add_element()
add_element()

