f = open("postalcodes\static\postalcodes.txt")

post_list_raw = f.readlines()

# post_list is een list, in lijst s gaan we de rommel er uit halen en alles in een dictionary zetten

def make_dict(post_list):

    l= []
    for line in post_list:
        s=[]
        remove_tab =line.replace("\t", ",")
        remove_newline=remove_tab.replace("\n", "")
        remove_newline=remove_newline.split(",")
        
        s.append(remove_newline)
        l.append(s)

    # maak postcodelist ... 
    
    l2= []
    for code in range(len(l)):
        postcode = l[code][0][0]
        l2.append(postcode)
       
    dict1={}   
    for item in range(len(l)):
        p_code =l[item][0][0]
        city =l[item][0][1]
        dict1[p_code] = city

    return dict1, l2, l        

dict1, l2, l = make_dict(post_list_raw)

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
    return list3            
                    
list3 = matching('2800',l2)


for code2 in list3:
    for item in range(len(l)):
        code = l[item][0][0]
        city = l[item][0][1]

        if code2 == code:
            print(code2 + ' - ' + city)

