class IntentClassifier:
    """
    Determine user's main intent:
    inspect, build, run, stop, logs, write
    """

    def __init__(self, llm_client):
        self.llm = llm_client

    def detect(self, prompt: str) -> str:
        intent_prompt = f"""
Classify the user intent for a Docker agent.
Possible intents: inspect, build, run, stop, logs, write

User prompt:
{prompt}

Return just one label.
"""
        intent = self.llm.invoke(intent_prompt).strip().lower()
        return intent
