# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)
data=data.rename(columns={'Total':'Total_Medals'})
data.head(10)


# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] =np.where(data['Total_Summer'] == data['Total_Winter'],'Both',data['Better_Event'])

better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here

#Subsetting the dataframe
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

#Dropping the last row
top_countries=top_countries[:-1]

#Function for top 10
def top_ten(data, col):
    
    #Creating a new list
    country_list=[]
    
    #Finding the top 10 values of 'col' column
    country_list= list((data.nlargest(10,col)['Country_Name']))
    
    #Returning the top 10 list
    return country_list



#Calling the function for Top 10 in Summer
top_10_summer=top_ten(top_countries,'Total_Summer')
print("Top 10 Summer:\n",top_10_summer, "\n")

#Calling the function for Top 10 in Winter
top_10_winter=top_ten(top_countries,'Total_Winter')
print("Top 10 Winter:\n",top_10_winter, "\n")

#Calling the function for Top 10 in both the events
top_10=top_ten(top_countries,'Total_Medals')
print("Top 10:\n",top_10, "\n")

#Extracting common country names from all three lists
common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))

print('Common Countries :\n', common, "\n")

#Code ends here


# --------------
#Code starts here


#Usage of isin() function
summer_df=data[data['Country_Name'].isin(top_10_summer)]

winter_df=data[data['Country_Name'].isin(top_10_winter)]


top_df=data[data['Country_Name'].isin(top_10)]

# Initialize figure and axes
fig, (ax_1, ax_2, ax_3) = plt.subplots(1,3, figsize=(20,10))

# Stacked bar-chart representing counts
res = data.groupby(['Country_Name', 'Total_Summer']).size().unstack()
res.plot(kind='bar', stacked=True, ax=ax_1)
ax_1.set_title('summer_df')

res_1 = data.groupby(['Country_Name', 'Total_Winter']).size().unstack()
res_1.plot(kind='bar', stacked=True, ax=ax_2)
ax_2.set_title('winter_df')

res_2 = data.groupby(['Country_Name', 'Total_Medals']).size().unstack()
res_2.plot(kind='bar', stacked=True, ax=ax_3)
ax_3.set_title('top_df')

# Code ends here







# --------------
#Code starts here

#Summer DF#
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer'] 
summer_max_ratio=max(summer_df['Golden_Ratio'])
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

#Winter DF#
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter'] 
winter_max_ratio=max(winter_df['Golden_Ratio'])
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

#Top_DF#
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals'] 
top_max_ratio=max(top_df['Golden_Ratio'])
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
#Print All#
print(summer_max_ratio)
print(summer_country_gold)
print(winter_max_ratio)
print(winter_country_gold)
print(top_max_ratio)
print(top_country_gold)


# --------------
#Code starts here


#Removing the last column of the dataframe
data_1=data[:-1]

#Creating a new column 'Total_Points'
data_1['Total_Points']= data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1  # Use of position index to handle the ambiguity of having same name columns


#Finding the maximum value of 'Total_Points' column
most_points=max(data_1['Total_Points'])

#Finding the country assosciated with the max value of 'Total_Column' column
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print('The maximum points achieved is ', most_points, ' by ', best_country )

#Code ends here


# --------------
#Code starts here
best=data[data['Country_Name']== eval('best_country')]

best=best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best)

res = best.groupby(['Gold_Total','Silver_Total','Bronze_Total']).size().unstack()
res.plot(kind='bar', stacked=True, figsize=(15,10))

# Plot stacked bar chart
plt.figure(figsize=[14,8])
plt.xlabel('United States')
plt.ylabel('Medals Tally')


plt.show()

plt.xticks(rotation=45)
# Display plot
plt.show()


