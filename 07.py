path = r"C:\Users\hand0\Desktop\py_folder\schoolagenda\data\coffee.csv"
mac_m = 0
mac_w = 0
bucks_m = 0
bucks_w = 0
with open(path, "r", encoding = "utf-8") as f:
    for row in f:
        row_array = row.split(",")
        sto = row_array[0]
        sex = row_array[1]
        if (sto == "マック") and (sex[0] == "男"):
            mac_m += 1
        elif (sto == "マック") and (sex[0] == "女"):
            mac_w += 1
        elif (sto == "スタバ") and (sex[0] == "男"):
            bucks_m += 1
        elif (sto == "スタバ") and (sex[0] == "女"):
            bucks_w += 1
m_array = [mac_m, bucks_m]
w_array = [mac_w, bucks_w]
import pandas as pd
num = [m_array, w_array]
index = ["男性", "女性"]
columns = ["マック", "スタバ"]
pic = pd.DataFrame(data = num, index = index, columns = columns)
print(pic)