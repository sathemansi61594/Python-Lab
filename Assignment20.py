#Write a Python program to get the key, value and item in a dictionary.
#input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dict_num ={1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
print("key" , "value")

#Use enumerate to loop through the dictionary values with a custom start value of 1
for(key,value) in enumerate(dict_num.values(), 1):
    print(key, ' ', value, ' ')


#Output
key value
1   10  
2   20  
3   30  
4   40  
5   50  
6   60  
    
    

    
  
   




