theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
result = list(map(lambda num: 'wiki' if num == 1 else 'woko', theBools))

print(result)


