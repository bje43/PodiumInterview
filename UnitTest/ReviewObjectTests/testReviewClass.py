from ReviewObjects.Review import Review
import unittest


class TestReviewMethods(unittest.TestCase):

    def test_initialize(self):
        r1_text = "test1"
        r1_score = 100
        r1 = Review(r1_text,r1_score)
        self.assertTrue(r1_text == r1.review_text)
        self.assertTrue(r1_score == r1.positivity_score)

    def test_comparator(self):
        compare_with = Review("", .5)

        lower_review = Review("", .49)
        self.assertTrue(compare_with.__lt__(lower_review))

        greater_review = Review("", .51)
        self.assertFalse(compare_with.__lt__(greater_review))

        equal_review = Review("", .5)
        self.assertFalse(compare_with.__lt__(equal_review))

    def test_set_pos_score(self):
        base_review = Review("", 0)

        base_review.set_positivity_score(-100)
        self.assertTrue(base_review.positivity_score == -100)

        base_review.set_positivity_score(100)
        self.assertTrue(base_review.positivity_score == 100)
