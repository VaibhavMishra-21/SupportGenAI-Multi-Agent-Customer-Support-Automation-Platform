class SupervisorAgent:

    def validate(
        self,
        response
    ):

        score = len(response) / 100

        if score > 1:
            score = 1

        return round(score, 2)
