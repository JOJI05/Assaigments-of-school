text = input()
output = ""
text_array = text.split(",")
for i in text_array:
    if int(i) % 2 == 0:
        output += i + ","
output = output.strip(",")
print(output)
