
#Importing all libraries
from bs4 import BeautifulSoup
import requests
import csv
import sys
import datetime
#1 Making sure headers are written at top and only once
headers_csv=["Dated","Timeblock","State","Demand met yesterday","Demand met today"]

s1="Vidyut"
s2=datetime.date.today().strftime("%d-%m-%y")
s3=".csv"

writeFile = s1+s2+s3

with open(writeFile, 'w') as fp:
	a = csv.writer(fp, delimiter=',' , lineterminator='\n')
	a.writerows([headers_csv])



#2 Creating a job func Passing the specific statename,time,day ,month at which scheduler will stop as a parameter
def job11(states):
	
	#3 extracting statenames from above html code
	for i in range(len(states)):
		statename= states[i]
		print(statename)
		
		#3a going on specific state website
		url= "http://vidyutpravah.in/state-data/"+statename
		headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}

		session= requests.session()
		session.headers.update(headers)


		try:
			r  = session.get(url)
			print("Requesting URL:"+ url)
		except requests.exceptions.HTTPError as e:
			print ("An HTTP error occured")
		except requests.exceptions.Timeout:
			print("Timeout error")
		except requests.exceptions.RequestException as e:
			print (e)

	    #3b Parsing and storing in a var
		dat = r.text
		#print(type(dat))
		soup = BeautifulSoup(dat, 'html.parser')
	        #print (soup.prettify())

	    #3c Extracting date,day,month
		date=soup.find("tr",class_="blue_bg")
		date=date.text[69:]
		print(date)

		day=soup.find("tr",class_="blue_bg")
		day=day.text[69:71]
		print(day)
		
		month=soup.find("tr",class_="blue_bg")
		month=month.text[72:75]
		print(month)

	     #3d Extracting timeblock and end time 
		timeblock=soup.find("tr",class_="blue_bg")
		timeblock=timeblock.text[48:61]
		print(timeblock)
		
		timepart=soup.find("tr",class_="blue_bg")
		timepart=timepart.text[48:53]
		print(timepart)

	     #3e Storing state name
		stateN=statename
	    
	     #3f Extracting previous demand
		prevD = soup.find("span",class_="value_PrevDemandMET_en value_StateDetails_en")
		prevD=prevD.text
		print(prevD)
	     
	     #3g Extracting current demand
		currD= soup.find("span",class_="value_DemandMET_en value_StateDetails_en")
		currD= currD.text
		print(currD)
	    
	     # All data extracted is in string form
	    
	    #4 Appending all data in list format and storing in 'data list'
		data=[]

		col1=[date]
		col2=[timeblock]
		col3=[stateN]
		col4=[prevD]
		col5=[currD]
		data.append(col1 + col2 +col3 +col4 +col5)#list of lists


   	    #5 writing data to csv file
		s1="Vidyut"
		s2=datetime.date.today().strftime("%d-%m-%y")
		s3=".csv"

		writeFile = s1+s2+s3
		with open(writeFile, 'a') as fp:
			a = csv.writer(fp, delimiter=',' , lineterminator='\n')
			a.writerows(data)
       
		print ("Data extracted!")
    	
	   
	
       
"""
window=Tk()

b1=Button(window,text="Download",command=daily1)
b1.grid(row=0,column=0)

b2=Button(window,text="File will be downloaded in location "+script_path)
b2.grid(row=1,column=0)

b3=Button(window,text="Close",command=window.destroy)
b3.grid(row=2,column=0)
window.mainloop()

"""


