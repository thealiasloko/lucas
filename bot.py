from telethon.sync import TelegramClient
from telethon import *
import time
from telethon import events, Button
from telethon import functions, types, events, utils
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.errors import SessionPasswordNeededError
from telethon.tl.types import ReplyInlineMarkup
from telethon.tl.types import KeyboardButtonRow
from telethon.tl.types import KeyboardButtonUrl
import configparser

from telethon import TelegramClient, Button, events 
import json
import asyncio
from datetime import date, datetime
import re
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from pathlib import Path
import asyncio
from telethon import Button
import logging
import requests
import re
import telethon
from sys import argv
from prettytable import PrettyTable
api_id = 11849455 #Apiid
api_hash = '0956032efc5694f60156fe65f9c19764' #APIHASH
username = '' #Username in telegram

def pregs(dets):
    arrays = re.findall(r'[0-9]+', dets)
    return arrays
from telethon import TelegramClient
from telethon.sync import TelegramClient
client = TelegramClient(username, api_id, api_hash)
client.start()

with client:
          print("STARTED")
          while True:
           try:
            asyncio.sleep(2)
            file1 = open("Scrapped.txt", "r+")    
# absolute file positioning 
            file1.seek(0)  
            ofid = file1.read()
            ofid = int(ofid)
            file1.close()  
            message = client.iter_messages('database',reverse=True,offset_id=ofid,min_id=ofid,wait_time=3)
            for msg in message:
             message = msg
             title = msg.text
             m = msg.id
             file = open("Scrapped.txt", 'r+')  
             file.truncate()
             file.write(str(m))
             file.close()  
             list = pregs(title)
             cc = list[0]
             if len(cc) == 0:
              break
             if len(cc) != 16:
              break
             con = requests.get("https://serverlostapis.000webhostapp.com/apis/binSearch.php?bin=" + cc).text
             if len(con) == 0:
              con = 'N.A'             
             mes = list[1]
             ano = list[2]
             ano1 = list[2]
             cvv = list[3]
             if len(mes) >= 3:
              ano = cvv
              cvv = mes
              mes = ano1
             lista = cc + "|" + mes + "|" + ano + "|" + cvv
             print(lista)
             respo = "<b>•> ROLDEXVERSE CC SCRAPPER\n°> CARD -> <code>" + lista + "</code>\n•> BIN -> " + con +"\n•> CHANNEL -> @RoldexVerse\n•> RECHECK -> @RoldexVerseChats\n•> OWNER -> <code>@r0ld3x</code></b>"
             # 
             file1 = open("Scrapped.txt", "a")
             m = lista + "\n"
             file1.write(m)
             file1.close() 
             client.send_message('database', respo,parse_mode='html')
             client.send_message('https://t.me/databasecc', respo,parse_mode='html')
           except errors.FloodWaitError as e:
               print('Have to sleep', e.seconds, 'seconds')
               time.sleep(e.seconds)
