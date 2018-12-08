from darksky import forecast
from datetime import date, timedelta
from pprint import pprint


key = '55ed40fb4bf86853b3d56b83522665b7'

# champaign = forecast(key, 40.1164, 88.2434)
# auckland = forecast(key, 36.8485, 174.7633)
# madrid = forecast(key, 40.4168, 3.7038)
# prague = forecast(key, 50.0755, 14.4378)
# santiago = forecast(key, 33.4489, 70.6693)
# kyoto = forecast(key, 35.0116, 135.7680)

locations = {
    "Saint charles": forecast(key, 41.9142, 88.3087),
    "Champaign": forecast(key, 40.1164, 88.2434),
    "Auckland": forecast(key, 36.8485, 174.7633),
    "Madrid": forecast(key, 40.4168, 3.7038),
    "Prague": forecast(key, 50.0755, 14.4378),
    "Santiago": forecast(key, 33.4489, 70.6693),
    "Kyoto": forecast(key, 35.0116, 135.7680)
}

for x in locations:
    print('Todays weather in ' + x + ' is ' + locations[x].summary + "\n")

weekday = date.today()
print('*************** Weekly forecast for Kyoto ***************')
for day in locations["Kyoto"].daily:
    print(date.strftime(weekday, '%a') + ": " + day.summary)
    print('     Range: ' + str(day.temperatureMax) + " to " + str(day.temperatureMin) + "\n")
    weekday += timedelta(1)