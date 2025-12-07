class Vector:

#Constructor which instantiates a null/zero and 'd'-dimensional 'Vector'  
 def __init__(self , d):
    self._coordinates = [0] * d

#Returns number of dimensions of vector using built-in 'len' function that keeps count of number of elements in  list    
 def __len__(self):
    return len(self._coordinates)

#Tried to use methods __getvalue__ and __setvalue__ but they won't work as expected
#Python uses __getitem__ and __setitem__ for indexing of list operations [ list[x]->actually uses list.__getitem__(x) ]

#Getter for retrieving coordinate of dimension at index 'j' of Vector list   
 def __getitem__(self, j):
    return self._coordinates[j]
#Setter for changing coordinate of dimension at index 'j' of Vector list  to 'value'   
 def __setitem__(self, j, value):
    self._coordinates[j] = value

#Addition of vectors
 def __add__(self, other):
    if len(self) != len (other):                #Vectors cannot be added if their number of dimensions are unequal
     raise ValueError('Dimensions must be equal')
    result = Vector(len(self))                  
    for j in range(len(self)):                  
     result[j] = self[j] + other[j]             #Adding values of the coordinates of both vectors at the same index
    return result

#Compares the list of coordinates of two Vectors to verify equality only if all coordinates are equal
 def __eq__(self, other):
   return self._coordinates == other._coordinates  

#Check for inequality of vector and returns 'True' even if one coordinate is different
 def __ne__(self, other):
   return not self == other

#String representation of vector
 def __str__(self):
   return '<' + str(self._coordinates)[1:-1] + '>'