import schedule
import time
import vidyut_f as ed
from tkinter import *

import os


class Checkbar(Frame):

	
	
	def __init__(self, parent=None, side=LEFT, anchor=W):
		Frame.__init__(self, parent)
		self.vars = []
		statedic={1:"himachal-pradesh",2:"delhi",3:"assam",4:"uttar-pradesh",5:"rajasthan",6:"chhattisgarh",7:"madhya-pradesh",8:"Odisha",9:"maharashtra",10:"telangana",11:"andhra-pradesh",12:"puducherry",13:"uttarakhand",14:"jharkhand",15:"tamil-nadu",16:"kerala",17:"punjab",18:"karnataka",19:"west-bengal",20:"tripura",21:"sikkim",22:"nagaland",23:"mizoram",24:"manipur",25:"meghalaya",26:"jammu-kashmir",27:"haryana",28:"goa",29:"gujarat",30:"chandigarh",31:"bihar",32:"arunachal-pradesh"}

		for i in range(1,33):
			val=statedic.get(i)
			var = IntVar()
			Checkbutton(self, text=val, variable=var).grid(row=i, sticky=W)
			self.vars.append(var)
			

	def state(self):
		return map((lambda var: var.get()), self.vars)

if __name__ == '__main__':
	statedic={1:"himachal-pradesh",2:"delhi",3:"assam",4:"uttar-pradesh",5:"rajasthan",6:"chhattisgarh",7:"madhya-pradesh",8:"Odisha",9:"maharashtra",10:"telangana",11:"andhra-pradesh",12:"puducherry",13:"uttarakhand",14:"jharkhand",15:"tamil-nadu",16:"kerala",17:"punjab",18:"karnataka",19:"west-bengal",20:"tripura",21:"sikkim",22:"nagaland",23:"mizoram",24:"manipur",25:"meghalaya",26:"jammu-kashmir",27:"haryana",28:"goa",29:"gujarat",30:"chandigarh",31:"bihar",32:"arunachal-pradesh"}

	
	s=[]
	statelist=[]
	root = Tk()
	st= Checkbar(root,["himachal-pradesh","delhi","assam","uttar-pradesh","rajasthan","chhattisgarh","madhya-pradesh","Odisha","maharashtra","telangana","andhra-pradesh","puducherry","uttarakhand","jharkhand","tamil-nadu","kerala","punjab","karnataka","west-bengal","tripura","sikkim","nagaland","mizoram","manipur","meghalaya","jammu-kashmir","haryana","goa","gujarat","chandigarh","bihar","arunachal-pradesh"])
	st.pack(side=TOP,  fill=X)
	st.config(relief=GROOVE, bd=2)

	
	i=0
	y=0
	for x in range(len(s)):
		print(s[x])
		if(s[x]==1):
			statelist.append(statedic.get(x))
	
	def allstates():
		s=list(st.state())
		for x in range(0,32):
			print(s[x])
			if(s[x]==1):
				y=x+1
				statelist.append(statedic.get(y))
	
	def job():
		ed.job11(statelist)

	
	def forgui():

		allstates()
		job()
		
		schedule.every(14).minutes.do(job)
		while 1:
			schedule.run_pending()
			time.sleep(1)
	
	
	script_path = os.path.dirname(os.path.abspath( __file__ ))

	fp="File will be downloaded in location "+script_path
	msg = Message(root, text =fp)
	msg.config(bg='lightgreen', font=('times', 24, 'italic'))
	msg.pack()



	Button(root, text='Quit', command=root.destroy).pack(side=RIGHT)
	Button(root, text='Run', command=forgui).pack(side=RIGHT)
	root.mainloop()
