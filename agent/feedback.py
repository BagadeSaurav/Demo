class FeedbackLoop:
    """
    Feedback from Claude for self-correction.
    """

    def __init__(self, llm_client):
        self.llm = llm_client

    def handle_error(self, step, err):
        print(f"[Feedback] Step failed: '{step}' → {err}")

    def verify(self, results):
        """
        Optional validation stage (future).
        """
        summary = "\n".join(
            f"{r['step']} = {r['status']}" for r in results
        )

        vp = f"""
Verify if the following execution results for a Docker agent make sense:

{summary}

Just reply 'valid' or 'fix needed'.
"""
        return self.llm.invoke(vp)
