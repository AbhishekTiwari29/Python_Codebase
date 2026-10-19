from collections import Counter

song = """Khairiyat poochho, kabhi toh kaifiyat poochho
Tumhare bin deewane ka kya haal hai
Dil mera dekho, na meri haisiyat poochho
Tere bin ek din jaise sau saal hai
Anjaam hai tay mera
Hona tumhein hai mera
Jitni bhi hon dooriyaan, filhaal hain
Yeh dooriyaan filhaal hain
Oh, khairiyat poochho, kabhi toh kaifiyat poochho
Tumhare bin deewane ka kya haal hai
Dil mera dekho, na meri haisiyat poochho
Tere bin ek din jaise sau saal hai
Tumhari tasveer ke sahare mausam kayi guzaare
Mausami na samjho par ishq ko humare
Nazron ke saamne main aata nahin tumhare
Magar rehte ho har pal manzar mein tum humare
'Gar ishq se hai mila
Phir dard se kya gila?
Iss dard mein zindagi khushhaal hai
Yeh dooriyaan filhaal hain
Oh, khairiyat poochho, kabhi toh kaifiyat poochho
Tumhare bin deewane ka kya haal hai
Dil mera dekho, na meri haisiyat poochho
Tere bin ek din jaise sau saal hai
Anjaam hai tay mera
Hona tumhein hai mera
Jitni bhi hon dooriyaan, filhaal hain
Yeh dooriyaan filhaal hain"""

l1 = list(song.lower().split())

frequency = Counter(l1)

max_word = max(frequency, key=frequency.get)

print("Word:", max_word)
print("Frequency:", frequency[max_word])