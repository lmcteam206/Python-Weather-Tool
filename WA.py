import requests
import art
from art import *
import subprocess
import time
import tqdm
from tqdm import tqdm

def get_weather(api_key, city):
    for _ in tqdm(range(100), desc="Connecting...", ascii=False, ncols=75):
            time.sleep(0.01)
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
 
        for _ in tqdm(range(100), desc="Check the data...", ascii=False, ncols=75):
            time.sleep(0.02)
        for _ in tqdm(range(100), desc="1...", ascii=False, ncols=75):
            time.sleep(0.0000000000000001)           
        response = requests.get(base_url, params=params)
        for _ in tqdm(range(100), desc="2...", ascii=False, ncols=75):
            time.sleep(0.0000000000000001) 
        response.raise_for_status()
        for _ in tqdm(range(100), desc="3...", ascii=False, ncols=75):
            time.sleep(0.0000000000000001) 
        data = response.json()
        for _ in tqdm(range(100), desc="4...", ascii=False, ncols=75):
            time.sleep(0.0000000000000001) 

        main_info = data['main']
        weather_info = data['weather'][0]

        # Removed unnecessary tqdm loops for clarity
        for _ in tqdm(range(100), desc="Getting the data...", ascii=False, ncols=75):
            time.sleep(0.01)

        print("--------------------------------------------------------------------")
        print(f"\nWeather in {city.title()}:")
        print(f" - Temperature: {main_info['temp']}°C (Feels like: {main_info['feels_like']}°C)")
        print(f" - Description: {weather_info['description'].capitalize()}")
        print(f" - Humidity: {main_info['humidity']}%")
        print(f" - Wind Speed: {data['wind']['speed']} m/s")
        print("--------------------------------------------------------------------")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("Error: Invalid API key.")
        elif response.status_code == 404:
            print("Error: City not found. Please check the city name.")
        else:
            print(f"HTTP Error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred: {req_err}")
    except KeyError:
        print("Unexpected response format. Please check the API and update the parsing logic.")

if __name__ == "__main__":
    
    api_key = input('Enter your openweather api:')  # Replace with your actual API key

    while True:
        tprint("---------WST----------")
        tprint("[Weather Scan Tool]", "rand")
        print(".---------------------------------------------------.")
        print(".---------------------------------------------------.")
        print("1-This Tool Uses [openweather.com] As The Data Source")
        print("2-This Tool Is Full Made BY LMCTEAM206")
        print(".---------------------------------------------------.")
        print(".---------------------------------------------------.")
        
        for _ in tqdm(range(100), desc="Starting...", ascii=False, ncols=75):
            time.sleep(0.01)
        city = input("Enter the city name: ")
        for _ in tqdm(range(100), desc="Loading the command...", ascii=False, ncols=75):
            time.sleep(0.01)
        get_weather(api_key, city)

        # Ask if the user wants to continue
        continue_choice = input("Do you want to check another city? (yes/no): ").lower()
        for _ in tqdm(range(100), desc="Ending...", ascii=False, ncols=75):
            time.sleep(0.01)
        if continue_choice != 'yes':
            
            break
