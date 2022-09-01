f = open("postalcodes\static\postalcodes.txt")

post_list_raw = f.readlines()


def make_list(post_list):
   
    list1= []
    for line in post_list:
        s=[]
        remove_tab =line.replace("\t", ",")
        remove_newline=remove_tab.replace("\n", "")
        remove_newline=remove_newline.split(",")
        
        s.append(remove_newline)
        list1.append(s)

    list2= []
    for code in range(len(list1)):
        postcode = list1[code][0][0]
        list2.append(postcode)
       
    # list1 = list of lists
    # list2 = list of postalcodes 
    return list2, list1        

list2, list1 = make_list(post_list_raw)

def matching(postcode, list2):

    list3 =[]
    for j in list2: 
        count = 0
        
        for i in j:
            if i in postcode:
                count +=1
            if i not in postcode:
                break
            if count ==3:
                list3.append(j)
    list3.sort()
    # list3 = list met postcodes
    return list3            
                    
list3 = matching('2800',list2)

l = [3,3,3,3,3,5,8,7,9,9]

def checker(list3):
           
    listA= list3
    listB = listA[:]
    listA.insert(0, None)
    listB.append(None)
    listC=[]
    listD=[]
    
    for index in range(len(listA)):
        if listA[index] != listB[index]:
            listC.append(listA[index])

        if listA[index] == listB[index]:
            listD.append(listA[index])
        
    print(listD)
    print(listC)
    
    
             
checker(l)            
        

def print_result(list1, list3):
    
    for code2 in list3:
        citylist = []
        
        for item in range(len(list1)):
            
            
            comparelist = []            # de huidige postcode uit alle postcodes

            code = list1[item][0][0]
                   
            city = list1[item][0][1]        
            
            # elke postcode komt in comparelist te staan 
            comparelist.append(code)
            
            # de postodes die we willen worden vergeleken met alle postcodes

            if code2 == comparelist[0]:
                citylist.append(city)

                
                
    #print(citylist)
    
        
              
print_result(list1, list3)                

