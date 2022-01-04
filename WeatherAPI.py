import requests

#organizing by moving code into function/main
def get_weather_desc_and_temp():
    api_key = "bf5a0b31211501c27b89497878290576"#Get this from the site youre requesting from
    city = "Fairfax"#variable made for url link
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"#Website

    request = requests.get(url)#requesting from url
    json = request.json()#new variable to turn request variable into json
                        
    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return{"description": description,
            "temp_min": temp_min,
            "temp_max": temp_max}

def main():
    weather_dict = get_weather_desc_and_temp()
    #printed results
    print("Today's forecast is", weather_dict.get("description"))
                                                                                #temp_min = json.get("main").get("temp_min")
    print("The minimum temperature is", weather_dict.get("temp_min"))
                                                                                #temp_max = json.get("main").get("temp_max")
    print("The maximum temperature is", weather_dict.get("temp_max"))
main()