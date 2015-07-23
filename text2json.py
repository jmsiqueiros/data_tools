##Example of text 2 jason at http://www.askyb.com/python/converting-tab-delimited-textfile-to-json/

import csv

# save the json output as emp.json 
jsfile = file('emp.json', 'w')
jsfile.write('[\r\n')

with open('employee.txt','r') as f:
    next(f) # skip headings
    reader=csv.reader(f,delimiter='\t')

    # get the total number of rows excluded the heading
    row_count = len(list(reader))
    ite = 0

    # back to first position
    f.seek(0)
    next(f) # skip headings
    
    for name,empid,dept in reader:

        ite+= 1
        
        jsfile.write('\t{\r\n')
        
        n = '\t\t\"name\": \"' + name + '\",\r\n'
        i = '\t\t\"empid\": \"' + empid + '\",\r\n'
        d = '\t\t\"department\": \"' + dept + '\"\r\n'
       
        jsfile.write(n)
        jsfile.write(i)
        jsfile.write(d)

        jsfile.write('\t}')

        # omit comma for last row item
        if ite < row_count:
            jsfile.write(',\r\n')

        jsfile.write('\r\n')

jsfile.write(']')
jsfile.close()

##For this data format
##Name	EmpId	Department
##John Smith	00383	Engineering
##Linda	00385	Finance
##Samuel	00387	Marketing
##Casey	00389	Management
##Albert	00390	Support
