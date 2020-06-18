import sys
import re
import os
import runpy

v1 = [5,6,7,8,9,10]
v2 = [0.01, 0.02, 0.03, 0.04, 0.05, 0.10, 0.20, 0.50, 0.75, 0.9, 1.0]
v3 = [1, 2, 5, 10, 20, 50, 100]

print(len(v1),len(v2),len(v3))

l = m = n = 0
print('Reading File:')
with open('SocialFD.conf','r') as f:
    content = f.read()
for i in range(0,len(v1),1):
    for j in range(0,len(v2),1):
        for k in range(0,len(v3),1):
            repl = {'var1':str(v1[i]), 'var2':str(v2[j]), 'var3':str(v3[k])}
            print('Replacing params:')
            repl_pattern = re.compile(r'(' + '|'.join(repl.keys()) + r')')
            final_data = repl_pattern.sub(lambda x: repl[x.group()], content)
            #print(final_data)
            print('Writing file')
#            with open('SocialMF'+str(i)+str(j)+str(k)+'.conf','w') as new:
#                new.write(final_data)
            with open('../SocialFDparams/TwitterEgoWithT/SocialFD'+str(i)+str(j)+str(k)+'.conf','w') as new1:
                new1.write(final_data)
            l, m, n = i, j, k
            try:
                runpy.run_path('../main/main1.py', run_name='__main__')
                print('Execution success')
                print ('='*80)
            except Exception as exe:
                print(exe)
                print('Execution failed')
                print ('='*80)
            if i==len(v1)-1 and j==len(v2)-1 and k==len(v3)-1:
                exit(0)
exit(0)
