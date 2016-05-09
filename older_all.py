import csv, mechanize, urllib2
from bs4 import BeautifulSoup

output = open('output3.csv', 'w')
writer = csv.writer(output)
writer.writerow(['Incident ID', 'Date Reported', 'Date Incident', 'County', 'TwnRngSec', 'Well Name', 'Oil Volume', 'Oil Units', 'SW Volume', 'SW Units', 'Other Volume', 'Other Units', 'Other Contaminant', 'Contained'])

br = mechanize.Browser()
br.open('http://www.ndhealth.gov/ehs/foia/spills/defaultOGArc.aspx')
#print br.response().read()

for i in range(1, 823):
    #print i

    br.select_form(nr=0)
    
    br.form['TextBoxPageIndex'] = str(i)  
    br.submit('ButtonGotoPage')

    html = br.response().read()
    #print html

    #use beautifulSoup to parse the HTML
    soup = BeautifulSoup(html, "html.parser")

    #select the table
    table = soup.find('table',
        {'id': 'GridView1'} 
    )
    #print table

    #grab stuff in table cells
    for row in table.find_all('tr'):
        #print row
        data = [cell.text.encode('utf-8') for cell in row.find_all('td')]
        #print data

        writer.writerow(data)
