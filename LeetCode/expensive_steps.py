def minCostClimbingStairs(cost):
    first = cost[0]
    second = cost[1]
    for i in range(2, len(cost)):
        current = cost[i] + min(first, second)
        first, second = second, current
    return min(first, second)
cost1 = [10, 15, 20]
print(minCostClimbingStairs(cost1)) 


cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost2)) 
