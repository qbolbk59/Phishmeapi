import requests
import os
import json
import csv
import time


#Fetch all Scenarios of Phishing Campaign

headers={'Authorization':'Token token="token value"'}
url='https://login.phishme.co.uk/api/v1/scenarios.json'    #Change url to the one relevant to you
r=requests.get(url,headers=headers)
results=r.json()


scenario_name=[]
scenario_id=[]

#List all Phishing Campaign Scenarios

for scenario in results:
    scenario_name.append(scenario["title"])

for ids in results:
    scenario_id.append(ids["id"])

Company_id=[]
for i in range(0,len(scenario_name)):
    if("any specific filter in campaign name" in scenario_name[i]):
        Company_id.append(scenario_id[i])


Company_id_csv=[]

for idvalues in Company_id:
    Company_id_csv.append(idvalues+".csv")


os.chdir("C:\\Users\\User\\Desktop\\Phishme")   #Change this directory as per your requirement
path=os.getcwd()

all_files=[]
for root, dirs, files in os.walk(path):
	for filename in files:
		all_files.append(filename)
		break


#List all ID's for which report is not extracted yet to ensure calls are made only for new Campaigns

difference=[]
difference=list(set(Company_id_csv)-set(all_files))

final_list=[]

for values in difference:
    final_list.append(values.strip('.csv'))






#Call Results of all new Campaigns
        
time.sleep(20)                                         # Time delay added to follow the API gateway throttling to avoid 403 error
os.chdir("C:\\Users\\User\\Desktop\\Phishme")          #Change this directory name and indexing to be done for all files in this directory
for i in range(0,len(final_list)):
    r=requests.get('https://login.phishme.co.uk/api/v1/scenario/'+str(final_list[i])+'/full_csv', headers=headers)
    file1=open(str(final_list[i])+".csv","w", encoding="utf-8")
    file1.write(r.text)
    time.sleep(20)

        
