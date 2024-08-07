import pytest
from unittest.mock import patch
from blackjack import PlayBlackJack, FinalHand, EndGame

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
        ([11, 10, 10], 31),
        ([10, 10, 10], 30),
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