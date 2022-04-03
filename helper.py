class fast_power:
  def __init__(self, m_, e_, n_):
    self.m = m_
    self.e = e_
    self.n = n_
    tmp = m_    
    a = 1
    self.list_m = [tmp]
    self.list_e = [a]
    while (a < e_):
      tmp = tmp * tmp % n_
      a = a + a
      self.list_m.append(tmp)
      self.list_e.append(a)

  def log_2(self, x):
    a = 0
    while (x > 1):
      x = x >> 1
      a = a + 1
    return a
    
  def cal(self):
    ans = 1
    e = self.e
    while (e > 0):
      tmp = self.log_2(e)
      ans = ans * self.list_m[tmp] % self.n
      e -= self.list_e[tmp]
    return ans

def int_sqrt(n):
  '''Newton Method - O(log(n))'''
  k1 = 0
  k2 = 1
  while (k1 != k2):
    k1 = k2
    k2 = (k1 + (n // k1)) >> 1
  return k2