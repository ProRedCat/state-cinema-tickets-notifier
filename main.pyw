import time
import random

import datetime

from log import *
from notify import *
from checkmovies import *

def main():
    # server = None
    titles = loadTitles()

    while (True):
        if(inOpenHours(datetime.datetime.now().time())):
            queriedTitles = getMovieTitles()

            for title in queriedTitles:
                if(title not in titles):
                    # if(server == None):
                        # server = connectToEmailServer()

                    subject = "{} Avaliable Now!".format(title)
                    body = "The movie {} have tickets avaliable now at State Cinemas".format(title)
                    # message = createEmail(subject, body)
                    
                    sendEmail(subject, body)

                    # sendEmail(server, message)

                    logTitle(title)
                    titles.add(title)

            # if(server != None):
                # disconnectEmailServer(server)
                # server = None
        
        time.sleep(900 + random.randint(-60, 60))
    
if __name__ == "__main__":
    main()
