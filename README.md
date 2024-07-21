
# `ccwc` Documentation

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Testing](#testing)
5. [Examples](#examples)

## Overview

`ccwc` (Coding Challenges Word Count) is a command-line tool inspired by the Unix `wc` command. It can count the number of lines, words, characters, and bytes in a text file. It also supports reading input from standard input.

## Installation

### Prerequisites

- Python 3.6+
- `virtualenv` (optional but recommended for creating isolated environments)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/ccwc.git
    cd ccwc
    ```

2. (Optional) Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

## Usage

You can run the `ccwc` command with various options:

```bash
python ccwc/ccwc.py [option] <filename>
```

### Options

- `-c`: Count bytes in the file.
- `-l`: Count lines in the file.
- `-w`: Count words in the file.
- `-m`: Count characters in the file.
- No option: Output the count of lines, words, and bytes.

### Example

To count the number of lines in `test.txt`:

```bash
python ccwc/ccwc.py -l test.txt
```

To count the number of lines, words, and bytes in `test.txt`:

```bash
python ccwc/ccwc.py test.txt
```

## Code Structure

```
ccwc/
├── ccwc.py        # Main script
├── __init__.py    # Init file for the package
└── tests/         # Directory for test cases
    ├── __init__.py
    └── test_ccwc.py
```

### `ccwc.py`

This is the main script that handles the command-line arguments, reads the file or standard input, and prints the required counts.

### `tests/test_ccwc.py`

This file contains the unit tests for the `ccwc` script. It uses the `unittest` framework to verify the functionality of the `ccwc` script.

## Testing

To run the tests, use the following command:

```bash
python -m unittest discover -s tests
```

The tests cover the following functionalities:
- Counting bytes (`-c`)
- Counting lines (`-l`)
- Counting words (`-w`)
- Counting characters (`-m`)
- Default behavior (counts lines, words, and bytes)
- Reading from standard input

## Examples

### Counting Bytes

```bash
python ccwc/ccwc.py -c test.txt
```

Output:

```
342190 test.txt
```

### Counting Lines

```bash
python ccwc/ccwc.py -l test.txt
```

Output:

```
7145 test.txt
```

### Counting Words

```bash
python ccwc/ccwc.py -w test.txt
```

Output:

```
58164 test.txt
```

### Counting Characters

```bash
python ccwc/ccwc.py -m test.txt
```

Output:

```
339292 test.txt
```

### Default Option

```bash
python ccwc/ccwc.py test.txt
```

Output:

```
7145 58164 342190 test.txt
```

