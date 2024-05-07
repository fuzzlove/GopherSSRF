Gopher HTTP requests (POST/GET) | By: Liquidsky

URL: gopher: // <host>:<port>/<gopher-path>_ followed by TCP data stream

Be careful not to forget the underscore "_" at the end. The TCP data stream begins after the underscore "_". If you do not add this "_", the message received by the server will not be complete. You can write this character at will.

Tip for determing POST request length:

└─$ echo "username=admin&password=admin" | wc -c 
 Output= 30
 Subtract 1 from this result. = 29 -> Then add this to content length header.
