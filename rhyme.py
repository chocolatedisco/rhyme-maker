import itertools

f = open('nicoi.txt')
data1 = f.read()
f.close()
lines = data1.split('\n')
words = []
for v in lines:
    try:
        tmp = v.split()
        tmp0 = tmp[0]
        tmp0 = tmp0[::-1]
        words.append(tmp0)
    except IndexError:
        pass
# ここまで逆辞書作成


s = input()
n = int(input())
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

for v in tmp:
    for d in words:
        if d.find(v)==0:
            print(d[::-1])
