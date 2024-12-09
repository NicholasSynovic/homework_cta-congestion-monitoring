# 5. Use a builder pattern to construct API url endpoints

## Context

The CTA provides access to three API services:

- [Trains](https://www.transitchicago.com/developers/traintracker/)
- [Busses](https://www.transitchicago.com/developers/bustracker/)
- [Customer Alerts](https://www.transitchicago.com/developers/alerts/)

Each of these services has many API endpoints. Each API endpoint takes different
parameters.

## Decision

Rather than writing logic within a `TrainAPI` class to handle creating all Train
API endpoints (for example), it makes more sense to leverage the
[Builder pattern](https://refactoring.guru/design-patterns/builder) to have a
single class with the methods to create each API endpoint.

For each of the API services, we will create a Builder class to create the API
endpoint URLs. These classes will not keep track of previously created API
endpoint URLs.

## Consequences

While we could keep track of previously created endpoint URLs, the operaton to
create the URLs is simple and efficient, so there is no reason why this class
needs to keep track of this data.

We will need to write test cases to ensure that APIs are generated correctly per
Builder class.
