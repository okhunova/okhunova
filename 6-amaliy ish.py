text = "man maktabga bugun bormadim"
print(text)
new_text = ''
search = input("qaysi belgini ikkilantirilsin\n>>>")
for n in text:
    if n==search:
        new_text+=n*2
    else:
        new_text+=n
print(new_text)

u = 0
for m in text:
    if m.upper()=="A" or m.upper()=="O" or m.upper()=="U" or m.upper()=="I" or m.upper()=="E" or m.upper()=="O'":
        u+=1
print(u,"ta unli xarf bor ekan")