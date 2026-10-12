def totalFruit(fruits):
    if not fruits:
        return 0
    max_fruits = 0
    l= 0
    fruit_count = {}
    for r in range(len(fruits)):
        fruit_count[fruits[r]] = fruit_count.get(fruits[r], 0) + 1
        while len(fruit_count) > 2:
            fruit_count[fruits[l]] -= 1
            if fruit_count[fruits[l]] == 0:
                del fruit_count[fruits[l]]
            l += 1
        max_fruits = max(max_fruits, r - l + 1)

    return max_fruits
Fruits = [1,2,1]
result = totalFruit(Fruits)
print(result)