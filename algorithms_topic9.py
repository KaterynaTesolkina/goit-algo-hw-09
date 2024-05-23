def find_coins_greedy(amount):
    # Набір доступних монет, впорядкований у спадаючому порядку
    coins = [50, 25, 10, 5, 2, 1]
    # Словник для зберігання кількості монет кожного номіналу
    coin_count = {coin: 0 for coin in coins}
    
    # Пройтися по кожному номіналу монет
    for coin in coins:
        # Поки поточний номінал монети не перевищує залишок суми
        while amount >= coin:
            # Використати монету поточного номіналу
            coin_count[coin] += 1
            # Зменшити залишок суми
            amount -= coin
    
    # Видалити номінали з нульовою кількістю для чистоти результату
    coin_count = {k: v for k, v in coin_count.items() if v != 0}
    
    return coin_count

# Приклад використання
amount = 113
change = find_coins_greedy(amount)
print(change)

def find_min_coins(amount):
    # Набір доступних монет
    coins = [50, 25, 10, 5, 2, 1]
    # Ініціалізація масиву для зберігання мінімальної кількості монет для кожної суми від 0 до amount
    min_coins = [float('inf')] * (amount + 1)
    # Ініціалізація масиву для зберігання використаних монет для кожної суми від 0 до amount
    coin_used = [-1] * (amount + 1)
    
    # Для суми 0 необхідно 0 монет
    min_coins[0] = 0
    
    # Заповнення масивів мінімальних монет та використаних монет
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin
    
    # Відновлення набору монет з використанням масиву coin_used
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin
    
    return result

# Приклад використання
amount = 113
change = find_min_coins(amount)
print(change)
