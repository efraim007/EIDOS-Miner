
print(" ______ _____ _____   ____   _____   __  __ _____                 ")
print("|  ____|_   _|  __ \ / __ \ / ____| |  \/  |_   _|                ")
print("| |__    | | | |  | | |  | | (___   | \  / | | |  _ __   ___ _ __ ")
print("|  __|   | | | |  | | |  | |\___ \  | |\/| | | | | '_ \ / _ \ '__|")
print("| |____ _| |_| |__| | |__| |____) | | |  | |_| |_| | | |  __/ |   ")
print("|______|_____|_____/ \____/|_____/  |_|  |_|_____|_| |_|\___|_|   ")

print ("\n\n")
print(" _             ______  __           _            ___   ___ ______ ")
print("| |           |  ____|/ _|         (_)          / _ \ / _ \____  |")
print("| |__  _   _  | |__  | |_ _ __ __ _ _ _ __ ___ | | | | | | |  / / ")
print("| '_ \| | | | |  __| |  _| '__/ _` | | '_ ` _ \| | | | | | | / /  ")
print("| |_) | |_| | | |____| | | | | (_| | | | | | | | |_| | |_| |/ /   ")
print("|_.__/ \__, | |______|_| |_|  \__,_|_|_| |_| |_|\___/ \___//_/    ")
print("        __/ |                                                     ")
print("       |___/       github.com/efraim007 - efraim007@protonmail.com")

print ("\n\n")

#import schedule
#import time
import os
import subprocess

#first input paramteres

cleosCmdTr = raw_input('Maxiumum transaction nummber  allowed to EIDOS mining (1..100..or 1000 etc.): ')
cleosWalletName = raw_input('Please type Cleos Wallet names: ')
cleosAccName = raw_input('Please give your EOS account name: ')
cleosCmd = 'cleos wallet unlock --name '+cleosWalletName


os.system(cleosCmd)

#check the cputime - we need to in the next version 

accountInfo = subprocess.check_output('cleos --url https://mainnet.meet.one get account '+cleosAccName, shell=True)
print (accountInfo)
print ("\n\n")

#cleos transfer command
cleosCommandTransfer = 'cleos --url https://mainnet.meet.one transfer '+cleosAccName+' eidosonecoin "0.0001 EOS" "EIDOS Mining by efraim007 - eoshungary.io"'

cleosMiningStart = raw_input('Do you start eidos mining? y/n ')

#check the integer or not
try:
    cleosCmdTr=int(cleosCmdTr)
except ValueError:
    print ("It is not integer number:"+cleosCmdTr)
else:
    #Start proccess
	if cleosMiningStart == "y":
		i = 1
		while i < cleosCmdTr:
			os.system(cleosCommandTransfer)
			i += 1

		cleosLockCmd = 'cleos wallet lock_all '
		os.system(cleosLockCmd)
		print("Have nice EIDOS :)! See you tomorrow!")
	else:
		print("Good By without EIDOS Mining!")
	
