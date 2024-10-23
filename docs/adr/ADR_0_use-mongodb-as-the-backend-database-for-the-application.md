# 0. Use MongoDB as the backend database for the application

## Context

We need to serve data to clients. This data has to be hosted within a database of some kind.
Additionally, we do not want to pay for any data hosting.

The following databases hosting options should be considered:

- Self hosted
- Heroku Postgres
- MongoDB
- Oracle Cloud

## Decision

We will use the MongoDB database to host our data to start.

MongoDB offers a fairly comprehensive set of libraries to interface with the database.
It is also free for the first 5 GB, which is far larger than we actually need for this application.

## Consequences

MongoDB is a No-SQL database. Thus, we can't easily define a schema for our data like a relational database.
Thus, when adding or querying documents, we need to validate the input/output schema of the document with techniques like JSON Schema.
