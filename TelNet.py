import getpass
import telnetlib

HOST = "192.168.1.1"
user = "reboot"
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

print(tn.read_until(b"> ", timeout=120).decode('ascii'))

command = input()
tn.write(command.encode('ascii') + b"\n")

print(tn.read_until(b". ", timeout=120).decode('ascii'))