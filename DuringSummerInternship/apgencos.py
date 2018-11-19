
# importing all libraries
from bs4 import BeautifulSoup
import requests
import csv
import time
import sys
import datetime
from tkinter import *
import os
script_path = os.path.dirname(os.path.abspath( __file__ ))

#print(script_path)
def daily1():
	

	url= "https://apgenco.gov.in/files/2.htm"
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}

	session= requests.session()
	session.headers.update(headers)

	try:
		r  = session.get(url)
		print (r.status_code)
	    #r.raise_for_status
		print("Requesting URL:"+ url)
	except requests.exceptions.HTTPError as e:
		print ("An HTTP error occured")
	except requests.exceptions.Timeout:
		print("Timeout error")
	except requests.exceptions.RequestException as e:
		print (e)

	dat = r.text

	soup = BeautifulSoup(dat, 'html.parser')
	#print (soup.prettify())
	table = soup.find("table",class_="xl686020")				
		


	rows= table.find_all("tr")

	data=[]
	k=8
	for trs in rows[8:16]:
		tds= trs.find_all("td")
		row= [ele.text.strip() for ele in tds]
		Station = row[0]
		k=k+1
		StationName= "Dr Narla Tatarao - "+ row[1]
		data.append([StationName]+ row[2:6])

	for trs in rows[16:]:
		tds= trs.find_all("td")
		row= [ele.text.strip() for ele in tds]
		Station = row[0]
		k=k+1
		if (Station =="APGENCO Thermal"):
			data.append(row[:5])
			break

		StationName= "Rayalaseema - "+ row[1]
		data.append([StationName]+ row[2:6])

	for trs in rows[k+1:]:
		tds= trs.find_all("td")
		row= [ele.text.strip() for ele in tds]
		k=k+1
		data.append(row[:5])
		Station = row[0]
		if (Station =="Tungabhadra (Total)"):
			break

	for trs in rows[44:45]:
		tds= trs.find_all("td")
		row= [ele.text.strip() for ele in tds]
		StationName= "Total SDSTPS - "+ row[1]
		data.append([StationName]+ row[2:6])

	t_day=datetime.date.today()
	
	s1="Apgenco_"
	s2=datetime.date.today().strftime("%d-%m-%y")
	s3=".csv"	
	       
	headers= ["Station", "Capacity", "Day_-2", "Day_-1", t_day]

	writeFile = s1+s2+s3
	with open(writeFile, 'w') as fp:
		a = csv.writer(fp, delimiter=',' , lineterminator='\n')
		a.writerows([headers])
		a.writerows(data)
	   
	print ("File will be downloaded in location "+script_path)
       

window=Tk()

b1=Button(window,text="Download",command=daily1)
b1.grid(row=0,column=0)

b2=Button(window,text="File will be downloaded in location "+script_path)
b2.grid(row=1,column=0)

b3=Button(window,text="Close",command=window.destroy)
b3.grid(row=2,column=0)
window.mainloop()

