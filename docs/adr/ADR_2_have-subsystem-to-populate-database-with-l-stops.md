# 2. Have subsystem to populate database with L stops

## Context

We need to know all of Chicago's L stops. This information will not change that
often, so we can cache this into an offline SQLite3 database. This way we can
efficiently query the information with SQL on the backend without pinging the
MongoDB database.

## Decision

We will have a small system that queries
[this API endpoint](https://data.cityofchicago.org/Transportation/CTA-System-Information-List-of-L-Stops/8pix-ypme/about_data)
and converts the JSON output into a SQLite3 database.

To do so we will leverage `ibis` and potentially `polars`. `ibis` provides a
simple connector to ~20 different data storage and database outputs. `polars` is
a DataFrame library implemented in Rust that is gaining popularity due to its
speed.

## Consequences

When querying information about CTA L stops, we will have to first query the
SQLite3 database for the relevant stop information.
