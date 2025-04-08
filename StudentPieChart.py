import matplotlib.pyplot as plot
# set up your lists
numlist = [8, 6, 5, 3]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
#each of these values linke to each other
colorlist = ['blue', 'green', 'pink', 'yellow' ]
#exslpode list chages distancce from center
explodelist = [0.0, 0.0, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.2f%%', colors=colorlist,
    	explode = explodelist, startangle = 5)
#changes where the first slice sits
plot.axis('equal')
plot.savefig('piechart.png')