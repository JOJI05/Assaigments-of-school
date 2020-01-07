def VOW_JUD(char):
    vowel = ["a", "i", "u", "e", "o"]
    JUD_array = []
    for v in vowel:
        JUD_array.append(v == char)
    jud = any(JUD_array)
    return(jud)

def F(array):
    new = []
    for verb in array:
        if verb[-1] == "f":
            verb = verb.strip("f")
            verb = verb + "ves"
            new.append(verb)
        else:
            new.append(verb)
    return(new)

def FEE(array):
    new = []
    for verb in array:
        if (verb[-1] == "e") and (verb[-2] == "f"):
            verb = verb.strip("fe")
            verb = verb + "ves"
            new.append(verb)
        else:
            new.append(verb)
    return(new)

def CON(array):
    new = []
    for verb in array:
        vow = VOW_JUD(verb[-2])
        con = not vow
        if (verb[-1] == "y") and con:
            verb = verb.strip("y")
            verb = verb + "ies"
            new.append(verb)
        else:
            new.append(verb)
    return(new)

def ES(array):
    new = []
    for verb in array:
        if (verb[-1] == "s") or (verb[-1] == "z") or (verb[-1] == "x") or ((verb[-1] == "h") and ((verb[-2] == "c") or (verb[-2] == "s"))):
            verb = verb + "es"
            new.append(verb)
        else:
            new.append(verb)
    return(new)

def O(array):
    new = []
    for verb in array:
        if verb[-1] == "o":
            verb = verb + "es"
            new.append(verb)
        else:
            new.append(verb)
    return(new)


DO_array = []
print("Enterだけを入力すると入力を終了します")
while True:
    DO = input("")
    if DO:
        DO_array.append(DO)
    else:
        break

f = ES(DO_array)
es = FEE(f)
f_2 = F(es)
o = O(f_2)
co = CON(o)
final = []
i = 0
for verb in co:
    if verb == DO_array[i]:
        verb = verb + "s"
    final.append(verb)
    i += 1
for verb in final:
    print(verb)
