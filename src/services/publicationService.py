from src.services.messageService import messageService, message

class publicationService(messageService):
    def __init__(self):
        super().__init__()

class publicationMessage(message):
    def __init__(self):
        super().__init__()
