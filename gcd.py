from decoder import Decoder
import sys
from gmpy2 import gcd, t_div

class rsaFile():
  def __init__(self, str):
    self.n = int(str[:256], 16)
    self.e = int(str[256:512], 16)
    self.c = int(str[512:768], 16)

targetFile1 = 'data2'
targetFile2 = 'data19'

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

d1 = Decoder(rsa1, fileInfos=0, timeInfos=1)
d2 = Decoder(rsa2, fileInfos=0, timeInfos=1)

a = gcd(d1.n, d2.n)

if a != 1:
    d1.p = a
    d2.p = a
    d1.q = t_div(d1.n, d1.p)
    d2.q = t_div(d2.n, d2.p)
    d1.pq_decode()
    d2.pq_decode()

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
