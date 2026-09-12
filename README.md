# Static Site Generator

A lightweight static site generator built in Python. This project converts Markdown content and HTML templates into a fully rendered, production-ready static website.

## Overview

This generator reads Markdown files from a content directory, parses them into intermediate HTML nodes, injects them into an HTML layout template, and writes the output files to a public directory alongside static assets (CSS, images, etc.).

## Key Concepts & Skills Practiced

### Object-Oriented Programming (OOP)
- **Inheritance & Polymorphism:** Designed a node hierarchy (such as `HTMLNode`, `LeafNode`, and `ParentNode`) where specialized nodes override base behaviors to render their respective HTML representations.
- **Encapsulation:** Isolated parsing, text-to-node conversion, and block-level transformations into dedicated, modular components with clear interfaces.

### Data Structures & Algorithms
- **Tree Structures:** Modeled HTML documents as Abstract Syntax Trees (ASTs), where parent nodes hold nested children, enabling recursive rendering.
- **File System Traversal:** Implemented recursive directory traversal to mirror source content directories to destination directories, handling nested pages dynamically.
- **Text Parsing & Regex:** Used regular expressions and string algorithms to parse inline markdown (links, images, bold, italic, code) and block structures (headings, lists, quotes).

### Software Engineering Practices
- **Unit Testing & TDD:** Created automated test suites using `unittest` to verify edge cases across text parsing, delimiter extraction, and node conversions.
- **Lexical Analysis & Compilers:** Implemented tokenization and AST parsing principles to transform plain text syntax into structured markup.
- **Shell Automation:** Automated local builds and test execution with Bash scripts.

## Getting Started

### Prerequisites
- Python 3.10+

### Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/xxxxzhouxx/Static_Site_Generator
   cd Static_Site_Generator
2. Run the generator script:
   ./main.sh
   # Or run directly: python3 src/main.py
4. serving locally:
   python3 -m http.server 8888 --directory docs
   # Open http://localhost:8888 in your browser

## Project Structure
- `src/` - Core Python source code (nodes, parsers, generation pipeline).
- `static/` - Static assets (CSS, images) copied to the destination.
- `content/` - Source Markdown files.
- `template.html` - Base HTML layout into which rendered content is injected.
- `docs/` - The generated static site output committed to the repo, served directly by GitHub Pages.
