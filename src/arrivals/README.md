# Train Arrivals API Handler

> [CTA API Docs](https://www.transitchicago.com/developers/ttdocs/#_Toc296199903)

## Table of Contents

- [Train Arrivals API Handler](#train-arrivals-api-handler)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How To Run](#how-to-run)
  - [Data Output](#data-output)

## About

The CTA Train Arrivals API returns the estimated time of arrival (ETA) of the
trains (i.e., runs) currently deployed on a given line. To get the ETA of a
given run, take the `arrT` response attribute and subtract it from the client's
current time.

## How To Run

This script is dependent upon the output of [this script](../stops/README.md).

```shell
Usage: main.py [OPTIONS]

Options:
  -k, --key TEXT                  CTA API key  [required]
  -l, --line [red|blue|green|brown|purple|purple-exp|yellow|pink|orange]
                                  CTA L train line API endpoint to access
                                  [required]
  -i, --input PATH                Path to CTA L train station SQLite3 database
                                  [required]
  -o, --output PATH               Path to store CTA L train arrivals in JSON
                                  file  [required]
  --help                          Show this message and exit.
```

**Example**: `python main.py -k $CTA_TOKEN -l red -i $STOPS_SQLITE -o red.json`

**NOTE**: Replace `$CTA_TOKEN` with a valid
[CTA API token](https://www.transitchicago.com/developers/).

**NOTE**: Replace `$STOPS_SQLITE` with the output of
[this script](../stops/README.md)

## Data Output

The output of this application is a JSON file containing an array of JSON
objects. The description of these objects is the `eta` field of the
`TrainArrivals()` schema described [here](../common/schemas.py).
