from pathlib import Path

import yaml


class RuleConfig:

    @staticmethod
    def load(path):

        with Path(path).open() as file:

            return yaml.safe_load(file)
