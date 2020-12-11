import requests
import datetime
import time
from win10toast import ToastNotifier
import urls


#DATE_LIMIT = datetime.datetime.strptime('2020-12-01 00:00:00','%Y-%m-%d %H:%M:%S').date()
#notif = ToastNotifier()

def check_drpciv_earliest_date(URL: str, operation: str, county_id: str) -> datetime:
    req_earliest = requests.get(urls.GET_OPERATIONS + operation + '/' + county_id)
    date_time_obj = datetime.datetime.strptime(req_earliest.json()[0],'%Y-%m-%d %H:%M:%S')
    return date_time_obj.date()

def get_county(county: str) -> str:
    req_county = requests.get(urls.GET_COUNTIES)
    county_id = req_county.json()[county]
    return county_id

def get_operation(oper: str, county: str) -> str:
    county_id = get_county(county)
    req_operation = requests.get(urls.GET_OPERATIONS + county_id)
    response_operation = req_operation.json()
    return response_operation

print(get_county('IS'))

"""while True:
    r = requests.get(URL)
    date_time_obj = datetime.datetime.strptime(r.json()[0],'%Y-%m-%d %H:%M:%S')
    print(date_time_obj.date())
    if(date_time_obj.date() < DATE_LIMIT):
        print("Fa programare")
        notif.show_toast("DRPCIV", f'Fa programare {date_time_obj.date()}', duration = 20) 
    else:
        print("Mai asteapta")
    time.sleep(10)
"""

    