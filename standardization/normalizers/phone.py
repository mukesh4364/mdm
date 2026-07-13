import re
from mdm.standardization.interfaces import Standardizer


class PhoneStandardizer(Standardizer):

    COUNTRY_CODE = "91"

    def standardize(self, value: str | None) -> str | None:

        if value is None:
            return None

        value = value.strip()

        # Keep only digits
        value = re.sub(r"\D", "", value)

        # Remove India country code
        if value.startswith(self.COUNTRY_CODE) and len(value) == 12:
            value = value[2:]

        return value
