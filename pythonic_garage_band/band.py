
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
    to_list=[]
    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.to_list+=[self]
    def play_solos(self):
        return [Guitarist(self.members[0]).play_solo(),Bassist(self.members[1]).play_solo(),Drummer(self.members[2]).play_solo()]

        