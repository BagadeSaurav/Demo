import subprocess


class DockerStopTool:
    name = "stop"

    def run(self, container_id=None):
        if not container_id:
            return {"error": "container_id required"}

        subprocess.check_output(["docker", "stop", container_id])
        subprocess.check_output(["docker", "rm", container_id])

        return {
            "container_id": container_id,
            "status": "stopped"
        }
