class Range:

#Constructor to instantiate a 'Range' object
 def __init__(self, start, stop=None, step=1):
  
#By default step is set to 1 but if an argument for 0 steps is passed, then error is flagged
  if step == 0:
   raise ValueError("Cannot take 0 steps")

#Scenario in which 'stop' or end point of range is not specified
#Argument passed for start is assumed as 'stop' and start defaults to 0 : Range(start,end)->Range(0,start)
  if stop is None:
   start, stop = 0, start    

#Calculate number of items in the range (fixed to handle negative steps too and max(0,...) ensures calculated length is never negative)   
  if step > 0:
   self._length = max(0, (stop - start + step - 1) // step)
  else:
   self._length = max(0, (start - stop - step - 1) // (-step))

#POSITIVE STEP R3(1,27,5)  = [27-1+5-1//5] = "6"
#NEGATIVE STEP R4(20,4,-5) = [20-4-(-5)-1)//-(-5)] = [20-4+5-1//5] = "4"

  self._start = start
  self._step = step
  self._stop = stop


#Returns number of entries/values in the range
 def __len__(self):
  return self._length


#Returns the entry in the range at specified index 'k'
 def __getitem__(self, k):
  
#Enables conversion of negative index e.g: in a list with 4 elements list[-1] = list[3]->(last element)
  if k < 0:
   k += len(self)

#Exception Handling if specified index is out of bounds
  if not 0 <= k < self._length:
   raise IndexError("Index out of range")

  return self._start + k * self._step  

#String representation 
 def __str__(self):
    return f"Range({self._start}, {self._stop}, {self._step})"