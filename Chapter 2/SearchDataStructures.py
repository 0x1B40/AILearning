# common data structure for any search problem involving nodes and trees
class Node:
   def __Init__(self,nodeState,nodeParent,nodeAction,nodePathCost):

       # stores the state of the node, state is dependant on the problem
       self.nodeState = nodeState

       # stores the parent node class object
       self.nodeParent = nodeParent

       # string to store the type of action taken to transition to another state
       self.nodeAction = nodeAction

       # cost of reaching the current node
       self.nodePathCost = nodePathCost
