from src.utils.logs import logs

class messageService:
    def __init__(self):
        self._logs = logs("messageService.log")
    
    def testLog(self):
        self._logs.doLog("Testeando...")

class message:        
    #idMessage
    @property
    def idMessage(self):
        return self._idMessage
    
    @idMessage.setter
    def idMessage(self, value):
        self._idMessage = value

    #sender
    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, value):
        self._sender = value

    #receiver
    @property
    def receiver(self):
        return self._receiver
    
    @receiver.setter
    def receiver(self, value):
        self._receiver = value

    #ownerGln
    @property
    def ownerGln(self):
        return self._ownerGln
    
    @ownerGln.setter
    def ownerGln(self, value):
        self._ownerGln = value

    #dataRecipient
    @property
    def dataRecipient(self):
        return self._dataRecipient
    
    @dataRecipient.setter
    def dataRecipient(self, value):
        self._dataRecipient = value

    #gtin
    @property
    def gtin(self):
        return self._gtin
    
    @gtin.setter
    def gtin(self, value):
        self._gtin = value

    #dateTime
    @property
    def dateTime(self):
        return self._dateTime
    
    @dateTime.setter
    def dateTime(self, value):
        self._dateTime = value

    def __init__(self):
        self._idMessage = None
        self._sender = None
        self._receiver = None
        self._ownerGln = None
        self._dataRecipient = None
        self._gtin = None
        self._dateTime = None
