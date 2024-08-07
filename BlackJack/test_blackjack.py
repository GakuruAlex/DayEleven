import pytest
from unittest.mock import patch
from blackjack import PlayBlackJack, FinalHand, EndGame

class TestPlayBlackJack:
    test_blackjack = PlayBlackJack()
    def test_play_blackjack(self):
        test_cards = [10, 11, 2, 4, 5, 6]
        with patch("blackjack.choice", return_value = 10):
            assert self.test_blackjack.play_blackjack(test_cards) == 10

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