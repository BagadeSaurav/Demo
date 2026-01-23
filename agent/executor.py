class Executor:
    """
    Execute docker tools in ordered plan.
    """

    def __init__(self):
        pass

    def execute(self, steps: list, selector, feedback):
        results = []

        for step in steps:
            tool = selector.select(step)

            if not tool:
                results.append({
                    "step": step,
                    "status": "no-tool",
                    "error": "No matching tool"
                })
                continue

            try:
                output = tool.run()
                results.append({
                    "step": step,
                    "status": "ok",
                    "output": output
                })

            except Exception as e:
                results.append({
                    "step": step,
                    "status": "error",
                    "error": str(e)
                })
                feedback.handle_error(step, e)

        return results
