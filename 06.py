import random
import time
X = [1, 1, 2, 3, 3]
anser_array = []
X_num = len(X)
epo = 0
while epo <= 100 * X_num:
    Sum = 0
    for i in range(X_num):
        Sum += X[i] * 10 ** i
    anser_array.append(Sum)
    X = random.sample(X, X_num)
    epo += 1
anser_array = sorted(list(set(anser_array)))
print("Enumerate!!!")
time.sleep(1)
for i in anser_array:
    print(i, end = "")
    print(" ", end = "")
time.sleep(1)
print("")
print("上の数字の種類は", len(anser_array))
print("解析的に計算すると全部で5*3*2*1 = ", len(anser_array))
print(sum(anser_array))