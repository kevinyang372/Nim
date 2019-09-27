# applies the Minimax and Alpha-beta pruning to find the best strategy

# decide based on the current state
def decide(state, alpha, beta, maxTurn):
    # determining final state
    if (sum(state) == 1 and maxTurn) or (sum(state) == 0 and not maxTurn): return (-1, [state])
    if (sum(state) == 1 and not maxTurn) or (sum(state) == 0 and maxTurn): return (1, [state])
    
    if maxTurn:
        res_max = -float('inf')
        res = None
        for i in find_next(state):
            # recursively search for the next possible move
            val, temp = decide(i, alpha, beta, not maxTurn)
            if val > res_max:
                res_max = val
                res = temp
            # update the upper bound
            alpha = max(alpha, val)
            # pruning
            if alpha >= beta:
                break
        return res_max, [state] + res
    else:
        res_min = float('inf')
        res = None
        for i in find_next(state):
            val, temp = decide(i, alpha, beta, not maxTurn)
            if val < res_min:
                res_min = val
                res = temp
            beta = min(beta, val)
            if alpha >= beta:
                break
        return res_min, [state] + res
    
# find all possible next moves
def find_next(state):
    visited = set()
    res = []
    
    for i in range(len(state)):
        for m in range(1, state[i] + 1):
            temp = list(state[:])
            temp[i] -= m
            
            # check if the stage already exists
            rearranged = tuple(sorted(temp))
            if rearranged not in visited:
                res.append(temp)
                visited.add(rearranged)
    
    return res