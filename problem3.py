

'problem 3'
class Vehicles:
  def __init__(self,color,count_wheel,mark,year):
    self.year =year
    self.color = color
    self.count_wheel = count_wheel
    self.mark = mark

  def v_age(self):
    return f'{2023 - self.year} year old'

  def hors_pow(self):
    return (f'{2**self.count_wheel} hors power')

  def mass(self):
    return ' depends on type of vehcile'



class car(Vehicles):
  def __init__(self,color,count_wheel,mark,year,num_door,country):
    super().__init__(color,count_wheel,mark,year)
    self.num_door = num_door
    self.country  = country

  def Country(self):
    return (f'car makes in {self.country}')


class Motorcycle(Vehicles):
  def __init__(self,color,count_wheel,mark,year,num_passengers):
    super().__init__(color,count_wheel,mark,year)
    self.num_passengers = num_passengers

  def max_spped(self):
    return '250 km/h'


class Bicycle(Vehicles):
  def __init__(self,color,count_wheel,mark,year):
     super().__init__(color,count_wheel,mark,year)

  def year_waranty(self):
    return 'year warranty'


cars = [ Bicycle('red',2,'suzuki',2010), Motorcycle('black',2,'kizashi',2017,3)]
for i in cars:
  print(i.mass())
  print(i.v_age())

c = car('white',4,'BMW',2020,4,"german")
print(c.hors_pow())
print(c.Country())
