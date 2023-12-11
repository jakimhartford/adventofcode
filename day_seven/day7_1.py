def convert_file_to_tuples(file_path):
    tuples_list = []
    with open(file_path, 'r') as file:
        for line in file:
            # Splitting each line into hand and bid
            parts = line.strip().split(' ')
            if len(parts) == 2:
                hand, bid = parts[0], int(parts[1])
                tuples_list.append((hand, bid))
    return tuples_list

# Usage
file_path = 'hands.txt'  # Replace with your file path
hands = convert_file_to_tuples(file_path)
# print(tuples)


def get_hand_type(hand):
    card_counts = {}
    for card in hand:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1

    # Sort the card counts in descending order
    sorted_counts = sorted(card_counts.values(), reverse=True)

    if sorted_counts == [5]:
        return "Five of a kind"
    elif sorted_counts == [4, 1]:
        return "Four of a kind"
    elif sorted_counts == [3, 2]:
        return "Full house"
    elif sorted_counts == [3, 1, 1]:
        return "Three of a kind"
    elif sorted_counts == [2, 2, 1]:
        return "Two pair"
    elif sorted_counts == [2, 1, 1, 1]:
        return "One pair"
    else:
        return "High card"

def get_adjusted_hand_rank(hand, hands):
    # Sort the hands based on their poker value, highest first
    sorted_hands = sorted(hands, key=lambda x: compare_hands_with_values(x, "22222"), reverse=True)

    # Find the rank of the given hand
    return sorted_hands.index(hand) + 1
 
def compare_hands_final(hand1, hand2):
    hand_order = {
        "Five of a kind": 7,
        "Four of a kind": 6,
        "Full house": 5,
        "Three of a kind": 4,
        "Two pair": 3,
        "One pair": 2,
        "High card": 1
    }

    type1 = get_hand_type(hand1)
    type2 = get_hand_type(hand2)

    # Compare hand types first
    if hand_order[type1] != hand_order[type2]:
        return hand_order[type1] - hand_order[type2]

    # Hands have the same type, so compare based on the highest card values
    card_values = "23456789TJQKA"
    sorted_hand1 = sorted(hand1, key=lambda card: card_values.index(card), reverse=True)
    sorted_hand2 = sorted(hand2, key=lambda card: card_values.index(card), reverse=True)

    for card1, card2 in zip(sorted_hand1, sorted_hand2):
        if card_values.index(card1) != card_values.index(card2):
            return card_values.index(card1) - card_values.index(card2)

    return 0
example_hands = hands
# Sort the hands based on their poker value and hand type, highest first
example_hands.sort(key=lambda x: compare_hands_final(x[0], "22222"), reverse=True)

# Calculate the score with adjusted ranking
adjusted_total_score_final = 0
sorted_example_hands = []
for hand, bid in example_hands:
    rank = get_adjusted_hand_rank_corrected(hand, [h for h, b in example_hands])
    score = rank * bid
    adjusted_total_score_final += score
    sorted_example_hands.append((hand, rank, bid, score))

# Sort the example hands by adjusted rank for better visualization
sorted_example_hands.sort(key=lambda x: x[1])

# Display sorted hands with scores
for hand_info in sorted_example_hands:
    print(f"Hand: {hand_info[0]}, Adjusted Rank: {hand_info[1]}, Bid: {hand_info[2]}, Score: {hand_info[3]}")


# Total adjusted score
print(adjusted_total_score_final)