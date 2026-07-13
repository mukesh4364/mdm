import json
from pathlib import Path

from mdm.canonical import CustomerRecord
from mdm.ingestion.interfaces import SourceConnector
from mdm.ingestion.mappers.customer_mapper import CustomerMapper


class JSONReader(SourceConnector):

    def __init__(self, path: str):
        self.path = Path(path)

    def read(self) -> list[CustomerRecord]:

        with self.path.open() as file:
            records = json.load(file)

        return [
            CustomerMapper.from_claims(record)
            for record in records
        ]
