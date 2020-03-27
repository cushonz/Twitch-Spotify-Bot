import os
import time
from datetime import datetime


class Utility:
    # Format with milliseconds: "%Y%m%d-%H%M%S-%f"
    # Format without milliseconds: "%Y%m%d-%H%M%S"
    timeFormat = '%Y%m%d-%H%M%S'

    def getCred(redirectUri='http://localhost/'):
        with open(os.path.expanduser('~/.spotify'), 'r') as file:
            content = file.read()
            if '\r' in content:
                data = content.split('\r\n')
            else:
                data = content.split('\n')
            os.environ["SPOTIPY_CLIENT_ID"] = data[1]
            os.environ["SPOTIPY_CLIENT_SECRET"] = data[2]
            os.environ["SPOTIPY_REDIRECT_URI"] = redirectUri
            return {'userName': data[0], 'clientId': data[1], 'clientSecret': data[2]}

    def getTimestamp(override=timeFormat):
        return datetime.now().strftime(override)

    def processInput(dividers, removes, searchString):
        for remove in removes:
            searchString = searchString.replace(remove[0], remove[1])
        for item in dividers:
            if item in searchString:
                return [x.strip() for x in searchString.split(item)]
        return [searchString]

    def sleep(seconds):
        time.sleep(seconds)