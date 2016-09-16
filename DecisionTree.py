#!/usr/bin/python

#Decision Tree ID3 implementation in python
#Jeffrey Brown

from math import log
from random import randint

class Tree:
	def __init__ (self, label):
		self.label = label
		self.children = []
	def __init__ (self, label, child1, child2):
		self.label = label
		self.children = ([child1, child2])
	def addChildren (self, child1, child2):
		self.children = ([child1, child2])

# Calculate the entropy of a probability distribution
def entropy (pDist):
	if len(pDist) < 2:
		return 0
	else:
		return sum(map(lambda p: 0 if not p else ((-p) * log(p,2)), pDist))

# Normalize a list of numbers
def normalized (data):
	if not sum(data):
		return data
	return list(map(lambda x: x/sum(data),data))

# Partition a list on a binary attribute
def bPart (data, attr):
	return ([[x for x in data if x[attr] is 0],[x for x in data if x[attr] is 1]])

# Calculate the probability distribution for a bParted attribute
def pDist (partedData):
	return normalized([len(partedData[0]),len(partedData[1])])

# Calculate conditional entropy
def conditionalEntropy (pDist1,w1,pDist2,w2):
	return entropy(pDist1)*w1 + entropy(pDist2)*w2

# Pick the attribute with the highest associated value
def pickAttr (attrList):
	return ([x for x in attrList if x[0] == max(list(zip(*attrList))[0])])

# Generate a random binary list
def r_bList (size):
	return ([randint(0,1) for x in range(0,size)])

# Generate random classData
def r_classData (size, attrNum):
	return ([r_bList(attrNum) for x in range(0,size)])

# Return majority class of a class partitioned list
def majorityClass (classPartedData):
	return 0 if len(classPartedData[0]) > len(classPartedData[1]) else 1

# Return last element of a list
def i_lastElem (l):
	return (len(l) - 1)

# Return a list without an element
def l_without (l,e):
	return ([x for x in l if x is not e])

# Return a list with the element at index i removed
def l_withoutI (l, i):
	return (l[:i]+l[(i+1):])

# Train a binary Decision Tree on some data
def train(classifiedData, labels):
	print(classifiedData)
	print(labels)
	if not classifiedData:
		return None
	if len(labels) == 1 or entropy(pDist(bPart(classifiedData, i_lastElem(classifiedData[0])))) == 0:
		print("out of labels or entropy is 0")
		return (Tree (majorityClass(bPart(classifiedData, i_lastElem(classifiedData[0]))), None,None))
	attrParts = list(map(lambda x: bPart(classifiedData,x),range(0,i_lastElem(classifiedData[0]))))
	classParts = list(map(lambda x: list(map(lambda y: bPart(y,i_lastElem(classifiedData[0])),x)),attrParts))
	pDists = list(map(lambda x: list(map(lambda y: pDist(y),x)),classParts))
	classPartLens = list(map(lambda x: normalized(list(map(lambda y: len(y[0])+len(y[1]),x))),classParts))
	condEnt = list(map(lambda x: conditionalEntropy(x[0][0],x[1][0],x[0][1],x[1][1]),list(zip(pDists,classPartLens))))
	Ig = list(map(lambda x: entropy(pDist(bPart(classifiedData,len(classifiedData[0])-1))) - x, condEnt))
	bestAttr = pickAttr(list(zip(Ig, labels[:-1]))) 
	bestAttrPart = bPart(classifiedData,labels.index(bestAttr[0][1]))
	removedBestAttr = list(map(lambda x: list(map(lambda y: l_withoutI(y,labels.index(bestAttr[0][1])),x)),bestAttrPart))
	print("best Attr ",bestAttr)
	return (Tree (bestAttr[0][1],train(removedBestAttr[0],l_without(labels,bestAttr[0][1])),train(removedBestAttr[1],l_without(labels,bestAttr[0][1]))))
	#return ([labels,attrParts,classParts,pDists,classPartLens,condEnt,Ig,bestAttr,bestAttrPart])

def readInput (fileName):
	labels = []
	classData = []

	ifile = open(fileName,'r')
	labels = ifile.readline().strip().split()

	for line in ifile:
		classData.append(line.strip().split())
	
	return (labels,classData)

def printTree (tree,prefix):
	while 
