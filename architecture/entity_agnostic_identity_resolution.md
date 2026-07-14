# Entity-Agnostic Identity Resolution Framework

## Overview

The current implementation of the Identity Resolution Engine is tightly coupled to the `customer` entity.

Example:

```python
rules = self.config["customer"]["matching_rules"]
```

While this works for customer master data, it limits the framework to a single domain.

Enterprise Master Data Management (MDM) platforms manage multiple business entities such as:

- Customers
- Suppliers
- Products
- Employees
- Vendors
- Stores
- Assets

The identity resolution framework should therefore be designed to work with **any entity type** rather than being hardcoded to customers.

---

# Current Design

```
Customer Record A
        │
Customer Record B
        │
        ▼
IdentityResolutionEngine
        │
        ▼
customer.matching_rules
```

Current implementation:

```python
rules = self.config["customer"]["matching_rules"]
```

The engine assumes every record being processed is a customer.

---

# Problems with the Current Design

The current implementation has several limitations.

## 1. Single Entity Support

The framework cannot resolve identities for suppliers or products without modifying the engine.

Example:

```python
engine.resolve(customer1, customer2)
```

There is no way to execute:

```python
engine.resolve(product1, product2)
```

because the engine always loads:

```yaml
customer:
```

---

## 2. Code Changes for Every New Entity

Suppose the organization decides to onboard Supplier Master Data.

The developer would need to modify the engine.

```python
if entity == "customer":
    rules = ...

elif entity == "supplier":
    rules = ...
```

This violates the Open/Closed Principle.

The engine should remain unchanged when introducing new entities.

---

## 3. Difficult to Maintain

As additional master data domains are introduced, conditional logic increases.

```
Customer

Supplier

Product

Employee

Vendor

Store
```

Eventually the engine becomes difficult to understand and maintain.

---

# Proposed Design

Instead of hardcoding the entity type, the caller provides it.

```python
result = engine.resolve(
    entity_type="customer",
    left=customer1,
    right=customer2,
)
```

or

```python
result = engine.resolve(
    entity_type="supplier",
    left=supplier1,
    right=supplier2,
)
```

The engine simply loads the appropriate configuration.

```python
rules = self.config[entity_type]["matching_rules"]
```

No additional code changes are required.

---

# Updated Engine

Current implementation

```python
def resolve(self, left, right):
```

Recommended implementation

```python
def resolve(
    self,
    entity_type,
    left,
    right,
):
```

Inside the engine

```python
matching_rules = self.config[entity_type]["matching_rules"]
```

The remainder of the workflow stays exactly the same.

```
Entity

↓

Load Matching Rules

↓

Execute Matchers

↓

Collect Evidence

↓

Calculate Score

↓

Decision Engine

↓

IdentityMatchResult
```

---

# Configuration

Instead of supporting only customers

```yaml
customer:

  matching_rules:

    - type: phone

    - type: email
```

the configuration can support multiple entities.

```yaml
customer:

  matching_rules:

    - type: phone
      weight: 40

    - type: email
      weight: 40

    - type: fuzzy_name
      weight: 20

supplier:

  matching_rules:

    - type: gst_number
      weight: 50

    - type: company_name
      weight: 30

    - type: address
      weight: 20

product:

  matching_rules:

    - type: sku
      weight: 60

    - type: product_name
      weight: 25

    - type: manufacturer
      weight: 15
```

The engine remains unchanged.

---

# Runtime Flow

Resolving Customers

```
main.py

↓

entity_type = customer

↓

Load Customer Rules

↓

Phone Matcher

↓

Email Matcher

↓

Name Matcher

↓

IdentityMatchResult
```

Resolving Suppliers

```
main.py

↓

entity_type = supplier

↓

Load Supplier Rules

↓

GST Matcher

↓

Company Matcher

↓

Address Matcher

↓

IdentityMatchResult
```

The same engine executes different workflows depending on the configuration.

---

# Benefits

## Reusable Framework

A single engine supports multiple master data domains.

---

## Configuration Driven

Business users can modify matching strategies without changing Python code.

---

## Open for Extension

New entities can be introduced simply by adding configuration.

Example

```yaml
employee:
```

No engine modifications are required.

---

## Enterprise Ready

This architecture aligns with commercial MDM platforms where one identity resolution framework processes multiple domains using different matching rules.

---

# Example

Customer Resolution

```python
result = engine.resolve(
    entity_type="customer",
    left=customer_a,
    right=customer_b,
)
```

Supplier Resolution

```python
result = engine.resolve(
    entity_type="supplier",
    left=supplier_a,
    right=supplier_b,
)
```

Product Resolution

```python
result = engine.resolve(
    entity_type="product",
    left=product_a,
    right=product_b,
)
```

The caller changes only the entity type.

The engine, matching pipeline, scoring engine, and decision engine remain identical.

---

# Conclusion

By making the Identity Resolution Engine entity-agnostic, the framework becomes significantly more flexible, reusable, and scalable.

This design follows several key software engineering principles:

- Single Responsibility Principle (SRP)
- Open/Closed Principle (OCP)
- Configuration over Hardcoding
- Separation of Concerns
- Domain-Driven Design

It provides a strong architectural foundation for supporting multiple master data domains without increasing code complexity.
