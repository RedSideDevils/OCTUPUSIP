import requests
from bs4 import BeautifulSoup
import os
from colorama import Fore,Back
import argparse

class IPLookup:
    def __init__(self,ip):
        self.ip = ip

    def options(self):
        self.API = "https://whatismyipaddress.com/ip/{}".format(self.ip) 
        proxy = {
            'https':'159.8.114.34:8123',
        }
        self.html = requests.get(self.API, proxies = proxy)

    def ScanIP(self):
        self.options()
        if self.html.status_code == 200:
            print("CONNECTED")
            self.soup = BeautifulSoup(self.html.text,'html.parser')
            ip_info = self.soup.find_all("td")
            os.system("clear")
            self.banner = """
                                                                                
 ██▓ ██▓███   ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███  
▓██▒▓██░  ██▒▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
▒██▒▓██░ ██▓▒▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
░██░▒██▄█▓▒ ▒▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
░██░▒██▒ ░  ░░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
░▓  ▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
 ▒ ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
 ▒ ░░░         ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
 ░               ░  ░    ░ ░      ░ ░  ░  ░      ░              
                                                                

            """
            self.output = Fore.GREEN + """        
IP           > {}
Decimal      > {}
Hostname     > {}
ASN          > {}
ISP          > {}
Organization > {}
Services     > {}
Type         > {}
Assignment   > {}
Content      > {}
Country      > {}
Latitude     > {}
Logitutde    > {}
            """.format(str(ip_info[0].get_text()),Fore.GREEN + str(ip_info[1].get_text()),str(ip_info[2].get_text()),str(ip_info[3].get_text()),str(ip_info[4].get_text()),str(ip_info[5].get_text()),str(ip_info[6].get_text()),str(ip_info[7].get_text()),str(ip_info[8].get_text()),str(ip_info[10].get_text()),str(ip_info[11].get_text()),str(ip_info[12].get_text()),str(ip_info[13].get_text()))
            print(Fore.RED + self.banner)
            print(self.output)
            print()

        else:
            print("NO CONNECTION")
            exit()
parser = argparse.ArgumentParser()
parser.add_argument('ip',help="TARGET IP")
args = parser.parse_args()

me = IPLookup(str(args.ip))
me.ScanIP()
