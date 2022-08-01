import pyfiglet
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
logo = pyfiglet.figlet_format('Leadership')
print(Z+logo)

loo = pyfiglet.figlet_format('Tools')
print(F+loo)

k=("----+----+-----+------+-----+")
 
print(C+k)

lo=("Tele:@X_PIRATE")
print(X+lo)

i=("----+----+-----+------+-----+")
print(C+i)
o=("#====================================##============================")

print(B+o)




import time,os,random
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
print("@X_PIRATE")
ch = "SDBB_Bot"
api_id = '5313808335'
api_hash = 'AAEULPanrtY79CZGjrMF8Msb_Tx16hl_3qU'
client = TelegramClient('session', api_id, api_hash)
client.start()
for cc in open("cc.txt","r").read().split("\n"):
    try:
        client.send_message(ch ,f"/chk {cc}")
        time.sleep(random.randint(30,30))
        mssag = client.get_messages(ch, limit=1)
        if "ANTI_SPAM" in str(mssag[0].message):
            t = str(mssag[0].message).split("again after ")[1]
            t = t.split("seconds")[0]
            t = int(t)
            print(f"Done Sleep : {t+2}")
            time.sleep(t+2)
        print(mssag[0].message)
        time.sleep(1)
    except:
        print(False)