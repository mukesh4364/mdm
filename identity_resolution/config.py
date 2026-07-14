from pathlib import Path

import yaml


class IdentityResolutionConfig:

    @staticmethod
    def load(path):

        with Path(path).open(
            "r",
            encoding="utf-8",
        ) as file:

            return yaml.safe_load(file)
