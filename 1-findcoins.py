import timeit

# Функція жадібного алгоритму
def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            result[coin] = num_coins
            amount -= num_coins * coin
    return result

# Функція динамічного програмування
def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Обгортка для вимірювання часу жадібного алгоритму
def measure_greedy_time():
    find_coins_greedy(113)

# Обгортка для вимірювання часу алгоритму динамічного програмування
def measure_dp_time():
    find_min_coins(113)

# Вимірювання часу виконання жадібного алгоритму
greedy_time = timeit.timeit(measure_greedy_time, number=1000)

# Вимірювання часу виконання алгоритму динамічного програмування
dp_time = timeit.timeit(measure_dp_time, number=1000)

# Приклад використання функцій
amount = 777
coins_greedy = find_coins_greedy(amount)
coins_dp = find_min_coins(amount)

print(f"Жадібний алгоритм для суми {amount}: {coins_greedy}")
print(f"Динамічне програмування для суми {amount}: {coins_dp}")

print(f"Час виконання жадібного алгоритму: {greedy_time:.6f} секунд")
print(f"Час виконання алгоритму динамічного програмування: {dp_time:.6f} секунд")

# Висновки у форматі markdown
markdown_output = f"""
# Висновки

## Жадібний алгоритм

- **Час виконання**: {greedy_time:.6f} секунд.
- **Продуктивність**: Працює добре для конкретного набору номіналів монет.
- **Недоліки**: Може не знайти оптимального рішення для деяких наборів номіналів.

## Динамічне програмування

- **Час виконання**: {dp_time:.6f} секунд.
- **Продуктивність**: Гарантує мінімальну кількість монет для будь-яких номіналів.
- **Переваги**: Завжди знаходить оптимальне рішення.

## Порівняння

- Жадібний алгоритм швидший, але не завжди оптимальний.
- Алгоритм динамічного програмування повільніший, але завжди оптимальний.
- Для великих сум динамічне програмування гарантує мінімальну кількість монет, хоча може вимагати більше часу на обчислення.
"""

with open('readme.md', 'w', encoding='utf-8') as f:
    f.write(markdown_output)