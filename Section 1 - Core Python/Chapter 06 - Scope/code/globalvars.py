"""."""

PORT = 9922
DB_FILE = "./db_File"


def get_server_string(server):
    """."""
    return server + ":" + str(PORT)


def set_port(new_port):
    """."""
    global PORT
    PORT = new_port

