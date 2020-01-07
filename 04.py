text = "Now I need a drink, alcoholic of course, after the heavy lectures involving puantum mechanics"
text_array = text.split()
for word in text_array:
    a = word.strip(",.")
    print(len(a), end = "")
