import random
X = [1, 1, 2, 3, 3]
X_num = len(X)
epo = 0
while epo <= 10 * X_num:
    Sum = 0
    for i in range(X_num):
        Sum += X[i] * 10 ** i
    print(Sum)
    X = random.sample(X, X_num)
    epo += 1
