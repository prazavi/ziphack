import pyzipper
import random

def factoriel(a):
    f=1
    while(a>0):
        f*=a
        a-=1
    return f

def numround(i,n):
    return factoriel(n)/factoriel(n-i)

with pyzipper.AESZipFile('testzip.zip') as f:
    c=0
    passbits=['sean','12','lopez','lerox','mohamad']
    while(c==0):
        for i in range(len(passbits)):
            tried=[]
            if c==1:
                break
            while(len(tried)<numround(i+1,len(passbits))):
                passguess=''
                rands=[]
                j=0
                while(j<i+1):
                    d=random.randint(0,len(passbits)-1)
                    if d not in rands:
                        rands.append(d)
                        j+=1
                        passguess+=passbits[d]
                if passguess in tried:
                    continue
                else:
                    tried.append(passguess)
                    try:
                        f.pwd = bytes(passguess,'utf-8')
                        f.extractall(pwd=f.pwd)
                        print('the password was: %s'%passguess)
                        c=1
                        break
                    except RuntimeError:
                        continue
        if i>=len(passbits)-1 and c==0:
            print('password was not in passbits')
            break
    # file_content = f.read('testfile.txt')
