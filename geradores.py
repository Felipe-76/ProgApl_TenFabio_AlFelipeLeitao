

class Gerador:
    def __init__(self, RA=0,Raj=0,Rajlim=0,RF=0,w=0,Rload=0,IL=0,Vf=0):
        # if RA <0 or Raj<0 or Rajlim<0 : raise ValueError('invalido')
        self.RA= RA
        self.Raj=Raj
        self.RF= RF
        self.w= w
        self.Rload= Rload
        self.IL= IL
        self.Rajlim=Rajlim
        self.Vf= Vf
        self.RA= RA
   
    def __str__(self):
         return f"{self.RA}, {self.Raj}"

    @property
    def RA(self):
        return self._RA

    @RA.setter
    def RA(self, RA):
        self._RA=RA



class Excind(Gerador):
    def __init__(self,RA=None,Raj=None,Rajlim=None,RF=None,w=None,Rload=None,IL=None,Vf=None,Vb=None,If=None, Vt=None):
        super().__init__(RA,Raj,Rajlim,RF,w,Rload,IL,Vf)
        self.Vb=Vb
        self.If=If
    

    def simular(self):
        
        Vt=1.23
        self.IL=21
        
        return(Vt, self.IL)
        ...

class Serie(Gerador):
    def __init__(self,w=None,RA=None,Rload=None,IL=None,Vt=None):
        super().__init__(RA, w,Rload,IL )
        
    def simular(self):
        self.Vt=1.23
        self.IL=23
        return None
    
class Shunt(Gerador):
    def __init__(self,RA=None,Raj=None,Rajlim=None,RF=None,w=None,Rload=None,IL=None,Vf=None,Vb=None,If=None, Vt=None):
        super().__init__(RA,Raj,Rajlim,RF,w,Rload,IL,Vf)
        self.Vb=Vb
        self.If=If
    

    def simular(self):
        
        Vt=1.23
        self.IL=21
        
        return(Vt, self.IL)
        ...
    


def main():
    gerador=Excind(RA=2,Raj=3)
    
    print(gerador.simular())
    
    
    
    
if __name__== '__main__' :main()