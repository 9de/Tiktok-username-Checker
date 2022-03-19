import random
import json
import colorama
import vlc
import requests
import time
import datetime
import easygui
import os
x = datetime.datetime.now()
from discord_webhook import DiscordWebhook,DiscordEmbed
settingsfile = open("settings.json",'r').read()
settings = json.loads(settingsfile)
colorama.init(autoreset=True)


def SendingToWebhook(username): 
    if settings["discordWebhook"]["enable"] == True:
        webhook = DiscordWebhook(url=settings["discordWebhook"]["url"],username=settings["discordWebhook"]["username"],avatar_url=settings["discordWebhook"]["avatarurl"])
        embed = DiscordEmbed(color=settings["discordWebhook"]["hexcolor"])
        embed.set_author(name='New Tiktok Hits Username', url='https://tiktok.com/@d8n', icon_url='https://a.top4top.io/p_2268fq9kj1.png')
    embed.set_footer(text='Tiktok Checker by @d8n')
    embed.set_timestamp()
    embed.add_embed_field(name='Username:', value=username)
    embed.add_embed_field(name='Hits At:', value=x.strftime("%x"))
    embed.set_thumbnail(url="https://a.top4top.io/s_2268fq9kj1.png")
    webhook.add_embed(embed)
    webhook.execute()


def checker(username):
 if(len(username) == 0):
    pass

 headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
     }
 req = requests.session()
 r = req.get(f"https://m.tiktok.com/node/share/user/@{username}",headers=headers).json()
 statuscode = r["statusCode"]
 if statuscode == 10202:
     print(colorama.Fore.GREEN + f"[{username}] Good")
     SendingToWebhook(username)
     file = open("Good.txt", 'a')
     file.write(username+"\n")
     if settings["mp3"]["enable"] == True:
        p = vlc.MediaPlayer(settings["mp3"]["file"])
        p.play()
        time.sleep(1.9)
        p.stop()
 elif statuscode == 10221:
    if settings["printbanned"] == True:
        print(colorama.Fore.RED + f"[{username}] Bad")
        if settings["SaveBanned"] == True:
         bannedfile = open("banned.txt",'a') 
         bannedfile.write(username)
 elif statuscode == 0 or statuscode == 10222 or statuscode == 10223 or statuscode == 10000:
    if settings["printbad"] == True:
        print(colorama.Fore.RED + f"[{username}] Bad")
    if settings["saveBad"] == True:
     badfile = open("Bad.txt",'a') 
     badfile.write(username)
 else: 
          print(username + "Can't find This statuscode")

        


if __name__ == '__main__':
    os.system("cls" or "clear")
    print(colorama.Fore.RED + """
    BBBB######B#########B##BBBBBGPP55PGGB#BGGG#BBB###########&####&###BBB###BBB##BBBBBBBB#BBGG#&@@@@@@@@
B#BB##BBBB##BB#######BBBBBBBGPPPPGGPGBGG5PGBBGGB##############BBB##BBGBBBBBBBBBBBBBBBBBBBGGB&@@@@@@@
&#B##BBG###BB#######BBBBBGGGGGGGGP55GPGPYYYPBBGBB########BBBBBBGGPPGBBBGGBBBBGBGGGGPPPPGGGGGB&@@@@@@
####BGGB###BB#####BBBGGGBBGGBBGGP5YPG5PPYJJJYGGP5PGBB##BBBGBBBBGPP555PGGGGGGGGGBBBBBBBGGGGBGGB#&@@@@
BBBBGGBBB##BBB##BBBBGGBBBGGGBGGP5YYPP5P5YJJJ?Y5P55555PPGGGBBBBBGGPP5P55PPPPPPPPPPPGPGGGBBB##BGB&&&&&
BBBBGBBBBB#BBBBBBBBBGBBGGGGGGGP5YYYP5555YJ?????Y555YYYYY55PGGGGGGBGGGGGGGGGGGGP555YYYYY55P55PPPGB###
BGGGGBBBBBBBGGB#BBBBBBGGGGGGPP5YYJJPP5Y5YJJ?????JYYYYYYYYYYYY55PPGGGGGGGBBBB###BBGGP55555PGPGGGG#&@@
BBBBBBBBBBBBBBBBBBBBBGGGGPPPP5YYYJJ5P5YYYY??????JYPGBBGGGGPP55555PGGBBGGPGGBBBBBB##BBBB#B##BBBBB#@@@
BBBBBBBBB###BBBB####BGGPPPPP55YYJJJJ5P5YYYJJJY5GB#BGGPP5P55555555Y55PGBBBGGGBBBBBB##############B#@@
BBBBBBBBBBBB########BGPPPP555YYJJJJ?Y5P5Y55GG###GP5YJJJJJJYYYYJJJYYYY5GBBGGBBBBBBGB####BBB##&&##BBB&
BBBBBBBBB####&&&&&&&#GGPP55YYYJJJJJJJJ5PGGBBBGP5YYYYJJY5YYYPP5PP55YYYY5GBBBBBBBBBBGGB###BBBB##&##BBB
#BBBBB##&&&&&&&&&&&@&#BBGGGP55YJJJJJJJJYPGPPP55PPGBBGG#########GYYJYJJY5PGBBBBBB###BBB####BBBB##&#BB
##&#B#&&&&&&&&&&&&&&&&######BBGPYJJJJJJJY555555PBBPB#B###BB#BG5JJJJJJYYY5PGBBBBBBB#############B###B
#&&#B####&&&&&&&&&&&&#BGGGGGPPPPP55YJJ?JJJJJYY5PP5YYPGGGP5PP5JJ???JJJJY5Y5PGB###BBBBBB##&&#########B
&&&&########&&&&&&&&&&#BB###BB##GGP55J??JJJ???Y5PPP5Y555YYYJ???????JJJY5555PGB######BBB#&&#&&#######
&&&&##########&&&&&&&&&##&&G55GBBBG55Y??JJJJ???JY5P5YJJJJ??????????JJJY5Y555PGB###&#######&&&&######
&&&#############&&&&&&#&&&#BP55P5YYJ5Y??JJJJJ????J5PYJJ????????????JJJYY555555PB#&&&&&&&&&&&&&&&####
################&&&&&&&#&&#GGG5YYYYJYY???JJJJJ????J55J?????????????JJJJY555555PGB#&&&&&&&&&&&&&&&&##
&&##############&&&&&&&#&&&GP55YYYJJYYJ??JJJJJJ????Y5Y?????????????JJJJYY55555PGGB&&&&&&&&&&&&&#&&&#
@&########&&#######&&&&#&&&#P5YYJJJJY5JJJJJJJJJJJJ?Y5YJ???????????JJJJJYYY5555PGGB&&&&&&&&&&&&##&&&#
@&#B######B#&###BB#&&&##&&&#G5YYYJJJY5YYYJJJJYYJJYYY55J???????????JJJJJJYYYYY5PGG#&&&&&&&&&&&&#&&&&#
@&&#######BB###&#BB##&&&&####G5YYJJJ55YYJ?JJJJJJJJY5YYJ???????????JJJJJJYYYYY5PG#&&&&&&&&&&&&&&&&@&&
@@@&#BB#BGBBB###&BB##&&&&#####GYYYJJYJ???JJJJYYYYYYJJJJ???????????JJJJJJJJYYY5PG#&&&&&&&&&&&&&#&&&&&
@@@@@#BBGGBBBBB##BBB##&&&######G5YJJJY5YYYY55YYYJJ??J???????????JJJJJJJJJJYYY5PBB#&&&&&&&&&&&&&&&&&&
@&&&##BGGGGBBBB#######&&&#######BPYYYY5P55PP5Y???????????????JJJJJJJJJJJJJYYY5GGG###&&&&&&&&&&&&&&##
#####BBBB#GBBB##########&##########G5YY555Y5YJJ??????????JJYYJJJJJJJJJJJYYYY5GPPPB#B#&&&&&&##&&&&&&&
&&&##BBBB#BBBB#&&#################&&#G5Y555555YYYJJYYYY5Y55PP5JJJJJJJJYYYYY5PP55PGBBB########&&&&&&&
&&&####BB#BBB#########&&###########&&&#G55PGGP5YYYY555PP5Y5555JJJJJJJJYYY5P5555Y5PGBB########&&&&&&&
&&&&###BB#B##########&&&###BB######&&&&&#G55PGGGGGPP5555YY5PPYJJJJJJJYYYPP5Y5YYYY5PGGB#B#######&&&&&
########BBB##########&&&############&&&####GPPPPPPPPPP555PP5JJJJJJYYY55P5YJYYYYYYY5PPGBB###########&
###BBB##BBBB####B#####&&#########BB#######B#BP55YYYYYY555YJJJJJJJJYY5P5YYJJYYJYYYY55PPGBBBB##BBBBBBB
@&&#####BBBBBB##BBBBB##&#############BB#######G555555YYJJJJJJJJJJY555YYJJJYYYYJYYYY5555PGBBBBBBBGGGG
@@@@@@@@@&BBBB##BBBGBBB##########BB####B####&##B5JJJJJ???????JJYY555YJJJJJJYJJJJJJJYYYYY55PGGGBBBBBG
@@@@@@@@@@&BBBBBB#BGGGBB###&###B##BB########&&&&#PYJJ??????JJY5555YJJJJJJJJYJJJJJJJJJYYJJJJY5555P5PP
@@@@@@@@@@@&##BBBB##BGGB#####&&########&&&&###&&&&BGPP555555555YYJJJJJJJJJJJJJ?JJJJJJJJ?JJJJJJJYYPGB
@@@@@@@@@@@@@&&BGBBBBGGBB####&&&&######&&&&BGB##BBGGBBGGGGP55YJJJJJJJJJJJJJYJJJJJJ?JJJJJJJJY5PGB#&&&
@@@@@@@@@@@@@@@@&#BGBBBBB##&&&&&&#########&#GPPPPGGP555555YYJJJJJJYYJJJJJJJJJJ??J???JJYPGB#&&&@&&&&&
@@@@@@@@@@@@@@@@@@#BBBB####&&&&&&&##&####BB#BP5PGGP5YYJYYJJ??J?JJJYJJJ?JJJJJJJJJ?J5PB#&@@@@&&&&&&&&&
@@@@@@@@@@@@@@@@@&#&##BB#&&&#&&&#&&#&#BGP555PPGBGP5YYYJJJJJ???JJJYYYJJJJJJJJJJJ5G#&&&&&&&&&&&&&&&&&&
@@@@@@@@@@@@@@@&&&&&#B#BB######&&&&##&BP5YYY5G#BPP5YYJJJJJJJJJYY55555YYYYYYY5G#&&&&&&&&&&&&&&&&&&&&&
@@@@@@@@@@@@@@@@@@###BB########&#&&&&&B5YYY5GBBGG5YJJJJJ?JJJJY555P5555555PG#&&&&&&&&&&&&&&&&&@&&&&&&
@@@@@@@@@@@@@@@@@&#######&##B####&&&&&&GYYYJYYYGPYJJJJJJJJJYYY55PPP555PG#&&@&&&&&&&&&&&&&&&&&&&&&&&&
@@@@@@@@@@@@@@@@@&#&@&######B###&&&&&&&&GYJJJJY55YJJJJJJJYYY555P55PPB#&@@&&&&&&&&&&&&&&&&@&&&&&&&&&#
@@@@@@@@@@@@@@@@@@&&&@&&######&&&&&&&&&&&#PYJJYYY5YYYYYY5555555PGB#&&@&&&&&&&&&&&&&&&&@@@&&&&&&&&&&&
@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&#P55555555555555PPG#&&&@&&&&&&&&&&&&&&&@@@@@&&&&&&&&&&&&&
@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&#BGPPPPPPPGGB##&&@@&&&&&&&&&&&&&&&@@&&&&&&&&&&&&&&&&&&&
@@@@@@@@@@@@@@@@@@@@@@&#&&&&&&&&&&&&&&&&&&&&&&&&&##&&&&&@&&&&&&&&&&&&&&&&&&&&&&@&&&&&&&&&&&&&&&&&&&&

instagram: ljzb
tiktok: d8n
Twitter: gha_
    """)
print("""
Welcome To Tiktok Checker
[1]: Automatic selection
[2]: Custom Names
""")
try:
 choose = int(input("> "))
 if choose == 1:
     letters = int(input("Number of letters: "))
     listing = int(input("How many accounts do you want to check: "))
     for i in range(listing):
        let = 'qwertyuioplkjhgfdsazxcvbnm123456789_'
        usernames = "".join(random.sample(let,letters))
        checker(username=usernames)
       
 elif choose == 2:
     files = easygui.fileopenbox("@d8n","Please choose the file with the name inside",filetypes="*.txt")
     namesfolder = open(files,'r').readlines()
     for names in namesfolder:
        checker(names.strip())
        
 else:
  print("Can't find The Number")
except ValueError: 
    print("Please Enter The Number Not String")
    input("> Enter Any Button To Leave!:")