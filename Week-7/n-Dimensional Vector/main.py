from Vector import Vector

A = Vector(4)
B = Vector(4)
C = Vector(3)
D = Vector(3)
Z = Vector(6)

#Display number of dimensions of vectors
print("The number of dimensions of vector A are :")
print("\t", A.__len__(), "\n")

#Checking equality of vectors
print("Do Vectors A", A, "and B", B, "have the  same coordinates ?")
print("\t", A == B, "\n")    #A.__eq__(B)

print("Original coordinates of vector C" , C ,"\n")

#Setting coordinates of vector
print("Setting coordinates of dimensions of vector C as 6 , 1 , 9 respectively")
C[0] = 6    #C.__setitem__(0,6)
C[1] = 1    #C.__setitem__(1,1)
C[2] = 9    #C.__setitem__(2,9)

#Return coordinates of vector
print("\nDisplaying new coordinates of Vector C:")
print(C[0])           #C.__getitem__(0)
print("\t",C[1])      #C.__getitem__(1)
print("\t\t",C[2])    #C.__getitem__(2)

#Checking inequality of vectors
print("Do Vectors C", C, "and D", D, "not have the same coordinates ?")
print("\t", C != D, "\n")    #C.__ne__(D)

#Testing addition functionality of Vectors
D[0] = 1 
D[1] = 1
D[2] = 1
E = C + D    #C.__add__(D)
print("Addition of Vectors C", C,"and D",D, "equals to :") 
print("\t", E,"\n")

#Displaying Vector attributes as String
print("Coordinates of Vector Z as string :")
print("\t", Z, "\n")    #Z.__str__()