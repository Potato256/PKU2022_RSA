from zmq import NULL
import time
from gmpy2 import iroot, mpz, divm, powmod, gcd, t_div, div
from gmpy2 import mpz_random, t_mod
import gmpy2
# gmpy2 speeded up my program by 100 times, gmpy2 is my god   

class Encoder():
  def __init__(self, p, q, m, e):
    self.p = mpz(p)
    self.q = mpz(q)
    self.d = (self.p - 1) * (self.q - 1)
    self.m = mpz(m)
    self.n = self.p * self.q
    self.e = mpz(e)
    self.c = powmod(self.m, self.e, self.n)

class Decoder():
  def __init__(self, rsa, fileInfos=True, timeInfos=True):
    self.n = mpz(rsa.n)
    self.e = mpz(rsa.e)
    self.c = mpz(rsa.c)
    self.p = mpz(0)
    self.q = mpz(0)
    self.d = mpz(0)
    self.m = mpz(0)
    self.rs = gmpy2.random_state()
    self.fileInfos = fileInfos
    self.timeInfos = timeInfos

    if fileInfos:
      print(f"n : {self.n}")
      print(f"n.bit_length : {self.n.bit_length()}")
      print()
      print(f"e : {self.e}")
      print(f"e.bit_length : {self.e.bit_length()}")
      print()
      print(f"c : {self.c}")
      print(f"c.bit_length : {self.c.bit_length()}")
      print()
  
  def pq2d(self):
    if self.p==0 or self.q==0 :
      print("p and q unknown!")
      return
    phi_p = (self.p - 1) * (self.q - 1)
    return divm(1, self.e, phi_p)

  def pq_decode(self):
    '''We already have p,q,n,e,c and we want d and m'''
    if self.p==0 or self.q==0 :
      print("p and q unknown!")
      return
    self.d = self.pq2d()
    self.m = powmod(self.c, self.d, self.n)
    return self.m

  def m_decode(self):
    '''We already know n,e,c,m and we want p,q,d'''
    '''------------That's impossible------------'''
    return NULL

  def Naive_Decoder(self):
    '''It's useless'''
    while(1):
      remainder = t_mod(self.n, p)
      if remainder == 0:
        print(p)
        break
      p += 2

  def Fermat_Decoder(self):
    '''Try to a,b such that n=(a+b)(a-b)'''
    a = iroot(self.n, 2)[0]
    b = 0
    find = False
    time0 = time.time()
    time_sum = 0
    loop_cnt = 0
    while (not find):
      loop_cnt += 1
      b_2 = self.n - a * a
      b_tuple = iroot(b_2, 2)
      b = b_tuple[0]
      if (b_tuple[1]):
        find = True
        break 
      a = a - 1
      if self.timeInfos:
        time1 = time.time()
        if (time1 - time0 > time_sum):
          print(f"Time spent : {time_sum}")
          print(f"Loop_cnt : {loop_cnt}")
          print(f"cnt.bit_length : {mpz(loop_cnt).bit_length()}")
          time_sum += 5
    print("Success!")
    print(f"p = {hex(a)}")
    print(f"q = {hex(b)}")
    self.p = a
    self.q = b

  def Simple_Low_Encryption_Decoder(self):
    k = 0
    time0 = time.time()
    time_sum = 0
    res = 0
    while 1:
      res = iroot(self.c + k * self.n, self.e)
      if res[1]:
        break
      k += 1
      if self.timeInfos:
        time1 = time.time()
        if (time1 - time0 > time_sum):
          print(f"Time spent : {time_sum}")
          print(f"Current k : {k}")
          print(f"Current k.bit_length : {k.bit_length()}")
          time_sum += 10
    print("Success!")
    print(f"m = {res[0]}")
    self.m = res[0]

  def E3_Low_Encryption_Decoder(self):
    return NULL

  def E5_Low_Encryption_Decoder(self):
    return NULL

  def Wiener_Decoder(self):
    return NULL

  def Pollard_rho_Decoder(self):
    def f(x, a):
      return t_mod(x * x + a, self.n)
    time0 = time.time()
    time_sum = mpz(0)
    cnt = mpz(0)
    while time_sum < 60:
      a = mpz_random(self.rs, self.n)
      slow = f(0, a)
      fast = f(f(0, a), a)
      t = 1
      while slow != fast and time_sum < 60:
        if slow < fast:
          delta = fast - slow
        else:
          delta = slow - fast
        t = t_mod(t * delta, self.n)
        slow = f(slow, a)
        fast = f(f(fast, a), a)
        if (t_mod(cnt, mpz(0x10000))==0) or (slow==fast):
          p = gcd(t, self.n)
          if p > 1:
            self.p = p
            self.q = t_div(self.n, p)  
            print("Success!")
            print(f"p : {self.p}")
            print(f"q : {self.q}")
            return True
          if self.timeInfos:
            time1 = time.time()
            if (time1 - time0 > time_sum):
              print(f"Time spent : {time_sum}")
              print(f"Current cnt : 0x{cnt.digits(16)}")
              print(f"Current cnt.bit_length : {cnt.bit_length()}")
              time_sum += 10
        cnt += 1     
    print("Fail to factorize n")
    return False


  def Pollard_p_1_Decoder(self):
    bound1 = mpz(0x100000)
    bound2 = mpz(0x10000)
    cnt = mpz(2)
    a = mpz(2)
    time0 = time.time()
    time_sum = 0
    while cnt <= bound2:
      a = powmod(a, cnt, self.n)
      cnt += 1
      # if self.timeInfos:
      #   time1 = time.time()
      #   if (time1 - time0 > time_sum):
      #     print(f"Time spent : {time_sum}")
      #     print(f"Current cnt : {cnt}")
      #     print(f"Current cnt.bit_length : {cnt.bit_length()}")
      #     time_sum += 10
    p = 0
    while cnt <= bound1:
      a = powmod(a, cnt, self.n)
      p = gcd(a-1, self.n)
      if 1 < p :
        self.p = p
        break
      cnt += 1
      # if self.timeInfos:
      #   time1 = time.time()
      #   if (time1 - time0 > time_sum):
      #     print(f"Time spent : {time_sum}")
      #     print(f"Current cnt : {cnt}")
      #     print(f"Current cnt.bit_length : {cnt.bit_length()}")
      #     time_sum += 10
    if self.p == 0:
      print("Fail to factorize n")
      return False
    else:
      self.q = t_div(self.n, self.p)
      print("Success!")
      print(f"p : {self.p}")
      print(f"q : {self.q}")
      return True
    
    