import requests, time, random, string
from colorama import Fore, Back, Style

def randomstring():
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(5))
    return x


def joinserver(token, invitecode):
    baseurl = f"https://discord.com/api/v8/invites/{invitecode}"

    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'de',
        'authorization': token,
        'content-length': '0',
        'cookie': '''__cfduid=d29b03c861c9946a94d03a0496cd094881618767505; __dcfduid=39c9736a6f12e98b7067efa27ab53c6a; locale=de; _ga=GA1.2.1440912255.1618809286; _gid=GA1.2.384772034.1618809286; __stripe_mid=392b57df-a061-4026-82e7-7d7d04e2097907427b; __stripe_sid=b7eb9154-6794-4726-9097-04dbc28cd69216e93c''',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/channels/@me',
        'sec-ch-ua': '''"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"''',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjMyNTAxNzA5ODU5MjA1OTM5MiIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI2Njc0NzQ2MjYzMzAyMzA3ODQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS4xMjggU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijg5LjAuNDM4OS4xMjgiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODI1OTAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
    }

    try:
        r = requests.post(baseurl, headers=headers, timeout=0.5)
        if r.status_code == 200:
            print(f"{Fore.GREEN}[+] Joined token : {token}")
        else:
            print(r.status_code)
    except Exception as e:
        print(f"{Fore.GREEN}[-] {e}")

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

def start():
    print(Fore.YELLOW)
    join = input("Join tokens to server? [y/n]")
    if join not in("y","n"):
        start()
    elif join == "y":
        invitecode = input("[+] https://discord.gg/")
        for token in open("tokens.txt", "r").read().splitlines():
            joinserver(token=token, invitecode=invitecode)
    else:
        pass
    tokens = []
    for token in open("tokens.txt", "r").read().splitlines():
        tokens.append(token)
    channelid = input("Channel ID: ")
    name = input("Thread Name: ")
    main(tokens=tokens, channelid=channelid, name=name)

start()
