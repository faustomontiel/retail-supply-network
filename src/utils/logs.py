import datetime as dt
import os
import time

class Logs:
    @property
    def logFileName(self):
        return self._logFileName
    
    def __init__(self, fileName = None):
        self._logFileName = None
        self._logDir = "./logs/"
        self._formatted_date = dt.datetime.now().strftime("%Y-%m-%d")
        self._last_time = time.perf_counter()
    
         
        if not os.path.exists(self._logDir):
            os.makedirs(self._logDir) 
        
        if fileName is None:
            fileName = f"app_{self._formatted_date}.log"

        self._logFileName = fileName


    def doLog(self, message):
        now = time.perf_counter()
        delta = now - self._last_time
        self._last_time = now

        current_time = dt.datetime.now().strftime('%H:%M:%S')
        log_message = f'[{current_time}] (+{delta:.4f}s) {message}'
    
        dest = self._logDir + self._logFileName

        with open(dest, 'a') as file:
            file.write(log_message + '\n') 

class Error:
    
    def __init__(self):
        from src.utils.logs import Logs
        self._logs = Logs()

    def _errorReturn(self, message, **kwargs):
        result = {'error': message, **kwargs}
        self._logs.doLog(result)
        return result