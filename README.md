# Cipher Lab

An interactive playground for experimenting with classical ciphers and text transformations.

## Description

Cipher Lab is a Python project designed to explore, implement and experiment with classical encryption algorithms.

The project aims to provide an interactive environment where users can encrypt and decrypt text using different ciphers, customize their parameters and observe how each algorithm transforms the input.

It is also a learning project focused on software design, clean code, testing and good development practices.

**Note:** This project is educational. The implemented ciphers are intended for experimentation and learning, not for protecting sensitive information.

## Goals

- Implement a variety of classical encryption algorithms.
- Provide a consistent interface for working with different ciphers.
- Allow users to configure algorithm-specific parameters.
- Explore software design principles and maintainable architecture.
- Apply Test-Driven Development (TDD) throughout the development process.
- Build an extensible foundation for experimenting with text transformations.

## Planned Features

- **Classical ciphers:** Caesar, Atbash, Vigenère, Rail Fence and other substitution and transposition ciphers.
- **Encryption and decryption:** Apply supported algorithms to user-provided text.
- **Configurable parameters:** Adjust keys, shifts, alphabets and other algorithm-specific settings.
- **Live preview:** Display the transformed text as the input or parameters change.
- **Cipher comparison:** Compare the output of different algorithms using the same input.
- **Transformation pipelines:** Combine multiple ciphers and transformations.
- **Educational explanations:** Explore how each algorithm works and how its parameters affect the result.

## Technologies

- **Python 3.12+**
- **pytest** — Automated testing.
- **Ruff** — Linting and code formatting.
- **mypy** — Optional static type checking.
- **Tkinter** — Planned graphical user interface.

## Development Status

<badge>Work in progress</badge>

Cipher Lab is currently in its early development stage.

The initial focus is on implementing and testing individual cipher algorithms before developing the application architecture and graphical interface.

Features and project structure may evolve as development progresses.

## Project Structure

```text
cipher-lab/
├── src/
│   └── cipher_lab/
│       └── ciphers/
├── tests/
│   ├── integration/
│   └── unit/
├── docs/
├── main.py
├── README.md
├── pyproject.toml
└── .gitignore
```

For more information about the design principles and planned architecture, see [docs/architecture.md](docs/architecture.md).