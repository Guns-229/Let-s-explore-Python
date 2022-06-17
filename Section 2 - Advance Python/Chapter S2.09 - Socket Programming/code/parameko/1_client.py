"""."""
from paramiko import SSHClient, AutoAddPolicy


def connect(username, password, ip, port=22, command="ls"):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(ip, port, username, password)
    shell = client.invoke_shell()
    _, out, _ = client.exec_command(command)
    for line in out:
        print('... ' + line.strip('\n'))

    shell.close()
    client.close()


connect("dummy", "dummy@2019", "127.0.0.1")
