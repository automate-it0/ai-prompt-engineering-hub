# 🧠 AI Prompt Engineering Hub

A command-line tool and database helper to organize, rank, filter, and export high-quality, professional AI prompts completely offline and securely.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📋 Features

* **🔒 Offline First**: Operates entirely locally using a JSON database file (`prompts.json`), ensuring your private templates are never sent over the web.
* **🏷️ Smart Categorization**: Tag and categorize prompts for easy searching and organizing.
* **📈 Popularity Ranking**: Sort and rank prompt templates by positive votes/likes.
* **💾 Multi-Format Exports**: Export your curated lists into Plain Text, Markdown (perfect for documentation), or JSON formats.

---

## 📁 Repository Layout

```text
ai-prompt-engineering-hub/
├── main.py             # Command-line utility to query and export prompts
├── prompts.json        # Curated local database containing prompt templates
├── requirements.txt    # Python dependencies list
└── README.md           # Documentation
```

---

## 🚀 Setup & Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

Run the hub CLI from your terminal:

### 1. View All Prompts
```bash
python main.py
```

### 2. Filter Prompts by Tag and Category
```bash
python main.py --category database --tag sql
```

### 3. Rank Prompts by Popularity
```bash
python main.py --rank
```

### 4. Export Curated Prompts to Markdown
```bash
python main.py --rank --export curated_prompts.md --format MD
```

---

## 📄 License
Licensed under the [MIT License](LICENSE).