import unittest
from question import Question

class TestQuestion(unittest.TestCase):
    def test_is_correct(self):
        q = Question("Exemple ?", ["a. Oui", "b. Non", "c. Peut-être"], "a")
        self.assertTrue(q.is_correct("a"))
        self.assertTrue(q.is_correct("A"))
        self.assertFalse(q.is_correct("b"))

if __name__ == "__main__":
    unittest.main()
