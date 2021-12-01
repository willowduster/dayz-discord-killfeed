import re
import time
import tailer
from discord_webhook import DiscordWebhook

def tell_discord(msg):
    webhook = DiscordWebhook(url='https://YOUR_DISCORD_WEBHOOK_URL', content=msg)
    response = webhook.execute()

## for use with KillFeed mod
# for line in tailer.follow(open('KillfeedLogs.txt')):
#    print(line)
#    tell_discord(re.sub(r" ?\([^)]+\)", "", line))

def killfeed(line):
    matches = ["killed","died","bled", "cut deep","exploded"]
    if any(x in line for x in matches):
        msg = re.sub(r" ?\([^)]+\)", "", line)
        return msg

def parse_adm(file):
    for line in tailer.follow(open(file)):
        print(line)
    f.closed

def parse_kf(file):
    for line in tailer.follow(open(file)):
        print(line)
        out = killfeed(line)
        if out is not None:
            print(out)
            tell_discord(out)
    f.closed

while True:
    try:
        print("Parsing")
        time.sleep(1)
        parse_kf('DayZServer_x64.ADM')
#        parse_adm('DayZServer_x64.ADM')    ## uncomment for all ADM messages in console
#        parse_kf('KillfeedLogs.txt')				## for killfeed mod only
    except:
        print("error")
        pass
