# Architecture

## 1. Project Structure

Cipher Lab follows a modular project structure based on the `src` layout.

The application code is located inside `src/cipher_lab/`, separating the actual package from project configuration, documentation and tests.

The project is organized around the following directories:

- `src/cipher_lab/`: Main application package.
- `tests/`: Automated tests, divided into unit and integration tests.
- `docs/`: Project documentation and architectural decisions.

The internal structure of the application will evolve as new requirements emerge.

## 2. Separation of Concerns

The application aims to maintain a clear separation between its main responsibilities:

- **Domain logic:** Cipher algorithms and their underlying rules.
- **Application logic:** Coordination and management of cipher operations.
- **Presentation:** User interface and interaction handling.

Cipher implementations must remain independent of the presentation layer.

This separation will allow the application to support different interfaces without modifying the underlying cipher algorithms.

## 3. Test-Driven Development (TDD)

The project follows the Test-Driven Development methodology.

Development is based on the Red-Green-Refactor cycle:

1. **Red:** Write a test that describes the expected behaviour and verify that it fails.
2. **Green:** Implement the minimum code necessary to make the test pass.
3. **Refactor:** Improve the code structure while preserving the expected behaviour.

Automated tests are written using `pytest`.

Unit tests verify individual components, while integration tests verify interactions between different parts of the application.

## 4. Design Principles

The project aims to follow established software design principles:

### SOLID

- **Single Responsibility Principle (SRP):** Each component should have a clearly defined responsibility.
- **Open/Closed Principle (OCP):** The architecture should allow new cipher algorithms to be added without unnecessary modifications to existing components.
- **Liskov Substitution Principle (LSP):** Implementations sharing the same contract should be interchangeable without breaking expected behaviour.
- **Interface Segregation Principle (ISP):** Components should not depend on operations they do not need.
- **Dependency Inversion Principle (DIP):** High-level components should depend on abstractions rather than concrete implementations.

### Additional Principles

- **DRY (Don't Repeat Yourself):** Avoid unnecessary duplication of logic.
- **KISS (Keep It Simple, Stupid):** Prefer straightforward solutions over unnecessary complexity.
- **YAGNI (You Aren't Gonna Need It):** Avoid implementing functionality before it is actually needed.
- **Separation of Concerns:** Keep different responsibilities independent.

These principles should guide design decisions without introducing unnecessary abstractions or complexity.

## 5. Coding Conventions

The project follows established Python conventions:

- PEP 8 for code style.
- PEP 257 for docstrings.
- Descriptive names following Python naming conventions.
- Type hints where appropriate.
- Consistent formatting and import ordering.

Ruff is used for linting and code formatting, while mypy may be used for static type checking.

## 6. Extensibility

Cipher Lab is designed to support multiple classical cipher algorithms.

New algorithms should be incorporable without requiring unnecessary changes to the application's central logic.

Common behaviour and shared responsibilities will be identified as the project evolves, avoiding premature abstractions.

## 7. Architectural Evolution

This document describes the initial architectural decisions.

The architecture is expected to evolve as new requirements and implementation challenges emerge.

Changes should be guided by actual needs, maintainability and the principles described above.