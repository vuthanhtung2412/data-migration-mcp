# Agents-MCP-Hackathon

## Description

Do data migration with NLP

## User stories / use cases

+ User want to migrate a subset of data from DB A to DB B (analytics DB)
  + Example : get all users of company X from DB A and add them to DB B

## Features

+ LLM explore db schema
+ **LLM generate read-only SQL query** to preview the data
+ LLM genernate Python code for DB migration
  + Explicitly tell the LLM which package is available in the server
+ Migration preview (something like terraform plan, LIMIT 10)
+ Migration execution directly on python server
+ (optional Prio 1) Dynamic DB connection
+ (optional Prio 1) Generate SQL model on migration to verify schema
+ (Optional Prio 1) LLM generate and deploy migration script to temporal
+ (Optional Prio 2) Enforce read-only query when preview
+ (Optional Prio 2) Generate a migration report
+ (Optional Prio 2) Data exploration
+ (Optional Prio 3) Reversion

## Input constraints / assumptions

+ Start with DB that supports SQL
+ The migration happen to data of small scale that can be done with 1 server
+ User know what data they want to migrate, no need for data exploration
+ Migration is done directly on the FastAPI server instead of a separate worker
+ Use Claude Desktop as the main UI and expose the fast API as MCP server
+ Let start with no SQLModel type safety

## System design

![1st architecture](/documentation/architecture.png)

## API endpoints

### get-connections

#### Description

return a list of available DB connections on the server

#### Output

```json
[
  {
    id: "postgresql-1",
    connectionURL: "postgresql://user:password@host:port/dbname",
    type: "postgresql",
  },
  {
    id: "sqlite-1",
    connectionURL: "sqlite:///path/to/database.db",
    type: "sqlite",
  }
]
```

### explore-schemas

#### Description

Explore schemas of both source and destination databases, return a list of tables and columns

#### Input

```json
{
  source: "postgresql-1",
  query: "SELECT * FROM information_schema.tables WHERE table_schema = 'public'"
}
```

### read

#### Input

```json
{
  source: "postgresql-1",
  query: "SELECT * FROM users WHERE company = 'X' LIMIT 10"
}
```

### preview

#### Description

Check the preview of the query, what will be change in the database

#### Input

```json
{
  source_id : "postgresql-1",
  destination_id : "sqlite-1",
  "source_query" : "SELECT $column1, $column2 FROM $table",
  "destination_query" : "INSERT INTO $table ($column1, $column2)"
}
```

#### Output

``` text
+++ |column1 | column2 |
+++ |--------|---------|
+++ | value1 | value2  |
+++ | value3 | value4  |
+++ |  ***   |   ***   |
+++ | value3 | value4  |
+++ |--------|----------
```

### apply

#### Description

Apply the change in the database

#### Input

```json
{
  source_id : "postgresql-1",
  destination_id : "sqlite-1",
  "source_query" : "SELECT $column1, $column2 FROM $table",
  "destination_query" : "INSERT INTO $table ($column1, $column2)"
}
```

#### Output

``` text
"n rows updated"
```

### Revert (Optional)

#### Description

Revert the last state of the databases

#### Input

.stateDB folder from a S3 bucket

#### Output

```json
{
  "info" : "success"
}
```

### CRUD Message endpoint

### CRUD Conversation endpoint

## Database design + type interface

## UI by V0

## Other notes

+ Study how to do NL2SQL

## Execution Plan / Tasks

### Must

+ [x] Connections tool (Leo)
+ [x] Explore schemas tool (Leo)
+ [x] Read tool (Tung)
+ [ ] Python code template for migration (Leo)
+ [ ] Preview tools (Tung)
+ [ ] Apply tools (Tung)

### Optional
