from copy import deepcopy

from mdm.canonical import CustomerRecord
from mdm.standardization.registry import StandardizationRegistry


class StandardizationEngine:

    def __init__(self, registry: StandardizationRegistry):
        self.registry = registry

    def standardize(self, customer: CustomerRecord) -> CustomerRecord:
        """
        Return a new standardized CustomerRecord.
        """

        customer = customer.model_copy(deep=True)
        #print(customer)

        for field_name, normalizer in self.registry.normalizers.items():
            #print(field_name)
            #print(normalizer)

            value = getattr(customer, field_name)
            #print(value)

            standardized = normalizer.standardize(value)

            setattr(customer, field_name, standardized)

        return customer
