import matplotlib.pyplot as plt
import numpy as np

# Funções que geram as curvas para os 3 tipos de geradores, Fonte: Solucionário Fundamentos de Maquinas Eletricas, Chapman

class Gerador:
    def __init__(self, r_a=0.18,r_adj=0,r_adjlim=30,r_f=24,w=1800,Rload=0,IL=0,Vf=0):
        # if r_a <0 or r_adj<0 or r_adjlim<0 : raise ValueError('invalido')
        self.r_a= r_a
        self.r_adj=r_adj
        self.r_f= r_f
        self.w= w
        self.Rload= Rload
        self.IL= IL
        self.r_adjlim=r_adjlim
        self.Vf= Vf
        self.r_a= r_a
    @property
    def r_a(self):
        return self._r_a

    @r_a.setter
    def r_a(self, r_a):
        self._r_a=r_a



class Excind(Gerador):
    def __init__(self,r_a=1,r_adj=1,r_adjlim=None,r_f=1,w=1800,Rload=None,IL=None,Vf=1,Vb=None,i_f=None, Vt=None):
        super().__init__(r_a,r_adj,r_adjlim,r_f,w,Rload,IL,Vf)
        self.Vb=Vb
        self.r_f = self.r_f + self.r_adj
        self.i_f=self.Vf/self.r_f
    

    def simular(self):
        
        def curvamag(corrente):
            ea_values=[0,8,16,24,32,40,48,56,64,71.9000000000000,79.5000000000000,86.7000000000000,93.1000000000000,98.7000000000000,103.500000000000,107.460000000000,110.660000000000,113.460000000000,115.860000000000,117.960000000000,120,122,123.900000000000,125.700000000000,127.400000000000,128.980000000000,130.420000000000,131.740000000000,132.950000000000,134.150000000000,135.400000000000,136.650000000000,138,139.250000000000,140.500000000000,141.800000000000]
            if_values=[0,0.2000,    0.4000,    0.6000,    0.8000,    1.0000,    1.2000,    1.4000,    1.6000,    1.8000,    2.0000,    2.2000,    2.4000,    2.6000,    2.8000,    3.0000,    3.2000,    3.4000,    3.6000,    3.8000,    4.0000,    4.2000,    4.4000,    4.6000,    4.8000,    5.0000,    5.2000,    5.4000,    5.6000,    5.8000,    6.0000,    6.2000,    6.4000,    6.6000,    6.8000,    7.0000]
    
            return np.interp(corrente, if_values, ea_values)*self.w/1800

        EA=curvamag(self.i_f)
        IL=np.linspace(0,40,300)
        VT= EA-IL*self.r_a

        return IL, VT
 

class Serie(Gerador):
    def __init__(self,w=None,r_a=None,Rload=None,IL=None,Vt=None):
        super().__init__(r_a, w,Rload,IL )
        
    def simular(self):
        self.Vt=1.23
        self.IL=23
        return None
    
class Shunt(Gerador):
    def __init__(self,r_a=None,r_adj=None,r_adjlim=None,r_f=None,w=1800,Rload=None,IL=None,Vf=None,Vb=None,i_f=None, Vt=None):
        super().__init__(r_a,r_adj,r_adjlim,r_f,w,Rload,IL,Vf)
        self.Vb=Vb
        self.i_f=i_f

 
    def Simularshunt(self):
        ea_values=[0,8,16,24,32,40,48,56,64,71.9000000000000,79.5000000000000,86.7000000000000,93.1000000000000,98.7000000000000,103.500000000000,107.460000000000,110.660000000000,113.460000000000,115.860000000000,117.960000000000,120,122,123.900000000000,125.700000000000,127.400000000000,128.980000000000,130.420000000000,131.740000000000,132.950000000000,134.150000000000,135.400000000000,136.650000000000,138,139.250000000000,140.500000000000,141.800000000000];
        if_values=[0,0.2000,    0.4000,    0.6000,    0.8000,    1.0000,    1.2000,    1.4000,    1.6000,    1.8000,    2.0000,    2.2000,    2.4000,    2.6000,    2.8000,    3.0000,    3.2000,    3.4000,    3.6000,    3.8000,    4.0000,    4.2000,    4.4000,    4.6000,    4.8000,    5.0000,    5.2000,    5.4000,    5.6000,    5.8000,    6.0000,    6.2000,    6.4000,    6.6000,    6.8000,    7.0000];
        n_0 = 1800;
        # # First, initialize the values needed in this program.
        # r_f = 24; # # Field resistance (ohms)
        # r_adj = 10; # Adjustable resistance (ohms)
        # r_a = 0.19; # Armature + series resistance (ohms)
        
        # # First, initialize the values needed in this program.
        r_f = self.r_f; # # Field resistance (ohms)
        r_adj = self.r_adj; # Adjustable resistance (ohms)
        r_a = self.r_a; # Armature + series resistance (ohms)
        
        i_f = np.arange(0,6+0.02,0.02); # Field current (A)
        n = 1800; # Generator speed (r/min)
        # Calculate Ea versus If
        Ea = np.interp(i_f,if_values,ea_values) * self.w/n_0;
        
        # Calculate Vt versus If
        Vt = (r_f + r_adj) * i_f;

        # Find the point where the difference between the two
        # lines is 3.6 V. This will be the point where the line
        # line "Ea - Vt - 3.6" goes negative. That will be a
        # close enough estimate of Vt.
        diff = Ea - Vt - 3.6;
        # This code prevents us from reporting the first (unstable)
        # location satisfying the criterion.
        was_pos = 0;
        for ii in range(0,len(i_f)): # pode dar problema no indice 0 ou 1
            if diff[ii] > 0:
                    was_pos = 1;
                    
            if ( diff[ii] < 0 & was_pos == 1 ):
                break;
              
        return i_f, Vt, Ea


class Serie(Gerador):
    def __init__(self,w=1800,r_a=None,Rload=None,IL=None,Vt=None,r_s=None):
        super().__init__(r_a, w,Rload,IL )
        
        self.r_s=r_s
        
    def simularserie(self):
        ea_values=[0,8,16,24,32,40,48,56,64,71.9000000000000,79.5000000000000,86.7000000000000,93.1000000000000,98.7000000000000,103.500000000000,107.460000000000,110.660000000000,113.460000000000,115.860000000000,117.960000000000,120,122,123.900000000000,125.700000000000,127.400000000000,128.980000000000,130.420000000000,131.740000000000,132.950000000000,134.150000000000,135.400000000000,136.650000000000,138,139.250000000000,140.500000000000,141.800000000000];
        if_values=[0,0.2000,    0.4000,    0.6000,    0.8000,    1.0000,    1.2000,    1.4000,    1.6000,    1.8000,    2.0000,    2.2000,    2.4000,    2.6000,    2.8000,    3.0000,    3.2000,    3.4000,    3.6000,    3.8000,    4.0000,    4.2000,    4.4000,    4.6000,    4.8000,    5.0000,    5.2000,    5.4000,    5.6000,    5.8000,    6.0000,    6.2000,    6.4000,    6.6000,    6.8000,    7.0000];
        n_0 = 1800;

        r_adj = self.r_adj; # Adjustable resistance (ohms)
        r_s = self.r_a + r_adj; # Armature + series resistance (ohms)
        
        i_f = np.arange(0,6+0.02,0.02); # Field current (A) = IL

        # Calculate Ea versus If
        Ea = np.interp(i_f,if_values,ea_values) * self.w/n_0;
        # Calculate Vt versus If
        Vt = Ea-i_f*(r_s)

        return i_f, Vt, Ea
        



def main():
    
    # teste excind
    gerador= Excind(r_a=5,Vf=200, r_f=40)
    gerador.simular()
    
    #teste shunt
    geradorshunt= Shunt(r_f = 24, r_adj = 10,r_a = 0.19)
    geradorshunt.Simularshunt()
    print(geradorshunt)

    #teste gerador serie
    geradorserie= Serie(r_a=15, r_s=20)
    geradorserie.simularserie()
    
if __name__== '__main__' :main()
