import math

class Utils:
  def reversed(x) -> int:
    if type(x) != int:
      raise TypeError
    res = 0
    while x > 0:
      digit = x % 10
      x = x // 10
      res = res * 10 + digit
    
    return res

  def formatter(x) -> tuple[int, int]:
    if type(x) != int:
      raise TypeError
    
    base_2 = 0
    pow_2_temp = x
    for i in range(math.ceil(math.log2(x))):
      base_2 += (pow_2_temp & 1) * 10**i
      pow_2_temp = pow_2_temp >> 1

    base_8 = 0
    pow_8_temp = x
    for i in range(math.ceil(math.log2(x) / 3)):
      base_8 = base_8 + (pow_8_temp & 7) * 10**i 
      pow_8_temp = pow_8_temp >> 3
    
    return (base_2, base_8)
