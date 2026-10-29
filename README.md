# AI Prompt Engineering Hub

A local-first reference collection and CLI for curated, production-grade AI prompts.
The repository ships a JSON database of hand-picked prompt templates for common
software engineering and creative tasks, together with a command-line tool that lets
you browse, filter by category or tag, rank by community likes, and export selections
as plain text, Markdown, or JSON. Everything runs offline — no API keys, no accounts,
and no prompt ever leaves your machine.

## Features

- **Offline-first design** — the prompt library is a plain JSON file (`prompts.json`)
  processed entirely on your machine; the tool makes no network calls and requires
  no API keys.
- **Category and tag filtering** — narrow the collection with `--category` and
  `--tag` (e.g. `--category debugging --tag security`) using case-insensitive matching.
- **Popularity ranking** — `--rank` sorts results by the number of likes each prompt
  has accumulated, in descending order.
- **Multi-format export** — write the current selection to a file with `--export`,
  choosing between `TEXT`, `MD`, and `JSON` output. Markdown exports are structured
  with headings, metadata, and fenced prompt bodies, ready for documentation.
- **Structured logging** — every load, filter, and export step is reported through
  timestamped log lines.

## The Collection

The bundled `prompts.json` database currently contains curated prompts across these
categories:

| Category     | Example prompt                                        |
| ------------ | ----------------------------------------------------- |
| `database`   | SQL query optimization expert                         |
| `frontend`   | React glassmorphism component generator               |
| `debugging`  | Python bug finder and explainer                       |
| `architecture` | System architecture diagram helper (Mermaid.js)     |
| `creative`   | Midjourney cinematic lighting formula                 |

Each entry carries a title, category, prompt body, like count, and a tag list, so the
dataset doubles as a research corpus for studying how effective prompts are structured.

## Installation

Clone the repository and install dependencies (there are none beyond the Python
standard library, so this is effectively a no-op that only verifies the environment):

```bash
git clone https://github.com/automate-it0/ai-prompt-engineering-hub.git
cd ai-prompt-engineering-hub
pip install -r requirements.txt
```

Requires Python 3.8+.

## Usage

### List every prompt in the database

```bash
python main.py
```

### Filter by category and tag

```bash
python main.py --category database --tag sql
```

### Rank by popularity

```bash
python main.py --rank
```

Combine filtering with ranking to get the most liked prompts in one area:

```bash
python main.py --category creative --rank
```

### Export a curated selection

Export to Markdown (structured headings, metadata, fenced prompt bodies):

```bash
python main.py --rank --export curated_prompts.md --format MD
```

Export to JSON for programmatic use:

```bash
python main.py --category debugging --export debugging.json --format JSON
```

### Point at your own database

The `--db` flag accepts any path to a JSON file with the same schema:

```bash
python main.py --db /path/to/your/prompts.json --rank
```

### Command-line options

| Option       | Default       | Description                                    |
| ------------ | ------------- | ---------------------------------------------- |
| `--db`       | `prompts.json`| Path to the local prompts JSON database.       |
| `--rank`     | off           | Rank prompts by popularity (likes).            |
| `--category` | —             | Filter prompts by category.                    |
| `--tag`      | —             | Filter prompts by tag.                         |
| `--export`   | —             | Filename to export the results to.             |
| `--format`   | `TEXT`        | Export format: `TEXT`, `MD`, or `JSON`.        |

## Data Format

Each prompt record in the database follows this schema:

```json
{
  "id": 1,
  "title": "SQL Query Optimization Expert",
  "category": "database",
  "prompt": "You are an expert database administrator. ...",
  "likes": 342,
  "tags": ["sql", "performance", "database"]
}
```

To extend the collection, append entries with the same keys to `prompts.json` or any
file passed via `--db`.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
