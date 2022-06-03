import time
import os

if __name__ == '__main__':
  cnt = 0
  while 1:
    if cnt%21 == 0:
      print('----------------------------------------------------------------')
      print(f"|                            loop {cnt//21}                            |")
      print('----------------------------------------------------------------')
    os.system(f'python ./decode.py data{cnt%21}')
    time.sleep(1)
    cnt += 1
    


