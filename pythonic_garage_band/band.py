
class Musician:

 def __init__(self,name):
  self.name=name

class Guitarist(Musician):
   
    def __str__(self):
     return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    def play_solo(self):
        return "face melting guitar solo"
    def get_instrument(self):
        return 'guitar'


class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    def play_solo(self):
        return "bom bom buh bom"
    def get_instrument(self):
        return 'bass'


class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    def play_solo(self):
        return "rattle boom crash"
    def get_instrument(self):
        return 'drums'


class Band:
    instances=[]
    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.instances+=[self]
    def __str__(self):
        return f'WE ARE THE {self.name.upper()}'
    def __repr__(self):
        return f'WE ARE THE {self.name.upper()}'
    def play_solos(self):
        solos=[]
        for m in self.members:
            solos+=[m.play_solo()]
        return solos
    def to_list():
        return Band.instances
        
