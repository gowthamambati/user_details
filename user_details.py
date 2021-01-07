#importing required libraries
import requests
import pandas as pd 

#loading given data in json
given_data=requests.get('https://api.github.com/users')
given_data=given_data.json()

#making required empty lists
user_login=[]
user_id=[]
user_name=[]
follower_id=[]
follower_login=[]

#looping through links to gather and add data to the above lists
for i in range(len(given_data)):
    d1=given_data[i]
    if d1['id']%10==0:
        info=requests.get(d1['url'])
        info=info.json()
        fol_info=requests.get(info['followers_url'])
        fol_info=fol_info.json()
        for j in range(len(fol_info)):
            d2=fol_info[j]
            follower_id.append(d2['id'])
            follower_login.append(d2['login'])
            user_login.append(info['login'])
            user_id.append(info['id'])
            user_name.append(info['name'])

#creating required csv file with the help of above lists
pd.DataFrame({'User Id':user_id,'User Login':user_login,'User Name':user_name,'Follower ID':follower_id,'Follower Login':follower_login}).to_csv('my_file.csv')

print('Required csv file has been created successfully.')
