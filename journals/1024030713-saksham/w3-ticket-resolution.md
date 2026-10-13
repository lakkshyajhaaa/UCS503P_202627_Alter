# Week 3: Resolving Hatchling Build Target & uv Sync Failures

## Ticket Summary
**ID:** `BUILD-003`  
**Assignee:** Saksham Raj (Full-Stack & Cloud Infrastructure Engineer)  
**Date:** August 29, 2026  
**Status:** Closed / Resolved  

---

## Problem / Error Description
During automated container builds and package synchronization using `uv sync` on the staging environment, the build aborted with backend packaging errors:

```
error: Failed to prepare build backend
Caused by: hatchling build error: Unable to determine which files to ship inside the wheel. 
No packages or modules found matching package name 'alter_twin'.
[ERROR] Command "uv sync" exited with status 1
```

---

## Relevant Context
The project uses `pyproject.toml` conforming to PEP 517/621 with `hatchling` as the build system. The project directory structure places backend Python code in `code/src/` rather than a root-level package folder matching the project name.

---

## Key Observation & Root Cause Analysis
By default, `hatchling` expects a root directory with the exact name declared under `[project] name`. Because our backend source files are organized under `code/src/`, `hatchling`'s heuristic auto-discovery failed to locate any Python modules, causing `uv sync` and `pip install -e .` to fail.

---

## Solution
Explicitly declared the build targets in `pyproject.toml` to guide `hatchling` directly to the `code/src` directory:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "alter-twin"
version = "0.1.0"
description = "Personal Digital Twin Backend Engine"
requires-python = ">=3.10"
dependencies = [
    "fastapi>=0.110.0",
    "uvicorn>=0.28.0",
    "sqlalchemy>=2.0.0",
    "pydantic>=2.0.0",
    "numpy>=1.26.0",
    "scipy>=1.12.0",
    "pandas>=2.2.0"
]

[tool.hatch.build.targets.wheel]
packages = ["code/src"]
```

Verified local build via `python -m build --wheel`, which generated a clean wheel containing the `src` package.

---

## Because
Configuring `[tool.hatch.build.targets.wheel]` explicitly instructs the build toolchain where to find packages, enabling custom monorepo directory structures without triggering packaging discovery errors.
