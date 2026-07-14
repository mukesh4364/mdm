class MatchScorer:
    """
    Calculates overall identity score.
    """

    def score(
        self,
        evidences,
    ):

        total = 0

        for evidence in evidences:

            total += evidence.score

        return total
