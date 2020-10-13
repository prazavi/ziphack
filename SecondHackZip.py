import timeit

code_to_test="""
import pyzipper
def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 5)
        nums.append(str(r))
    return ''.join(reversed(nums))

with pyzipper.AESZipFile('numpasstest2.zip') as f:
    c=0
    while(c==0):
        for i in range(5**8,(5**9)+1):
            if c==1:
                break
            passguess=ternary(i)
            if '0' in passguess:
                continue
            print(passguess)
            try:
                f.pwd = bytes(passguess,'utf-8')
                f.extractall(pwd=f.pwd)
                print('the password was: %s'%passguess)
                c=1
                break
            except RuntimeError:
                continue
"""
print(timeit.timeit(code_to_test,number=1))
    # file_content = f.read('testfile.txt')
