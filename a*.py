import heapq
 
class Node:
   """Class representing a node in the search tree."""
   def __init__(self, state, parent=None):
       self.state = state  # (x, y) position
       self.parent = parent  # Parent node
       self.g = 0  # Cost from start node to current node
       self.h = 0  # Estimated cost from current node to goal node
 
   def __lt__(self, other):
       """Compare nodes based on their f-score (g + h)."""
       return (self.g + self.h) < (other.g + other.h)
 
def astar(start, goal, get_neighbors, heuristic):
   """A* Search Algorithm"""
   open_list = []  # Priority queue for nodes to be evaluated
   closed_set = set()  # Set of evaluated nodes
 
   start_node = Node(start)
   start_node.h = heuristic(start, goal)
   heapq.heappush(open_list, start_node)  # Add start node to open list
 
   while open_list:
       current_node = heapq.heappop(open_list)  # Get node with lowest f-score
 
       if current_node.state == goal:
           # Goal reached, construct path
           path = []
           while current_node:
               path.append(current_node.state)
               current_node = current_node.parent
           return path[::-1]  # Reverse to get path from start to goal
 
       closed_set.add(current_node.state)
 
       for neighbor in get_neighbors(current_node.state):
           if neighbor in closed_set:
               continue  # Skip already evaluated nodes
 
           tentative_g = current_node.g + 1  # Assuming uniform cost
 
           neighbor_node = Node(neighbor, current_node)
           neighbor_node.g = tentative_g
           neighbor_node.h = heuristic(neighbor, goal)
 
           # Ensure that the node is updated if a better path is found
           in_open_list = False
           for node in open_list:
               if node.state == neighbor:
                   in_open_list = True
                   if tentative_g < node.g:
                       node.g = tentative_g
                       node.parent = current_node
                   break
 
           if not in_open_list:
               heapq.heappush(open_list, neighbor_node)
 
   return None  # No path found
 
def manhattan_distance(state, goal):
   """Heuristic function: Manhattan distance."""
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])
 
def get_neighbors(state):
   """Generate valid neighboring positions on a 5x5 grid."""
   x, y = state
   neighbors = []
   for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
       new_x, new_y = x + dx, y + dy
       if 0 <= new_x < 5 and 0 <= new_y < 5:  # Keep within 5x5 grid bounds
           neighbors.append((new_x, new_y))
   return neighbors
 
def print_solution(path):
   """Print the solution path."""
   if path:
       print("Solution Found:")
       for step, state in enumerate(path):
           print(f"Step {step}: {state}")
   else:
       print("No solution found.")
 
def main():
   start = (0, 0)  # Starting position
   goal = (4, 4)  # Goal position
 
   path = astar(start, goal, get_neighbors, manhattan_distance)
 
   print_solution(path)
 
if __name__ == "__main__":
   main()