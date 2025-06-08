# MCP Tool: get_table_schemas

**Description:**
Retrieves the schema (table and columns) for all tables in a given connection.

**Parameters:**
- `connection_id` (int): The ID of the database connection.

**Returns:**
- `list[Schema]`: A list of schema objects, each describing a table and its columns.

**Example Usage:**
```
get_table_schemas(connection_id=1)
# Output: [Schema(table="employee", columns=[Column(name="id", type="INTEGER"), ...]), ...]
```

**Notes:**
- Each `Schema` object contains the table name and a list of `Column` objects (with `name` and `type`).
- Don't use this tool without having a valid connection ID.
- Please avoid using this tool if you only need a specific table's schema. Use `get_table_schema` instead.