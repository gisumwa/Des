class PrimeChecker(object):
    def __init__(self,number=""):
        self.number = number
    def is_prime(self):
      try:
        self.number=int(self.number)
      except ValueError:
          return False
      if self.number == 2:
        return True
      if self.number < 2:
        return False
      for i in range(2,self.number):
        if self.number % i == 0:
            return False
      return True

CP=PrimeChecker('17')
print(CP.is_prime())