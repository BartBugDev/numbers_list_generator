

print( )
print( )
print( )
print('^^^^^^^^^^ Password List Generator ^^^^^^^^^^')
print( )
print( )

fileName = input("Type the name of your txt new file with password list: \n")

startNumber = input("Type first  number of password list: \n")
intStartNumber = int(startNumber)

lastNumber = input("Type last number of password list: \n")
intLastNumber = int(lastNumber)

fh = open(fileName, 'w')

for number in range (intStartNumber, intLastNumber) :
    stringNumber = str(number)
    fh.write(stringNumber)
    fh.write('\n')

fh.close()

