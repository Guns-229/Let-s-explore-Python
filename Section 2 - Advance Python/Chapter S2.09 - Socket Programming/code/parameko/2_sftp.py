"""."""
from paramiko import Transport, SFTPClient, AutoAddPolicy


def connect(username, password, ip, port=22):
    client = Transport(ip, port)
    #   client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(username=username, password=password)
    #shell = client.invoke_shell()
    sftp = SFTPClient.from_transport(client)
    sftp.put("1_client.py", "1_client.py")

    client.close()
    sftp.close()

connect("dummy", "dummy@2019", "127.0.0.1")
