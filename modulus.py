from decoder import Decoder
import sys
from gmpy2 import gcdext, powmod, t_mod

class rsaFile():
  def __init__(self, str):
    self.n = int(str[:256], 16)
    self.e = int(str[256:512], 16)
    self.c = int(str[512:768], 16)

targetFile1 = 'data11'
targetFile2 = 'data14'

if (len(sys.argv) > 3):
  print("Too much arguments!")
  exit(0)
elif (len(sys.argv) == 3):
  targetFile1 = sys.argv[1]
  targetFile2 = sys.argv[2]

targetStr1 = ''
targetStr2 = ''

with open('targets/' + targetFile1, 'r') as file:
  targetStr1 = file.read()
with open('targets/' + targetFile2, 'r') as file:
  targetStr2 = file.read()

rsa1 = rsaFile(targetStr1)
rsa2 = rsaFile(targetStr2)

d1 = Decoder(rsa1, fileInfos=1, timeInfos=1)
d2 = Decoder(rsa2, fileInfos=1, timeInfos=1)

t = gcdext(d1.e, d2.e)

a = powmod(d1.c, t[1], d1.n)
b = powmod(d2.c, t[2], d2.n)

d1.m = t_mod(a * b, d1.n)
d2.m = d1.m

with open("decoded/" + targetFile1 + '.txt', 'w') as file:
    file.write('----------------------------------------------------------------\n')
    file.write('|                      File Name : ' + targetFile1 +'                       |\n')
    file.write('----------------------------------------------------------------\n\n')
    file.write("n : " + d1.n.digits(16) + '\n\n')
    file.write("e : " + d1.e.digits(16) + '\n\n')
    file.write("c : " + d1.c.digits(16) + '\n\n')
    file.write("p : " + d1.p.digits(16) + '\n\n')
    file.write("q : " + d1.q.digits(16) + '\n\n')
    file.write("d : " + d1.d.digits(16) + '\n\n')
    file.write("m : " + d1.m.digits(16) + '\n\n')
    s = d1.m.digits(16)
    s = s[-16:]
    t = ""
    for i in range(1, 9):
        tmp = (chr(int(s[2*i-2:2*i], 16)))
        if tmp == ' ':
            t += '\ '
        else:
            t += tmp
    
    file.write("text : " + t + '\n\n')
    file.write('----------------------------------------------------------------')
with open("decoded/" + targetFile2 + '.txt', 'w') as file:
    file.write('----------------------------------------------------------------\n')
    file.write('|                      File Name : ' + targetFile2 +'                       |\n')
    file.write('----------------------------------------------------------------\n\n')
    file.write("n : " + d2.n.digits(16) + '\n\n')
    file.write("e : " + d2.e.digits(16) + '\n\n')
    file.write("c : " + d2.c.digits(16) + '\n\n')
    file.write("p : " + d2.p.digits(16) + '\n\n')
    file.write("q : " + d2.q.digits(16) + '\n\n')
    file.write("d : " + d2.d.digits(16) + '\n\n')
    file.write("m : " + d2.m.digits(16) + '\n\n')
    s = d2.m.digits(16)
    s = s[-16:]
    t = ""
    for i in range(1, 9):
        tmp = (chr(int(s[2*i-2:2*i], 16)))
        if tmp == ' ':
            t += '\ '
        else:
            t += tmp
    
    file.write("text : " + t + '\n\n')
    file.write('----------------------------------------------------------------')

exit(0) 