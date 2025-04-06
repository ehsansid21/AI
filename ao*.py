import heapq
 
class Node:
   """A class representing a node in the search tree."""
   def __init__(self, state, parent=None):
       self.state = state  # Current state of the node
       self.parent = parent  # Parent node
       self.g = 0  # Cost from start node to current node
       self.h = 0  # Heuristic estimate from current node to goal node
       self.f = 0  # Total estimated cost (g + h)
 
   def __lt__(self, other):
       """Comparison function for priority queue (min heap)."""
       return self.f < other.f
 
def ao_star(start, goal, get_neighbors, heuristic):
   """AO* search algorithm."""
   open_list = []  # Priority queue for nodes to be evaluated
   open_dict = {}  # Dictionary to track nodes in open_list
   closed_set = set()  # Set of nodes already evaluated
 
   # Initialize start node
   start_node = Node(state=start)
   start_node.h = heuristic(start, goal)
   start_node.f = start_node.g + start_node.h
   heapq.heappush(open_list, start_node)
   open_dict[start] = start_node
 
   while open_list:
       current_node = heapq.heappop(open_list)
       open_dict.pop(current_node.state, None)  # Remove from tracking
 
       if current_node.state == goal:
           # Goal reached, reconstruct the path
           path = []
           while current_node:
               path.append(current_node.state)
               current_node = current_node.parent
           path.reverse()
           return path
 
       closed_set.add(current_node.state)
 
       for neighbor_state in get_neighbors(current_node.state):
           if neighbor_state in closed_set:
               continue  # Skip already evaluated nodes
 
           # Compute tentative cost
           tentative_g = current_node.g + 1  # Assuming uniform step cost
 
           if neighbor_state in open_dict:
               neighbor_node = open_dict[neighbor_state]
               if tentative_g < neighbor_node.g:
                   neighbor_node.g = tentative_g
                   neighbor_node.f = neighbor_node.g + neighbor_node.h
                   neighbor_node.parent = current_node
                   heapq.heapify(open_list)  # Re-sort priority queue
           else:
               # Create new node
               neighbor_node = Node(state=neighbor_state, parent=current_node)
               neighbor_node.g = tentative_g
               neighbor_node.h = heuristic(neighbor_state, goal)
               neighbor_node.f = neighbor_node.g + neighbor_node.h
               heapq.heappush(open_list, neighbor_node)
               open_dict[neighbor_state] = neighbor_node
 
   return None  # No path found
 
def manhattan_distance(state, goal):
   """Heuristic function: Manhattan distance."""
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])
 
def get_neighbors(state):
   """Get neighboring states (moving up, down, left, right in a 5x5 grid)."""
   x, y = state
   neighbors = []
   for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
       new_x, new_y = x + dx, y + dy
       if 0 <= new_x < 5 and 0 <= new_y < 5:  # Grid boundaries
           neighbors.append((new_x, new_y))
   return neighbors
 
def print_solution(path):
   """Print the solution path."""
   print("Solution Path:")
   for i, state in enumerate(path):
       print(f"Step {i}: {state}")
 
def main():
   """Example problem: Find path in a 5x5 grid."""
   start = (0, 0)
   goal = (4, 4)
   path = ao_star(start, goal, get_neighbors, manhattan_distance)
   if path:
       print_solution(path)
   else:
       print("No solution found.")
 
if __name__ == "__main__":
   main()
