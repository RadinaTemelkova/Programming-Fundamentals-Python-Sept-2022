deck_of_cards = input().split()
faro_shuffles_count = int(input())

for shuffle in range(faro_shuffles_count):
    final_deck_of_cards = []
    middle_of_the_deck = len(deck_of_cards) // 2
    cards_in_left = deck_of_cards[0:middle_of_the_deck]
    cards_in_right = deck_of_cards[middle_of_the_deck::]
    for card_index in range(len(cards_in_left)):
        final_deck_of_cards.append(cards_in_left[card_index])
        final_deck_of_cards.append(cards_in_right[card_index])
    deck_of_cards = final_deck_of_cards
print(deck_of_cards)




