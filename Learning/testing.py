import unittest
import test


class TestCap(unittest.TestCase):

    def one_word(self):
        text = 'python'
        result = test.cap_text(text)
        self.assertEqual(result, ' Python')

    def multipl_words(self):
        text = 'monty python'
        result = test.cap_text(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
    unittest.main()

