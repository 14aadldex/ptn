arra = ['Kennedy', 'Eltcin', 'Pop']
print(arra)
#print(type(arra[0]))

index = arra.index('Pop')
who_absent = arra.pop(index)
print('he cant visit us - ' + str(who_absent) )
arra.insert(index,'Mike Jackson')
print(arra)

arra.insert(0,'dunkan mclaut')
arra.append('li Jonns')
print(arra)

arra.sort()
print(arra)

arra.sort(reverse=True)
print(arra)

print(sorted(arra))
print(arra)
print(len(arra))