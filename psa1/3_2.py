# this algorithm will use bits to solve this problem
# I will transform every hand into bits by their occurrences at first
# EXAMPLE
# [9, 9, 9, 9, K] translates to binary
# 0000 0001 0000 0000 0000 1111 0000 0000 0000 0000 0000 0000 0000
# A    K    Q    J    T    9    8    7    6    5    4    3    2
# now next I will translate this bit number into decimal
# decimal % 15 = 1 -> four of a kind
# decimal % 15 = 10 -> full house
# decimal % 15 = 9 -> three of a kind
# decimal % 15 = 7 -> two pairs
# decimal % 15 = 6 -> one pair
# decimal % 15 = 5 -> high card
# to check for straights I will form this bit number by just one appearance but for ace low manually check
# [5, 6, 7, 8, 9] translates to binary 000001111100000
# Then I use bitwise AND with the negative of itself to get the least significant bit:000001111100000 & -000001111100000
# Then I divide this bit by the least significant bit and I will get a bit that will have the length
# according to the number of consecutive appearances
# for flush we can just check if all suits are the same not need for bits
# in the end let's say both hands have the same combination then we will sort this cards by number of apparitions and
# then by the face value
# after that we transform this number into a bit by shifting first number by 16, second 12, third 8, forth 4 and last 0

with open("poker.txt", "r") as f:
    games = []
    for line in f:
        games.append(line.split())

card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                   "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


def transform_to_binary(hand):
    values = [i[0] for i in hand]
    value_counts = {}
    for value in values:
        value_counts[value] = 0

    binary = ['0' for _ in range(15 * 4)]
    for value in values:
        index = card_order_dict[value] * 4 + value_counts[value]
        binary[index] = '1'
        value_counts[value] += 1

    str_binary = ''
    for i in range(15 * 4 - 1, -1, -1):
        str_binary += binary[i]
    return str_binary


def transform_to_decimal(binary):
    return int(binary, 2)


def to_int(str_binary):
    i = len(str_binary) - 1
    new_str_binary = ''
    while str_binary[i] == '0' or i < 0:
        i -= 1
    for j in range(i + 1):
        new_str_binary += str_binary[j]
    return int(str_binary)


def check_straight(hand):
    values = [i[0] for i in hand]
    binary = ['0' for _ in range(15)]
    for value in values:
        binary[card_order_dict[value]] = '1'
    str_binary = ''
    for i in range(15 - 1, -1, -1):
        str_binary += binary[i]
    int_binary = to_int(str_binary)
    least_bit = to_int(bin(int_binary & (-int_binary))[2:])
    normalized_number = int_binary // least_bit
    if normalized_number == 11111:
        return True
    if set(values) == {"A", "2", "3", "4", "5"}:
        return True
    return False


def check_flush(hand):
    suits = [h[1] for h in hand]
    if len(set(suits)) == 1:
        return True
    else:
        return False


def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False


def check_royal_flush(hand):
    values = [i[0] for i in hand]
    rank_values = [card_order_dict[i] for i in values]
    if check_straight_flush(hand) and max(rank_values) == 14 and min(rank_values) == 10:
        return True
    return False


def get_score(hand):
    values = [i[0] for i in hand]
    value_counts = {}
    for value in values:
        value_counts[value] = 0
    for value in values:
        value_counts[value] += 1
    for i in range(len(values)):
        for j in range(0, len(values) - i - 1):
            if value_counts[values[j]] < value_counts[values[j + 1]]:
                values[j], values[j + 1] = values[j + 1], values[j]
            elif value_counts[values[j]] == value_counts[values[j + 1]]:
                if card_order_dict[values[j]] < card_order_dict[values[j + 1]]:
                    values[j], values[j + 1] = values[j + 1], values[j]
    str_binary = ''
    for value in values:
        value_binary = bin(card_order_dict[value])[2:]
        while len(value_binary) < 4:
            value_binary += '0'
        str_binary += value_binary
    return transform_to_decimal(str_binary)


def is_player1_winner(hand1, hand2):
    number1 = transform_to_decimal(transform_to_binary(hand1))
    number2 = transform_to_decimal(transform_to_binary(hand2))
    if check_royal_flush(hand1):
        return True
    if check_royal_flush(hand2):
        return True
    if check_straight_flush(hand1) and check_straight_flush(hand2):
        if get_score(hand1) > get_score(hand2):
            return True
        return False
    elif check_straight_flush(hand1):
        return True
    elif check_straight_flush(hand2):
        return False
    if number1 % 15 == 1 and number2 % 15 == 1:
        if get_score(hand1) > get_score(hand2):
            return True
        return False
    elif number1 % 15 == 1:
        return True
    elif number2 % 15 == 1:
        return False
    if number1 % 15 == 10 and number2 % 15 == 10:
        if get_score(hand1) > get_score(hand2):
            return True
        return False
    elif number1 % 15 == 10:
        return True
    elif number2 % 15 == 10:
        return False
    if check_flush(hand1) and check_flush(hand2):
        if get_score(hand1) > get_score(hand2):
            return True
        return False
    elif check_flush(hand1):
        return True
    elif check_flush(hand2):
        return False
    if check_straight(hand1) and check_straight(hand2):
        if get_score(hand1) > get_score(hand2):
            return True
        return False
    elif check_straight(hand1):
        return True
    elif check_straight(hand2):
        return False
    if number1 % 15 == 9 and number2 % 15 == 9:
        if get_score(hand1) > get_score(hand2):
            return True
        return False
    elif number1 % 15 == 9:
        return True
    elif number2 % 15 == 9:
        return False
    if number1 % 15 == 7 and number2 % 15 == 7:
        if get_score(hand1) > get_score(hand2):
            return True
        return False
    elif number1 % 15 == 7:
        return True
    elif number2 % 15 == 7:
        return False
    if number1 % 15 == 6 and number2 % 15 == 6:
        if get_score(hand1) > get_score(hand2):
            return True
        return False
    elif number1 % 15 == 6:
        return True
    elif number2 % 15 == 6:
        return False
    if number1 % 15 == 5 and number1 % 15 == 5:
        if get_score(hand1) > get_score(hand2):
            return True
        return False


player1 = 0
player2 = 0
for game in games:
    if is_player1_winner(game[:5], game[5:]):
        player1 += 1
    else:
        player2 += 1
print(f"""player 1 has won {player1} times \nplayer 2 has won {player2} times""")

