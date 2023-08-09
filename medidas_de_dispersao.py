#Medidas de dispersão
#data deve ser uma estrutura iterável contendo números. Tratar a exceção

def mean(data):
    sum = 0
    n = 0
    for value in data:
        sum += value
        n += 1
    return sum / n

def gmean(data):
    product = 1
    n = 0
    for value in data:
        product *= value
        n += 1
    return product **(1.0/n)

def hmean(data):
    numerator = 0
    denominator = 0
    for value in data:
        numerator += 1
        denominator += 1.0 / value
    return numerator / denominator

def wmean(data, weights):
    sum = 0
    wsum = 0
    i = 0
    for value in data:
        sum += value * weights[i]
        wsum += weights[i]
        i += 1
    return sum / wsum

def median(data):
    n = 0
    for value in data:
        n += 1
    if(n % 2 == 1):
        print(2)
    else:
        print(3)