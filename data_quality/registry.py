from mdm.data_quality.rules.required import RequiredRule
from mdm.data_quality.rules.phone import PhoneRule
from mdm.data_quality.rules.email import EmailRule
from mdm.data_quality.rules.min_length import MinLengthRule
from mdm.data_quality.rules.date import DateRule


class RuleRegistry:

    def __init__(self):

        self.rules = {

            "required": RequiredRule(),

            "phone": PhoneRule(),

            "email": EmailRule(),

            "min_length": MinLengthRule(),

            "date": DateRule(),

        }

    def get(self, name):

        return self.rules[name]
