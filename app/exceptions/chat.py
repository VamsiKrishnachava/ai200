

class ChatNoMessageException(Exception):
    def __init__(self, message: str = "Message cannot be empty."):
        self.message = message
        super().__init__(self.message)