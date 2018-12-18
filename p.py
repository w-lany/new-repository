def stringify(n):
    a = ""
    if n %2 == 0:
        a = str(n) + " is even"
    else:
        a = str(n) + " is odd"
    return a

assert stringify(10) == "10 is even"
assert stringify(5) == "5 is odd"

def compute_stats(lst):
    stats= []
    list = lst
    list.sort()
    stats.append(list[-2])
    n= 0
    for i in list:
        n += i
    stats.append(int(n/len(list)))
    a = 0
    if len(list)%2 == 0:
        a = (list[len(list)/2] + list[(len(list)/2)+1])/2
    else:
        a = list[(len(list)//2)]
    stats.append(a)
    return stats

stats = compute_stats([1, 12, 4, 5, 8])
assert stats[0]==8 and stats[1]==6 and stats[2]==5


def count_letters(s):
    dic = {"upper":0, "lower":0}
    for i in s:
        if i.isupper():
            dic["upper"] += 1
        if i.islower():
            dic["lower"] += 1
    return dic

d = count_letters("Abc Defg HiJ!")
assert d["upper"]==4 and d["lower"]==6


def mirror(s):
    str = ""
    print(str)
    for i in range(2, len(s)+1):
        str += s[-i]
    return s+str

assert mirror("")==""
assert mirror("a")=="a"
assert mirror("abc")=="abcba"

