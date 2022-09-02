f = open("postalcodes\static\postalcodes.txt")

post_list_raw = f.readlines()




def make_list(post_list):
    
    city_code= []
    for line in post_list:
        
        remove_tab =line.replace("\t", ",")
        remove_newline=remove_tab.replace("\n", "")
        citylist=remove_newline.split(",")
        
        city_code.append(citylist)   

    return city_code        

city_code = make_list(post_list_raw)




def matching(postcode, cityCode):
   
    final_matches = []

    for citys in cityCode: 
        
        #print(citys)
        code = citys[0]
        city = citys[1]
        matched_list = []
        
        count = 0
        
        for number in code:
            #print(number)

            if number in postcode:
                #print(number + 'in inputcode')
                count +=1
                if number not in postcode:
                    break
            if count ==4:
                matched_list.append(code)
                matched_list.append(city)
                #print(matched_list)
                final_matches.append(matched_list)
    
    final_matches.sort()
    return final_matches           
                    
final_matches = matching('2800', city_code)




def sort_result(all_matches):
    #print(all_matches)
   
    seen = []
    originals = []
    duplicates = []
    
    for match in all_matches:
        code = match[0]
        city = match[1]
    
        if code in seen:
            duplicates.append(match)
                   
        else:
            seen.append(code)
            originals.append(match)
    
    #print('seen:')
    #print(seen)
    print('')
    print('duplicates:')
    print(duplicates)
    print('')
    print('originals:')
    print(originals)

    return seen , duplicates
        
    
seen, duplicates = sort_result(final_matches)              

