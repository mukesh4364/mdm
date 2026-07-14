                   main.py
                      │
                      ▼
         +-----------------------+
         | DataQualityEngine     |   ← engine.py
         +-----------------------+
                      │
          Reads validation rules
                      │
                      ▼
         +-----------------------+
         | RuleRegistry          |   ← registry.py
         +-----------------------+
          │         │         │
          ▼         ▼         ▼
    Required   EmailRule  PhoneRule
                      ▲
                      │
          implements ValidationRule
                      │
                      ▼
         +-----------------------+
         | interfaces.py         |
         +-----------------------+

CustomerRecord ─────────────► models.py

YAML Rules ────────────────► config.py
