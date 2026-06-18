import json

class KnowledgeAgent:

    def retrieve(self, intent):

        with open(
            "knowledge_base/faq.json",
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        return data.get(
            intent,
            "No relevant information found."
        )
