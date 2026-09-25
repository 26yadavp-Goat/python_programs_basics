rows = 5
for i in range(1, rows + 1):
    # Prints the decreasing padding spaces
    for j in range(rows - i):
        print(" ", end=" ")
    
    # Prints the increasing stars (includes the 'i'th star)
    for k in range(i):
        print("*", end=" ")
        
    print()

