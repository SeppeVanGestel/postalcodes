f = open("postalcodes\static\postalcodes.txt")

post_list_raw = f.readlines()




def make_list(post_list):
    """
    It takes a list of strings, splits them into a list of lists, and then creates a dictionary from the
    first element of each list as the key and the second element as the value
    
    :param post_list: a list of strings, each string is a line from the file
    """

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
       
    dict1={}   
    for item in range(len(l)):
        p_code =l[item][0][0]
        city =l[item][0][1]
        dict1[p_code] = city

    return dict1, l2, l        

dict1, l2, l = make_list(post_list_raw)




def matching(postcode, list2):
    """
    It takes a postcode and a list of postcodes and returns a list of postcodes that match the first 3
    digits of the postcode
    
    :param postcode: '2800'
    :param list2: a list of lists, each list containing 3 strings
    """
    
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
    print(list3)            
    return list3            
                    
list3 = matching('2800',l2)

def print_result(l, list3):
    """
    For each code2 in list3, for each item in the range of the length of l, if code2 is equal to code,
    print code2 and city
    
    :param l: list of tuples
    :param list3: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14',
    '15', '16', '17', '18', '19', '20',
    """
    for code2 in list3:
        for item in range(len(l)):
            code = l[item][0][0]
            city = l[item][0][1]

            if code2 == code:
                print(code2 + ' - ' + city)
print_result(l, list3)                

