def mean(x):
    if x == str(x):
        return "None"
    else:
        return round(sum(x) / len(x), 2)

def median(x):
    x.sort()
    mid = (0 + len(x)) // 2
    Avg = x[mid]
    if len(x) % 2 == 0:
        return x[Avg-1]
    else:
        return Avg

def mode(x):
    if x == str(x):
        return "None"
    else:
        Avg = max(set(x),key=x.count)
        return Avg

def range(x):
    return 4