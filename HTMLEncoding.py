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
print(a.encode('latin-1', 'xmlcharrefreplace'))
print(a.encode('utf-8', 'xmlcharrefreplace'))
a= '这'
print(a.encode('latin-1', 'xmlcharrefreplace'))
print(a.encode('utf-8', 'xmlcharrefreplace'))

b = '&#00e8;&#00bf;&#0099;'
print(escape('这'))
print(unescape(b))
print(escape(a.encode('utf-8','xmlcharrefreplace')))
