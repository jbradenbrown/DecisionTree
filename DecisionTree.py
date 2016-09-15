#!/usr/bin/python

#Decision Tree ID3 implementation in python
#Jeffrey Brown

from math import log

#def entropy (pDist):
#	if pDist.size < 2:
#		return 0
#	else:
#		return sum(map(lambda p: (-p) * log(p,2), pDist))
#
class Tree:
	def __init__ (self, label):
		self.label = label
		self.children = []
	def __init__ (self, label, child1, child2):
		self.label = label
		self.children = ([child1, child2])
	def addChildren (self, child1, child2):
		self.children = ([child1, child2])

#def attrPart (data, val, attrNumber):
#	return ([x for x in data if x[attrNumber] is val])
#
#def classPart (data, val):
#	return ([x for x in data if x[-1:] is val])
#
#def attrSum (data):
#	return ([sum(x) for x in zip(*data)])
#
#def classSum (data):
#	return (len(classPart(data,0)),len(classPart(data,1).size))
#
#def normalized (data):
#	return list(map(lambda x: x/sum(data)),data)
#
#def attrEntropy (attrSumMatrix):
#	return list(map(entropy,[normalized(x) for x in attrSumMatrix]))
#
#def conditionalEntropy (labeledData, attrNumber):
#	return entropy(normalized(classSum(attrPart(labeledData,0,attrNumber))))*len(attrPart(labeledData,0,attrNumber))+entropy(normalized(classSum(attrPart(labeledData,1,attrNumber))))*len(attrPart(labeledData,1,attrNumber))

from random import randint

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

def r_bList (size):
	return ([randint(0,1) for x in range(0,size)])

def r_classData (size, attrNum):
	return ([r_bList(attrNum) for x in range(0,size)])

def majorityClass (classPartedData):
	return 0 if len(classPartedData[0]) > len(classPartedData[1]) else 1

def i_lastElem (l):
	return (len(l) - 1)

def l_without (l,e):
	return ([x for x in l if x is not e])

def l_withoutI (l, i):
	return (l[:i]+l[(i+1):])

# Train a binary Decision Tree on some data
def train(classifiedData, labels):
	print(classifiedData)
	print(labels)
	if classifiedData == [] or len(labels) == 1:
		print("out of labels")
		return (Tree (majorityClass(bPart(classifiedData, i_lastElem(classifiedData[0]))), None,None))
	if entropy(pDist(bPart(classifiedData, i_lastElem(classifiedData[0])))) == 0:
		print("1")
		print(entropy(pDist(bPart(classifiedData, i_lastElem(classifiedData[0])))))
		print(labels)
		return (Tree (classifiedData[0][-1], None, None))
	elif len(classifiedData[0]) == 1:
		print("2")
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
	
	 
