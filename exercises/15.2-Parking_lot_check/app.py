parking_state = [
  [1,0,1,1,0,1],
  [2,0,1,1,0,1],
  [1,0,2,1,0,1],
  [1,0,1,1,0,1],
  [1,0,1,1,0,2],
  [1,0,1,1,0,1]
]

#Your code go here:

def get_parking_lot():
    state = {
      'totalSlots' : 0,
      'availableSlots' : 0, # 2
      'occupiedSlots' : 0 # 1
    }

    for fil in parking_state:
        for col in fil:
            state['totalSlots'] +=1 
            if col != 0:
                if col == 1:
                    state['occupiedSlots'] +=1
                else:
                    state['availableSlots'] +=1
    
    return state
    

print(get_parking_lot())
