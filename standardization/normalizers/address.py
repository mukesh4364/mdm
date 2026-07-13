from mdm.standardization.interfaces import Standardizer


class AddressStandardizer(Standardizer):

    def __init__(self, replacements: dict[str, str]):
        self.replacements = replacements

    def standardize(self, value: str | None):

        if not value:
            return None

        value = value.strip()
        return self.replacements.get(value, value)
