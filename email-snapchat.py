import os
try:
 import requests,random
except ModuleNotFoundError:
 os.system('pip install requests')
try:
 import time
except ModuleNotFoundError:
 os.system('pip install time')
try:
 from colorama import Fore
except ModuleNotFoundError:
 os.system('pip install colorama')
try:
 import threading
except ModuleNotFoundError:
 os.system('pip install threading')
SP = Fore.YELLOW
WIT = Fore.WHITE
RD = Fore.RED
r=requests.session()
print(SP+"""
   ____  By JOKER @vv1ck @TweakPY
  / ___| _ __   __ _ _ __  
  \___ \| '_ \ / _` | '_ \ 
   ___) | | | | (_| | |_) |  check EMAIL 
  |____/|_| |_|\__,_|J.__/ 
                    |_|   
"""+WIT)
fils = input('[?] Enter the email file name : ')
try:
	file = open(fils,'r')
except FileNotFoundError:
	print(f'[!] {file} file not found')
	input('Enter to exit')
	exit()
prxs = input('[?] Enter the proxy file name : ')
try:
	proxy =  open(prxs,'r').read().splitlines()
except FileNotFoundError:
	print(f'[!] {prxs} file not found')
	input('Enter to exit')
	exit()
print('********** Checker started **********')
time.sleep(1.2)
def snapchatCK():
	while True:
		emal = file.readline().split('\n')[0]
		QTR = []
		for pro in proxy:
			QTR.append(pro)
			JO = str(random.choice(QTR))
		PROXY = {"https":JO,"http":JO}
		headers = {
				'Host': 'accounts.snapchat.com',
				'Cookie': 'xsrf_token=aDpeseUJS0ysikB9nhdNzA; _ga=GA1.2.113171992.1627308862; _scid=f8244bc8-117d-45aa-b1b0-f24ab31edabc; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; sc_at=v2|H4sIAAAAAAAAAE3GwRGAMAgEwIqY4cIJxG6MSBUp3m/2teq4YEOlrEuIWpIfSxbD36fB2bFBveEjTDM991H9AatYyihAAAAA; _sctr=1|1627257600000; web_client_id=e64bb4c8-1a1f-4de7-970d-d637c2e9a642',
				'User-Agent': 'Mozilla/5.0 (@vv1ck) Gecko/20100101 Firefox/90.0',
				'Accept': 'application/json, text/plain, */*',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Content-Type': 'application/json',
				'X-Xsrf-Token': 'aDpeseUJS0ysikB9nhdNzA',
				'Content-Length': '49',
				'Origin': 'https://accounts.snapchat.com',
				'Referer': 'https://accounts.snapchat.com/accounts/merlin/login',
				'Sec-Fetch-Dest': 'empty',
				'Sec-Fetch-Mode': 'cors',
				'Sec-Fetch-Site': 'same-origin',
				'Te': 'trailers',
				'Connection': 'close'}
		data = {
			"email":emal,"app":"BITMOJI_APP"}
		try:
			Send = r.post('https://accounts.snapchat.com/accounts/merlin/login',headers=headers,json=data,proxies=PROXY)
			if 'hasSnapchat' in Send.text:
				print(Fore.GREEN+'[+] linked on snapchat ')
				print('  Email >> '+emal)
				with open('linked-snap.txt', 'a') as x:
					x.write(emal+ '\n')
			elif Send.status_code == 204:
				print(RD+'[-] Not linked on snapchat')
				print('  Email >> '+emal)
			elif Send.status_code == 429:
				print(WIT+'[-] Bad proxy..')
			else:
				pass
		except requests.exceptions.ConnectionError:
			print(WIT+'[-] Bad proxy..')
		except KeyboardInterrupt:
			exit()
J_QTR =[]
for i in range(30):
	th1 = threading.Thread(target=snapchatCK)
	th1.start()
	J_QTR.append(th1)
for th2 in J_QTR:th2.join()
