from ingestion.readers.csv_reader import CSVReader
from ingestion.readers.json_reader import JSONReader


class ReaderFactory:

    @staticmethod
    def create(source_type: str, path: str):

        if source_type == "csv":
            return CSVReader(path)

        if source_type == "json":
            return JSONReader(path)

        raise ValueError(source_type)
