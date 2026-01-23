#!/usr/bin/env python3
import sys
import readline

from agent import AgentBrain, Planner, IntentClassifier, ToolSelector, Executor, FeedbackLoop
from models.bedrock import BedrockClaudeClient

# Tools
from tools.docker_list import DockerListTool
from tools.docker_build import DockerBuildTool
from tools.docker_run import DockerRunTool
from tools.docker_stop import DockerStopTool
from tools.docker_logs import DockerLogsTool
from tools.file_writer import FileWriterTool


def build_tool_registry():
    return {
        "list": DockerListTool(),
        "build": DockerBuildTool(),
        "run": DockerRunTool(),
        "stop": DockerStopTool(),
        "logs": DockerLogsTool(),
        "write": FileWriterTool(),
    }


def process_prompt(prompt: str):
    # core logic
    llm = BedrockClaudeClient()
    brain = AgentBrain(llm)
    planner = Planner(llm)
    intents = IntentClassifier(llm)
    selector = ToolSelector(build_tool_registry())
    executor = Executor()
    feedback = FeedbackLoop(llm)

    print(f"[intent] {intents.detect(prompt)}")

    steps = planner.make_plan(prompt)
    print(f"[plan] {steps}")

    results = executor.execute(steps, selector, feedback)
    print("[results]")
    for r in results:
        print(r)

    print("[verify]")
    print(feedback.verify(results))


def chat_mode():
    print("Docker Agent Chat Mode (type 'exit' to quit)")
    while True:
        try:
            prompt = input("agent> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nexit")
            break

        if not prompt:
            continue
        if prompt.lower() in ["exit", "quit"]:
            break

        process_prompt(prompt)


def one_shot_mode(text: str):
    process_prompt(text)


def main():
    if len(sys.argv) > 1:
        one_shot_mode(" ".join(sys.argv[1:]))
    else:
        chat_mode()


if __name__ == "__main__":
    main()
