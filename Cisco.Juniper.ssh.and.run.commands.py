import paramiko
import cmd
import time
import sys

output = ''

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('1.2.3.4', username='user', password='abc123')
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
terminal = ssh.invoke_shell()

# Enable mode
terminal.send('enable\n')
time.sleep(1)
output = terminal.recv(9999)
print output

# Enable password
terminal.send('abc123\n')
time.sleep(1)
output = terminal.recv(9999)
print output

# Disable paging
terminal.send('terminal length 0\n')
time.sleep(1)
output = terminal.recv(9999)
print output

# Configuration mode
terminal.send('conf t\n')
time.sleep(1)
output = terminal.recv(9999)
print output

# Apply configuration changes
terminal.send('mac access-list extended Authorized_Clients\n')
terminal.send('permit e47f.b200.0000 0000.00ff.ffff any\n')
terminal.send('deny   any any\n')
terminal.send('interface fa0/20\n')
terminal.send('no switchport access vlan 100\n')
terminal.send('switchport access vlan 1\n')
terminal.send('mac access-group Authorized_Clients in\n')
terminal.send('interface fa0/10\n')
terminal.send('switchport trunk allowed vlan remove 100\n')
terminal.send('do write mem\n')
time.sleep(1)
output = terminal.recv(9999)
print output

# Veriy configuration changes
terminal.send('do show access-lists\n')
terminal.send('do sh run interface fa0/20\n')
terminal.send('do show run\n')
time.sleep(1)
output = terminal.recv(9999)
print output

Log = output.strip()
Log = Log.replace('\r','')

writeFile = open('Script_output.txt','w')
writeFile.write (Log)
writeFile.close
sys.exit()




