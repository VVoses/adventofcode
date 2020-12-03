infile = open('PATHHERE', 'r')
lines = [line.split(":") for line in infile]
infile.close()

rules = [i.split() for i, j in lines]
pws = [j.strip() for i, j in lines]



cnt = 0
cnt2 = 0
for i in range(len(rules)):

    char_occ = pws[i].count(rules[i][1])
    upper = int(rules[i][0].split("-")[1])
    lower = int(rules[i][0].split("-")[0])

    if char_occ >= lower and char_occ <= upper:
        cnt+=1

    if (pws[i][lower-1] == rules[i][1] and not pws[i][upper-1] == rules[i][1]) or (pws[i][upper-1] == rules[i][1] and not pws[i][lower-1] == rules[i][1]):
        cnt2+=1
        print(pws[i])
        print(rules[i])
        print(lower)
        print(upper)


print(cnt2)
