print('''
'##:::::::'####:'##::::'##:'########::::'##::::'##::'#######:::'######::'########:::::'######::'##::::'##:'########::'######::'##:::'##:
 ##:::::::. ##:: ##:::: ##: ##.....::::: ##:::: ##:'##.... ##:'##... ##:... ##..:::::'##... ##: ##:::: ##: ##.....::'##... ##: ##::'##::
 ##:::::::: ##:: ##:::: ##: ##:::::::::: ##:::: ##: ##:::: ##: ##:::..::::: ##::::::: ##:::..:: ##:::: ##: ##::::::: ##:::..:: ##:'##:::
 ##:::::::: ##:: ##:::: ##: ######:::::: #########: ##:::: ##:. ######::::: ##::::::: ##::::::: #########: ######::: ##::::::: #####::::
 ##:::::::: ##::. ##:: ##:: ##...::::::: ##.... ##: ##:::: ##::..... ##:::: ##::::::: ##::::::: ##.... ##: ##...:::: ##::::::: ##. ##:::
 ##:::::::: ##:::. ## ##::: ##:::::::::: ##:::: ##: ##:::: ##:'##::: ##:::: ##::::::: ##::: ##: ##:::: ##: ##::::::: ##::: ##: ##:. ##::
 ########:'####:::. ###:::: ########:::: ##:::: ##:. #######::. ######::::: ##:::::::. ######:: ##:::: ##: ########:. ######:: ##::. ##:
........::....:::::...:::::........:::::..:::::..:::.......::::......::::::..:::::::::......:::..:::::..::........:::......:::..::::..::
''')

from pathlib import Path
import argparse
import requests
import threading
import sys


print('Made By- Aves Ahmed Khan')
print('')
print('If You Have Any Query PM me at:')
print('Twitter  - https://twitter.com/av3sk77')
print('LinkedIn - https://www.linkedin.com/in/aves-ahmed-khan-b835a7168/')
print('')

parser = argparse.ArgumentParser()
parser.add_argument("-o", dest="out", help='Output File [Ex. -o "found.txt"]')

required = parser.add_argument_group('Required Arguments')
required.add_argument("-w", dest="wordlist", help='Wordlist file Location [Ex. -w "/root/Desktop/domains.txt"]', required=True)

args = parser.parse_args()

if not Path(args.wordlist).exists() & Path(args.wordlist).is_file():
   print("Domains File Not Found:", args.wordlist)
   sys.exit()

out_file = args.out
if out_file is not None:
   write_file = open(out_file, "a")

def check(list):
    try:
        response = requests.get("https://"+list, timeout=3)

    except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
        try:
            response = requests.get("http://" + list, timeout=3)
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
            pass
        else:
            if out_file is not None:
                write_file.write(list+"\n")
            print(f"{list} is Exist")
    else:
        if out_file is not None:
            write_file.write(list+"\n")
        print(f"{list} is Exist")

with open(args.wordlist, 'r') as domains:
    for list in domains.read().splitlines():
        t = threading.Thread(target=check, args=(list,))
        t.start()
if out_file is not None:
    write_file.close()
