from __future__ import print_function
import urllib.request
import json


var2 = " "
var1 = 'Weather Data'
print("_______________________________________________")
print(var2)
print(var1)


user_input = input("Enter Name of Location: ") 
print("_______________________________________________ ")
loc = user_input.title()
mylocation = 'q='+ loc
url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?key=cf08cd35666f43c79bd131333170507&'+mylocation+'&num_of_days=2&tp=3&format=json'
response = urllib.request.urlopen(url).read()
json_obj = str(response, 'utf-8')
mydata = json.loads(json_obj)     
    
#iterating through the data to show what is needed       
for d in mydata.values():
       for a in d['request']:
                 print(a['query'])

       for b in d['current_condition']:
                 print('Temp: '+b['temp_F']+' F') 
                 print('Temp: '+b['temp_C']+' C') 
                 print('Wind Speed: '+b['windspeedMiles']+' Mph') 
                 print('Wind Speed: '+b['windspeedKmph']+' Kmph')
                 print('Time: '+b['observation_time']) 

       for c in d['weather']:
                 print('Date: '+c['date']) 
