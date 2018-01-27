def iterative(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


print("iterative function", iterative(100))

# recursive calls upon itself but iterative functions just keep building and building


def recursive(n):
    if n == 1:
        return 1
    else:
        return n + recursive(n - 1)


print("recursive function", recursive(100))

