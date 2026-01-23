class ToolSelector:
    """
    Select matching docker tool for plan step.
    """

    def __init__(self, tool_registry: dict):
        self.tools = tool_registry

    def select(self, plan_step: str):
        if not plan_step:
            return None

        norm = plan_step.lower()

        # direct match
        if norm in self.tools:
            return self.tools[norm]

        mapping = {
            "list": ["list", "show", "ps", "inspect", "running", "containers"],
            "build": ["build", "image", "compile"],
            "run": ["run", "start", "launch", "execute"],
            "stop": ["stop", "kill", "remove"],
            "logs": ["logs", "stdout", "output"],
            "write": ["write", "create", "dockerfile", "file", "generate"],
        }

        for key, words in mapping.items():
            for w in words:
                if w in norm and key in self.tools:
                    return self.tools[key]

        # fallback match by key substring
        for key in self.tools.keys():
            if key in norm:
                return self.tools[key]

        return None

    def available(self):
        return list(self.tools.keys())
