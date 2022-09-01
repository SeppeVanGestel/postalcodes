from unicodedata import name
import csv
# steek alles in een dictionary ...



def read_postal():
    with open("postalcodes\static\postalcodes.txt", 'r', encoding='latin-1')as file:
        with open('out.csv', 'w') as output:
                for line in file:
                    stripped=line.strip() # zet elke lijn apart               
                    line=stripped.split(',')
                    writer= csv.writer(output)
                    writer.writerow(line)

       
        
        

            
        
        
# make a csv ...
        

sample_str = 'seppe'            
first_chars = sample_str[0:3]

print(first_chars)


if __name__ == "__main__":
    read_postal()
    