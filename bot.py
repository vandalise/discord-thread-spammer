import requests, time, random, string
from colorama import Fore, Back, Style

def randomstring():
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(5))
    return x

def main(tokens, channelid, name):
   while True:
       for token in tokens:
            try:
                threadname = f"{name} {randomstring()}"
                r = requests.post(f"https://discord.com/api/v{random.randint(6,9)}/channels/{channelid}/threads", headers={"content-type": "application/json", "Authorization": token}, json={"name": threadname, "type": 11, "auto_archive_duration": 1440})
                if r.status_code == 200 or r.status_code == 201:
                    print(f"{Fore.GREEN}[+] Created thread : {threadname}")
                elif r.status_code == 429:
                    timex = int(r.json()["retry_after"])
                    print(f"{Fore.RED}[-] Ratelimited | Retrying after {timex} seconds...")
                    time.sleep(10) # i did this instead of sleeping for timex cuz I wanted to see the ratelimit time get updated
            except Exception as e:
                print(f"{Fore.RED}[-] {e}")

print(Fore.YELLOW)
tokens = []
for token in open("tokens.txt", "r").read().splitlines():
    tokens.append(token)
channelid = input("Channel ID: ")
name = input("Thread Name: ")
main(tokens=tokens, channelid=channelid, name=name)
