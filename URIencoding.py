import urllib.parse
ascii = range(0,128)
twoFiftySix = range(0,256)


print("RAW BYTES:")
for i in ascii:
    print(chr(i))

print("percent Encoded:")
for i in ascii:
    print(chr(i) + " = " + urllib.parse.quote(chr(i), safe=""))
   

print("percent encoded as bytes")
for i in ascii:
    print(str(bytes(chr(i), "ascii")) + " = " + urllib.parse.quote(chr(i), safe=""))
    
    
print("Latin-1 URI encoding.")

print("percent encoded as Latin-1 bytes")
for i in twoFiftySix:
    print(str(bytes(chr(i), "Latin-1")) + " = " + urllib.parse.quote(chr(i), safe=""))
   

print("percent encoded as UTF-8 bytes")
utf8 = str(bytes(chr(180), "utf-8"))
latin = str(bytes(chr(180), "Latin-1"))
print("char 180, [" + chr(180) + "]") 
print(latin)
print(utf8)


   
