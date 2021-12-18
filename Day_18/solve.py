from functools import reduce
from math import ceil, floor
import re


class Num:
	def __init__(self, val):
		self.val = val
		self.is_num = True
	
	def magnitude(self):
		return self.val
	
	def split(self):
		return Pair(floor(self.val / 2), ceil(self.val / 2))
	
	def __repr__(self) -> str:
		return f"Num({self.val})"


class Pair:
	def __init__(self, left, right):
		self.left, self.right = left, right
		self.is_num = False
	
	@staticmethod
	def make_pair(s):
		return eval(
			re.sub(
				pattern = "[0-9]{1,}", 
				repl = lambda x: f"Num({x.group()})", 
				string = s.replace("[", "Pair(").replace("]", ")")
			)
		)
	
	def __add__(self, other):
		return Pair(self, other)
		
	def __repr__(self) -> str:
		return f"Pair({self.left}, {self.right})"
	
	def reduce(self):
		if self.left.is_num and self.left.val >= 10:
			self.left = self.left.split()
		

	def explode(self):
		pass

	"""
	Add to right/ left-most by starting dfs from parent, 
	keep visited in set to prevent querying subtree starting from
	starting node (the one to "explode"). 
	"""

	def split(self):
		pass

	def magnitude(self):
		return 3 * self.left.magnitude() + 2 * self.right.magnitude()


with open("input") as f:
	pairs = [Pair.make_pair(line) for line in f.read().split("\n") if line]

print(reduce(lambda x, y: x + y, pairs))
