from blackjack import PlayBlackJack, FinalHand, EndGame
from logo import logo
def main() -> None:

    player_turn = PlayBlackJack()
    games_turn = PlayBlackJack()
    play_game = PlayBlackJack()
    end_the_game = EndGame()
    final = FinalHand()
    is_playing = True
    user_wants_another = True

    while is_playing:
        player_cards = []
        games_cards = []
        answer = input("Do you want to play a game of Blackjack ? Type 'y' or 'n' : ")
        if answer == "y":
            print(f"{logo}\n")
# draw two cards for the player and  for the Computer
            for _ in range(2):
                player_turn.scores_lst(player_cards, player_turn.play_blackjack())
                games_turn.scores_lst(games_cards, games_turn.play_blackjack())

# Display the player cards and their total and Computer card
            print(play_game.display_game_status(player_cards, games_cards))
            while user_wants_another:
                another_card=input(f"Type 'y' to get another card,  type 'n' to pass. ")

                if another_card.lower() == 'y':

# Draw another card for the player
                    player_turn.scores_lst(player_cards, player_turn.play_blackjack())

# Display the player cards and their total and Computer card
                    print(play_game.display_game_status(player_cards, games_cards))

# Player doesn't want another card
                elif another_card.lower() == "n":
                    user_wants_another = False

# get the games score
            games_score = games_turn.current_score(games_cards)
            player_score = player_turn.current_score(player_cards)
            while games_score < 17 and games_score != 0 and player_score != 0:

# draw more cards for the computer if computer score is less than 17
                games_turn.scores_lst(games_cards, games_turn.play_blackjack())
                games_score = games_turn.current_score(games_cards)

#get player scores and games score
            games_score = games_turn.current_score(games_cards)

            print(end_the_game.end_game(games_cards,player_cards,player_score, games_score))

        elif answer == 'n':
            is_playing = False
        else:
            print("Invalid!")
            break

if __name__ == "__main__":
    main()
