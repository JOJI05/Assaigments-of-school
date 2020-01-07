import re
text = "The quick brown fox jumps over the lazy dog."
text = str.lower(text)
chars_array = list(text)
char_dict = {}
for char in chars_array:
    if re.search("[a-z]", char):
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict.setdefault(char, 1)
if len(char_dict) == 26:
    print("全部含まれている")
else:
    print("足りない、探して")
    print(char_dict)
