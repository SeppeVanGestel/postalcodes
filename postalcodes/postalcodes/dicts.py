f = open("postalcodes\static\postalcodes.txt")

post_list_raw = f.readlines()




def make_dict(post_list):
    """
    It takes a list of strings, splits each string into a list of strings, and then creates a dictionary
    where the first item in each list is the key and the second item is the value
    
    :param post_list: a list of strings, each string is a line from the file
    :return: A dictionary with the postcode as the key and the city as the value.
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
    return dict1        

dict1 = make_dict(post_list_raw)




def matching(postcode, dictionary):
    """
    For each city in the dictionary, if the first four characters of the city name are in the postcode,
    add the city name and the corresponding value to a new dictionary
    
    :param postcode: a string of the postcode
    :param dictionary: a dictionary of cities and their corresponding postcodes
    :return: A dictionary with the city as the key and the postcode as the value.
    """
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




def sort(dictionary):
    """
    It takes a dictionary as input, converts the keys to integers, sorts the integers, converts the
    integers back to strings, and returns a list of the sorted strings
    
    :param dictionary: a dictionary of the form {'code': 'name'}
    :return: A list of the keys in the dictionary in ascending order.
    """
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




def print_result(inputdict, codelist):
    """
    It takes a dictionary and a list as input, and prints the key-value pairs of the dictionary, where
    the key is in the list
    
    :param inputdict: a dictionary of postal codes and cities
    :param codelist: list of postal codes
    """
    
    for pc in codelist:
        city = inputdict[pc]
        print('{} - {}'.format(pc, city ))
        
print_result(dict1,list2)


    



