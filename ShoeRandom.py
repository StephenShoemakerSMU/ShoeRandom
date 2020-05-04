from random import random
from random import seed
import math
import hashlib
class ShoeRandom:
    def __init__(self,seed=random()):
        self.seed=seed

    def getSeed(self):
        return self.seed

    def setSeed(self,seed):
        self.seed = seed
    
class ShoeRandomInPlace:
    def __init__(self,seed=random()):
        
        self.seed = seed
    
    def getSeed(self):
        return self.seed

    def setSeed(self,seed):
        self.seed = seed

    def getSeedLocation(self,num):
        
        
        seed = hashlib.sha256()
        
            
        seed.update(num.to_bytes(24,'big'))
            
            
        
        return int.from_bytes(seed.digest(),'big')

class ShoeStandardRandom:
    def __init__(self,seed=random()):
       
        
        self.seed = seed
    
    def getSeed(self):
        return self.seed

    def setSeed(self,seed):
        self.seed = seed
    
    
    def getSeedLocation(self,num):
        
        seed(self.seed)
        for x in range(num):
            random()
        return random()

       
        
    

    