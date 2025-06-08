# MCP Tool: get_connections

**Description:**
Retrieves all database connections stored in the system.

**Parameters:**
- None

**Returns:**
- `list[Connection]`: A list of all database connection objects.

**Example Usage:**
```
get_connections()
# Output: [
#   Connection(id=1, name="SQLite Database 1", ...),
#   Connection(id=2, name="SQLite Database 2", ...),
#   ...
# ]
```

**Notes:**
- Use this tool to discover available database connections for further operations.
