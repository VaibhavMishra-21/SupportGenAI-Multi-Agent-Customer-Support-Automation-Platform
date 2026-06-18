class IntentAgent:

    def detect(self, query):

        query = query.lower()

        if "refund" in query:
            return "billing"

        if "password" in query:
            return "technical"

        if "subscription" in query:
            return "account"

        if "cancel" in query:
            return "cancellation"

        return "general"
