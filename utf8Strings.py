import sys

print("The platform system default encoding is: " +  sys.getdefaultencoding()) 
input = u'''The chemical formula of water is H\u2082O. Water dissociates into H\u207A and OH\u207B'''
print( input )
print("Now using ascii:")
try:
    print( input.encode('ascii'))  
except UnicodeError as e:
    print(e)
 
print("Now using cp1251:") 
try:
    print( input.encode('cp1251'))  
except UnicodeError as e:
    print(e)
 
print("Now using iso2022_jp:") 
try:
    print( input.encode('iso2022_jp'))  
except UnicodeError as e:
    print(e)

print("Now using latin_1:")
try:
    print( input.encode('latin_1'))  
except UnicodeError as e:
    print(e)    
    
print("Now using utf_7:")   
try:
    print( input.encode('utf_7'))  
except UnicodeError as e:
    print(e)    
    
print("Now using utf_8:")   
try:
    print( input.encode('utf_8'))  
except UnicodeError as e:
    print(e) 
#Translating from utf-8 to a lower encoding is destructive.  
#https://docs.python.org/3.7/library/codecs.html#standard-encodings