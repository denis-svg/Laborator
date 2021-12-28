from fractions import Fraction


# getting all the lines from the tree
n = int(input())
lht = []

for i in range(1, n + 1):
    line = [Fraction(1, i)]
    if i > 1:
        for j in range(2, i + 1):
            line.append(lht[i - 2][j - 2] - line[j - 2])
    lht.append(line)

# converting lines from fraction to string
for i in range(len(lht)):
    for j in range(len(lht[i])):
        lht[i][j] = str(lht[i][j])

spaces = []
last_line = lht[-1]
second_last = lht[-2]
j_last = 0
j_second = 0
for i in range(1, 1 + len(last_line) + len(second_last)):
    if i % 2 != 0:
        spaces.append(len(last_line[j_last]))
        j_last += 1
    else:
        spaces.append(len(second_last[j_second]))
        j_second += 1

spaces.append(0)


def add_spaces_after(s, n):
    for i in range(n):
        s += " "
    return s


def add_spaces_before(s, n):
    for i in range(n):
        s = " " + s
    return s


# printing the triangle on screen
for i in range(len(lht)):
    lines_before = len(lht) - (i + 1)
    spaces_before = 0
    for k in range(lines_before):
        spaces_before += spaces[k]
    start_line = len(lht) - (i + 1)
    for j in range(len(lht[i])):
        if j == 0:
            lht[i][0] = add_spaces_before(lht[i][0], spaces_before)
            lht[i][0] = add_spaces_after(lht[i][0], spaces[start_line] - len(lht[i][j]) + spaces_before +
                                         spaces[start_line + 1])
        else:
            lht[i][j] = add_spaces_after(lht[i][j], spaces[start_line] - len(lht[i][j]) + spaces[start_line + 1])
        start_line += 2
        print(lht[i][j], end="")
    print("\n", end="")