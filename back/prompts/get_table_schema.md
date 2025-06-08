# MCP Tool: get_table_schema

**Description:**
Retrieves the schema for a specific table in a given connection.

**Parameters:**
- `connection_id` (int): The ID of the database connection.
- `table_name` (str): The name of the table to inspect.

**Returns:**
- `Schema`: A schema object containing the table name and its columns.

**Example Usage:**
```
get_table_schema(connection_id=1, table_name="employee")
# Output: Schema(table="employee", columns=[Column(name="id", type="INTEGER"), ...])
```

**Notes:**
- Use `list_table` to find valid table names.
- Don't use this tool without having a valid connection ID.
