##Example of text 2 jason at http://www.askyb.com/python/converting-tab-delimited-textfile-to-json/

import csv

# save the json output as emp.json 
jsfile = file('salud_ti.json', 'w')
jsfile.write('[\r\n')

with open('salud_MX_ti.csv','r') as f:
    next(f) # skip headings
    #reader=csv.reader(f,delimiter='\t')
    reader=csv.reader(f,delimiter='|')

    # get the total number of rows excluded the heading
    row_count = len(list(reader))
    ite = 0

    # back to first position
    f.seek(0)
    next(f) # skip headings
    
    for UT,TI in reader:

        ite+= 1
        
        jsfile.write('\t{\r\n')
        
        u = '\t\t\"UT\": \"' + UT + '\",\r\n'
        t = '\t\t\"TI\": \"' + TI + '\",\r\n'
        #d = '\t\t\"department\": \"' + dept + '\"\r\n'
       
        jsfile.write(u)
        jsfile.write(t)
        #jsfile.write(d)

        jsfile.write('\t}')

        # omit comma for last row item
        if ite < row_count:
            jsfile.write(',\r\n')

        jsfile.write('\r\n')

jsfile.write(']')
jsfile.close()

# For this data format
# Name	EmpId	Department
# John Smith	00383	Engineering
# Linda	00385	Finance
# Samuel	00387	Marketing
# Casey	00389	Management
# Albert	00390	Support
