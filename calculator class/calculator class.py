
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def division(self):
        return self.a/self.b

    def is_even_odd(self):
      if self.a % 2 ==0:
            return 'Even'
      else:
          return 'Odd'

calculations=Calculator(1,2)

print(calculations.add())
print(calculations.subtract())
print(calculations.division())
print(calculations.multiply())
print(calculations.is_even_odd())

