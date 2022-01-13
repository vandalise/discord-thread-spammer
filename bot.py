try:
    import requests, threading, random, string, sys, os
    from colorama import Fore, Back, Style
except:
    print("You need to install the required modules!\nrequests, threading, random, string, colorama, sys, os")
    sys.exit()


if os.path.exists("tokens.txt"):
    pass
else:
    tokens = open("tokens.txt", "w")
    print(f"{Fore.RED}[-] Input tokens in tokens.txt")
    sys.exit()

valid_tokens = open("valid.txt", "w")

count = 0

def randomstring():
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(5))
    return x

def isvalid(token):
    request = requests.get("https://discordapp.com/api/v6/users/@me/library", headers={'Content-Type': 'application/json', 'authorization': token})
    if request.status_code == 200:
        return True

def create_threads(token, channelid, name):
    global count
    while True:
        threadname = f"{name} {randomstring()}"
        r = requests.post(f"https://discord.com/api/v9/channels/{channelid}/threads", headers={"content-type": "application/json", "Authorization": token}, json={"name": threadname, "type": 11, "auto_archive_duration": 1440})
        if r.status_code == 200 or r.status_code == 201:
            count += 1
            print(f"{Fore.GREEN}[+]  Created thread: {threadname} | {count} Threads created")
        else:
            create_threads(token, channelid, name)


def start():
    os.system("cls||clear")
    tokencount = 0
    for token in open("tokens.txt", "r").read().splitlines():
        tokencount += 1
    validcount = 0
    print(f"{Fore.YELLOW}[/] Checking {tokencount} tokens...")
    for token in open("tokens.txt", "r").read().splitlines():
        if isvalid(token) == True:
            valid_tokens.write(token)
            validcount+=1
            print(f"{Fore.GREEN}[+] Valid token saved to valid.txt")
    print(f"{Fore.GREEN}[+] Loaded {validcount} valid tokens!")

    channelid = input(f"{Fore.YELLOW}[/] Channel ID: ")
    threadnames = input("[/] Thread Names: ")
    for token in open("valid.txt", "r").read().splitlines():
        t = threading.Thread(target=create_threads, args=(token, channelid, threadnames, )).start

if __name__ == "__main__":
    start()
