#!/usr/bin/env python3

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import time
import requests
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
time.sleep(3)

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
def send_cookie_back():
    http_response = requests.get(targetsite, cookie) 
   
        
# - Generate a .html file to capture the contents of the HTTP response
    with open("HTTP_Response.html", "w") as f:
        f.write(http_response.text)
    f.close
# - Open it with Firefox
    webbrowser.open_new_tab('HTTP_Response.html')

send_cookie_back()
