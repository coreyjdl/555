class Astable():
  '''Astable 555 timer circuit calculator. Input units are microfarads and Ohms. Output units are Hertz and seconds.'''
    
  def __init__(self, cap, r_one, r_two):
    self.cap = cap
    self.r_one = r_one
    self.r_two = r_two
    self.adj_cap = cap / 1000000
    
  def __str__(self):
    return f'Astable 555\nFrequency: {self.frequency():.2f} Hz\nTime: {self.time():.2f} sec\nDuty Cycle: {self.duty_cycle():.2f}%\nCapacitor: {self.cap:,} µF\nResistor 1 value: {self.r_one:,} Ω\nResistor 2 value: {self.r_two:,} Ω\n '
      
  def frequency(self):
    return 1.44 / ((self.r_one + (2 * self.r_two) ) * self.adj_cap)
        
  def time(self):
    return 1 / self.frequency()
    
  def high_time(self):
    return .69 * (self.r_one + self.r_two) * self.adj_cap
      
  def low_time(self):
    return .69 * self.r_two * self.adj_cap

  def mark_space(self):
    return self.high_time() / self.low_time()
      
  def duty_cycle(self):
    return (self.high_time() / self.time()) * 100

class Monostable():
  '''Monostable 555 timer circuit calculator. Input units are microfarads and Ohms. Output units are Hertz and seconds.'''

  def __init__(self, cap, r_one):
    self.cap = cap 
    self.r_one = r_one
  
  def __str__(self):
    return f'Monostable 555\nPulse Time: {self.time():.2f} sec\nResistor value: {self.r_one:,} Ω\nCapacitor value {self.cap:,} µF'
    
  def time(self):
    return 1.1 * self.r_one * ( self.cap / 1000000 )


# sample monostable
capacitor = 100 # ohms
resistor = 330 # microfarads
mono = Monostable(capacitor, resistor)
print(mono)

print()

# sample astable
capacitor = 100
resistor_one = 330
resistor_two = 330
astable = Astable(capacitor, resistor_one, resistor_two)
print(astable)
