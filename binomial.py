import math

def prob(n, p, N):
    nCk = math.factorial(N) / (math.factorial(n) * math.factorial(N - n))
    result = nCk * pow(p, n) * pow(1 - p, N - n)
    return result

def infoMeasure(n, p, N):
    pr = prob(n, p, N)
    result = - math.log(pr, 2)
    return result

def sumProb(N, p):
    """ Khi gọi hàm sumProb(10, 0.5) ta được kết quả là 0.998046875 ~ 1
        Khi gọi hàm sumProb(50, 0.3) ta được kết quả là 0.9999999999999982 ~ 1
        Như vậy hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố binamial bằng 1 """
    sum = 0
    for i in range(1, N):
        sum += prob(i, p, N)
    return sum

def approxEntropy(N, p):
    """ Entropy của nguồn binomial với N=100, p=1/2 là 4.369011409223017
        Entropy của nguồn binomial với N=1000, p=1/2 là 6.029987607045884 """
    entropy = 0
    for i in range(1, N):
        entropy += prob(i, p, N) * infoMeasure(i, p, N)
    return entropy

print(approxEntropy(100, 0.5))
print(approxEntropy(1000, 0.5))
