import unittest
from unittest.mock import patch, mock_open

class TestQuizGame(unittest.TestCase):

    @patch('builtins.input', return_value='testuser')
    def test_get_username(self, mock_input):
        from quiz import get_username
        self.assertEqual(get_username(), 'testuser')

    @patch('builtins.open', new_callable=mock_open)
    def test_initialize_high_scores(self, mock_file):
        from quiz import initialize_high_scores
        initialize_high_scores('high-scores.txt')
        mock_file.assert_called_with('high-scores.txt', 'x')

    @patch('builtins.input', side_effect=['5', '2'])
    def test_ask_question_invalid_then_valid(self, mock_input):
        from quiz import ask_question
        question = "Who is the fastest man in the world?"
        choices = ["1. Tyson GAY,", "2. Usain St. Leo Bolt OJ", "3. Asafa POWELL, USA", "4. Trayvon BROMELL"]
        self.assertEqual(ask_question(question, choices), 2)

    def test_update_score_correct(self):
        from quiz import update_score
        self.assertEqual(update_score(2, 2), 5)

    def test_update_score_incorrect(self):
        from quiz import update_score
        self.assertEqual(update_score(1, 2), -2)

    @patch('builtins.open', new_callable=mock_open)
    def test_save_score(self, mock_file):
        from quiz import save_score
        save_score('high-scores.txt', 'testuser', 10)
        mock_file().write.assert_called_with('Username: testuser, Score: 10\n')

    @patch('builtins.open', new_callable=mock_open, read_data='Username: testuser, Score: 10\n')
    @patch('builtins.print')
    def test_display_high_scores(self, mock_print, mock_file):
        from quiz import display_high_scores
        display_high_scores('high-scores.txt')
        mock_print.assert_called_with(f"{Fore.GREEN}testuser {Fore.YELLOW}10")

if __name__ == "__main__":
    unittest.main()
