import requests
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print('\n\033[1;36;40m[\033[0;37;40m\033[1;33;40m',current_time,'\033[1;36;40m] ~ [\033[1;33;40m Adminer Finder \033[1;36;40m]\033[0;37;40m')
url = input('\033[1;36;40m[\033[0;37;40m\033[1;33;40m website \033[1;36;40m] > ')
exploit = '/adminer.php'
exploit2 = '/wp/adminer.php'
exploit3 = '/home/adminer.php'

r = requests.get(url+exploit)
r2 = requests.get(url+exploit2)
r3 = requests.get(url+exploit3)

if r.status_code == 200:
    print('\033[1;36;40m[\033[0;37;40m\033[1;33;40m',current_time,'\033[1;36;40m] ~ [\033[1;33;40m Found \033[1;36;40m]\033[0;37;40m > ',r.url)
    
if r2.status_code == 200:
    print('\033[1;36;40m[\033[0;37;40m\033[1;33;40m',current_time,'\033[1;36;40m] ~ [\033[1;33;40m Found \033[1;36;40m]\033[0;37;40m > ',r2.url)

if r3.status_code == 200:
    print('\033[1;36;40m[\033[0;37;40m\033[1;33;40m',current_time,'\033[1;36;40m] ~ [\033[1;33;40m Found \033[1;36;40m]\033[0;37;40m > ',r3.url)
