# for <var> in <sequence>:
      #<do something>
'''
for i in range(0,11):
    print(i)
'''

nums_list = list(range(0,120,7))
print(nums_list)

for i in nums_list:
    if i % 2 == 0 and i != 0 :
        print(i) 
