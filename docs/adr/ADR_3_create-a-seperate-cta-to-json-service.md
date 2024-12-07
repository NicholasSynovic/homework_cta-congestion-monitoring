# 3. Create a seperate CTA to JSON service

## Context

Rather than storing all of the code under one directory, split each individual
service into its own sub directory within the `src` folder.

## Decision

The CTA to JSON service should have its own directory called `cta`. It should
also contain all of the supporting files necessary to install the project within
a Docker container.

This includes:

- `requirements.txt`
- `pyproject.toml`
- `Makefile`
- Source code

## Consequences

Each of these services will have to be entirely decoupled from one another. In
doing so, code duplication will most likely rise.
