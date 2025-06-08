# MCP Tool: list_table

**Description:**
Returns a list of all table names for the given database connection.

**Parameters:**

- `connection_id` (int): The ID of the database connection to inspect.

**Returns:**

- `list[str]`: A list of table names in the connected database.

**Example Usage:**
list_table(connection_id=1)

# Output: [

# "employee",

# "department",

# ...

# ]

**Notes:**

- ALWAYS use `get_connections` first to find valid connection IDs.
- NEVER use this tool without having a valid connection ID.
