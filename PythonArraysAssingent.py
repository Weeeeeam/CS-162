import numpy as np
x=1
y=10
#creates a 5 by 5 Array with a max value of y and a min value of x 
WholeArray = np.random.randint(x, y, size=(5,5), dtype=int)
#calculates the Average value in each row
MeansOfRows=(np.mean(WholeArray, axis=1))
#displays the value on the second row third column.
#uses value 1 and 2 instead of 2 and 3 cause 0 is counted
ValueOf2ndRow3rdColumn=(WholeArray[1, 2])
#shares the largest value in each column
MaximumValuePerColumn=(np.max(WholeArray, axis=0))
#Shows all values in Array added together
SumOfArray= np.sum(WholeArray)
#print all previous information with labels.
print(f'The entire array:',WholeArray,
      'Value at second row 3 column:',ValueOf2ndRow3rdColumn,
      'The sum of all values in the array:',SumOfArray,
      'Avearage value in each row:',MeansOfRows,
      'Maximum value in each column:',MaximumValuePerColumn)