
dict1={'2300':'Turnhout','2340': 'beerse','6500': 'janville', '4588': 'JosVille', '5814': 'vevoTown',}

# string comparrison...
        
def searcher(postalcodes):
    for p_code in postalcodes:
        city = postalcodes[p_code]
        if '1' in p_code: 
            print('{} - {}'.format(p_code, city ))
           
searcher(dict1)
 