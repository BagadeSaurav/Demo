import subprocess


class DockerRunTool:
    name = "run"

    def run(self, image="app:latest", ports=None):
        cmd = ["docker", "run", "-d"]

        if ports:
            for host, container in ports.items():
                cmd.extend(["-p", f"{host}:{container}"])

        cmd.append(image)

        container_id = subprocess.check_output(cmd).decode().strip()

        return {
            "container_id": container_id,
            "image": image
        }
