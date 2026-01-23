class AgentBrain:
    """
    Wraps Bedrock Claude as agent reasoning module.
    """

    def __init__(self, llm_client):
        self.llm = llm_client

    def think(self, prompt: str) -> str:
        """
        Primary reasoning call.
        """
        return self.llm.invoke(prompt)

    def reflect(self, context: str) -> str:
        """
        Reflection / verification stage.
        """
        rp = f"Reflect on this execution and improve if needed:\n{context}"
        return self.llm.invoke(rp)
