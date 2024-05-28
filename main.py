'''
The main functions of this program:
    1. Get the weather data from NOAA
    2. Check to see if geo-magnetic storm is strong enough to be seen from home / nearby
    3. Send an email or an alert to say when it will be at it's strongest and when within the forecast
    4. Check to see if there are any meteor showers and follow steps 2 & 3.
'''
import urllib.request
import datetime 


def daily_check():
    weather_info = get_geo_magnetic_forecast()
    data_set = parse_geo_data(weather_info)
    filter_data(data_set)

# Get the forecast 
def get_geo_magnetic_forecast():
    with urllib.request.urlopen('https://services.swpc.noaa.gov/text/3-day-geomag-forecast.txt') as response:
        html = response.readlines()        
    return html



def parse_geo_data(html):
    weather_data = html[18:]
    weather_list = []
    for line in weather_data:
        new_line = line.split()
        weather_list.append(new_line)
    #print(weather_list)
    return weather_list


def filter_data(weather_list):
    # this should be recursive to see when the top strength is.
    # Absolutely not good code.
    first_weather_set = weather_list[0]
    second_weather_set = weather_list[1]
    third_weather_set = weather_list[2]
    todays_weather = max(first_weather_set)
    print(f"Today's geo-magnetic strength is {float(todays_weather)}")


'''
The above is set up as a rough dataset at the moment.

I should be able to have a variable for today tomorrow and the day after.
that way the function can just say what today will be as one thing, tomorrow etc..

Then when it parses through each of the values it should only really be looking at one part of each list like 1, 2, and 3.
And then it can be stored there to see which one will be the highest and the estimates will kind of fall in line with if else checks?
(probably really bad code practice.)

But once it checks it can just kind of hold off on the days after and really only should be looking at tonight or tomorrow so I can plan accordingly.


'''


daily_check()
