import boto3
import yaml
import json
import os


class BedrockClaudeClient:
    """
    Wrapper for invoking Claude 3.5 Sonnet via AWS Bedrock.
    config.yaml provides:
       bedrock.region
       bedrock.model
    """

    def __init__(self, config_path="config.yaml"):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config missing: {config_path}")

        with open(config_path, "r") as f:
            cfg = yaml.safe_load(f)

        self.region = cfg.get("bedrock", {}).get("region", "us-east-1")
        self.model = cfg.get("bedrock", {}).get("model", "anthropic.claude-3-5-sonnet-v1")

        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=self.region
        )

    def invoke(self, prompt: str) -> str:
        """
        Invoke Claude with simple text prompt.
        Returns plain string text output.
        """

        try:
            body = json.dumps({
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 2048,
                "temperature": 0.2
            })

            resp = self.client.invoke_model(
                modelId=self.model,
                accept="application/json",
                contentType="application/json",
                body=body
            )

            payload = resp.get("body").read().decode("utf-8")
            return self._extract(payload)

        except Exception as e:
            return f"[Bedrock Error] {e}"

    def _extract(self, payload: str) -> str:
        """
        Extracts Claude 3.5 text output from JSON
        """
        try:
            parsed = json.loads(payload)
            blocks = parsed.get("content", [])
            text = "".join(b.get("text", "") for b in blocks)
            return text.strip()
        except Exception:
            return payload.strip()
