# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html
from platform import node

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  """
  frontier = util.Stack()
  frontier.push((problem.getStartState(), [], 0))
  
  while not frontier.isEmpty():
    node, path, cost = frontier.pop()        
    if problem.isGoalState(node):
      return path
    for n, p, c in problem.getSuccessors(node):
      if n not in frontier.list and n not in problem._visitedlist:
        frontier.push((n, path + [p], c))
  return False
  
  
def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  bfs = util.Queue()
  bfs.push((problem.getStartState(), [], 0))
  explored = set()
  
  while not bfs.isEmpty():
    node, path, cost = bfs.pop()        
    if problem.isGoalState(node):
      return path
    if node in explored:
      continue
    explored.add(node)
    for n, p, c in problem.getSuccessors(node):
      if n not in bfs.list and n not in explored:
        bfs.push((n, path + [p], c))
  return False
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  ucs = util.PriorityQueue()
  ucs.push((problem.getStartState(), []), 0)
  explored = set()
  
  while not ucs.isEmpty():
    (node, path) = ucs.pop()        
    if problem.isGoalState(node):
      return path
    if node in explored:
      continue
    explored.add(node)
    for n, p, c in problem.getSuccessors(node):
      if n not in ucs.heap and n not in explored:
        ucs.push((n, path + [p]), c)
  return False

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  astar = util.PriorityQueue()
  astar.push((problem.getStartState(), []), 0)
  explored = set()
  
  while not astar.isEmpty():
    (node, path) = astar.pop()        
    if problem.isGoalState(node):
      return path
    if node in explored:
      continue
    explored.add(node)
    for n, p, c in problem.getSuccessors(node):
      if n not in astar.heap and n not in explored:
        astar.push((n, path + [p]), c + heuristic(n, problem))
  return False
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
