#Write a Python script to concatenate the following dictionaries to create a new one.
#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}

dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50, 6:60}

dict4={}
for newdict in (dict1,dict2,dict3):
    dict4.update(newdict)
print(dict4)


#Output

{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}




