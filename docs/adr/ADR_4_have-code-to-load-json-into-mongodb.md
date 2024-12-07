# 4. Have code to load JSON into MongoDB

## Context

Once we have JSON locally on our system, we need to be able to upload it to
MongoDB.

## Decision

We will have a seperate service that will:

1. Read a directory for JSON files,
1. Load the JSON data into memory, and
1. Upload to a MongoDB collection

## Consequences

The system may become bloated by the number of JSON files written to disk. It
may be necessary to have a `bash` script to compress the old data for archival
purposes.
