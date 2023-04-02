import os
import pandas as pd
import numpy as np
os.chdir("C:/roshil")
data = pd.read_csv("BangaloreZomatodata.csv")
data3=data.drop(columns=['IsHomeDelivery','isTakeaway','isIndoorSeating','isVegOnly','Dinner Ratings',
                         'Dinner Reviews','PeopleKnownFor','PopularDishes','KnownFor'])
data3 = data3.head(20)
print(np.unique(data3['Area']))     #it gives unique valuse of a perticular column
#dtypes are object,int64 and category
#category take less memory as compare to object
data3['Area'] = data3['Area'].astype('category')
data3['Delivery Ratings'] =data3['Delivery Ratings'].astype('float64')  #CHANGE DATATYPE
print(data3.info())
print(data3['Area'].nbytes)         #we can get memory of each column, we also use it while converting datatype
#This is most important to replace the values
data3['Name'].replace('Burger King',"BURGER KING",inplace=True)

print(data3.isnull().sum())         #This is use to sum the null values

#we add a new column and insert the values using the for loop
data3.insert(6,"Ratings","")
for i in range(0,len(data3['Delivery Ratings']),1):
    if (data3['Delivery Ratings'][i]<4.0):
        data3['Ratings'][i]="Avg"
    elif (data3['Delivery Ratings'][i]<4.5):
        data3['Ratings'][i]="Medium"
    else: data3['Ratings'][i]="High"

#we add a new column and insert the values using the while loop
data3.insert(7,"Avgcost","")
i=0

while i<len(data3['AverageCost']):
    if (data3['AverageCost'][i]<=200):
        data3['Avgcost'][i]= "Low price"
    elif (data3['AverageCost'][i]<=500):
        data3['Avgcost'][i]= "Medium price"
    else: data3['Avgcost'][i]= "High price"
    i=i+1

data3['Avgcost'].value_counts()     #it is use to count the no. of values in each attribute
#======================================================================================================================
# DEFINE A FUNCTION USING (DEF)
def c_convert(val):
    val_converted = val/100
    return val_converted
data3["Delivery_Reviews"] = c_convert(data3["Delivery Reviews"])
data3["Delivery_Reviews"] = round(data3['Delivery_Reviews'],2)


data3.insert(9,'ddr','')
data3.insert(10,'drv','')
def c_convert(val1,val2):
    val_1 = val1/100
    val_2 = val2/val1       #we can defined as we want
    return [val_1,val_2]
data3['ddr'],data3['drv'] = c_convert(data3['Delivery Ratings'],data3['Delivery Reviews'])

#======================================================================================================================

#THis is frequency table checking
pd.crosstab(index=data['Area'],columns='count',dropna=True)    #to checking crosstab
#This is Two way table
d1=pd.crosstab(index=data['Area'],                             #we can check one or more columns using crosstab function
            columns=data['KnownFor'],
            dropna=True)
#Two way table-joint probability ~ in this we use normalize function to create all the no. values to the proportional
#Joint probability is the likelihood of the two indenpendent events happining at the same time.
d1=pd.crosstab(index=data['Area'],
            columns=data['KnownFor'],
            normalize= True,
            dropna=True)
#Two way table-Marginal probability ~ in this we use margins fuction in it
#Marginal probability is the probability of the occurence of the single event.
d1=pd.crosstab(index=data['Cuisines'],
            columns=data['KnownFor'],
            margins=True,
            normalize=True,
            dropna=True)

#Two way table - Conditional probability we just change the normalize from true to 'index',thats it.
# >conditional probability is the probability of an event (A), given that another event (B) has already occurred.
d1=pd.crosstab(index=data['Cuisines'],
            columns=data['KnownFor'],
            margins=True,
            dropna=True,
            normalize='index')
#======================================================================================================================
#Correlation : The strength of association between two variables, it is bounded between -1 to +1 zero represents no relation
#Visual represent for correlation ~ scatter plot
'''
Syntax: Dataframe.corr(self, method='pearson')
1. To compute pairwise correlation of columns excluding NA/null values
2. Excluding the categorical variables to find the Pearson's correlation
'''
#first we take only numerical data type
num_type = data.select_dtypes(exclude='object')
corr_matrix = num_type.corr()


#CHANGE DATA TYPE
data['isVegOnly']=data['isVegOnly'].astype(object)
data['isVegOnly'].info()



