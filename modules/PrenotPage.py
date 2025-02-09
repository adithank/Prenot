import sys

class PrenotPage:

    def __init__(self):

        self._url = 'https://prenotami.esteri.it/Services/Booking/4996'

        self._locators = {
            'login': {
                'BY': 'ID', # How to locate the elements
                'LOGIN_EMAIL': "login-email", # By.ID
                'LOGIN_PASSWORD': "login-password" # By.ID
            },
            'user_area': {
                'BY': 'LINK_TEXT', # How to locate the elements
                'USERAREA_PRENOTA': 'Prenota' # By.LINK_TEXT
            },
            'calendar': {
                'BY': 'XPATH', # How to locate the elements
                'FORWARD': '//*[@id="datetimepicker"]/div/ul/ul/div/div[1]/table/thead/tr[1]/th[3]/span',
                'BACKWARD': '//*[@id="datetimepicker"]/div/ul/ul/div/div[1]/table/thead/tr[1]/th[1]/span',
                'MONTH': '//*[@id="datetimepicker"]/div/ul/ul/div/div[1]/table/thead/tr[1]/th[2]',
                'GREEN_DAYS': 'day.availableDay', # The class name of the green days in the calendar
                'HOURS': 'fascia.act', # The class name of the hours button
                'OTP': '//*[@id="idOtp"]',
                'OTP_OK': '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button[3]',
                'SUBMIT': '/html/body/main/div[2]/div/div[2]/button'

            }
        }
        
        return None
    
    def get_locator(self, name=''):
        # self.__check_args(name, str)
        self._service_name = name.lower()

        if name not in self._locators.keys():
            print('Name is wrong. Shutting down.')
            sys.exit()

        return self._locators[name]

    def get_url(self):
        return self._url