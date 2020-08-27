oriMessageP1 = "ai2.appinventor.mit.edu/"
oriMessageP2 = "galleryId=5520801296416768"

key = 14

decodedP1 = ""
decodedP2 = ""

for i in oriMessageP1:
   if i.isupper():
       value = ord(i)-int(key)
       i = chr(value)
       if not i.isupper():
            value = value-26
            i = chr(value)
   decodedP1 = decodedP1+i

for i in oriMessageP2:
   if i.isupper():
       value = ord(i)-int(key)
       i = chr(value)
       if not i.isupper():
            value = value-26
            i = chr(value)
   decodedP2 = decodedP2+i

print(decodedP1 + "?" + decodedP2)

#hvs hwqysh wg vwrrsb oacbu hvs odd





































#https://scratch.mit.edu/projects/420584105
