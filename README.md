# CTA L Tracker

> Chicago Transit Authority (CTA) Elevated (L) Train Tracker

## Table of Contents

- [CTA L Tracker](#cta-l-tracker)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Supported Systems](#supported-systems)
  - [How To Build From Source](#how-to-build-from-source)
  - [How To Run The Application](#how-to-run-the-application)
    - [MongoDB Configuration](#mongodb-configuration)
    - [Getting L Route Alerts](#getting-l-route-alerts)
    - [Getting L Station Alerts](#getting-l-station-alerts)
    - [Getting L Stops](#getting-l-stops)

## About

This application (i.e, CLT) is a full stack application to provide an
alternative experience to tracking the status and location of CTA L trains
across all lines. The backend of this applicaton is powered by Python 3.10, the
database is implemented as a MongoDB database, the API gateway is implemented
with FastAPI, and the frontend is a mobile first, JS + HTML5 application.

While this application does not meet full feature parity with the CTA Ventra
application, it is a step in the direction to providing a self-hostable platform
for monitoring public transit and implementing traffic monitoring and prediction
algorithms.

## Supported Systems

This application has been tested on:

- Pop!\_OS 22.04 LTS

Currently, the following requirements are necessary to build, test, and run the
application:

- `python3.10`

## How To Build From Source

1. `make create-dev`
1. `source env/bin/activate`
1. `make build`

## How To Run The Application

### MongoDB Configuration

1. Create a MongoDB database called `cta`
1. Create the following collections within the `cta` database:

- `l_route_alerts`
- `l_station_alerts`
- `l_stops`

### Getting L Route Alerts

1. `python3.10 apps/l_route_alerts/app.py --help`

### Getting L Station Alerts

1. `python3.10 apps/l_station_alerts/app.py --help`

### Getting L Stops

1. `python3.10 apps/l_stops/app.py --help`
