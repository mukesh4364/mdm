from mdm.standardization.normalizers.address import AddressStandardizer
from mdm.standardization.normalizers.email import EmailStandardizer
from mdm.standardization.normalizers.name import NameStandardizer
from mdm.standardization.normalizers.phone import PhoneStandardizer


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
