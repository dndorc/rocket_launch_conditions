
# importing the library
import requests
from bs4 import BeautifulSoup

# determine weather conditions``
def weather_check(t, s, w):
    results = [
        "Weather conditions look great",
        "A real-life launch would be postponed",
        "It's a bit cold today",
        "Spaceship launches prefer clear skies",
        "Wind conditions or otherwise might make launch more difficult"
    ]

    # prepare inputs
    s = s.strip()
    w = w.strip()
    temp_int = ""
    
    # receive int for temperature
    for i in range(len(t)):
        if t[i].isdigit():
            temp_int += t[i]
    temp_int = int(temp_int)

    # clear weather conditions
    if (s == "Sunny" or s == "Clear") and temp_int >= 20 and w == ".":
        print(results[0])
    # issues with launch
    else:
        print(results[1])
        
        # too cold
        if temp_int < 20:
            print(results[2])
        # cloudy
        if (s != "Sunny" and s != "Clear"):
            print(results[3])
        # weather conditions
        if w != ".":
            print(results[4])


# enter city name
city = input("Which city would you like to check? ")
 
# create url
url = "https://www.google.com/search?q="+"weather"+city
 
# request instance
html = requests.get(url).content

# get raw data
soup = BeautifulSoup(html, 'html.parser')

try:
# temperature
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    
    # time and sky description
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # format data
    data = str.split('\n')
    time = data[0]
    sky = data[1]


    # list having all div tags having particular class name
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    
    # particular list with required data
    strd = listdiv[5].text
    
    # formatting the string
    pos = strd.find('Wind')
    other_data = strd[pos:]


    # printing all the data
    print("Temperature is", temp)
    print("Time: ", time)
    print("Sky Description: ", sky)
    print(other_data)

    # print(weather_check(temp, sky, other_data))

    weather_check(temp, sky, other_data)

except:
    print("City not found")
