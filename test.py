import DecisionTree as dt

for x in range(0,1):
	classData = [[1,0,0,1],[0,0,1,1],[0,0,0,0],[1,1,0,0],[0,0,0,0],[1,0,1,1],[0,1,1,0],[1,0,0,1],[0,0,0,0],[1,0,0,1]]
	things = dt.train(classData, ["nigeria","viagra","learning","class"])
