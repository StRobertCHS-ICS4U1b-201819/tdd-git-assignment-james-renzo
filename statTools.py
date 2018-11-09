def mean(x):
    if(x) == str(x):
        return "None"
    else:
        return round(sum(x) / len(x), 2)

def median(x):
    midLoc = (0 + len(x))//2
    Avg = x[midLoc]
    return Avg