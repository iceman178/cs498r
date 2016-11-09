import sys
import math



class SegmentTreeNode():
	def __init__(self, nodeSum, indexLeft, indexRight):
		"""Initialize a tree node
		"""
		self.nodeSum = nodeSum
		self.indexLeft = indexLeft
		self.indexRight = indexRight

	def printNode(self):
		print("NS " + str(self.nodeSum).zfill(2) + " L ", str(self.indexLeft).zfill(2), " R " + str(self.indexRight).zfill(2))

	def toString(self):
		return "NS " + str(self.nodeSum).zfill(2) + " L " + str(self.indexLeft).zfill(2) + " R " + str(self.indexRight).zfill(2)
		

class SegmentTree():

	def __init__(self, size):
		"""Initialize the tree
		"""
		self.size = size
		self.space = 2 * size - 1
		self.data = []
		for _ in range(self.space):
			newNode = SegmentTreeNode(0, 0, 0)
			self.data.append(newNode)



	def __len__(self):
		"""Returns the current length of the data list
		"""
		return len(self.data)

	def __str__(self):
		"""Returns a string of what is currently in the data list
		"""
		return str(self.data)

	def printTree(self):
		"""Prints the data in the tree.
			Prints the data in array format
		"""
		dLen = len(self.data)

		print("Segment Tree")
		for pos in range(dLen):
			print(str(pos).zfill(2))
			print("  " + self.data[pos].toString())

		


	def initializeTree(self, values):
		"""This will add the data from an array to the tree
		"""
		if len(self.data) == 0:
			raise Exception("Tree has not been initialized")

		vLen = len(values)

		print("Values", values)
		print("Values len", vLen)
		print("Space", self.space)

		#self.printTree()


		dataPos = self.space - 1

		for vPos in range(vLen - 1, -1, -1):
			self.data[dataPos].nodeSum = values[vPos]
			self.data[dataPos].indexLeft = vPos
			self.data[dataPos].indexRight = vPos
			dataPos -= 1


		self.printTree()

		self.calculateSum(0, "root")

		#self.printTree()

	def calculateSum(self, pos, direction):
		print("Pos", pos)

		leftChildPos = 2 * pos + 1
		rightChildPos = 2 * pos + 2

		if leftChildPos >= self.space:
			return pos




		# Left Child
		leftChildPos = self.calculateSum(2 * pos + 1, "left")

		# Right Child
		rightChildPos = self.calculateSum(2 * pos + 2, "right")

		print("LP", leftChildPos, "RP", rightChildPos)
		

		#self.data[pos].nodeSum = self.data[2 * pos + 1].nodeSum + self.data[2 * pos + 2].nodeSum





	def calculateSum2(self, pos, direction):
		print("Pos", pos)
		# Base Case
		if pos >= self.space:
			if direction == "left":
				return (pos - 1) / 2
			elif direction == "right":
				return (pos - 2) / 2
			elif direction == "root":
				return 0


		# Left Child
		leftChildPos = self.calculateSum(2 * pos + 1, "left")

		# Right Child
		rightChildPos = self.calculateSum(2 * pos + 2, "right")

		print("LP", leftChildPos, "RP", rightChildPos)
		

		#self.data[pos].nodeSum = self.data[2 * pos + 1].nodeSum + self.data[2 * pos + 2].nodeSum



	def setValue(self, value, index):
		"""This will set the value in the tree using the index
		"""






	def getSumSlow(self, indexLeft, indexRight):
		"""This is the brute force way to get the sum.
			This is for verifying that the sum is correct
		"""
		if indexRight >= len(self.data) or indexRight < 0:
			raise IndexError()
		if indexLeft >= len(self.data) or indexLeft < 0:
			raise IndexError()

		totalSum = 0
		for index in range(indexLeft, indexRight + 1):
			totalSum += self.data[index]
		print("TotalSum", totalSum)





	def getSum(self, indexLeft, indexRight):
		"""This will return the sum using the given indexes
		"""





































