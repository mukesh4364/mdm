import re
from mdm.standardization.interfaces import Standardizer


class NameStandardizer(Standardizer):

    def standardize(self, value: str | None) -> str | None:

        if not value:
            return None

        value = value.strip()
        value = re.sub(r"\s+", " ", value)
        return value.title()
