# Web Crawler in Python

An asynchronous web crawler that maps the internal linking structure of websites.

## Features

- Asynchronous crawling with configurable concurrency
- HTML parsing and link extraction
- Internal link tracking and reporting
- Generates network graph visualization of site structure
- Customizable crawl limits

## Requirements

- Python 3.13+
- Dependencies listed in `pyproject.toml`
- [uv](https://github.com/astral-sh/uv) project and package manager

## Installation

1. Clone the repository:
```sh
git clone https://github.com/fatkungfu/crawler-python.git
cd crawler-python
```

2. Set up a Python virtual environment:
```sh
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```sh
uv sync
```

## Usage

Run the crawler with the following command:

```sh
uv run main.py <base_url> <max_concurrency> <max_pages>
```

Arguments:
- `base_url`: The starting URL to crawl (e.g., https://example.com)
- `max_concurrency`: Maximum number of concurrent requests
- `max_pages`: Maximum number of pages to crawl

Example:
```sh
uv run main.py https://blog.boot.dev 5 100
```
## Output

The crawler produces:

1. A console report showing internal link counts
2. A [website_graph.png](website_graph.png) visualization file showing the site structure

## Testing

Run the test suite with:

```sh
uv run -m unittest
```

## Project Structure

- `main.py`: Entry point and CLI interface
- `crawl.py`: Core crawler implementation
- `report.py`: Report generation
- `test_crawl.py`: Crawler tests
- `test_report.py`: Report generator