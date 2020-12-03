

infile = open('PATHHERE', 'r')
data = infile.readline()
infile.close()

list = data.split()
list = [int(i) for i in list]

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] + list[k] == 2020:
            print(list[i] * list[k])
        for k in range(j+1, len(list)):
            if list[i] + list[j] + list[k] == 2020:
                print(list[i])
                print(list[j])
                print(list[k])
                print(list[i] * list[j] * list[k])
