from ..segment_tree.segmenttree import *
import unittest


class SegmentTree_Test(unittest.TestCase):
	"""This class contains the test cases for the Node class and the UnrolledLinkedList class
		This class goes through the different functions and tests them to ensure that 
		each class is operating correctly and returning the correct results.
	"""

	"""This class contains the test cases for the SegmentTree class
	"""

	
	#SegmentTree Class Tests

	def testSegmentTreeCreation(self):
		"""Test creating a segment tree
		"""
		st = SegmentTree(8)
		#self.assertEqual(st.size, 8)
		#self.assertEqual(len(st.data), 8)

	def testInitializeWithArray(self):
		"""Test creating a segment tree using a provided array
		"""
		st = SegmentTree(8)
		values = [5, 3, 2, 5, 7, 2, 1, 9]
		st.initializeTree(values)





























