import pandas as pd
from mregression import * 
from tabulate import tabulate


class recommend:
	cdj:str
	mdj:str
	data=pd.DataFrame()
	cat=pd.DataFrame()
	district=[]
	tab=[]

	def __init__(self):
		cols=['DISTRICT','TOWN','DESTINATION','Category']
		self.data=pd.read_csv("datasets/FinalCategorydb .csv",names=cols)
	
	def sortcat(self):
		self.cat=self.data[self.data['Category']==self.cdj]
		self.cat=pd.DataFrame(self.cat)
		self.district=list(self.cat['DISTRICT'])
		print (self.district)
		
	def clearlist(self):
		#self.res.clear()
		self.tab.clear()

	def createtab(self):
		#tab=[]
		dest=list(self.cat['DESTINATION'])
		tow=list(self.cat['TOWN'])
		for i in range(len(dest)):
			t=[]
			t.append((dest[i]))
			t.append((tow[i]))
			self.tab.append(t)
		print(self.tab)
		print('\n\n' +tabulate(self.tab, headers=['DESTINATION', 'TOWN']))

	def maxvisit(self):
		Visit=[]
		for i in (self.district):
			val=regression(i, 2019, self.mdj)
			Visit.append(val)
		print(Visit)
		if ("Visitors" in self.cat.columns):
			pass
		else:
			self.cat.insert(4,"Visitors", Visit)
		self.cat.sort_values("Visitors", ascending= False, inplace= True)
		self.createtab()


	def setcat(self,sc):
		self.cdj=sc
		self.sortcat()


	def conv_month(self,sm):
		d={'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'Sep':9, 'October':10, 'Nov':11, 'Dec':12}
		val=int(d[sm])
		return val

	def setmonth(self,sm):
		self.tab.clear()
		sm=self.conv_month(sm)
		self.mdj=sm
		self.maxvisit()
		return self.tab
	
	def getgraph(self,city,mon,year):
		final = graph(city,mon,year)
		return final

def main():
	r1=recommend()
	r1.setcat(input("Enter Category: "))
	#r1.sortcat()
	r1.setmonth(input("Enter Month: "))	
	#r1.maxvisit()

	r1.clearlist()

	r1.setcat(input("Enter Category: "))
	#r1.sortcat()
	r1.setmonth(input("Enter Month: "))	
	
	r1.clearlist()
	r1.setcat(input("Enter Category: "))
	#r1.sortcat()
	r1.setmonth(input("Enter Month: "))
#main()