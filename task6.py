def find_items_greedy(budget, items):
    result = {}
    remaining_budget = budget

    # список продуктів із кількістю калорій на одиницю вартості
    item_list = []
    for item, info in items.items():
        calories_per_cost = info['calories'] / info['cost']
        item_list.append((item, info['cost'], info['calories'], calories_per_cost))
    
    # сортуємо список за кількістю калорій на одиницю вартості (за зменшенням)
    sorted_items = sorted(item_list, key=lambda x: x[3], reverse=True)

    for item, cost, calories, _ in sorted_items:
        if remaining_budget >= cost:
            num_items = 1  # вибираємо кожен предмет тільки один раз
            remaining_budget -= num_items * cost
            result[item] = num_items
    
    return result


def find_max_calories_dp(budget, items):
    
    item_names = list(items.keys())
    costs = [items[item]['cost'] for item in item_names]
    calories = [items[item]['calories'] for item in item_names]
    n = len(items)
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    item_taken = [[False] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                if dp[i - 1][w - costs[i - 1]] + calories[i - 1] > dp[i - 1][w]:
                    dp[i][w] = dp[i - 1][w - costs[i - 1]] + calories[i - 1]
                    item_taken[i][w] = True
                else:
                    dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = dp[i - 1][w]

    result = {}
    w = budget
    for i in range(n, 0, -1):
        if item_taken[i][w]:
            item = item_names[i - 1]
            result[item] = 1
            w -= costs[i - 1]
    
    return result



if __name__ == "__main__":
   
    items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
    }

    budget = int(input("Введіть бюджет на харчування (середня вартість 100): "))
    # жадібний алгоритм
    print(f"Жадібний алгоритм: {find_items_greedy(budget, items)}")  

    # динамічне програмування
    print(f"Динамічне програмування: {find_max_calories_dp(budget, items)}")  