import requests
import datetime
import time
from win10toast import ToastNotifier
import urls
import drpciv


def win10alert(date_limit: datetime.datetime, operation: str, county: str):
    drpciv_obj = drpciv.Drpciv(operation, county)
    notif = ToastNotifier()
    while True:
        return_date = drpciv_obj.check_drpciv_earliest_date()
        if(return_date < date_limit):
            print(f'make the appointment dude {return_date}')
            notif.show_toast("DRPCIV", f'Fa programare {return_date}', duration = 20) 
            return return_date
        else:
            print(f'Wait. The earlist date you can make an appointment is {return_date}')
        time.sleep(10)
