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
            print("Fa programare")
            notif.show_toast("DRPCIV", f'Fa programare {return_date}', duration = 20) 
            return return_date
        else:
            print("Wait")
        time.sleep(10)
