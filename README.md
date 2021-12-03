## Tests and linter status:
[![Maintainability](https://api.codeclimate.com/v1/badges/773d5f4a0b15c2116805/maintainability)](https://codeclimate.com/github/VVtatarinoff/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/773d5f4a0b15c2116805/test_coverage)](https://codeclimate.com/github/VVtatarinoff/python-project-lvl2/test_coverage)
[![Linter-check](https://github.com/VVtatarinoff/python-project-lvl2/actions/workflows/linter.yml/badge.svg)](https://github.com/VVtatarinoff/python-project-lvl2/actions/workflows/linter.yml)
[![Test passed](https://github.com/VVtatarinoff/python-project-lvl2/actions/workflows/pytest.yml/badge.svg)](https://github.com/VVtatarinoff/python-project-lvl2/actions/workflows/pytest.yml)

# Comparison of data in files
Gendiff is a package that provide service of comparisons variables stored in two types of file:
    - JSON
    - YAML
The package provides as terminal session work as python package to include in 3rd parties
The output is a text report. During termainal session it output to stdout, as a function it returns string with report

The package is created during educational courses at [Hexlet](https://ru.hexlet.io) step 2.

## Installation
to install the package you could enter a command:

##### python3 -m pip install --user git+https://github.com/VVtatarinoff/python-project-lvl2

to uninstall use the opposite command

## Usage

### Terminal session
command: gendiff
parameters: two paths with files (first_file and second_file)

options:
    -f (or --format) to choose output style:
        stylish (or omitted) - stylish format
        json - JSON format
        plain - wording description about changes
    -h (or --help) - short help about usage of command

## Links
This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [flake](https://flake8.pycqa.org/en/latest/)                                | "Tool For Style Guide Enforcement"                      |
| [pytest](https://pytest.org/en/latest/)                                     | "Helps you write better programs"                       |

## Video capturing of package running
### Fist step - introducing help and comparison of plain json files
[![asciicast](https://asciinema.org/a/IvsTxKLUL68EdSNxaTLlRcUmb.svg)](https://asciinema.org/a/IvsTxKLUL68EdSNxaTLlRcUmb)

### Second step - adding working with yaml files in package
[![asciicast](https://asciinema.org/a/0ITCH2p4zbInE3jZpaI6dL1ZQ.svg)](https://asciinema.org/a/0ITCH2p4zbInE3jZpaI6dL1ZQ)

### Third step - working with complex structures
[![asciicast](https://asciinema.org/a/gZOR6zbUIWtxpwq6oor6TZB1Q.svg)](https://asciinema.org/a/gZOR6zbUIWtxpwq6oor6TZB1Q)

### Fourh step - implementing 'plain' format of output
[![asciicast](https://asciinema.org/a/zEO9qJHXvEJubse2EqYj3B8gN.svg)](https://asciinema.org/a/zEO9qJHXvEJubse2EqYj3B8gN)

### Last step - 'json' format of output was implemented
[![asciicast](https://asciinema.org/a/4vPEU7IvT8MjyY151Q5hFEKRi.svg)](https://asciinema.org/a/4vPEU7IvT8MjyY151Q5hFEKRi)