
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
hello = []
for x in my_list:
    if isinstance(x, (list, dict)):
        hello.append(x)

print(hello)
