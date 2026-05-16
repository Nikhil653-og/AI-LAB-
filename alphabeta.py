import math

leaf_values = [5, 3, 2, 4, 1, 3, 6, 2, 8, 7, 5, 1, 3, 4]

index = len(leaf_values) - 1 

def alpha_beta(depth, is_max, alpha, beta):
    global index

    if depth == 4:
        val = leaf_values[index]
        print(f"Leaf reached: {val}")
        index -= 1
        return val

    if is_max:
        best = -math.inf

        for _ in range(2):
            if index < 0: break
            val = alpha_beta(depth + 1, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            

            if beta <= alpha:
                print(f"  Pruning at MAX level (depth {depth})")
                break
        return best
    else:
        best = math.inf

        for _ in range(2):
            if index < 0: break
            val = alpha_beta(depth + 1, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                print(f"  Pruning at MIN level (depth {depth})")
                break
        return best

print("Starting Search (Right-to-Left)...\n")
result = alpha_beta(0, False, -math.inf, math.inf)
print(f"\nThe final value at the root (MIN) is: {result}")