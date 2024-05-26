import random
import matplotlib.pyplot as plt

# симуляція кидків кубиків
def roll_dice_simulation(num_rolls):
    results = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        results[roll_sum] += 1
    return results

# ймовірность на основі результатів симуляції
def calculate_probabilities(results, num_rolls):
    probabilities = {k: v / num_rolls * 100 for k, v in results.items()}
    return probabilities

if __name__ == "__main__":
    # задаємо кількість симуляцій
    num_rolls = 10000

    simulation_results = roll_dice_simulation(num_rolls)
    simulated_probabilities = calculate_probabilities(simulation_results, num_rolls)

    # з задачі ймовірності
    analytical_probabilities = {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78
    }

    # порівняння результатів
    print(f"{'Сума':<4} {'Ймовірність (Монте-Карло)':<26} {'Ймовірність (Аналітична)':<26}")
    for sum_value in range(2, 13):
        print(f"{sum_value:<4} {simulated_probabilities[sum_value]:<26.2f} {analytical_probabilities[sum_value]:<26.2f}")

    # будуємо графік
    sums = list(simulated_probabilities.keys())
    sim_probs = list(simulated_probabilities.values())
    anal_probs = list(analytical_probabilities.values())

    plt.plot(sums, sim_probs, label='Монте-Карло', marker='o')
    plt.plot(sums, anal_probs, label='Аналітична', marker='x')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірність сум при киданні двох кубиків')
    plt.legend()
    plt.grid(True)
    plt.show()
