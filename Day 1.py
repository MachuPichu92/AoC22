file = r'01.txt'

with open(file) as f:
    
        data = [line.strip() for line in f.readlines()]

groups = []
nums = []

for el in data:
    if el != '':
        nums.append(int(el))
    else:
        groups.append(sum(nums))
        nums=[]
     
        
# Answer 1
print(sorted(groups,reverse=True)[0])

# Answer 2
print(sum(sorted(groups,reverse=True)[:2]))
