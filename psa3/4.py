import json
import matplotlib.pyplot as plt

with open('tweets.json', encoding='utf-8') as data_file:
    tweets = json.loads(data_file.read())


def find_max(d, not_available, words):
    max = None
    for word in words:
        if word in not_available:
            continue
        if '.' in word or '*' in word or '@' in word or '%' in word or '’' in word:
            continue
        if word == 'https' or word == 'RT':
            continue
        if max is None:
            max = word
        elif d[max] < d[word]:
            max = word
    return max


"""Problem 1. Popular"""
print('---------------------')
print('Problem 1')
popular = {}
words = []
for tweet in tweets:
    text = tweet['text'].split()
    for i in range(len(text)):
        text[i] = text[i].replace('.', '')
        text[i] = text[i].replace(',', '')
        text[i] = text[i].replace('!', '')
        text[i] = text[i].replace('+', '')
        text[i] = text[i].replace('-', '')
        text[i] = text[i].replace('=', '')
        text[i] = text[i].replace('/', '')
        text[i] = text[i].replace('"', '')
        text[i] = text[i].replace('.', '')
        text[i] = text[i].replace('*', '')
        text[i] = text[i].replace('&', '')
        text[i] = text[i].replace('$', '')
        text[i] = text[i].replace('@', '')
        text[i] = text[i].replace('?', '')
        text[i] = text[i].replace(')', '')
    for word in text:
        if word in popular:
            popular[word] += 1
        else:
            words.append(word)
            popular[word] = 1

not_available = []
out = []
for i in range(5):
    out.append(find_max(popular, not_available, words))
    not_available.append(out[-1])

for i in range(5):
    print(f"""{out[i]} - {popular[out[i]]}""")

"""Problem 2. Nouns"""
print('---------------------')
print('Problem 2')

import nltk

# function to test if something is a noun
is_noun = lambda pos: pos[:2] == 'NN'
# do the nlp stuff
nouns_dict = {}
words2 = []
for tweet in tweets:
    line = tweet['text']
    tokenized = nltk.word_tokenize(line)
    for (word, pos) in nltk.pos_tag(tokenized):
        if is_noun(pos):
            if word in nouns_dict:
                nouns_dict[word] += 1
            else:
                nouns_dict[word] = 1
                words2.append(word)

not_available = []
out = []
for i in range(10):
    out.append(find_max(nouns_dict, not_available, words2))
    not_available.append(out[-1])

for i in range(10):
    print(f"""{out[i]} - {nouns_dict[out[i]]}""")

"""Problem 3. Proper Nouns"""
print('---------------------')
print('Problem 3')

import nltk

# function to test if something is a noun
is_noun = lambda pos: (pos[:] == 'NNP' or pos[:] == 'NNPS')
# do the nlp stuff
nouns_dict = {}
words3 = []
for tweet in tweets:
    line = tweet['text']
    tokenized = nltk.word_tokenize(line)
    for (word, pos) in nltk.pos_tag(tokenized):
        if is_noun(pos):
            if word in nouns_dict:
                nouns_dict[word] += 1
            else:
                nouns_dict[word] = 1
                words3.append(word)

not_available = []
out = []
for i in range(10):
    out.append(find_max(nouns_dict, not_available, words3))
    not_available.append(out[-1])

for i in range(10):
    print(f"""{out[i]} - {nouns_dict[out[i]]}""")

"""Problem 4. Frequency"""
print('---------------------')
print('Problem 4')
word = input("Give a word to check frequency: ")
frequency = {}
x_axis = []
y_axis = []
for tweet in tweets:
    text = tweet['text'].split()
    for i in range(len(text)):
        text[i] = text[i].replace('.', '')
        text[i] = text[i].replace(',', '')
        text[i] = text[i].replace('!', '')
        text[i] = text[i].replace('+', '')
        text[i] = text[i].replace('-', '')
        text[i] = text[i].replace('=', '')
        text[i] = text[i].replace('/', '')
        text[i] = text[i].replace('"', '')
        text[i] = text[i].replace('.', '')
        text[i] = text[i].replace('*', '')
        text[i] = text[i].replace('&', '')
        text[i] = text[i].replace('$', '')
        text[i] = text[i].replace('@', '')
        text[i] = text[i].replace('?', '')
        text[i] = text[i].replace(')', '')

    k = 0
    for w in text:
        if w == word:
            k += 1
    if k > 0:
        if tweet['created_at'].split()[0][:-3] in frequency:
            frequency[tweet['created_at'].split()[0][:-3]] += k
        else:
            frequency[tweet['created_at'].split()[0][:-3]] = k
            x_axis.append(tweet['created_at'].split()[0][:-3])

for date in x_axis:
    y_axis.append(frequency[date])
plt.style.use("fivethirtyeight")
plt.barh(x_axis, y_axis)
plt.tight_layout()
plt.show()

"""Problem 5.Popularity"""
print('---------------------')
print('Problem 5')
likes = {}
retweets = {}
for tweet in tweets:
    text = tweet['text'].split()
    for i in range(len(text)):
        text[i] = text[i].replace('.', '')
        text[i] = text[i].replace(',', '')
        text[i] = text[i].replace('!', '')
        text[i] = text[i].replace('+', '')
        text[i] = text[i].replace('-', '')
        text[i] = text[i].replace('=', '')
        text[i] = text[i].replace('/', '')
        text[i] = text[i].replace('"', '')
        text[i] = text[i].replace('.', '')
        text[i] = text[i].replace('*', '')
        text[i] = text[i].replace('&', '')
        text[i] = text[i].replace('$', '')
        text[i] = text[i].replace('@', '')
        text[i] = text[i].replace('?', '')
        text[i] = text[i].replace(')', '')
    for w in text:
        if w in likes:
            likes[w] += tweet['likes']
            retweets[w] += tweet['retweets']
        else:
            likes[w] = tweet['likes']
            retweets[w] = tweet['retweets']

score = {}
for word in words:
    score[word] = popular[word] * (1.4 + retweets[word]) * (1.2 + likes[word])

not_available = []
out = []
for i in range(10):
    out.append(find_max(score, not_available, words))
    not_available.append(out[-1])

for i in range(10):
    print(f"""{out[i]} - {score[out[i]]}""")

"""Problem 6.Suggestion"""
print('---------------------')
print('Problem 6')
word = input("Type an incomplete word: ")
possible_out = []
for w in words:
    if word in w and w[0:len(word)] == word:
        possible_out.append(w)

not_available = []
out = []
for i in range(3):
    out.append(find_max(popular, not_available, possible_out))
    not_available.append(out[-1])

for i in range(3):
    print(f"""{out[i]} - {popular[out[i]]}""")

"""Problem 7.Suggestion occurrences"""
print('---------------------')
print('Problem 7')
word = input("Type a word: ")
popular = {}
words = []
for tweet in tweets:
    text = tweet['text'].split()
    for i in range(len(text)):
        text[i] = text[i].replace('.', '')
        text[i] = text[i].replace(',', '')
        text[i] = text[i].replace('!', '')
        text[i] = text[i].replace('+', '')
        text[i] = text[i].replace('-', '')
        text[i] = text[i].replace('=', '')
        text[i] = text[i].replace('/', '')
        text[i] = text[i].replace('"', '')
        text[i] = text[i].replace('.', '')
        text[i] = text[i].replace('*', '')
        text[i] = text[i].replace('&', '')
        text[i] = text[i].replace('$', '')
        text[i] = text[i].replace('@', '')
        text[i] = text[i].replace('?', '')
        text[i] = text[i].replace(')', '')
    flag = False
    for w in text:
        if flag:
            if w in popular:
                popular[w] += 1
            else:
                popular[w] = 1
                words.append(w)
            flag = False
        if w == word:
            flag = True

not_available = []
out = []
for i in range(3):
    out.append(find_max(popular, not_available, words))
    not_available.append(out[-1])

for i in range(3):
    print(f"""{out[i]} - {popular[out[i]]}""")