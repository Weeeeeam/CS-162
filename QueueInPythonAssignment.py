from queue import Queue    
def SortIntoList():
    Priority = Queue(maxsize = 0)
    Standard = Queue(maxsize = 0)
    Economy = Queue(maxsize = 0)
    X=['S Mary','P Dee','P Dee','E Eileen','E Mike','E Joe','P Dee','E Vicky','E George','P Dee','P Joe','E Sally','P Joe','S Pete','P Dee','S Bill','S Chase','E Price','P Dee','E Sue']
    while X[0]!= ' ':
        y=0
        InputLists= X[y]
        if InputLists[0]=='P':
            Priority.put(InputLists)
            y=y+1
        elif InputLists[0]=='S':
            Standard.put(InputLists)
            y=y+1
        elif InputLists[0]=='E':
            Economy.put(InputLists)
            y=y+1
        else:
            print(list(Economy.queue))
            exit
SortIntoList()
