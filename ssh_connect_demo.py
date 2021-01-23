import paramiko as paramiko
from utilities.configurations import *

ssh = paramiko.SSHClient()
host=getConfig()['Server']['host']
port=getConfig()['Server']['port']
username=getConfig()['Server']['username']
password=getConfig()['Server']['password']
ssh.connect(host,port,username,password)

#Run commands
#stdin,stdout,stderr = ssh.exec_command('ls -a')
stdin,stdout,stderr = ssh.exec_command('cat demofile')
#print(stdout.readlines())
lines=stdout.readlines()

#Upload files
sftp = ssh.open_sftp()
destinationPath = "script.py"
localePath = 'batchFiles/script.py'
sftp.put(localePath,destinationPath)

destinationPath = "loanasa.csv"
localePath = 'batchFiles/loanasa.csv'
sftp.put(localePath,destinationPath)

#Trigger the batch command
stdin,stdout,stderr = ssh.exec_command('python scripts.py')

#Download files to local system
sftp.get("loanasa.csv","outputFiles/loanasa.csv")

ssh.close()