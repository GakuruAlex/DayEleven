from random import choice
class PlayBlackJack:
    def play_blackjack(self, cards: list=[ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]) ->int:
        """_populate cards and choose a card_

        Returns:
            int: _chosen card_
        """
        return choice(cards)

    def current_score(self, scores: list) -> int:
        """_Calculate the sum of scores_

        Args:
            scores (list): _list of scores_

        Returns:
            int: _Sum of the scores_
        """
        return sum(scores)

    def scores_lst(self, scores: list, card: int) -> list:
        """_Populate scores list_

        Args:
            scores (list): _List to append scores_
            card (int): _Card to be added_

        Returns:
            list: _description_
        """
        scores.append(card)
        return scores
    def display_game_status(self, player_cards: list,  games_cards: list) -> str:
        """_Return Display of current hand_

        Args:
            player_cards (list): _List of player cards_
            games_cards (list): _List of Computer cards_

        Returns:
            str: _string of the Current hand_
        """
        player_total = self.current_score(player_cards)
        return f"\t\tYour cards: {player_cards}, current score: {player_total}\n\t\tComputer's first card: {games_cards[0]}"

class FinalHand(PlayBlackJack):
    def display_game_status(self, player_cards: list, games_cards: list) -> str:
        """_End game message_

        Args:
            player_cards (list): _Player cards list_
            games_cards (list): _Computer cards list_

        Returns:
            str: _String for game's' hand_
        """
        player_total = self.current_score(player_cards)
        games_total = self.current_score(games_cards)
        return f"\t\tYour final hand: {player_cards}, final score: {player_total}\n\t\tComputer's final hand: {games_cards} final score: {games_total}"

class EndGame(FinalHand):
    def end_game(self, games_cards: list, player_cards: list, player_score: int, games_score: int) -> str:
        """_Message to display on game over_

        Args:
            player_score (int): _Final player score_
            games_score (int): _Final Computer score_

        Returns:
            str: _A string message of the games end_
        """
        if player_score == 21 or player_score < 21 and player_score > games_score:
            return f"{self.display_game_status(player_cards, games_cards)}\n You Win!"
        elif games_score > 21 and player_score < 21:
            return f"{self.display_game_status(player_cards, games_cards)}\n Your opponent went over. You Win!"
        else:
            return f"{self.display_game_status(player_cards, games_cards)}\n You Loose!"

