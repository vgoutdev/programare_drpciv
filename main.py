import drpciv
import alerts
import datetime

if __name__ == '__main__':
    date_limit = datetime.datetime.strptime('2021-03-20 00:00:00','%Y-%m-%d %H:%M:%S').date()
    alerts.win10alert(date_limit,'vehicleFirstRegistration','IS')
