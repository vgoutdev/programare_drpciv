import requests
import datetime
import time
from win10toast import ToastNotifier
import urls
import operations


class Drpciv():

    def __init__(self, operation = 'vehicleFirstRegistration', county = 'IS' ):
        self.county = self.__get_county(county)
        self.available = operations.available
        self.operation = self.__get_operation(operation)
        self.operation_desc = operation
        self.booking = urls.BOOKING_URL

    def check_drpciv_earliest_date(self, county: str = None, operation: str = None) -> datetime:
        if operation is None:
            operation = self.operation
        else:
            operation = self.__get_operation(operation)
        if county is None:
            county = self.county
        else:
            county = self.__get_county(county)
        req_earliest = requests.get(urls.GET_AVAILABLE + str(operation) + '/' + str(county))
        date_time_obj = datetime.datetime.strptime(req_earliest.json()[0],'%Y-%m-%d %H:%M:%S')
        return date_time_obj.date()

    def __get_county(self, county: str) -> str:
        req_county = requests.get(urls.GET_COUNTIES)
        county_id = req_county.json()[county]
        return county_id

    def __get_operations(self) -> tuple:
        req_operation = requests.get(urls.GET_OPERATIONS + str(self.county))
        response_operation = req_operation.json()
        return (response_operation,self.county)
    
    def __get_operation(self, operation) -> str:
        if(operation not in self.available):
            raise Exception("Not an available operation")
        else:
            return self.available[operation]

    def check_all_operations(self) -> str:
        operations = self.__get_operations()
        dict_oper = {}
        for operation in operations[0]:
            date = self.check_drpciv_earliest_date(operation['code'],operations[1])
            dict_oper[operation['description']] = str(date)
        return dict_oper
    
    def generate_booking_form(self) -> str:
        return self.booking + '/' + self.county + self.operation_desc