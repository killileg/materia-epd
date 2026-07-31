# Generic EPD Aggregator

[![Build](https://github.com/pbaustert/materia-epd/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/pbaustert/materia-epd/actions/workflows/ci.yml)
![Coverage](https://raw.githubusercontent.com/pbaustert/materia-epd/main/coverage.svg)
[![PyPI](https://img.shields.io/pypi/v/materia-epd.svg)](https://pypi.org/project/materia-epd/)
[![Python](https://img.shields.io/pypi/pyversions/materia-epd.svg)](https://pypi.org/project/materia-epd/)
[![Documentation](https://readthedocs.org/projects/materia-epd/badge/?version=latest)](https://materia-epd.readthedocs.io/en/latest/)
[![License](https://img.shields.io/github/license/pbaustert/materia-epd)](https://github.com/pbaustert/materia-epd/blob/main/LICENSE.txt)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://pre-commit.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Flake8](https://img.shields.io/badge/linting-flake8-blue)](https://flake8.pycqa.org/en/latest/)

---

# Features

- Parse ILCD process and flow XMLs
- Normalize material properties and LCIA modules
- Aggregate impacts and compute weighted averages
- Write new ILCD XML datasets

---

## Installation

Install via PyPI:

```console
pip install materia-epd
```

Requires Python 3.10+.

---

## Documentation

Full documentation is hosted on [Read the Docs](https://materia-epd.readthedocs.io/en/latest/).

It covers the EPD pipeline, module reference, contributing guidelines, and the changelog.

---

## Usage

### Run the aggregator

```console
python -m materia_epd <generic_processes_dir> <epd_processes_dir> -o <output_dir> -v
```

Note that you need to point to the root `processes` folders and need to provide a `matches` folder in the generic data folder to link generic products and EPDs.
Add the flag `--v` or `-v` for verbosity. Logs files with details will be automatically created in `<output_dir>`.
The `<generic_processes_dir>` folder should be structured like this:


```
<generic_process_dir>
├── flows
│   ├── <flow-uuid-1>.xml   # Reference flow of generic-uuid-1
│   ├── <flow-uuid-2>.xml
│   └── ...
├── matches
│   ├── <generic-uuid-1>.json   # Source EPDs for generic-uuid-1
│   ├── <generic-uuid-2>.json
│   └── ...
├── PDFs
├── processes
│   ├── <generic-uuid-1>.xml   # Skeleton process for generic-uuid-1
│   ├── <generic-uuid-2>.xml
│   └── ...
└── templates
    ├── GenPro_template.xml # Template with the EPD schema
    └── GenRef_template.xml # Template with the flow schema

```

#### Source EPDs (`<epd_processes_dir>`)

```
<epd_process_dir>
├── flows       # Reference flows for all source EPDs
└── processes   # All potential source EPD process XMLs
```

### Matches JSON

Files in `matches/` are named after the corresponding generic product UUID:

```json
{
  "type": "<aggregation_type>",
  "uuids": [
    "<uuid-1>",
    "<uuid-2>",
    "<uuid-3>",
    "... more UUIDs ..."
  ]
}
```

`type` is `"average"`, `"market-average"`, or `"assembled"`. The `uuids` list links to process files in the source EPD `processes/` folder.

---

## Development / running tests

See [DEVELOP.md](DEVELOP.md) for local setup, versioning, and PyPI release instructions.

For local development, install the package in editable mode with developer dependencies:

```console
python -m pip install -e ".[dev]"
```

Then run tests:

```console
pytest
```
