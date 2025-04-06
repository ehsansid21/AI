class State:
   def __init__(self, jug1, jug2):
       # Initialize the state of the jugs
       self.jug1 = jug1  # Amount of water in jug1
       self.jug2 = jug2  # Amount of water in jug2
 
   def __eq__(self, other):
       # Define equality of states
       return self.jug1 == other.jug1 and self.jug2 == other.jug2
 
   def __hash__(self):
       # Define hash function for states
       return hash((self.jug1, self.jug2))
 
def dfs(start, target, visited):
   # Check if a state is the goal state
   if start == target:
       return [start]  # If the current state is the target state, return it
   
   visited.add(start)  # Add the current state to visited states
   
   for next_state in get_successors(start):  # For each possible next state
       if next_state not in visited:  # If the next state has not been visited
           path = dfs(next_state, target, visited)  # Recursively call DFS on the next state
           if path:  # If a solution path is found
               return [start] + path  # Return the current state and the solution path
   return None  # If no solution path is found, return None
 
def get_successors(state):
   # Generate successor states from a given state
   successors = []  # List to store successor states
   
   # Fill jug1 (fill jug1 to its capacity, which is 3)
   if state.jug1 < 3:
       successors.append(State(jug1=3, jug2=state.jug2))
 
   # Fill jug2 (fill jug2 to its capacity, which is 4)
   if state.jug2 < 4:
       successors.append(State(jug1=state.jug1, jug2=4))
 
   # Empty jug1 (empty jug1 to 0)
   if state.jug1 > 0:
       successors.append(State(jug1=0, jug2=state.jug2))
 
   # Empty jug2 (empty jug2 to 0)
   if state.jug2 > 0:
       successors.append(State(jug1=state.jug1, jug2=0))
 
   # Pour jug1 to jug2
   pour_amount = min(state.jug1, 4 - state.jug2)  # Amount that can be poured from jug1 to jug2
   if pour_amount > 0:
       successors.append(State(jug1=state.jug1 - pour_amount, jug2=state.jug2 + pour_amount))
 
   # Pour jug2 to jug1
   pour_amount = min(state.jug2, 3 - state.jug1)  # Amount that can be poured from jug2 to jug1
   if pour_amount > 0:
       successors.append(State(jug1=state.jug1 + pour_amount, jug2=state.jug2 - pour_amount))
 
   return successors
 
def print_solution(path):
   # Print the solution path
   print("Solution:")
   for i, state in enumerate(path):
       print(f"Step {i}: Jug1={state.jug1}, Jug2={state.jug2}")
 
def main():
   # Initial state of the jugs
   start_state = State(jug1=0, jug2=0)
   
   # Target state we want to achieve (2 units in jug1 and 0 units in jug2)
   target_state = State(jug1=2, jug2=0)
   
   # Set to store visited states
   visited = set()
   
   # Find solution using DFS
   path = dfs(start_state, target_state, visited)
   
   if path:  # If solution path is found
       print_solution(path)  # Print the solution path
   else:  # If no solution path is found
       print("No solution found.")
 
if __name__ == "__main__":
   main()
 
