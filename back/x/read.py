from services.connection import ConnectionService

def test_read():
    connection_id = 1  # Change this to a valid connection id in your DB
    query = "SELECT * FROM employee LIMIT 3"  # Change this to a valid table and columns
    try:
        results = ConnectionService.read(connection_id, query)
        from pprint import pprint
        print("Read Results:")
        pprint(results)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_read()
