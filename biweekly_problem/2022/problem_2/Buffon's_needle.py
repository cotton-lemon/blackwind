from math import sin,pi
from random import random

def needle():
    while True:
        while True:
            try:
                t=input('Length of a needle:')
                if t.isdigit():
                    l=int(t)
                else:
                    l=float(t)
                if l>0:
                    break
                raise Valueerror
            except:
                print('Wrong value!')
        while True:
            try:
                t=input('Distance of lines:')
                if t.isdigit():
                    d=int(t)
                else:
                    d=float(t)
                if d>0:
                    break
                raise Valueerror
            except:
                print('Wrong value!')
        if l>d:
            print('Lenth of a needle must not longer than distance of lines')
        else:
            break
    while True:
        t=input("number of simulation:")
        if t.isdigit():
            n=int(t)
            if n>0:
                break
        print('Wrong value!')
    calculated=(2*l)/(d*pi)
    ans=sum(random()*d+sin(random()*pi)*l>=d for i in range(n))
    if ans==0:
        print('Not a single needle acrossed the line')
        return
    simulated_ratio=ans/n
    simulated_pi=2*l/simulated_ratio/d
    print(f'{n} time simulated, {ans} needles acrossed the line')
    print(f'simulated ratio: {simulated_ratio:.4f}, calculated ratio:{calculated:.4f},relative error:{1-(simulated_ratio/calculated):.4f}')
    print(f'simulated pi: {simulated_pi:.4f}, relative error:{1-(simulated_pi/pi):.4f}')
    
if __name__ == "__main__":
    needle()
    input()
