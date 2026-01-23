import subprocess
import json


class DockerListTool:
    name = "list"

    def run(self):
        cmd = ["docker", "ps", "--format", "{{json .}}"]
        output = subprocess.check_output(cmd).decode().strip().split("\n")

        containers = [json.loads(line) for line in output if line]

        formatted = []
        for c in containers:
            formatted.append({
                "name": c.get("Names"),
                "image": c.get("Image"),
                "status": c.get("Status"),
                "ports": c.get("Ports") or "none"
            })

        return formatted
