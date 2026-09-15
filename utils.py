class Utils:
  def reversed(x: int) -> int:
    res = 0
    while x > 0:
      digit = x % 10
      x = x // 10
      res = res * 10 + digit
    
    return res

  def formatter(x: int) -> (int, int):
    base_2 = 0
    pow_2_temp = x
    while pow_2_temp > 0:
      base_2 = base_2 * 10 + (pow_2_temp & 1)
      pow_2_temp = pow_2_temp >> 1

    base_8 = 0
    pow_8_temp = x
    while pow_8_temp > 0:
      base_8 = base_8 * 10 + (pow_8_temp & 0h7)
      pow_8_temp = pow_8_temp >> 3
    
    return (base_2, base_8)
