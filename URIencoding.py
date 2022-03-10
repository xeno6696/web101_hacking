import urllib.parse
ascii = range(0,128)

print("RAW BYTES:")
for i in ascii:
    print(chr(i))

print("URL Encoded:")
for i in ascii:
    print(chr(i) + " = " + urllib.parse.quote(chr(i), safe=""))
   

print("URL encoded as bytes")
for i in ascii:
    print(str(bytes(chr(i), "ascii")) + " = " + urllib.parse.quote(chr(i), safe=""))
    