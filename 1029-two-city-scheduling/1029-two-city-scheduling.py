class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        # calculate the total cost of sending all people to city A
        totalCost = 0
        difCost = []
        for cost in costs:
            totalCost += cost[0]
            # calculate the diffence of sending each person to city B
            # instead of city A
            difCost.append(cost[1] - cost[0])
        
        # sort the array
        difCost = sorted(difCost)
        
        # calculate cost after moving people to city B
        people = int(len(costs)/2)
        for i in range(people):
            totalCost += difCost[i]
            
        return totalCost