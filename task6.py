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
            num_items = remaining_budget // cost
            remaining_budget -= num_items * cost
            result[item] = num_items
    
    return result


def find_max_calories_dp(budget, items):
    
    item_names = list(items.keys())
    costs = [items[item]['cost'] for item in item_names]
    calories = [items[item]['calories'] for item in item_names]
    n = len(items)
    
    dp = [0] * (budget + 1)
    item_count = [{} for _ in range(budget + 1)]

    for i in range(n):
        for j in range(costs[i], budget + 1):
            if dp[j - costs[i]] + calories[i] > dp[j]:
                dp[j] = dp[j - costs[i]] + calories[i]
                item_count[j] = item_count[j - costs[i]].copy()
                if item_names[i] in item_count[j]:
                    item_count[j][item_names[i]] += 1
                else:
                    item_count[j][item_names[i]] = 1

    return item_count[budget]


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