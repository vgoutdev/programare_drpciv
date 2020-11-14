import requests
import datetime
import time
from win10toast import ToastNotifier

#registration
#URL = 'https://www.drpciv.ro/drpciv-booking-api/getAvailableDaysForSpecificService/8/22'
#transcription
URL = 'https://www.drpciv.ro/drpciv-booking-api/getAvailableDaysForSpecificService/4/22'

#counties
counties_URL = 'https://www.drpciv.ro/drpciv-booking-api/counties'



DATE_LIMIT = datetime.datetime.strptime('2020-12-01 00:00:00','%Y-%m-%d %H:%M:%S').date()
notif = ToastNotifier()

while True:
    r = requests.get(URL)
    date_time_obj = datetime.datetime.strptime(r.json()[0],'%Y-%m-%d %H:%M:%S')
    print(date_time_obj.date())
    if(date_time_obj.date() < DATE_LIMIT):
        print("Fa programare")
        notif.show_toast("DRPCIV", f'Fa programare {date_time_obj.date()}', duration = 20) 
    else:
        print("Mai asteapta")
    time.sleep(10)


    