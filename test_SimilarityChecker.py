from unittest import TestCase

from SimilarityChecker import SimilarityChecker


class Test(TestCase):
    def setUp(self) -> None:
        self.sc = SimilarityChecker()
        super().setUp()

    def test_similarity_checker(self):
        self.sc.run(["ABCDE", "ABCDE"])
        self.assertEqual(100, self.sc.getScore())

    def test_similarity_checker2(self):
        self.sc.run(["ABCDE", "FGHIJ"])
        self.assertEqual(100, self.sc.getScore())

    def test_similarity_checker3(self):
        self.sc.run(["ABCDE", "FGH"])
        self.assertEqual(60, self.sc.getScore())

    def test_similarity_checker4(self):
        self.sc.run(["ABCDE", "F"])
        self.assertEqual(0, self.sc.getScore())
