"""."""

PORT = 9922
DB_FILE = "./db_File"
USERS = ['rohit', 'Roshan', 'GV']

def get_server_string(server):
    """."""
    global PORT
    return server + ":" + str(PORT)


def set_port(new_port):
    """."""
    global PORT
    PORT = new_port

def gettest_details():
    return {"port": PORT, "db" : DB_FILE}


def add_user(username):
	USERS.append(username)

print("User List:", USERS)
add_user("P.B.")
print("Users are now:", USERS)
