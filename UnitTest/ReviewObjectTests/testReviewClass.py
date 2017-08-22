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

        lowerReview = Review("", .49)
        self.assertTrue(compare_with.__lt__(lowerReview))

        greaterReview = Review("", .51)
        self.assertFalse(compare_with.__lt__(greaterReview))

        equalReview = Review("", .5)
        self.assertFalse(compare_with.__lt__(equalReview))

    def test_set_pos_score(self):
        base_review = Review("", 0)

        base_review.set_positivity_score(-100)
        self.assertTrue(base_review.positivity_score == -100)

        base_review.set_positivity_score(100)
        self.assertTrue(base_review.positivity_score == 100)
