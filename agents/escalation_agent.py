class EscalationAgent:

    def check(
        self,
        sentiment,
        confidence
    ):

        if sentiment == "negative":
            return True

        if confidence < 0.50:
            return True

        return False
