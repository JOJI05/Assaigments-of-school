import re
import matplotlib.pyplot as plt
path = r"C:\Users\hand0\Desktop\py_folder\schoolagenda\data\anne.txt"
with open(path, "r", encoding = "utf-8") as f:
    text = f.read()
key = []
sent_array = re.findall('[A-Z].*[\.\!\?]', text)
for sent in sent_array:
    word_array = sent.split()
    key.append(len(word_array))
maxkey = max(key)
minkey = min(key)
sent_len = {key: 0 for key in range(minkey, maxkey + 1)}
for le in key:
    sent_len[le] += 1
print(sent_len)
del sent_len[1]
del sent_len[2]
print("今回は厳密に文の長さを量れていないからグラフを書く際には1,2を省いた。")
x = list(sent_len.keys())
y = list(sent_len.values())
plt.plot(x, y)
