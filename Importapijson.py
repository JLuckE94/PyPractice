import requests
#Variable = call to site get data
response = requests.get("http://api.open-notify.org/astros.json")
#make json file readable.json()
json = response.json()

print("The people currently in space are:")
#loop name calling json variable access "People" list print loop and key value "name"
for person in json ["people"]:
    print(person["name"])