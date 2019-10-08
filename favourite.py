import pandas as pd
import numpy as np 

class favourite:
	data=pd.DataFrame()
	cols=[]
	data1=pd.DataFrame()
	cols1=[]
	

	def add(self,ID, Town,Des):
		#self.cols=['DISTRICT','TOWN','DESTINATION','Category','Favourite']
		self.data = pd.read_csv("datasets/FinalCategorydb1.csv")
		#self.cols1=['UserID', 'Town', 'Destination']
		self.data1 = pd.read_csv("datasets/user.csv")
		fav=(self.data['Favourite'][self.data['DESTINATION']==Des])
		#if(flag==1):
		if(Des in list(self.data1['Destination'][self.data1['UserID']==ID])):
			print('Unnecesary add')
			#self.remove_user('yash','Aurangabad (CB)','Ajanta')
			pass
		else:
			fav=fav+1
			print('necessary add')
			self.add_user(ID, Town, Des)
		'''else: 
									if(Des in list(self.data1['Destination'][self.data1['UserID']==ID])):
										self.remove_user(ID, Town, Des)
										print("necesary remove")
										fav=fav-1'''
		self.data['Favourite'][self.data['DESTINATION']==Des]=fav
		#data.drop(data.index[0])
		#print(self.data)
		self.data.to_csv("datasets/FinalCategorydb1.csv",index=False)

	def add_user(self,ID, Town, Destination):
		Id=[]
		town=[]
		des=[]
		Id.append(ID)
		town.append(Town)
		des.append(Destination)
		d={"UserID":Id, "Town":town, "Destination":des}
		df=pd.DataFrame(d)
		print(df)
		print(self.data1)
		l=len(self.data1)
		self.data1.loc[l]=[ID]+[Town]+[Destination]
		print(self.data1)
		self.data1.to_csv("datasets/user.csv",index=False)

	def remove_user(self,ID, Town, Des):
		print('xyz')
		li=list(self.data1[self.data1["UserID"]==ID].index)
		des=[]
		for i in li:
			des.append(self.data1.iloc[i,2])
		for i in range(len(des)):
			if(des[i]==Des):
				final=i
		self.data1=self.data1[self.data1.index!=final+1]
		self.data1.to_csv("datasets/user.csv",index=False)

	def user_fav(self, ID):
		user=pd.read_csv("datasets/user.csv")
		user=user[user["UserID"]==ID]
		final={"Destination":list(user["Destination"]), "Town":list(user["Town"])}
		#print(final)
		return final

	def popularity(self):
		pop=pd.read_csv("datasets/FinalCategorydb1.csv")
		popular=pop[pop['Favourite']>0]
		popular.sort_values("Favourite", ascending= False, inplace= True)
		final={"Destination":list(popular["DESTINATION"]), "Town":list(popular["TOWN"])}
		#print(final)
		return final

'''
f1=favourite()
f1.add('yash','MAtheran','Matheran')
fin = f1.popularity()
fin1 = f1.user_fav('yash')

print (fin)
print(fin1)'''