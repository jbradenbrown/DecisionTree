import DecisionTree as dt


classData = dt.readInput('train.dat')
things = dt.train(classData[1], classData[0])
dt.printTree(things,"")
	
