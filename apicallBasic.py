import requests

def get_w():
    api_key ="0f734225b37a77a9162c2ff96e34e55b"
    base_url ="https://api.openweathermap.org/data/3.0/onecall"
    params ={"q":city,appid:apikey,"units":"metric"}
    response =request.get (base_url,params=params)
    
    if response.status_code==200:
        data =resposae.json()
        print(F"city:{data['name']}")
        print(f"Temp:{data ['main']['temp']}")
        print(f"Weather:{data['weather'][0]["description"]}")              
        
    else:
        print("404")
        
        city = input("enter city anme ")
        get_w(city)