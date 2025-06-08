# MCP Tool: migrate_to_table

**Description:**
Migrates data from a source database to a table in a destination database using a SQL query. It executes the provided SELECT query on the source connection and inserts the resulting rows into the specified table of the destination connection.

**DANGER!**

- This tool is very powerful and damage your data system.
- Please stop the loop and check the input with the user before running it.

**Parameters:**

- `source_id` (int): The ID of the source database connection.
- `query` (str): The SELECT SQL query to execute on the source database to fetch the data.
- `destination_id` (int): The ID of the destination database connection.
- `table_name` (str): The name of the table in the destination database where the data will be inserted.

**Returns:**

- `Result[int, str]`: On success, returns
  `(number_of_rows_migrated) rows migrated` where
  `number_of_rows_migrated` is the count of rows successfully inserted.
  On failure, returns `(error_message)` with a description of the error.

**Example Usage:**

```
migrate_to_table(
  source_id=1,
  query="SELECT id, name, email FROM users WHERE active = TRUE",
  destination_id=2,
  table_name="active_users_backup"
)
# Output (Success):
# 150 rows migrated

# Output (Failure - e.g., table not found):
# Table 'active_users_backup' not found in connection 2

# Output (Failure - e.g., invalid query):
# Only SELECT (readonly) queries are allowed.
```

**Notes:**

- The target table in the destination database must already exist
  and its schema should be compatible with the columns returned by the query.
- Only SELECT queries are permitted to ensure
  no unintended modifications are made to the source database.
- NEVER use this tool without thorough checking of the form of the query result
  (you can achieve this with `read` tool) and
  the schema of the target table
  (you can achieve this with `get_table_schema` tool).
