from queue import Queue   
Priority = Queue(maxsize = 10)
Standard = Queue(maxsize = 10)
Economy = Queue(maxsize = 10)
def LoadDataBasic():
    X=['S Mary','P Dee','P Dee','E Eileen','E Mike','E Joe','P Dee','E Vicky','E George','P Dee','P Joe','E Sally','P Joe','S Pete','P Dee','S Bill','S Chase','E Price','P Dee','E Sue']
    return X
def LoadDataFile():
    X=list()
    with open('input queue-1.txt', 'r') as file:
        for line in file:
            X.append(line.rstrip('\n'))
    return(X)

def SortIntoList():
    X=LoadDataFile()
    
    y=0
    while y<len(X):
        Item= X[y]
        if Item[0]=='P':
            Priority.put(Item)
        elif Item[0]=='S':
            Standard.put(Item)
        elif Item[0]=='E':
            Economy.put(Item)
        y=y+1
    print(list(Economy.queue))
    print(list(Priority.queue))
    print(list(Standard.queue))
   


def EmptyQueue():
    while Priority.empty()!=True or Standard.empty()!=True or Economy.empty()!=True:
        if  Priority.empty()!=True:
            print(Priority.get())
        if  Priority.empty()!=True:   
            print(Priority.get())
        if  Priority.empty()!=True:
            print(Priority.get())
        if Economy.empty()!=True:
            print(Economy.get())
        if Economy.empty()!=True:
            print(Economy.get())
        if Standard.empty()!=True:
            print(Standard.get())

SortIntoList()
EmptyQueue()