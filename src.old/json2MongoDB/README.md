# JSON To MongoDB

> Upload JSON data to a MongoDB `arrivals` collection

## Table of Contents

- [JSON To MongoDB](#json-to-mongodb)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How To Install](#how-to-install)
  - [How To Run](#how-to-run)
    - [Options](#options)

## About

This code uploads JSON data to a MongoDB `arrivals` collection.

## How To Install

1. `make create-dev`

## How To Run

- `python main.py --help`

### Options

```shell
Usage: main.py [OPTIONS]

Options:
  -i, --input-dir PATH    Input directory to read JSON files  [required]
  -u, --username TEXT     MongoDB Atlas username  [required]
  -p, --password TEXT     MongoDB Atlas password  [required]
  -c, --cluster-uri TEXT  MongoDB Atlas clusterURI  [required]
  --help                  Show this message and exit.
```
