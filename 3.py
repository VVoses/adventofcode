infile = open('PATHHERE', 'r')

lines = infile.read().split()
infile.close()


def traverse(right, down, lines):

    trees = 0
    i = 0

    def inc(index):
        index += right
        if index > 30:
            index -= 31
        return index

    for k in range(0, len(lines), down):
        if not lines[k][i] == ".":
            trees += 1
            print(lines[k][:i] + 'X' + lines[k][i+1:])
        else:
            print(lines[k][:i] + 'O' + lines[k][i+1:])

        i = inc(i)


    return trees
