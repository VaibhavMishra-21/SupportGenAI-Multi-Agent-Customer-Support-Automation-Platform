from agents.intent_agent import IntentAgent
from agents.sentiment_agent import SentimentAgent
from agents.knowledge_agent import KnowledgeAgent
from agents.response_agent import ResponseAgent
from agents.supervisor_agent import SupervisorAgent
from agents.escalation_agent import EscalationAgent

intent_agent = IntentAgent()

sentiment_agent = SentimentAgent()

knowledge_agent = KnowledgeAgent()

response_agent = ResponseAgent()

supervisor_agent = SupervisorAgent()

escalation_agent = EscalationAgent()


def run_support_workflow(query):

    intent = intent_agent.detect(query)

    sentiment = sentiment_agent.analyze(query)

    context = knowledge_agent.retrieve(intent)

    response = response_agent.create_response(
        query,
        context
    )

    confidence = supervisor_agent.validate(
        response
    )

    escalated = escalation_agent.check(
        sentiment,
        confidence
    )

    return {
        "intent": intent,
        "sentiment": sentiment,
        "response": response,
        "confidence": confidence,
        "escalated": escalated
    }
