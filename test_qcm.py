import unittest
from question import Question

class TestQuestion(unittest.TestCase):
    def test_est_correct(self):
        q = Question("Exemple ?", ["a. Oui", "b. Non", "c. Peut-être"], "a")
        self.assertTrue(q.est_correct("a"))
        self.assertTrue(q.est_correct("A"))
        self.assertFalse(q.est_correct("b"))

if __name__ == "__main__":
    unittest.main()
