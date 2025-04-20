def LoadDataFile():
    X=list()
    with open('input queue-1.txt', 'r') as file:
        for line in file:
            X.append(line.rstrip('\n'))
    return(X)
      
print( LoadDataFile())