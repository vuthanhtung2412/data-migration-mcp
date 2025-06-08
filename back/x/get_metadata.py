from services.connection import ConnectionService


def test_list_table():
    connection_id = 1  # Change this to a valid connection id in your DB
    print("Tables:", ConnectionService.list_table(connection_id))


def test_get_table_schemas():
    connection_id = 1  # Change this to a valid connection id in your DB
    print("Schemas:", ConnectionService.get_table_schemas(connection_id))


def test_get_table_schema():
    connection_id = 1  # Change this to a valid connection id in your DB
    table_name = "employee"  # Change this to a valid table name
    print("Schema:", ConnectionService.get_table_schema(connection_id, table_name))


if __name__ == "__main__":
    test_list_table()
    # test_get_table_schemas()
    # test_get_table_schema()
