from html import escape, unescape
ascii = range(0,128)
iso8858_1 = range(0,256)

print("HTML Escaping (done the wrong way.)")
for i in ascii:
    print(str(bytes(chr(i), "UTF-8")) + " = " + escape(chr(i)))

print("BETTER:")
a = u"äöüßáà"    
print(a)
print(a.encode('ascii', 'xmlcharrefreplace'))