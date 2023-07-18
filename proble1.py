

from abc import ABC

class storage(ABC):
  def __init(self,name):
    self.name = name

  def save(self):
    pass

  def load(self):
    pass

  def delete(self):
    pass

class file_stor(storage):
    def __init__(self, name):
        super().__init__(name)

    def delete(self,value):
        with open(self.name , 'r') as f:
            st = f.read()

        st = st.split(" ")
        contet = [i for i in st if value != i]
        with open(self.name, 'w') as f:
            f.write(str(contet))

    def save(self,value):
        with open(self.name , "a") as f:
            f.write(value)

    def load(self):
        with open(self.name , "r") as f:
            return f.read()

a = Filestorage()

class data_store(storage):

    def __init__(self, name):
        super().__init__(name)
        self.db = []

    def load(self):
        return self.db

    def save(self,value):
        self.db.append(value)

    def delete(self,value):
        self.db.remove(value)
