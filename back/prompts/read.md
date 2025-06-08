# MCP Tool: read

**Description:**
Executes a read-only SQL SELECT query on the specified database connection and returns the result as a list of dictionaries.

**Parameters:**

- `connection_id` (int): The ID of the database connection.
- `query` (str): The SQL SELECT query to execute.

**Returns:**

- `list[dict]`: A list of result rows, each represented as a dictionary mapping column names to values.

**Example Usage:**

```
read(connection_id=1, query="SELECT * FROM employee LIMIT 3")
# Output: [
#   {"id": 1, "name": "Alice Johnson", ...},
#   {"id": 2, "name": "Bob Smith", ...},
#   ...
# ]
```

**Notes:**

- Only SELECT queries are allowed. Other types of queries will result in an error.
- ALWAYS limit the response by 5 rows.
- NEVER use this tool without having enough information about the connection and table schemas.
- Use `get_connections`, `list_table` and `get_table_schema` to discover available database connections, tables and columns to construct your query.
- For `WHERE` clause on string columns, ALWAYS use `LIKE` instead of `=`.
- On int and date(time) columns ALWAYS query with a SMALL range instead of a perfect match.
- ONLY use point query when it make sense or when you are sure about the value.
