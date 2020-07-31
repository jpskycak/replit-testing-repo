import sys
sys.path.append('src')
#sys.path.append('home/runner/replittestingrepo/src')
#print(sys.path)
import os
print(os.listdir("src"))
from ClassA import ClassA

class_a = ClassA()
#from .src.ClassA import ClassA