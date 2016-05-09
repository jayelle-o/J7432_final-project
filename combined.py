import csv, mechanize, urllib2
from bs4 import BeautifulSoup

output = open('output.csv', 'w')
writer = csv.writer(output)
writer.writerow(['Incident ID', 'Date Reported', 'Date Incident', 'County', 'TwnRngSec', 'Well Name', 'Oil Volume', 'Oil Units', 'SW Volume', 'SW Units', 'Other Volume', 'Other Units', 'Other Contaminant', 'Contained'])


#scrape the newer, contained oilfield incidents
br = mechanize.Browser()
br.open('http://www.ndhealth.gov/ehs/foia/spills/defaultOGContained.aspx')
#print br.response().read()

html = br.response().read()
soup = BeautifulSoup(html, "html.parser")

#automate range from website info
number = soup.find("span", id = "LabelPageCount")
# print number.text
x = int(number.text) + 1
# print x

for i in range(1, int(x)):
    # print i

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
        data = [cell.text.encode('utf-8').strip() for cell in row.find_all('td')]
        #print data

        if len(data) > 0:    
            writer.writerow(data)
            #print data

print "finished writing newer, contained oilfield incidents" 

#now scrape the newer, not contained oilfield incidents
br = mechanize.Browser()
br.open('http://www.ndhealth.gov/ehs/foia/spills/defaultOGNotContained.aspx')
#print br.response().read()

html = br.response().read()
soup = BeautifulSoup(html, "html.parser")

#automate range from website info
number = soup.find("span", id = "LabelPageCount")
# print number.text
x = int(number.text) + 1
# print x

for i in range(1, int(x)):
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
        data = [cell.text.encode('utf-8').strip() for cell in row.find_all('td')]
        #print data

        if len(data) > 0:
            writer.writerow(data)

print "finished writing newer, not contained oilfield incidents"

#now scrape the older oilfield incidents:
br = mechanize.Browser()
br.open('http://www.ndhealth.gov/ehs/foia/spills/defaultOGArc.aspx')
#print br.response().read()

html = br.response().read()
soup = BeautifulSoup(html, "html.parser")

#automate range from website info
number = soup.find("span", id = "LabelPageCount")
# print number.text
x = int(number.text) + 1
# print x

for i in range(1, int(x)):
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
        data = [cell.text.encode('utf-8').strip() for cell in row.find_all('td')]
        #print data

        if len(data) >0:
            writer.writerow(data)

print "finished writing older oilfield incidents"