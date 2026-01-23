import subprocess


class DockerLogsTool:
    name = "logs"

    def run(self, container_id=None, lines=200):
        if not container_id:
            return {"error": "container_id required"}

        cmd = ["docker", "logs", "--tail", str(lines), container_id]
        logs = subprocess.check_output(cmd).decode()

        return {
            "container_id": container_id,
            "logs": logs
        }
