a_team_players = 11
b_team_players = 11
a_sent_off_players = []
b_sent_off_players = []
game_terminated = False
red_cards = input()
red_cards_list = red_cards.split()

for index in range(len(red_cards_list)):
    current_card = red_cards_list[index]
    if current_card in a_sent_off_players or current_card in b_sent_off_players:
        continue

    if "A" in current_card:
        a_team_players -= 1
        a_sent_off_players.append(current_card)
    elif "B" in current_card:
        b_team_players -= 1
        b_sent_off_players.append(current_card)

    if a_team_players < 7 or b_team_players < 7:
        game_terminated = True
        break

print(f"Team A - {a_team_players}; Team B - {b_team_players}")
if game_terminated:
    print("Game was terminated")
