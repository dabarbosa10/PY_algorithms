dict_capt={"Madrid": 'Spain', "Lisboa": 'Portugal', "Bogotá":'Colombia'}
#print(dict_capt)
#print(dict_capt['Bogotá'])
#Triying to access a key that is not in the dictionary:
#print(dict_capt.get('Prague'))

nums=[2,4,9,6,5]
mp={}
for i in range(len(nums)):
    mp[i]=nums[i]
#print(mp[0])
print(mp.keys())