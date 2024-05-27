import random
import matplotlib.pyplot as plt
import math

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

# обчислення RMSE
def calculate_rmse(simulated_probs, analytical_probs):
    differences = [(simulated_probs[sum_value] - analytical_probs[sum_value]) ** 2 for sum_value in simulated_probs]
    mean_square_error = sum(differences) / len(differences)
    rmse = math.sqrt(mean_square_error)
    return rmse

if __name__ == "__main__":
    # задаємо кількість симуляцій
    num_rolls = 1000000

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

    # рахуємо RMSE
    rmse = calculate_rmse(simulated_probabilities, analytical_probabilities)
    
    # порівняння результатів
    print(f"{'Сума':<4} {'Ймовірність (Монте-Карло)':<26} {'Ймовірність (Аналітична)':<26}")
    for sum_value in range(2, 13):
        print(f"{sum_value:<4} {simulated_probabilities[sum_value]:<26.2f} {analytical_probabilities[sum_value]:<26.2f}")

    print(f"\nСередньоквадратичне відхилення (RMSE): {rmse:.4f}")

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
