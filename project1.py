

'project 1'
class Resource:
  def __init__(self,name,manufacturer,total=  10, allocated = 5):
    if total > allocated and isinstance(name,str) and isinstance(manufacturer,str):
      self.name = name
      self.manufacturer = manufacturer
      self._total =total
      self._allocated = allocated


  def __str__(self):
    return self.name

  def __repr__(self):
    l =  [self.name,self.manufacturer,self._total,self._allocated]
    return (f'Resource init arguments length {len(l)}')

  def claim(self,m):
    if m < self._total - self._allocated:
      self._allocated += m
    else:
      raise ValueError('take little bit resource')

  def freeup(self,p):
    self._allocated -= p
    self._total -= p


  def purchesd(self,p):
    if  p >0 and type(p) == int:
      self._total += p
    else:
      raise TypeError('the p must be int or zero ')

  def died(self,p):
    if p > 0 and type(p) == int and p < self.alloacted:
      self._total -= p
      self._allocated -= p
    raise ValueError('take argument lovcer then alloacted ')


  @property
  def Category(self):
      return self.__class__.__name__.lower()


  @property
  def total_elec(self):
    return self._total

  @property
  def allocated_elec(self):
    return self._allocated


class Storage(Resource):
  def __init__(self, name, manufacturer, total, allocated, capacity_GB):
      super().__init__(name, manufacturer, total, allocated)
      self.capacity_GB = capacity_GB

  @property
  def capacity_GB(self):
      return self._capacity_GB

  @capacity_GB.setter
  def capacity_GB(self,val_GB):
    self._capacity = val_GB

class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface):
      if capacity_GB > 0 and isinstance(capacity_GB,int):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self.__interface = interface
      else:
        raise TypeError('Capacity must be integer')

    @property
    def interface(self):
        return self.__interface



class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self.__size = size
        self.__rpm = rpm

    @property
    def Get(self):
      return self.size,self.__rpm

    @Get.setter
    def Get(self,tp):
      self.__size = tp[0],
      self.__rpm= tp[1]


class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores):
        super().__init__(name, manufacturer, total, allocated)
        self._cores = cores

    @property
    def cores(self):
        return self._cores

    @cores.setter
    def cores(self,new_count_cores):
      return new_count_cores

class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores):
        super().__init__(name, manufacturer, total, allocated)
        self.__cores = cores

    @property
    def cores(self):
        return self.__cores
