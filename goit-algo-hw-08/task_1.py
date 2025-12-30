import heapq


def connect_cables(cables):
    if len(cables) == 0:
        return 0

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        current_connect_cost = first + second
        total_cost = total_cost + current_connect_cost

        heapq.heappush(cables, current_connect_cost)

    return total_cost


my_cables = [4, 2, 8, 6, 7, 9]
result = connect_cables(my_cables)
print(result)
