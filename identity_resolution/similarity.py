from difflib import SequenceMatcher


class Similarity:

    @staticmethod
    def ratio(left: str, right: str) -> float:
        """
        Returns similarity percentage (0-100).
        """
        if not left or not right:
            return 0.0

        return SequenceMatcher(
            None,
            left.lower(),
            right.lower()
        ).ratio() * 100
