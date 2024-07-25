## Formal Verification of Vyper's safemath
- take the basic arithmetic operators:

| Description                | Operation  |
|----------------------------|------------|
| Addition                   | x + y      |
| Subtraction                | x - y      |
| Multiplication             | x * y      |
| Integer division           | x // y     |
| Exponentiation             | x**y       |
| Modulo                     | x % y      |


- create an external entrypoint for each operator
- create invariants for all operators
- prove the correctness of the spec using Certora Prover

## Usafge
- `export CERTORAKEY=your_key`
- to run the tests: `certoraRun config.conf`