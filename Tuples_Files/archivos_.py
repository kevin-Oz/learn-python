'''
output = open(r'C:\spam', 'w') Create output file ( 'w' means write)
input = open('data', 'r') Create input file ( 'r' means read)
input = open('data') Same as prior line ( 'r' is the default)
aString = input.read() Read entire file into a single string
aString = input.read(N) Read up to next N characters (or bytes) into a string
aString = input.readline() Read next line (including \n newline) into a string
aList = input.readlines() Read entire file into list of line strings (with \n )
output.write(aString) Write a string of characters (or bytes) into file
output.writelines(aList) Write all line strings in a list into file
 output.close() Manual close (done for you when file is collected)
output.flush() Flush output buffer to disk without closing
anyFile.seek(N) Change file position to offset N for next operation
for line in open('data'): use line File iterators read line by line
open('f.txt', encoding='latin-1') Python 3.0 Unicode text files ( str strings)
open('f.bin', 'rb') Python 3.0 binary bytes files ( bytes strings)
'''
#abrir archivo vacio nuevo
file1 = open('data.txt', 'w')
file1.write('hola desde python\n')
file1.write('por que este mundo es cruel \n')
file1.close()
# leyendo contenido
    #file1 = open('data.txt')
    #print(file1.readline())
print(open('data.txt').read())
#
for line in open('data.txt'):
    print(line, end='')
#
text = 'spamer'
file2 = open('datafile.txt', 'w')
file2.write(text)
file2.close()
print(open('datafile.txt').read())
#
file3 = open('numbers.txt', 'w')
file3.write('1 2 3 4 5 6 7 8 9 10\n11 12 13 14 15\n16 17 18 19\n20 21\n22')
file3.close()
print(open('numbers.txt').read())




