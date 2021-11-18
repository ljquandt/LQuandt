import json
import requests


print('Welcome to the Current Weather Forecast Program.')

def get_input(): #determine path for API connection
    lookup_path = input("Would you like to look up US weather data by city or zipcode? Enter 1 for City and 2 for Zip code: ")
    if lookup_path == '1':
        city()
    elif lookup_path == '2':
        zipcode()
    else:
        print('Invalid input, please try again.')
        get_input()


def zipcode(): #input zip code and units of measurement to get correct API URL
    measurement_units = input('Would you like to use Kelvin [K], Celsius[C] or Fahrenheit[F]? Please enter the corresponding letter: ')
    if measurement_units.upper() == 'F':
        zipcode_input = input("Please the zip code to use: ")
        url_zipcode = f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode_input}&units=imperial&appid=d2949d460dbf3479eb845240646dbf60'
        establish_connection(url_zipcode, zipcode_input)
    elif measurement_units.upper() == 'C':
        zipcode_input = input("Please the zip code to use: ")
        url_zipcode=f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode_input}&units=metric&appid=d2949d460dbf3479eb845240646dbf60'
        establish_connection(url_zipcode, zipcode_input)
    elif measurement_units.upper() == 'K':
        zipcode_input = input("Please the zip code to use: ")
        url_zipcode = f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode_input}&appid=d2949d460dbf3479eb845240646dbf60'
        establish_connection(url_zipcode, zipcode_input)
    else:
        print("Invalid input, please try again.")
        zipcode()


def city(): #determine city/state name and units of measurement
    measurement_units = input('Would you like to use Kelvin [K], Celsius[C] or Fahrenheit[F]? Please enter the corresponding letter: ')
    if measurement_units.upper() == 'F':
        cityname_input = input('Please enter the city name: ')
        state_input = input("Please enter the full state name or 3 letter abbreviation (EX:neb): ")
        url_city=f'https://api.openweathermap.org/data/2.5/weather?q={cityname_input},{state_input}&units=imperial&appid=d2949d460dbf3479eb845240646dbf60'
        establish_connection(url_city, cityname_input)
    elif measurement_units.upper() == 'C':
        cityname_input = input('Please enter the city name: ')
        state_input = input("Please enter the full state name or 3 letter abbreviation (Ex:neb): ")
        url_city = f'https://api.openweathermap.org/data/2.5/weather?q={cityname_input},{state_input}&units=metric&appid=d2949d460dbf3479eb845240646dbf60'
        establish_connection(url_city, cityname_input)
    elif measurement_units.upper() == 'K':
        cityname_input = input('Please enter the city name: ')
        state_input = input("Please enter the full state name or 3 letter abbreviation (Ex:neb): ")
        url_city = f'https://api.openweathermap.org/data/2.5/weather?q={cityname_input},{state_input}&units&appid=d2949d460dbf3479eb845240646dbf60'
        establish_connection(url_city, cityname_input)
    else:
        print('Invalid input, please try again')
        city()

def establish_connection(a,b): #connect to API using correct URL above and print output
    url = a
    cityname_input = b
    zipcode_input = b
    try:
        response=requests.request('GET', url)
    except:
        print('Error connecting to API.')
    data=response.text
    sort_weather = json.loads(data)
    if 'main' not in sort_weather: #catch user errors if zipcode/city input is not valid
        print('Error connecting to API, please try again checking your Zip code or City Name')
    else:
        print("Connected to API")
        temp_sort = [sort_weather['main']] # ??? correct way to handle JSON dict? Made into list
        cloud_sort = sort_weather['weather']
        for item in temp_sort: #sort through JSON dict 'main' to get output
            print('Current Weather Conditions in:',cityname_input or zipcode_input)
            print('Current Tempature: ', item['temp'])
            print('High Temp: ', item['temp_max'])
            print('Low Temp: ', item['temp_min'])
            print('Humidity: ', item['humidity'],'%')
            print('Pressure: ', item['pressure'],"pHA")
        for item in cloud_sort: #sort through JSON dict 'weather' to get output
            print('Cloud Cover: ', item['description'])


def main():
    initiate_program = input('Would you like to look up the weather in a US location using Zip code or City name? Enter Y/N: ')
    if initiate_program.upper() == 'N':
        print("Thank you for using my weather program.")
    elif initiate_program.upper() == 'Y':
        while initiate_program.upper() == 'Y':
            get_input()
            initiate_program = input('Would you like to look up the weather in another US location using Zip code or City name? Enter Y/N: ')
        if initiate_program.upper() == 'N':
            print("Thank you for using my weather program.")
        else:
            print('Invalid response, please try again.')
            main()
    else:
        print("Invalid response, please try again. Please use the letter Y or N")
        main()


if __name__ == '__main__':
    main()
