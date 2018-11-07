def mean(x):
    if x == "Illegal Input":
        return "None"
    else:
        return round(sum(x) / len(x), 2)

