from decoder import Decoder
import time
import math
import sys

class rsaFile():
  def __init__(self, str):
    self.n = int(str[:256], 16)
    self.e = int(str[256:512], 16)
    self.c = int(str[512:768], 16)

targetFile = 'data0'
if (len(sys.argv) > 2):
  print("Too much arguments!")
  exit(0)
elif (len(sys.argv) == 2):
  targetFile = sys.argv[1]

targetStr = ''
with open('targets/' + targetFile, 'r') as file:
  targetStr = file.read()

rsa = rsaFile(targetStr)
print("Current File : <" + targetFile + ">")
d = Decoder(rsa, fileInfos=False, timeInfos=1)

# exit(0)

if d.Pollard_rho_Decoder():
  d.pq_decode()
  
  with open("decoded/" + targetFile + '.txt', 'w') as file:
    file.write('----------------------------------------------------------------\n')
    file.write('|                      File Name : ' + targetFile +'                       |\n')
    file.write('----------------------------------------------------------------\n\n')
    file.write("n : " + d.n.digits(16) + '\n\n')
    file.write("e : " + d.e.digits(16) + '\n\n')
    file.write("c : " + d.c.digits(16) + '\n\n')
    file.write("p : " + d.p.digits(16) + '\n\n')
    file.write("q : " + d.q.digits(16) + '\n\n')
    file.write("d : " + d.d.digits(16) + '\n\n')
    file.write("m : " + d.m.digits(16) + '\n\n')
    s = d.m.digits(16)
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
