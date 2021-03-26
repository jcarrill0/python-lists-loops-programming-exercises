
coordinatesList = [[33.747252,-112.633853],
                  [-33.867886, -63.987],
                  [41.303921, -81.901693],
                  [-33.350534, -71.653268]]

# Your code go here:

longitud = []
for arr in coordinatesList:
    for log in range(len(arr)-1, len(arr)):
        print(arr[log])

