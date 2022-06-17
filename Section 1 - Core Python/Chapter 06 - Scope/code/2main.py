from globalvars_1 import PORT as PORT
from globalvars_1 import set_port as sp
from globalvars_1 import get_server_string as gss


def update_port(new_port):
    global PORT
    PORT = new_port


def set_server_string():
    global PORT
    return "localhost:" + str(PORT)


def set_server_string_1():
    return "localhost" + str(PORT)


print(set_server_string())
print(set_server_string_1())
update_port(8877)
print(set_server_string())
print(set_server_string_1())
print(gss("myserver"))
sp(4444)
print(gss("myserver"))

