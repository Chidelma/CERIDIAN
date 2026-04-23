# CERIDIAN Dog Breed Processor

Python assessment project that fetches dog breed data from an external API, stores it in SQLite, and reports breed or sub-breed counts.

## Goal

The application demonstrates a small ingestion pipeline:

- `modules/breed.py` retrieves breed data from a remote API.
- `modules/db.py` persists the results in SQLite.
- `main.py` coordinates the import and summary output.

## Requirements

- Python 3.11+
- pip

## Setup

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Validation

```bash
python -m compileall .
```

## Notes

- The SQLite database filename is controlled inside the modules and defaults to `breeds.db`.
- Running the script makes outbound HTTP requests to the public dog breeds API.
