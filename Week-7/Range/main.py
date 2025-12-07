from Range import Range

#Instantiating 'Range' objects
R1 = Range(5)
R2 = Range(1,10)
R3 = Range(1,27,5)
R4 = Range(20,4,-5)

#Displaying number of entries/values in Range
print(R1,"has",len(R1), "elements")
print("\t",R2,"has",len(R2), "elements")
print("\t\t",R3,"has",len(R3), "elements")
print("\t\t\t",R4,"has",len(R4), "elements\n")

#Using getter to return entry at any specific index
print("The 3rd element of",R1,"is",R1[2])
print("\tThe 1st element of",R2,"is",R2[0])
print("\t\tThe last element of",R3,"is",R3[-1])
print("\t\t\tThe 2nd element of",R4,"is",R4[1])