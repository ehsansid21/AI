class State:
    def __init__(self, missionaries, cannibals, boat):
      
        self.missionaries = missionaries  
        self.cannibals = cannibals        
        self.boat = boat                 
    def __eq__(self, other):
        
        return (self.missionaries == other.missionaries and 
                self.cannibals == other.cannibals and 
                self.boat == other.boat)

    def __hash__(self):
        
        return hash((self.missionaries, self.cannibals, self.boat))


def is_valid(state):
    
    if state.missionaries < state.cannibals and state.missionaries > 0:
        return False
    if 3 - state.missionaries < 3 - state.cannibals and 3 - state.missionaries > 0:
        return False
    return True


def get_successors(state):
    
    successors = []
    if state.boat == 0:  
        for i in range(1, 3): 
            for j in range(0, 3):
                if is_valid(State(state.missionaries - i, state.cannibals - j, 1)):
                    successors.append(State(state.missionaries - i, state.cannibals - j, 1))
    else: 
        for i in range(1, 3): 
            for j in range(0, 3):
                if is_valid(State(state.missionaries + i, state.cannibals + j, 0)):
                    successors.append(State(state.missionaries + i, state.cannibals + j, 0))
    return successors


def bfs(start, target):
    
    visited = set()       
    frontier = []           
    frontier.append([start])  

    while frontier:
        path = frontier.pop(0)  
        current_state = path[-1]       

        if current_state == target: 
            return path

        visited.add(current_state)

        for next_state in get_successors(current_state): 
            if next_state not in visited:               
                new_path = list(path)               
                new_path.append(next_state)             
                frontier.append(new_path)   

    return None  


def print_solution(path):
   
    print("Solution:")
    for i, state in enumerate(path):
        print(f"Step {i}: Left Bank({state.missionaries}, {state.cannibals}), "
              f"Right Bank({3 - state.missionaries}, {3 - state.cannibals}), "
              f"Boat: {'Left' if state.boat == 0 else 'Right'}")


def main():
   
    start_state = State(3, 3, 0)      
    target_state = State(0, 0, 1)      
    path = bfs(start_state, target_state)  
    if path:  
        print_solution(path)          
    else: 
        print("No solution found.")


if __name__ == "__main__":
    main()