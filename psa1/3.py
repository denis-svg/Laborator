with open("poker.txt", "r") as f:
    games = []
    for line in f:
        games.append(line.split())

card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                   "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


# function to return key for any value
def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"


def check_flush(hand):
    suits = [h[1] for h in hand]
    if len(set(suits)) == 1:
        return True
    else:
        return False


def check_straight(hand):
    values = [i[0] for i in hand]
    value_counts = {}
    for value in values:
        value_counts[value] = 0
    for value in values:
        value_counts[value] += 1
    rank_values = [card_order_dict[i] for i in values]
    range_value = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (range_value == 4):
        return True
    else:
        # check straight with low Ace
        if set(values) == {"A", "2", "3", "4", "5"}:
            return True
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


def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = {}
    for value in values:
        value_counts[value] = 0
    for value in values:
        value_counts[value] += 1
    if sorted(value_counts.values()) == [1, 4]:
        return True
    return False


def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = {}
    for value in values:
        value_counts[value] = 0
    for value in values:
        value_counts[value] += 1
    if sorted(value_counts.values()) == [2, 3]:
        return True
    return False


def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = {}
    for value in values:
        value_counts[value] = 0
    for value in values:
        value_counts[value] += 1
    if sorted(value_counts.values()) == [1, 1, 3]:
        return True
    return False


def check_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = {}
    for value in values:
        value_counts[value] = 0
    for value in values:
        value_counts[value] += 1
    if sorted(value_counts.values()) == [1, 2, 2]:
        return True
    return False


def check_one_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = {}
    for value in values:
        value_counts[value] = 0
    for value in values:
        value_counts[value] += 1
    if sorted(value_counts.values()) == [1, 1, 1, 2]:
        return True
    return False


def get_max_rank(hand):
    values = [i[0] for i in hand]
    rank_values = [card_order_dict[i] for i in values]
    return max(rank_values)


def get_max_rank_by_encounters(hand, num):
    values = [i[0] for i in hand]
    value_counts = {}
    for value in values:
        value_counts[value] = 0
    for value in values:
        value_counts[value] += 1
    return card_order_dict[get_key(num, value_counts)]


def get_max_rank_of_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = {}
    pair1 = 0
    pair2 = 0
    i = 0
    for value in values:
        value_counts[value] = 0
    for value in values:
        value_counts[value] += 1
    for key, value in value_counts.items():
        if value == 2 and i == 0:
            pair1 = card_order_dict[key]
            i += 1
        elif value == 2 and i == 1:
            pair2 = card_order_dict[key]
            i += 1

    return pair1, pair2


def delete_key(hand, key):
    new_hand = []
    for h in hand:
        if h[0] != key:
            new_hand.append(h)
    return new_hand


def is_player1_winner(hand1, hand2):
    # in this function we don't consider ties since in every game it states that it must be a clear winner
    # checks the straight flush there is no point in checking royal flush since the royal flush is the best combination
    # of a straight flush
    if check_straight_flush(hand1) and check_straight_flush(hand2):
        m1 = get_max_rank(hand1)
        m2 = get_max_rank(hand2)
        if m1 > m2:
            return True
        elif m2 > m1:
            return False
    elif check_straight_flush(hand1):
        return True
    elif check_straight_flush(hand2):
        return False
    # checking 4 cards of a kind
    # two players cannot have four of a kind simultaneous but I will check that anyways
    if check_four_of_a_kind(hand1) and check_four_of_a_kind(hand2):
        m1 = get_max_rank_by_encounters(hand1, 4)
        m2 = get_max_rank_by_encounters(hand2, 4)
        if m1 > m2:
            return True
        elif m2 > m1:
            return False
        elif m2 == m1:
            return get_max_rank_by_encounters(hand1, 1) > get_max_rank_by_encounters(hand1, 1)
    if check_four_of_a_kind(hand1):
        return True
    elif check_four_of_a_kind(hand2):
        return False
    # checking full house
    if check_full_house(hand1) and check_full_house(hand2):
        m1 = get_max_rank_by_encounters(hand1, 3)
        m2 = get_max_rank_by_encounters(hand2, 3)
        if m1 > m2:
            return True
        elif m1 < m2:
            return False
        elif m1 == m2:
            return get_max_rank_by_encounters(hand1, 2) > get_max_rank_by_encounters(hand2, 2)
    elif check_full_house(hand1):
        return True
    elif check_full_house(hand2):
        return False
    # checking the flush
    if check_flush(hand1) and check_flush(hand2):
        m1 = get_max_rank(hand1)
        m2 = get_max_rank(hand2)
        if m1 > m2:
            return True
        elif m1 < m2:
            return False
        elif m1 == m2:
            while m1 == m2:
                key = get_key(m1, card_order_dict)
                hand1 = delete_key(hand1, key)
                hand2 = delete_key(hand2, key)
                m1 = get_max_rank(hand1)
                m2 = get_max_rank(hand2)
            return m1 > m2
    elif check_flush(hand1):
        return True
    elif check_flush(hand2):
        return False
    # checking straights
    if check_straight(hand1) and check_straight(hand2):
        m1 = 0
        m2 = 0
        if "5" in hand1 and "A" in hand1:
            m1 = 5
        else:
            m1 = get_max_rank(hand1)
        if "5" in hand2 and "A" in hand2:
            m2 = 5
        else:
            m2 = get_max_rank(hand2)
        if m1 > m2:
            return True
        elif m2 > m1:
            return False
    elif check_straight(hand1):
        return True
    elif check_straight(hand2):
        return False
    # check three of a kind
    if check_three_of_a_kind(hand1) and check_three_of_a_kind(hand2):
        m1 = get_max_rank_by_encounters(hand1, 3)
        m2 = get_max_rank_by_encounters(hand2, 3)
        if m1 > m2:
            return True
        elif m1 < m2:
            return False
        elif m1 == m2:
            for _ in range(3):
                key = get_key(m1, card_order_dict)
                hand1 = delete_key(hand1, key)
                hand2 = delete_key(hand2, key)
            m1 = get_max_rank(hand1)
            m2 = get_max_rank(hand2)
            while m1 == m2:
                key = get_key(m1, card_order_dict)
                hand1 = delete_key(hand1, key)
                hand2 = delete_key(hand2, key)
                m1 = get_max_rank(hand1)
                m2 = get_max_rank(hand2)
            return m1 > m2
    elif check_three_of_a_kind(hand1):
        return True
    elif check_three_of_a_kind(hand2):
        return False
    # checking two pair
    if check_two_pairs(hand1) and check_two_pairs(hand2):
        m11, m12 = get_max_rank_of_two_pairs(hand1)
        m21, m22 = get_max_rank_of_two_pairs(hand2)
        if max([m11, m12]) > max([m21, m22]):
            return True
        elif max([m11, m12]) < max([m21, m22]):
            return False
        elif max([m11, m12]) == max([m21, m22]):
            if min([m11, m12]) > min([m21, m22]):
                return True
            elif min([m11, m12]) < min([m21, m22]):
                return False
    elif check_two_pairs(hand1):
        return True
    elif check_two_pairs(hand2):
        return False
    # checking one pair
    if check_one_pairs(hand1) and check_one_pairs(hand2):
        m1 = get_max_rank_by_encounters(hand1, 2)
        m2 = get_max_rank_by_encounters(hand2, 2)
        if m1 > m2:
            return True
        elif m1 < m2:
            return False
        elif m1 == m2:
            while m1 == m2:
                key = get_key(m1, card_order_dict)
                hand1 = delete_key(hand1, key)
                hand2 = delete_key(hand2, key)
                m1 = get_max_rank(hand1)
                m2 = get_max_rank(hand2)
            return m1 > m2
    elif check_one_pairs(hand1):
        return True
    elif check_one_pairs(hand2):
        return False
    # after we checked all we have to only check for the highest values
    m1 = get_max_rank(hand1)
    m2 = get_max_rank(hand2)
    if m1 > m2:
        return True
    elif m1 < m2:
        return False
    elif m1 == m2:
        while m1 == m2:
            key = get_key(m1, card_order_dict)
            hand1 = delete_key(hand1, key)
            hand2 = delete_key(hand2, key)
            m1 = get_max_rank(hand1)
            m2 = get_max_rank(hand2)
        return m1 > m2


player1 = 0
player2 = 0
for game in games:
    if is_player1_winner(game[:5], game[5:]):
        player1 += 1
    else:
        player2 += 1
print(f"""player 1 has won {player1} times \nplayer 2 has won {player2} times""")
