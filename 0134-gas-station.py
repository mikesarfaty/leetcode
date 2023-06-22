class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        nn = len(gas)
        tank = 0
        min_tank = 0
        min_station = 0

        for i in range(len(gas)):
            if i > 0:
                tank -= cost[i - 1]
            if tank < min_tank:
                min_tank = tank
                min_station = i
            tank += gas[i]

        tank -= cost[i]
        if tank < min_tank:
            min_tank = tank
            min_station = nn

        if tank >= 0:
            return min_station % nn
        else:
            return -1
