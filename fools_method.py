from distutils.log import info
from decoder import Decoder
from gmpy2 import iroot, mpz, divm, powmod

class rsaFile():
  def __init__(self, str):
    self.n = int(str[:256], 16)
    self.e = int(str[256:512], 16)
    self.c = int(str[512:768], 16)

if __name__ == '__main__':

  str = 'Albert E'
  str_i = ''
  for i in range(0,8):
    str_i += hex(ord(str[i]))[-2:]
  # print(str_i)
  #str_i = '20224c6f67696320'
  m = '9876543210abcdef000000040000000000000000000000000000000000000000000000000000000000000000000000000000000000000000' + str_i
  print(m)
  m = int(m, 16)
  
  for i in range(0,21):
    targetFile = f'data{i}'
    
    targetStr = ''
    with open('targets/' + targetFile, 'r') as file:
      targetStr = file.read()
    
    rsa = rsaFile(targetStr)
    d = Decoder(rsa, infos=False)
    d.m = mpz(m)
    if (powmod(d.m, d.e, d.n) == d.c):
      print(i)


  # 8
  # str = 'will get'
  # str_i = '77696C6C20676574'
  # m = '9876543210abcdef000000080000000000000000000000000000000000000000000000000000000000000000000000000000000000000000' + str_i

  # 12
  # str = ' "Logic '
  # str_i = '20224c6f67696320'
  # m = '9876543210abcdef000000070000000000000000000000000000000000000000000000000000000000000000000000000000000000000000' + str_i
  
