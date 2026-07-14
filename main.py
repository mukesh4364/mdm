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
    print(dq_config)
    dq_engine = DataQualityEngine(dq_config, RuleRegistry())
    valid_customers = []
    invalid_customers = []
    tmp_list = []
    for customer in customers:
        print("=" * 30+"Original Data"+"=" * 30)
        print(customer)
        result1 = engine.standardize(customer)
        print("=" * 30+"Standardized Data"+"=" * 30)
        tmp_list.append(result1)
        result = dq_engine.validate(result1)
        print(result)
        print("=" * 30+"Validated Data"+"=" * 30)
        print(result)
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
    print("=" * 30+"Matching Data"+"=" * 30)
    from identity_resolution.config import (
                IdentityResolutionConfig,
                )

    from identity_resolution.engine import (
                IdentityResolutionEngine,
                )
    from identity_resolution.registry import MatchingRegistry

    config = IdentityResolutionConfig.load(
                "config/identity_resolution_rules.yaml"
                )

    engine = IdentityResolutionEngine(config)
    customer1 = tmp_list[0]
    customer2 = tmp_list[-2]
    customer3 = tmp_list[-1]
    result = engine.resolve(entity_type="customer",left=customer1,right=customer2,)
    print(result)
    result = engine.resolve(entity_type="customer",left=customer1,right=customer3,)
    print(result)
    print("=" * 60)


if __name__ == "__main__":
    main()
