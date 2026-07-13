from pathlib import Path

import pandas as pd

from mdm.canonical import CustomerRecord
from mdm.ingestion.interfaces import SourceConnector
from mdm.ingestion.mappers.customer_mapper import CustomerMapper


class CSVReader(SourceConnector):
    """Reads customer data from a CSV file."""

    def __init__(self, path: str):
        self.path = Path(path)

    def read(self) -> list[CustomerRecord]:
        #dataframe = pd.read_csv(self.path,dtype={"phone": str})
        dataframe = pd.read_csv(self.path,dtype=str,keep_default_na=False)

        customers: list[CustomerRecord] = []

        for row in dataframe.to_dict(orient="records"):
            #print(row)
            customers.append(CustomerMapper.from_crm(row))
        #print(customers)

        return customers
