def judge(inputScore):
    return 'good' if inputScore >= 80 else 'bad'
scores = [70,80,90]
for s in scores:
    print(judge(s))

def judge2(inputScore):
    # negative, positive
    return ('bad','good')[inputScore >= 80]
for s in scores:
    print(judge2(s))

def judge3(inputScore):
    if inputScore >= 80:
        return 'good'
    else:
        return 'bad'
for s in scores:
    print(judge3(s))

def judge4(x):
    if x >= 90:
        return 'A'
    elif x>=80:
        return 'B'
    elif x>=70:
        return 'C'
    elif x>=60:
        return 'D'
    else:
        return 'fail'

for s in scores:
    print(judge4(s))