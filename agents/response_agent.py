from services.gemini_service import generate

class ResponseAgent:

    def create_response(
        self,
        query,
        context
    ):

        prompt = f"""
        Customer Query:
        {query}

        Context:
        {context}

        Generate a professional support response.
        """

        return generate(prompt)
