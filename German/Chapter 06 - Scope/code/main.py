from globalvars import PORT as PORT
from globalvars import get_server_string as gss


def update_port(new_port):
    global PORT
    PORT = new_port


def set_server_string():
    global PORT
    return "localhost:" + str(PORT)


print(set_server_string())
update_port(8877)
print(set_server_string())

print(gss("myserver"))
