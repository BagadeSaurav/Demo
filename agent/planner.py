class Planner:
    """
    Converts a natural user prompt into
    step-by-step executable plan using Claude.
    """

    def __init__(self, llm_client):
        self.llm = llm_client

    def make_plan(self, user_prompt: str) -> list:
        plan_prompt = f"""
Convert the following user request into a list of execution steps
for a Docker agent. Only return the steps. No explanation.

User prompt:
{user_prompt}
"""
        plan_txt = self.llm.invoke(plan_prompt)
        return self._parse(plan_txt)

    def _parse(self, raw: str) -> list:
        steps = []
        for line in raw.split("\n"):
            line = line.strip(" -•\t")
            if line:
                steps.append(line)
        return steps
