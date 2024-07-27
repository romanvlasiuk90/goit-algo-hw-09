
# Висновки

## Жадібний алгоритм

- **Час виконання**: 0.000406 секунд.
- **Продуктивність**: Працює добре для конкретного набору номіналів монет.
- **Недоліки**: Може не знайти оптимального рішення для деяких наборів номіналів.

## Динамічне програмування

- **Час виконання**: 0.038350 секунд.
- **Продуктивність**: Гарантує мінімальну кількість монет для будь-яких номіналів.
- **Переваги**: Завжди знаходить оптимальне рішення.

## Порівняння

- Жадібний алгоритм швидший, але не завжди оптимальний.
- Алгоритм динамічного програмування повільніший, але завжди оптимальний.
- Для великих сум динамічне програмування гарантує мінімальну кількість монет, хоча може вимагати більше часу на обчислення.