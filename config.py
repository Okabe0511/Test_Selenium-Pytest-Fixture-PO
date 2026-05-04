import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR, 'Log')
REPORT_DIR = os.path.join(BASE_DIR, 'Report')
SCREENSHOT_DIR = os.path.join(REPORT_DIR, 'screenshots')

BASE_URL = 'http://localhost:8777'
LOGIN_URL = BASE_URL + '/#/login'
MAIN_URL = BASE_URL + '/#/home/list'
CREATE_URL = BASE_URL + '/#/home/create'




EXPLICIT_WAIT = 10

BROWSER = 'Firefox'

GECKODRIVER_PATH = r'A:\webdriver\geckodriver.exe'

HEADLESS = False

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
