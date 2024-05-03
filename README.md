# file-sentry
Python based file integrity monitoring tool


## Features

- File Event Monitoring 
- File Diff Generator (todo)
- Virustotal integration (todo)
- Cross platform (todo)

## Installation

In order to download all dependencies and run the project without any issues, download and setup Poetry following the documentation here: https://python-poetry.org/docs/#installation

**Install Dependencies**
```bash
git clone git@github.com:brpat/file-sentry.git

poetry install
```

## Usage

*Interactive
```python
poetry shell 
python app/file_sentry.py
```

Non-Interactive (Service)
```python
poetry run python3 app/file_sentry.py
```