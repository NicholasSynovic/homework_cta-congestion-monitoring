# MongoDB Data Loader

> Tooling to store JSON documents in a MongoDB Atlas database

## Table of Contents

- [MongoDB Data Loader](#mongodb-data-loader)
  - [Table of Contents](#table-of-contents)
  - [About](#about)

## About

This component is meant to load JSON documents to a MongoDB Atlas database. It
does not need to and will not perform removals, updates, or deletes from the
database.

This component is expecting a JSON file as input. It will then validate the JSON
document against a JSON schema. If it passes the schema, the component will load
the data into the appropriate database table.
