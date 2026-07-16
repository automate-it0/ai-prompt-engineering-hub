#!/usr/bin/env python3
"""
AI Prompt Engineering Hub CLI Tool
A local-first tool to manage, search, rank, and export high-quality AI prompts securely without API keys.
"""

import argparse
import json
import logging
import os
from typing import List, Dict, Any

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DEFAULT_DB_FILE = 'prompts.json'

def load_prompts(db_file: str) -> List[Dict[str, Any]]:
    """
    Loads prompts from the local database JSON file.
    """
    if not os.path.exists(db_file):
        logging.error(f"Database file '{db_file}' not found.")
        return []
    
    try:
        with open(db_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            logging.info(f"Loaded {len(data)} prompts from '{db_file}'.")
            return data
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing database file: {e}")
        return []
    except Exception as e:
        logging.error(f"Failed to load prompts: {e}")
        return []

def filter_prompts(prompts: List[Dict[str, Any]], category: str = None, tag: str = None) -> List[Dict[str, Any]]:
    """
    Filters prompts by category or tag.
    """
    filtered = prompts
    if category:
        filtered = [p for p in filtered if p.get('category', '').lower() == category.lower()]
    if tag:
        filtered = [p for p in filtered if tag.lower() in [t.lower() for t in p.get('tags', [])]]
    return filtered

def rank_prompts(prompts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Ranks prompts by the number of likes in descending order.
    """
    return sorted(prompts, key=lambda x: x.get('likes', 0), reverse=True)

def save_prompts_to_file(prompts: List[Dict[str, Any]], filename: str, format_type: str) -> None:
    """
    Saves the list of prompts to a file in Text, Markdown, or JSON format.
    """
    try:
        if format_type.upper() == 'JSON':
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(prompts, f, indent=2, ensure_ascii=False)
        elif format_type.upper() == 'MD':
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("#curated AI Prompts\n\n")
                for p in prompts:
                    f.write(f"### {p.get('title')} ({p.get('likes')} 👍)\n")
                    f.write(f"- **Category**: `{p.get('category')}`\n")
                    f.write(f"- **Tags**: {', '.join([f'`{t}`' for t in p.get('tags', [])])}\n\n")
                    f.write(f"```text\n{p.get('prompt')}\n```\n\n---\n\n")
        else:  # TEXT format
            with open(filename, 'w', encoding='utf-8') as f:
                for p in prompts:
                    f.write(f"Title: {p.get('title')} ({p.get('likes')} likes)\n")
                    f.write(f"Prompt: {p.get('prompt')}\n")
                    f.write("=" * 40 + "\n")
        
        logging.info(f"Successfully exported prompts to '{filename}' in {format_type.upper()} format.")
    except Exception as e:
        logging.error(f"Error saving prompts to file: {e}")

def main() -> None:
    parser = argparse.ArgumentParser(description='AI Prompt Engineering Hub CLI')
    parser.add_argument('--db', default=DEFAULT_DB_FILE, help='Path to the local prompts JSON database')
    parser.add_argument('--rank', action='store_true', help='Rank prompts by popularity (likes)')
    parser.add_argument('--category', help='Filter prompts by category')
    parser.add_argument('--tag', help='Filter prompts by tag')
    parser.add_argument('--export', help='Filename to export the results to')
    parser.add_argument('--format', choices=['TEXT', 'MD', 'JSON'], default='TEXT', help='Export format (default: TEXT)')
    args = parser.parse_args()

    # Load
    prompts = load_prompts(args.db)
    if not prompts:
        return

    # Filter
    if args.category or args.tag:
        prompts = filter_prompts(prompts, category=args.category, tag=args.tag)
        logging.info(f"Filtered down to {len(prompts)} prompts.")

    # Rank
    if args.rank:
        prompts = rank_prompts(prompts)
        logging.info("Sorted prompts by likes.")

    # Display in console
    print("\n--- AI Prompts ---")
    for idx, p in enumerate(prompts, 1):
        print(f"[{idx}] {p.get('title')} ({p.get('likes')} 👍) [{p.get('category')}]")
        print(f"    Prompt: {p.get('prompt')}\n")

    # Export
    if args.export:
        save_prompts_to_file(prompts, args.export, args.format)

if __name__ == '__main__':
    main()