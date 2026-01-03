import time


def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount = amount % coin

    return result


def find_coins_dynamic(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [None] * (amount + 1)
    dp[0] = []

    for i in range(1, amount + 1):
        for coin in coins:
            remainder = i - coin
            if remainder >= 0 and dp[remainder] != None:
                new_option = dp[remainder] + [coin]
                if dp[i] == None or len(new_option) < len(dp[i]):
                    dp[i] = new_option

    final_list = dp[amount]
    result = {}
    if final_list is not None:
        for coin in final_list:
            result[coin] = result.get(coin, 0) + 1

    return result


test_amount = 1000

# 1. Жадібний алгоритм
start_time = time.time()
greedy_result = find_coins_greedy(test_amount)
greedy_time = time.time() - start_time

# 2. Динамічне програмування
start_time = time.time()
dynamic_result = find_coins_dynamic(test_amount)
dynamic_time = time.time() - start_time

print(f"Сума для видачі: {test_amount}")
print("-" * 30)
print(f"Жадібний алгоритм: {greedy_result}")
print(f"Час виконання: {greedy_time:.6f} сек")
print("-" * 30)
print(f"Динамічний алгоритм: {dynamic_result}")
print(f"Час виконання: {dynamic_time:.6f} сек")
