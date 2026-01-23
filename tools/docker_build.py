import subprocess


class DockerBuildTool:
    name = "build"

    def run(self, tag="app:latest", context="."):
        cmd = ["docker", "build", "-t", tag, context]
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
        return {
            "image": tag,
            "build_log": output
        }
