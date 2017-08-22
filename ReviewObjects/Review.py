class Review(object):

    def __init__(self,review_text,pos_score):
        self.review_text = str(review_text)
        self.positivity_score = pos_score

    def set_positivity_score(self,score):
        self.positivity_score = score

    def __lt__(self, other):
        return self.positivity_score > other.positivity_score
