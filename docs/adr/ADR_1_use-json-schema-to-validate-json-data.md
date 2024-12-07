# 1. Use JSON Schema to validate JSON data

## Context

JSON data from the CTA API and the MongoDB Atlas database can be returned in
non-standard formats. It is imperative that the application can simply check if
the data returned by both the API and the database are in valid formats in order
to simplify the processing the application needs to perform.

## Decision

As the data is primarily in JSON format, we will use the `jsonschema` Python
package to read data from the CTA API stored on disk and load data into MongoDB
database.

## Consequences

The JSON schema will have to be represented by a class that takes JSON data as
input and can perform comparisons against the schema. It is possible to write
this as a single method, but in doing so we lose the ability to introspecitvely
look into the input data and see where there are formatting issues.
