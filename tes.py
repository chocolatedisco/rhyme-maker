import itertools

s = input()
n = 3
s = s[::-1]
dict = {"あ":"あかがさざただなはばぱまやらわ", "い":"いきぎしじちぢなひびぴみり", "う":"うくぐすずつづぬふぶぷむゆる","え":"えけげせぜてでねへべぺれ","お":"おこごそぞとどのほぼぽよろを"}
tmp = list(dict[s[0]])
for i in range(1,n):
    rym = list(itertools.product(tmp,list(dict[s[i]])))
    tmp = []
    for v in rym:
        text = "".join(map(str, v))
        tmp.append(text)

# tmpに検索用リストが入っている。
