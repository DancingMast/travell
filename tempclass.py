import pandas as pd
from tabulate import tabulate



#		print town






class recommend:

	beach=[]
	dist=[]
	towns=[]
	place=[]
	catego=[]
	tab=[]
	d=[]
	cdj:str
	mdj:str


	def __init__(self):

		self.cols=['DISTRICT','TOWN','DESTINATION','Rating','Category']
		self.cols1=['District','July','August','Sep','October','Nov','Dec','January','February','March','April','May','June',"Total"]

		self.data=pd.read_csv("datasets/FinalCategorydb .csv",names=self.cols)
		self.data1=pd.read_csv("datasets/visitors.csv",names=self.cols1,skiprows=1)
		places=self.data['DESTINATION']

		self.place=list(places)
		cat=self.data['Category']
		self.catego=list(cat)
		self.d=list(self.data['DISTRICT'])
		
	def sortcat(self):
		#pl=input('Enter the Category:')
		pl=self.cdj
		
		#he try kartoy zaal tr bhaarich ahe
		self.beach.clear()
		self.dist.clear()
		self.towns.clear()
		self.tab.clear()

		for i in range(len(self.place)):
			if(self.catego[i]==pl):
				self.beach.append(self.place[i])
				self.dist.append(self.d[i])
				self.towns.append(self.data['TOWN'][i])
		print( self.beach)
		print (self.dist)
		print (self.towns)

	def setcat(self,sc):
		self.cdj=sc
		self.sortcat()

	def setmonth(self,sm):
		self.tab.clear()
		self.mdj=sm
		self.maxvisit()
		return self.tab

	def createtab(self,dest,tow):
		#tab=[]
		for i in range(len(dest)):
			t=[]
			t.append((dest[i]))
			t.append((tow[i]))
			self.tab.append(t)

		print('\n\n' +tabulate(self.tab, headers=['DESTINATION', 'TOWN']))
		

	def printtown(self,res):
		town=[]
		to=list(self.data['TOWN'])
		des=list(self.data['DESTINATION'])
		for j in range(len(res)):
			for i in range(len(des)):
				if(des[i]==res[j]):
					town.append(to[i])
		print(list(town))
		print("/n/n/n/********************RESULT**********************/n")
		self.createtab(res,list(town))



	def printres(self,y):
		res=[]
		for i in range(len(y)):
				for j in range(len(self.dist)):
					if(y[i]==self.dist[j]):
						res.append(self.beach[j])
		print (res)
		return (res)

	def maxvisit(self):
		print("Hello!!")
		
		#usemonth=input("Enter the required month:  ")
		usemonth=self.mdj
		mn=list(self.data1[usemonth])
		md=list(self.data1['District'])
		print (mn)

		def sortlist(mn,md):
				zipped_pairs=zip(md,mn)
				z=[x for _,x in sorted(zipped_pairs)]
				return z
		y=sortlist(md,mn)

		y.reverse()
		print (y)
		res=self.printres(y)
		self.printtown(res)
	
	def clearlist(self):
		#self.res.clear()
		self.tab.clear()

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