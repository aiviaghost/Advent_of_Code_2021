from functools import reduce
from math import ceil, floor
from os import stat
import re

def gen_id():
	id = 0
	while True:
		yield id
		id += 1

id_generator = gen_id()

class Num:
	def __init__(self, val, par = None, is_left = None):
		self.val = val
		self.is_num = True
		self.par = par
		self.is_left = is_left
	
	def magnitude(self):
		return self.val
	
	def split(self, par, is_left):
		return Pair(Num(floor(self.val / 2)), Num(ceil(self.val / 2)), par)
	
	def is_reduced(self, surrounding_pars = 0):
		if self.val >= 10:
			if self.is_left:
				self.par.left = self.split(self.par, self.is_left)
			else:
				self.par.right = self.split(self.par, self.is_left)
			return False
		return True

	def explode(self, start_id, return_id, go_left, val, vis, found):
		if go_left:
			return self if self.id < start_id and (found == None or found.id < self.id) else found
		else:
			return self if self.id > start_id and (found == None or found.id > self.id) else found


	def __repr__(self) -> str:
		return f"Num({self.val})"


class Pair:
	def __init__(self, left, right, par = None, is_left = None):
		self.left, self.right = left, right
		self.left.is_left, self.right.is_left = True, False
		self.is_num = False
		self.par = par
		self.is_left = is_left
		self.left.par = self.right.par = self

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
		while True:
			# print(self)
			self.label()
			if self.is_reduced():
				break
		return self
	
	def label(self):
		self.id = next(id_generator)
		if self.left.is_num:
			self.left.id = next(id_generator)
		else:
			self.left.label()
		if self.right.is_num:
			self.right.id = next(id_generator)
		else:
			self.right.label()

	
	def is_reduced(self, surrounding_pars = 0):
		if not self.is_num and self.left.is_num and self.right.is_num and surrounding_pars >= 4:
			self.explode(self.left.id, self.id, True, self.left.val, set())
			self.explode(self.right.id, self.id, False, self.right.val, set())
			# print(self)
			if self.is_left:
				self.par.left = Num(0, self.par, True)
			else:
				self.par.right = Num(0, self.par, False)
			return False
		
		is_reduced = self.left.is_reduced(surrounding_pars + 1)
		if not is_reduced:
			return False
		is_reduced = self.right.is_reduced(surrounding_pars + 1)
		return is_reduced

	def explode(self, start_id, return_id, go_left, val, vis, found = None):
		if self in vis:
			return found
		vis.add(self)
		found = self.left.explode(start_id, return_id, go_left, val, vis, found)
		found = self.right.explode(start_id, return_id, go_left, val, vis, found)
		if self.par != None:
			found = self.par.explode(start_id, return_id, go_left, val, vis, found)
		if self.id == return_id and found != None:
			found.val += val
		else:
			return found

	"""
	Add to right/ left-most by starting dfs from parent, 
	keep visited in set to prevent querying subtree starting from
	starting node (the one to "explode"). 
	"""

	def magnitude(self):
		return 3 * self.left.magnitude() + 2 * self.right.magnitude()


with open("input") as f:
	pairs = [Pair.make_pair(line) for line in f.read().split("\n") if line]

# print(pairs[0].reduce())

num = pairs[0].reduce()
for i in range(1, len(pairs)):
	num = (num + pairs[i]).reduce()
	print(i)
print(num.magnitude())
