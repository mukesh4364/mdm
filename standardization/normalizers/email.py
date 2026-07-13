from mdm.standardization.interfaces import Standardizer


class EmailStandardizer(Standardizer):

    def standardize(self, value: str | None) -> str | None:

        if not value:
            return None

        return value.strip().lower()
