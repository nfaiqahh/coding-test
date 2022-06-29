def sum_recursive(start, end):
    numrange = list(range(start, end+1))
    total = 0
    for x in numrange:
        total = total + x
    print(total)

sum_recursive(1, 10)