from copy import deepcopy
from sys import maxsize

with open("matrix.txt", "r") as f:
    lines = f.readlines()
    names = lines[0].split("|")
    graph = {}
    for i in range(0, len(names)):
        names[i] = names[i].strip()
    for i in range(1, len(lines)):
        line = lines[i].split()
        graph[names[i - 1]] = []
        for j in range(0, len(line)):
            if line[j] == "1":
                graph[names[i - 1]].append(names[j - 3])

with open("influence.txt", "r") as f:
    lines = f.readlines()
    influence = {}
    for line in lines:
        t = line.split(" : ")
        t[1] = t[1][0:-1]
        influence[t[0]] = float(t[1])

with open("interests.txt", "r") as f:
    interests = f.readlines()
    for i in range(len(interests)):
        interests[i] = interests[i][0:-1]

with open("people_interests.txt", "r") as f:
    people_interests = {}
    lines = f.readlines()
    for line in lines:
        people_interests[line.split(":")[0].strip()] = line.split(":")[1].split()

"""Problem 1. Friends"""
print("-----------------------------------------")
print("Problem 1")
most_friends = names[0]
for name in names:
    if len(graph[name]) > len(graph[most_friends]):
        most_friends = name
print(f"""The most amount of friends has {most_friends}. He/she has {len(graph[most_friends])} friends.""")

"""Problem 2. Sort"""
print("-----------------------------------------")
print("Problem 2")
sorted_list = deepcopy(names)

for i in range(len(sorted_list)):
    min_idx = i
    for j in range(i + 1, len(sorted_list)):
        if len(graph[sorted_list[min_idx]]) > len(graph[sorted_list[j]]):
            min_idx = j
    sorted_list[min_idx], sorted_list[i] = sorted_list[i], sorted_list[min_idx]

for i in range(len(sorted_list)):
    print(f"""{sorted_list[i]} - {len(graph[sorted_list[i]])}""")

"""Problem 3. Let's do ratings"""
print("-----------------------------------------")
print("Problem 3")


def min_node(dijkstra, visited):
    min = [maxsize, None]
    for name in names:
        if min[0] > dijkstra[name][0] and name not in visited:
            min[0] = dijkstra[name][0]
            min[1] = name
    return min[1]


def shortest_path(start):
    visited = []
    unvisited = deepcopy(names)
    dijkstra = {}
    for name in names:
        dijkstra[name] = [maxsize, None]
    dijkstra[names[start]][0] = 0
    while unvisited:
        current_node = min_node(dijkstra, visited)
        neighbors = graph[current_node]
        for neighbor in neighbors:
            if dijkstra[neighbor][0] == maxsize:
                dijkstra[neighbor][0] = dijkstra[current_node][0] + 1
                dijkstra[neighbor][1] = current_node
            elif dijkstra[neighbor][0] > dijkstra[current_node][0] + 1:
                dijkstra[neighbor][0] = dijkstra[current_node][0] + 1
                dijkstra[neighbor][1] = current_node
        visited.append(current_node)
        unvisited.remove(current_node)
    return dijkstra


# start = 0
# end = 1
# dijkstra = shortest_path(start)
# print(f"""{names[end]}<-""", end="")
# previous_node = dijkstra[names[end]][1]
# while names[start] != previous_node:
#    print(f"""{previous_node}<-""", end="")
#    previous_node = dijkstra[previous_node][1]
# print(names[start])
# print(dijkstra)


ratings = {}
for i in range(0, len(names)):
    score = 0
    dijkstra = shortest_path(i)
    for name in names:
        score += dijkstra[name][0]
    ratings[names[i]] = score

for name in names:
    print(name, ratings[name])

"""Problem 4. Influential people"""
print("-----------------------------------------")
print("Problem 4")
for name in names:
    influence[name] *= 0.5 * ratings[name]
sorted_influence = deepcopy(names)
for i in range(len(sorted_influence)):
    min_idx = i
    for j in range(i + 1, len(sorted_influence)):
        if influence[sorted_influence[min_idx]] > influence[sorted_influence[j]]:
            min_idx = j
    sorted_influence[min_idx], sorted_influence[i] = sorted_influence[i], sorted_influence[min_idx]

for i in range(len(sorted_influence)):
    print(f"""{sorted_influence[i]} - {influence[sorted_influence[i]]}""")

"""Problem 5.  Analyze your content"""
print("-----------------------------------------")
print("Problem 5")
sentence = "From T-Rex to Multi Universes: How the Internet has Changed Politics, Art and Cute Cats.".split()
my_interests = []
for i in range(0, len(sentence)):
    if ":" in sentence[i] or "." in sentence[i]:
        sentence[i] = sentence[i][0:-1]
    if sentence[i] in interests:
        print(sentence[i])
        my_interests.append(sentence[i])

"""Problem 5.  Analyze your content"""
print("-----------------------------------------")
print("Problem 5")
for name in names:
    nr = 0
    for interest in people_interests[name]:
        if interest in my_interests:
            nr += 1
    m = nr * 0.2
    influence[name] *= m

sorted_influence = deepcopy(names)
for i in range(len(sorted_influence)):
    min_idx = i
    for j in range(i + 1, len(sorted_influence)):
        if influence[sorted_influence[min_idx]] > influence[sorted_influence[j]]:
            min_idx = j
    sorted_influence[min_idx], sorted_influence[i] = sorted_influence[i], sorted_influence[min_idx]

for i in range(len(sorted_influence)):
    print(f"""{sorted_influence[i]} - {influence[sorted_influence[i]]}""")

