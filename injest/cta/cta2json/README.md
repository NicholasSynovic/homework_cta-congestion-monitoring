# CTA To JSON

> CTA Train Arrivals REST API to JSON files

## Table of Contents

- [CTA To JSON](#cta-to-json)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How To Install](#how-to-install)
  - [How To Run](#how-to-run)
    - [Options](#options)

## About

This code queiries the CTA Train Arrivals REST API and outputs a JSON file for
each station.

If an error arises when querying a station stop, an empty JSON file is created.

## How To Install

1. `make create-dev`

## How To Run

- `python main.py --help`

### Options

```shell
Usage: main.py [OPTIONS]

  Export CTA Train REST API endpoint data as JSON files

Options:
  -k, --key TEXT        CTA API key  [required]
  -o, --ouput-dir PATH  Output directory to store JSON files  [required]
  --help                Show this message and exit.
```
