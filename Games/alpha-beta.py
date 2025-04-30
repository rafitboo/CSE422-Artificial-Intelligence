import math
import random

def strength(x):
    return math.log2(x + 1) + (x / 10)

def utility(maxV, minV):
    i = random.randint(0, 1)  
    random_factor = ((-1) ** i) * (random.randint(1, 10) / 10)
    return strength(maxV) - strength(minV) + random_factor

def minimax(depth, alpha, beta, maximizer, maxV, minV):

    if depth == 0:
        return utility(maxV, minV)
    
    if maximizer: 
        max_eval = -math.inf
        for _ in range(2):
            eval = minimax(depth-1, alpha, beta, False, maxV, minV)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if alpha >= beta:
                break  
        return max_eval
    
    else:
        min_eval = math.inf
        for _ in range(2):
            eval = minimax(depth-1, alpha, beta, True, maxV, minV)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if alpha >= beta:
                break 
        return min_eval
    
# problem -1

def simulate_games():

    starting_player = int(input("Enter starting player for game 1 (0 for Carlsen, 1 for Caruana): "))
    carlsen_strength = float(input("Enter base strength for Carlsen: "))
    caruana_strength = float(input("Enter base strength for Caruana: "))
    
    results = []
    
    for game in range(4): 
        if (starting_player + game) % 2 == 0:
            max_player = "Magnus Carlsen"
            min_player = "Fabiano Caruana"
            maxV = carlsen_strength
            minV = caruana_strength
        else:
            max_player = "Fabiano Caruana"
            min_player = "Magnus Carlsen"
            maxV = caruana_strength
            minV = carlsen_strength
        
        value = minimax(5, -math.inf, math.inf, True, maxV, minV)
        

        if value > 0:
            winner = f"{max_player} (Max)"
        elif value < 0:
            winner = f"{min_player} (Min)"
        else:
            winner = "Draw"
        
        if "Carlsen" in winner:
            results.append("Carlsen")
        else:
            results.append("Caruana")
        print(f"Game {game+1} Winner: {winner} (Utility value: {value:.2f})")
    
    carlsen_wins = results.count("Carlsen")
    caruana_wins = results.count("Caruana")
    draws = 4 - carlsen_wins - caruana_wins
    
    print("\nOverall Results:")
    print(f"Magnus Carlsen Wins: {carlsen_wins}")
    print(f"Fabiano Caruana Wins: {caruana_wins}")
    print(f"Draws: {draws}")
    
    if carlsen_wins > caruana_wins:
        print("Overall Winner: Magnus Carlsen")
    elif caruana_wins > carlsen_wins:
        print("Overall Winner: Fabiano Caruana")
    else:
        print("Overall Winner: Draw")


simulate_games()

###################################problem -2########################################

def minimax2(depth, alpha, beta, maximizer, maxV, minV, use_mind_control=False):

    if depth == 0:
        return utility(maxV, minV)
    
    if maximizer:
        max_eval = -math.inf
        for _ in range(2):
            if use_mind_control:
                eval = minimax2(depth-1, alpha, beta, True, maxV, minV, False)
            else:
                eval = minimax2(depth-1, alpha, beta, False, maxV, minV, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for _ in range(2): 
            eval = minimax2(depth-1, alpha, beta, True, maxV, minV, False)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def chess_with_mind_control():
    first_player = int(input("Enter who goes first (0 for Light, 1 for L): "))
    cost = float(input("Enter the cost of using Mind Control: "))
    light_strength = float(input("Enter base strength for Light: "))
    l_strength = float(input("Enter base strength for L: "))

    if first_player == 0:
        max_player, min_player = "Light", "L"
        maxV, minV = light_strength, l_strength
    else:
        max_player, min_player = "L", "Light"
        maxV, minV = l_strength, light_strength
    
    normal_value = minimax2(5, -math.inf, math.inf, True, maxV, minV, False)
    mc_value = minimax2(5, -math.inf, math.inf, True, maxV, minV, True)
    mc_net_value = mc_value - cost
    
    print(f"\nMinimax value without Mind Control: {normal_value:.2f}")
    print(f"Minimax value with Mind Control: {mc_value:.2f}")
    print(f"Minimax value with Mind Control after incurring the cost: {mc_net_value:.2f}")
    
    if normal_value > 0 and mc_net_value > 0:
        print(f"{max_player} should NOT use Mind Control as the position is already winning.")
    elif normal_value <= 0 and mc_net_value <= 0:
        print(f"{max_player} should NOT use Mind Control as the position is losing either way.")
    elif normal_value <= 0 < mc_net_value:
        print(f"{max_player} should use Mind Control.")
    else:
        print(f"{max_player} should NOT use Mind Control as it backfires.")


chess_with_mind_control()