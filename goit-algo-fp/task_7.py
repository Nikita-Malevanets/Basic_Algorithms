import random

num_experiments = 100_000

sum_counts = {sum_value: 0 for sum_value in range(2, 13)}

for _ in range(num_experiments):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    current_sum = dice_1 + dice_2
    sum_counts[current_sum] += 1

monte_carlo_probabilities = {}

for sum_value in range(2, 13):
    count_for_sum = sum_counts[sum_value]
    monte_carlo_probability = count_for_sum / num_experiments
    monte_carlo_probabilities[sum_value] = monte_carlo_probability

theoretical_probabilities = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36
}

print("Сума | Monte-Carlo | Теорія")
print("-" * 32)

for sum_value in range(2, 13):
    mc = monte_carlo_probabilities[sum_value]
    theory = theoretical_probabilities[sum_value]
    print(f"{sum_value:>4} | {mc:>11.4f} | {theory:>7.4f}")
