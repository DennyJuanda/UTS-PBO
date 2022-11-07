# looping python with range
for i in range(5):
    print(i)

#looping python with break
for i in range(2,22):
    print(i,' x ',i ,' = ',i*i)
    if i == 10:
        break

# looping python with continue
for i in range(2,22):
    if i == 10:
        continue
    print(i,' x ',i ,' = ',i*i)

# nested loop
listCity = ['Kalimantan', 'Jawa', 'Sulawesi']
listPlace = ['East', 'West', 'Central']
for city in listCity:
    for place in listPlace:
        print(city, place)



# contoh penambahan terkait break/continue
for val in "bahasa":
    if val == "h":
        continue
        #break
    print (val)
print ("selesai")