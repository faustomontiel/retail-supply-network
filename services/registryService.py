from services.messageService import messageService, message

class registryService(messageService):
    def __init__(self):
        self._registered = None
        super().__init__()

class registryMessage(message):
    def __init__(self):
        super().__init__()
