text = input()
text_array = text.split(",")
SUM = sum(int(i) for i in text_array)
print(SUM)
