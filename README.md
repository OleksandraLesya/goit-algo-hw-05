# Python Fundamentals: Functional Programming and CLI Utilities

This repository contains solutions to several Python programming challenges focusing on core language features, functional programming concepts, data structures, and command-line interface (CLI) application development.

---

## 1. Caching Fibonacci (`fibonacci_cache.py`)

### Description

This project implements a Fibonacci sequence calculator that leverages **closures and memoization (caching)** to optimize performance for repeated calculations. The `caching_fibonacci` function returns an inner `fibonacci` function that "remembers" previously computed values, avoiding redundant recursive calls.

### Features

- Efficient Fibonacci number calculation using recursion.
- Built-in caching mechanism for performance optimization.
- Demonstrates the concept of closures in Python.

---

## 2. Income Generator and Summation (`number_sorted.py`)

### Description

This project involves processing text to extract and sum numerical data, specifically real numbers representing income components. It utilizes a **generator function** for memory-efficient iteration over the extracted numbers and a dedicated function for summing them.

### Features

- Extraction of real numbers from text using regular expressions.
- Implementation of a Python generator for lazy evaluation and memory efficiency.
- Flexible summation function accepting a generator as an argument.

---

## 3. Log File Analyzer (`log_parser/log_analyzer.py`)

### Description

A command-line Python script designed to read and analyze log files. It parses log entries, provides a statistical count of entries by log level (INFO, DEBUG, ERROR, WARNING), and offers the functionality to filter and display all logs of a specified level. The associated `logfile.log` is located within the `log_parser` directory.

### Features

- Command-line argument parsing (`sys.argv`).
- Robust log file loading with error handling (`try-except` for `FileNotFoundError`, `IOError`).
- Parsing of log lines into structured data (dictionaries).
- Statistical counting of log levels using `collections.Counter`.
- Filtering log entries by level using list comprehensions.
- Formatted display of results in a table.

### Usage

Navigate to the root of the repository (`goit-algo-hw-05`).

To get general log statistics:
`python log_parser/log_analyzer.py log_parser/logfile.log`

To get statistics and detailed logs for a specific level (e.g., ERROR):
`python log_parser/log_analyzer.py log_parser/logfile.log error`

---

## 4. Console Assistant Bot with Error Handling (`contact_assistant_bot.py`)

### Description

An enhanced version of a console-based contact management assistant bot. This bot allows users to add, change, view, and list contacts. A key feature is the robust **error handling implemented using decorators**, which gracefully manages common input errors (e.g., missing arguments, unknown commands, non-existent contacts) without crashing the application.

### Features

- Interactive command-line interface.
- Contact management: add, change, phone (show), all.
- **Decorator-based error handling** for `KeyError`, `ValueError`, and `IndexError`.
- User-friendly error messages.
- Graceful application termination.

### Usage

Run the script from the repository root:
`python contact_assistant_bot.py`

Then enter commands like:

- `hello`
- `add [name] [phone]`
- `change [name] [new_phone]`
- `phone [name]`
- `all`
- `close` or `exit`
