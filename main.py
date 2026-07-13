from pathlib import Path
import yaml
from ingestion.factory import ReaderFactory
from standardization.registry import StandardizationRegistry
from standardization.engine import StandardizationEngine
from common.config import ConfigLoader
from data_quality.engine import DataQualityEngine
from data_quality.registry import RuleRegistry

def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    config = load_config(Path("config/app.yaml"))

    print("=" * 60)
    print(config["application"]["name"])
    print(f"Version : {config['application']['version']}")
    print("=" * 60)
    reader = ReaderFactory.create(source_type="csv",path="sample_data/crm.csv",)
    customers = reader.read()
    config = ConfigLoader.load("config/standardization_rules.yaml")
    registry = StandardizationRegistry(config)
    engine = StandardizationEngine(registry)
    dq_config = ConfigLoader.load("config/data_quality_rules.yaml")
    dq_engine = DataQualityEngine(dq_config, RuleRegistry())
    valid_customers = []
    invalid_customers = []
    for customer in customers:
        print("=" * 30+"Original Data"+"=" * 30)
        print(customer)
        result = engine.standardize(customer)
        print("=" * 30+"Standardized Data"+"=" * 30)
        print(result)
        result = dq_engine.validate(result)
        print("=" * 30+"Validated Data"+"=" * 30)
        if result.passed:
            valid_customers.append(customer)
            print("Validation PASSED")
        else:
            invalid_customers.append((customer,result))
            print("Validation FAILED")
            for error in result.errors:
                print(error)
    print("=" * 60)
    print(valid_customers)
    print(invalid_customers)
    print("=" * 60)


if __name__ == "__main__":
    main()
