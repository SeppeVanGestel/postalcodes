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

    
    l2= []
    for code in range(len(l)):
        postcode = l[code][0][0]
        l2.append(postcode)
    #print(l2)    



    dict1={}   
    for item in range(len(l)):
        p_code =l[item][0][0]
        city =l[item][0][1]
        dict1[p_code] = city
    return dict1        

dict1 = make_dict(post_list_raw)

# kijk of caharacters van de inputpostcodes in de postcode zitten en returned dit in dict2

def matching(postcode, dictionary):
    dict2={}
    
    for city in dictionary:
        count = 0
        for j in city:
            if j in postcode:
                count +=1
            if j not in postcode:
                break
            if count ==4:
                dict2[city]=dictionary[city]
    return dict2            
                    
dict2 = matching('2800',dict1)

# sort postcode by value in list

def sort(dictionary):
    list1=[]
    list2=[]

    for code in dictionary:
        code = int(code)
        list1.append(code)  
    list1.sort()

    
    for int2 in list1:
        code = str(int2)
        list2.append(code)

    #print(list2)
    return list2

list2=sort(dict2)

# check for citys with the same postalcodes => check with list for multiple keys

def check_values():
    pass

# zoek met de values uit de list de values van de ditionary en print het resultaat

def print_result(inputdict, codelist):
    
        for pc in codelist:
            city = inputdict[pc]
            print('{} - {}'.format(pc, city ))
        
print_result(dict1,list2)


    



