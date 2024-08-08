from blackjack import PlayBlackJack, FinalHand, EndGame
from logo import logo
def main() -> None:

    player_turn = PlayBlackJack()
    games_turn = PlayBlackJack()
    play_game = PlayBlackJack()
    end_the_game = EndGame()
    final = FinalHand()
    is_playing = True

    while is_playing:
        player_cards =[]
        computer_cards = []
        start_or_stop = input("Do you want to play a game of blackjack ? Type 'y' for yes or 'n' for no. ")

        if start_or_stop.lower() == "y":
            print(f"{logo}")
            #Draw two cards for both the computer and player
            play_game.draw_start_cards(player_cards=player_cards, computer_cards=computer_cards)
            #Calculate sum of the cards for the player and computer
            sum_of_player_cards =player_turn.current_score(scores=player_cards)
            sum_of_computer_cards = player_turn.current_score(scores=computer_cards)

            print(play_game.display_game_status(player_cards=player_cards, games_cards=computer_cards))
            #While player score is not a blackjack and score is still below 21 ask if they want another card
            while sum_of_player_cards != 0 and sum_of_player_cards < 21:
                answer = input("Do you want another card? Type 'y' for yes and 'n' for no. ")
                if answer.lower() == 'y':
                    #If player wants another card update their cards list with new card
                    play_game.scores_lst(card =play_game.play_blackjack(), scores=player_cards)
                    #update the sum of player cards
                    sum_of_player_cards =player_turn.current_score(scores=player_cards)
                    #Display current game status
                    print(play_game.display_game_status(games_cards=computer_cards, player_cards=player_cards))
                else:
                    #If player wants no more cards display current game status
                    sum_of_player_cards =player_turn.current_score(scores=player_cards)
                    print(play_game.display_game_status(games_cards=computer_cards, player_cards=player_cards))
                    break
                #While the sum of computer cards is still below 17 and not a blackjack
            while sum_of_computer_cards < 17 and sum_of_computer_cards != 0:
                #Update the computer score list with new card and new sum
                        play_game.scores_lst(card=play_game.play_blackjack(), scores=computer_cards)
                        sum_of_computer_cards =  games_turn.current_score(scores=computer_cards)
            #Display the end of the game
            sum_of_computer_cards =  games_turn.current_score(scores=computer_cards)
            print(f"Game Over! \n{end_the_game.end_game(games_cards=computer_cards, player_cards=player_cards, player_score=sum_of_player_cards, games_score=sum_of_computer_cards)}")
        else:
            is_playing = False
if __name__ == "__main__":
    main()
