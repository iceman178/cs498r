from ..segment_tree.segmenttree import SegmentTree
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
		self.assertEqual(st.size, 8)
		self.assertEqual(st.data, [])




