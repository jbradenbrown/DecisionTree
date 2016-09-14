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
#class Tree:
#	def __init__ (self, data):
#		self.data = data
#		self.children = {}
#	def addChild (self, attrName, child):
#		self.children[attrName] = child
#
#class dNode:
#	def __init__ (self, attrName, possibleValues):
#		self.attrName = attrName
#		self.possibleValues = possibleValues
#
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

# Calculate the entropy of a probability distribution
def entropy (pDist):
	if pDist.size < 2:
		return 0
	else:
		return sum(map(lambda p: (-p) * log(p,2), pDist))

# Normalize a list of numbers
def normalized (data):
	return list(map(lambda x: x/sum(data)),data)

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
	return ([x for x in attrList if x[1] == max(zip(*attrList)[1])])

# Train a binary Decision Tree on some data
def train(classifiedData,tree):
	labels = list(range(0,len(classifiedData[0])))
	attrParts = map(lambda x: bPart(classifiedData,x),range(0,len(classifiedData[0])))
	classParts = map(lambda x: map(lambda y: bPart(y,((len(y)-1) if len(x) > 0 else 0)),x),attrParts)
	pDists = map(lambda x: pDist(bPart(x,((len(x)-1) if len(x) > 0 else 0))))
	
	
