class ReviewPrinter(object):

    def print_review_list(self, review_list, number_to_display):
        review_report = self.get_formatted_reviews(review_list, number_to_display)
        print(review_report)
        return

    def get_formatted_reviews(self, review_list, number_to_display):
        formatted_report = ""
        count = 1
        for review in review_list:
            if count > number_to_display:
                break
            else:
                formatted_report += self.get_review_report_text(review)
            count += 1

        return formatted_report

    def get_review_report_text(self, review):
        formatted_review = "Review positivity score: " + (str(review.positivity_score))
        formatted_review += "\nReview content: " + review.review_text + "\n\n"
        return formatted_review