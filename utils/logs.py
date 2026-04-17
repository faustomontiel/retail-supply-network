import datetime as dt
import os

class logs:
    @property
    def logFileName(self):
        return self._logFileName
    
    def __init__(self, fileName = None):
        self._logFileName = None
        self._logDir = "./logs/"
        self._dayStarted = dt.datetime.now().day
         
        if not os.path.exists(self._logDir):
            os.makedirs(self._logDir) 
        
        if fileName is None:
            fileName = "app.log"
        self._logFileName = fileName


    def doLog(self, message):
        current_time = dt.datetime.now().strftime('%H:%M:%S')
        log_message = f'[{current_time}] {message}'
    
        dest = self._logDir + self._logFileName

        with open(dest, 'a') as file:
            file.write(log_message + '\n') 
