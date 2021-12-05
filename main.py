import time

from notify import *
from checkmovies import *

def main():
    #titles = loadTitles()
    titles = set()

    server = None
    while (True):
        queriedTitles = getMovieTitles()

        for title in queriedTitles:
            if(title not in titles):
                if(server == None):
                    server = connectToEmailServer()

                subject = "{} Avaliable Now!".format(title)
                body = "The movie {} have tickets avaliable now at State Cinemas".format(title)
                message = createEmail(subject, body)

                sendEmail(server, message)

                #logTitle(title)
                queriedTitles.add(title)

        if(server != None):
            disconnectEmailServer(server)
            server = None
        
        time.sleep(900)


    
if __name__ == "__main__":
    main()
