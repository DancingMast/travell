import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def print_val(val):
	#print(val)
	if(val<0):
		return 0
	else:
		return val
def regression(city, year, month):
	cols1=['YEAR','MONTH', 'AHMEDNAGAR', 'AKOLA', 'AMRAVATI', 'AURANGABAD', 'BEED', 'BHANDARA', 'BULDHANA', 'CHANDRAPUR', 'DHULE', 'GADCHIROLI', 'GONDIA',  'HINGOLI', 'JALGAON', 'JALNA', 'KOLHAPUR', 'LATUR', 'MUMBAI', 'NAGPUR',  'NANDURBAR', 'NASIK', 'NANDED', 'OSMANABAD', 'PARBHANI', 'PUNE',  'RAIGHAD', 'RATNAGIRI', 'SANGLI', 'SATARA', 'SINDHUDURG', 'SOLAPUR', 'THANE', 'WARDHA', 'WASHIM', 'YAVATMAL', 'TOTAL']
	data1=pd.read_csv("datasets/final3.csv", names=cols1, skiprows=1)
	NO=list(np.arange(36))
	li=[]
	for i in range(len(data1)):
		date= data1.iloc[i, 0:2].values
		li.append(date)
	d=np.array(li)

	poly = PolynomialFeatures(degree = 2) 
	X = np.arange(36)
	y=np.array(data1[city])

	X_train, X_test, y_train, y_test = train_test_split(d, y,test_size=1/3)

	lin=LinearRegression()
	lin.fit(X_train, y_train) 

	accuracy =lin.score(X_test, y_test)
	accuracy = float(accuracy)
	  
	#print("Accuracy: ",accuracy)

	X_poly = poly.fit_transform(d)
	poly.fit(X_poly, y)

	lin2 = LinearRegression() 
	lin2.fit(X_poly, y)  

	plt.scatter(X, y, color = 'blue') 

	plt.plot(X, lin2.predict(poly.fit_transform(d)), color = 'red')  
	#plt.show() 

	plt.title('Polynomial Regression') 
	plt.xlabel('Months') 
	plt.ylabel('Visitors') 



	
	year=year-2000

	val=(lin2.predict(poly.fit_transform([[year,month]])))
	val=print_val(int(val))
	return val
'''
city=input("Enter the District : ")
year=input("Enter the year : ")
year=int(year)
month=input("Enter the month : ")
month=int(month)
regression(city, year, month)
d=list(d)
y=list(y)
for i in range (12,21):
	for j in range(1,13):
		d.append([i,j])
		y.append(int(lin2.predict(poly.fit_transform([[i,j]]))))
d=np.array(d)    
y=np.array(y)     


X_poly = poly.fit_transform(d)
poly.fit(X_poly, y)

lin2 = LinearRegression() 
lin2.fit(X_poly, y)  
X=np.arange(144)
plt.scatter(X, y, color = 'blue') 

plt.plot(X, lin2.predict(poly.fit_transform(d)), color = 'red')  
plt.show() 

plt.title('Polynomial Regression') 
plt.xlabel('Months') 
plt.ylabel('Visitors') 
'''

def graph(city):
	cols1=['YEAR','MONTH', 'AHMEDNAGAR', 'AKOLA', 'AMRAVATI', 'AURANGABAD', 'BEED', 'BHANDARA', 'BULDHANA', 'CHANDRAPUR', 'DHULE', 'GADCHIROLI', 'GONDIA',  'HINGOLI', 'JALGAON', 'JALNA', 'KOLHAPUR', 'LATUR', 'MUMBAI', 'NAGPUR',  'NANDURBAR', 'NASIK', 'NANDED', 'OSMANABAD', 'PARBHANI', 'PUNE',  'RAIGHAD', 'RATNAGIRI', 'SANGLI', 'SATARA', 'SINDHUDURG', 'SOLAPUR', 'THANE', 'WARDHA', 'WASHIM', 'YAVATMAL', 'TOTAL']
	data1=pd.read_csv("datasets/final3.csv", names=cols1, skiprows=1)
	NO=list(np.arange(36))
	li=[]
	for i in range(len(data1)):
		date= data1.iloc[i, 0:2].values
		li.append(date)
	d=np.array(li)

	poly = PolynomialFeatures(degree = 5) 
	X = np.arange(36)
	y=np.array(data1[city])


	X_poly = poly.fit_transform(d)
	poly.fit(X_poly, y)

	lin2 = LinearRegression() 
	lin2.fit(X_poly, y)  

	plt.scatter(X, y, color = 'blue') 

	plt.plot(X, lin2.predict(poly.fit_transform(d)), color = 'red')  
	#plt.show()
	month=[]
	d=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	visits=[] 

	for i in range(9,12):
		for j in range(0,12):
			li=[]
			visits.append(int(lin2.predict(poly.fit_transform([[i, j]]))))
			li.append(str(i))
			li.append('-')
			li.append(d[j])
			word=''.join(li)
			month.append(word)
	final={'months':month,'visitors':visits}
	#print (final)
	return final

    





	
#pl=graph('PUNE')
#print(pl)