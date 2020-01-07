import re
path = r"C:\Users\hand0\Desktop\py_folder\schoolagenda\data\anne.txt"
with open(path, "r", encoding = "utf-8") as f:
    text = f.read()

print("1行目から順に")
sent_array = re.findall('[A-Z].*[\.\!\?]', text)
for sent in sent_array:
    word_array = sent.split()
    print(len(word_array), end = ",")
