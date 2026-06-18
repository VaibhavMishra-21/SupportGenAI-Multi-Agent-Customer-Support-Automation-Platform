import uuid

class TicketService:

    @staticmethod
    def create_ticket():

        return str(uuid.uuid4())[:8]
