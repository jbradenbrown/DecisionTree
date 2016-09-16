import DecisionTree as dt

for x in range(0,100):
	classData = dt.r_classData(100,5)
	things = dt.train(classData, ["one","two","three","four","class"])

for x in range(0,100):
	classData = dt.r_classData(100,10)
	things = dt.train(classData, ["one","two","three","four","five","six","seven","eight","nine","class"])
	
