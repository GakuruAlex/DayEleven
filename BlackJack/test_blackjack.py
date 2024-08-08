import pytest
from unittest.mock import patch
from blackjack import PlayBlackJack, FinalHand, EndGame

#Test play_blackjack function
class TestPlayBlackJack:
    test_blackjack = PlayBlackJack()
    def test_play_blackjack(self):
        test_cards = [10, 11, 2, 4, 5, 6]
        with patch("blackjack.choice", return_value = 10):
            assert self.test_blackjack.play_blackjack(test_cards) == 10
        with patch("blackjack.choice", return_value = 11):
            assert self.test_blackjack.play_blackjack(test_cards) == 11

#Test whether current scores returns the correct summation given a list
class TestCurrentScore:
    test_scores_sum = PlayBlackJack()
    @pytest.mark.parametrize("test_scores, expected_score", [
        ([10,10], 20),
        ([10, 7, 5], 22),
        ([10], 10),
        ([11, 10, 10], 21),
        ([10, 10, 10], 30),
        ([10, 11], 0)
    ])
    def test_current_score(self, test_scores, expected_score):
        assert self.test_scores_sum.current_score(test_scores) == expected_score

#Test whether score list returns correct result given a list and a card
class TestScoresList:
    scores_list = PlayBlackJack()
    @pytest.mark.parametrize("test_list, a_card, expected_list", [
        ([], 10, [10]),
        ([10, 11], 10, [10, 11, 10]),
        ([], 11, [11]),
        ([2, 3], 10, [2, 3, 10])
    ])
    def test_scores_lst(self, test_list, a_card, expected_list):
        assert self.scores_list.scores_lst(test_list, a_card) == expected_list

#Test display current hand status
class TestDisplayGameStatus:
    games_status = PlayBlackJack()
    @pytest.mark.parametrize("player_cards, games_cards, display_text", [
        ([10, 11], [8, 4], "\t\tYour cards: [10, 11], current score: 0\n\t\tComputer's first card: 8" ),
         ([11, 2, 5], [3, 8], "\t\tYour cards: [11, 2, 5], current score: 18\n\t\tComputer's first card: 3"),
         ([3, 2, 9], [7, 6], "\t\tYour cards: [3, 2, 9], current score: 14\n\t\tComputer's first card: 7"),
         ([10, 10, 10], [10, 1], "\t\tYour cards: [10, 10, 10], current score: 30\n\t\tComputer's first card: 10"),])
    def test_display_game_status(self, player_cards, games_cards, display_text):
        assert self.games_status.display_game_status(player_cards, games_cards) == display_text

#Test End game scenarios
class TestEndGame:
    end_game = EndGame()
    @pytest.mark.parametrize("player_cards,player_score, computer_cards,computer_score, game_over_text",[
        ([10, 10], 20, [10, 10], 20, f"\t\tYour final hand: [10, 10], final score: 20\n\t\tComputer's final hand: [10, 10] final score: 20\n Draw"),
        ([10, 11], 0, [3, 5, 7, 2], 17, f"\t\tYour final hand: [10, 11], final score: 0\n\t\tComputer's final hand: [3, 5, 7, 2] final score: 17\n You Win!"),
        ([10, 5, 4], 19, [10, 7, 3], 20, f"\t\tYour final hand: [10, 5, 4], final score: 19\n\t\tComputer's final hand: [10, 7, 3] final score: 20\n You loose!"),
        ([7, 8, 5], 20, [7, 7, 2], 19, f"\t\tYour final hand: [7, 8, 5], final score: 20\n\t\tComputer's final hand: [7, 7, 2] final score: 16\n You Win!"),
        ([8, 9, 6], 23, [10, 5, 5], 20, f"\t\tYour final hand: [8, 9, 6], final score: 23\n\t\tComputer's final hand: [10, 5, 5] final score: 20\n You went over. You loose!"),
        ([5, 10, 4], 19, [10, 5, 10], 25, f"\t\tYour final hand: [5, 10, 4], final score: 19\n\t\tComputer's final hand: [10, 5, 10] final score: 25\n Your opponent went over. You Win!")
    ])
    def test_end_game(self, player_cards, player_score, computer_cards, computer_score, game_over_text):
        assert self.end_game.end_game(player_cards=player_cards, games_cards= computer_cards, games_score=computer_score, player_score=player_score) == game_over_text