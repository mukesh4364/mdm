from standardization.normalizers.address import AddressStandardizer
from standardization.normalizers.email import EmailStandardizer
from standardization.normalizers.name import NameStandardizer
from standardization.normalizers.phone import PhoneStandardizer


class StandardizationRegistry:

    def __init__(self, config: dict):

        self.normalizers = {
            "full_name": NameStandardizer(),
            "phone": PhoneStandardizer(),
            "email": EmailStandardizer(),
            "address": AddressStandardizer(config["address"]),
        }

    def get(self, field: str):
        return self.normalizers.get(field)
