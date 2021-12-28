from copy import deepcopy


def helper(length, subset, i, out):
    if i == length:
        out.append(deepcopy(subset))
    else:
        subset[i] = 0
        helper(length, deepcopy(subset), i + 1, out)
        subset[i] = 1
        helper(length, deepcopy(subset), i + 1, out)


def all_subsets(length):
    out = []
    helper(length, [1 for _ in range(length)], 0, out)
    return out


n = input()
table = ""
prev_letters = {}

# find all variables in the expression and putting it in the table variable
for c in n:
    if c not in ['*', '+', '!', '(', ')', ' '] and c not in prev_letters:
        table += c
        prev_letters[c] = 0

# printing the first line in the truth table
o = 0
for c in table:
    if o == 0:
        print(f"""{c} |""", end='')
    else:
        print(f""" {c} |""", end='')
    o += 1
print(f""" {n}""")
mid_lines = ''
for i in range(len(n) + 1 + 4 * len(table) - 1):
    mid_lines += '-'
print(mid_lines)


# taking all the possible combinations between 1 and 0
values = all_subsets(len(table))

# evaluating the expression with each possible combination of 1 and 0 and printing it on the screen
for i in range(len(values)):
    expression = ''
    for j in range(len(n)):
        if n[j] not in ['*', '+', '!', '(', ')', ' ']:
            expression += str(values[i][table.find(n[j])])
        else:
            expression += n[j]
    o = 0
    for value in values[i]:
        if o == 0:
            print(f"""{value} |""", end="")
        else:
            print(f""" {value} |""", end="")
        o += 1
    expression = expression.replace("*", " and ")
    expression = expression.replace("!", " not ")
    expression = expression.replace("+", " or ")
    if not eval(expression):
        print(f""" {0} """)
    else:
        print(f""" {1} """)