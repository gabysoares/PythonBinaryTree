"""
Gabriella Soares
gsoa420
"""

class ListBinaryTree:
	"""A binary tree class with nodes as lists."""
	DATA = 0    # just some constants for readability
	LEFT = 1
	RIGHT = 2   

	def __init__(self, root_value, left=None, right=None):
		"""Create a binary tree with a given root value
		left, right the left, right subtrees        
		""" 
		self.node = [root_value, left, right]
		
	def create_tree(self, a_list):
		return ListBinaryTree(a_list[0], a_list[1], a_list[2])

	def insert_value_left(self, value):
		"""Inserts value to the left of this node.
		Pushes any existing left subtree down as the left child of the new node.
		"""
		self.node[self.LEFT] = ListBinaryTree(value, self.node[self.LEFT], None)

	def insert_value_right(self, value):
		"""Inserts value to the right of this node.
		Pushes any existing left subtree down as the left child of the new node.
		"""      
		self.node[self.RIGHT] = ListBinaryTree(value, None, self.node[self.RIGHT])

	def insert_tree_left(self, tree):
		"""Inserts new left subtree of current node"""
		self.node[self.LEFT] = tree

	def insert_tree_right(self, tree):
		"""Inserts new left subtree of current node"""
		self.node[self.RIGHT] = tree

	def set_value(self, new_value):
		"""Sets the value of the node."""
		self.node[self.DATA] = new_value

	def get_value(self):
		"""Gets the value of the node."""
		return self.node[self.DATA]

	def get_left_subtree(self):
		"""Gets the left subtree of the node."""
		return self.node[self.LEFT]

	def get_right_subtree(self):
		"""Gets the right subtree of the node."""
		return self.node[self.RIGHT]

	def __str__(self):
		return '['+str(self.node[self.DATA])+', '+str(self.node[self.LEFT])+', '+\
	 str(self.node[self.RIGHT])+']'


def construct_tree(inorder, preorder, start, end):
	if start > end:
		return None

	#create node
	tree = ListBinaryTree(preorder[construct_tree.preIndex])
	construct_tree.preIndex += 1

	if start == end:
		return tree

	inorder_node_index = inorder.index(tree.get_value())
	
	#set left and right nodes
	tree.insert_tree_left(construct_tree(inorder, preorder, start, inorder_node_index - 1))
	tree.insert_tree_right(construct_tree(inorder, preorder, inorder_node_index + 1, end))
	
	#insert node to tree list
	return tree

construct_tree.preIndex = 0


def main():
	print("Binary Tree reconstructed by gsoa420:") 
	inorder = input("Please enter the inorder sequence: ")
	preorder = input("Please enter the preorder sequence: ")
	
	tree = construct_tree(inorder, preorder, 0, len(preorder) - 1)

	print(tree)

main()




