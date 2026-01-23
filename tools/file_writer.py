from pathlib import Path


class FileWriterTool:
    name = "write"

    def run(self, filename="Dockerfile", content=""):
        ws = Path("workspace")
        ws.mkdir(exist_ok=True)

        path = ws / filename
        path.write_text(content)

        return {"file": str(path), "status": "written"}
