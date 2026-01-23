# Docker Agent AI (ChatGPT-like Agent for Docker)

This project provides a natural language interface for Docker using Claude 3.5 Sonnet via AWS Bedrock.

## Features

- ChatGPT-like interface
- Planning + tool execution
- Dockerfile generation
- docker ps / logs / run / build / stop
- Chat mode + one-shot CLI
- Fully local docker execution

## Requirements

- Ubuntu 24.04 (recommended)
- Python 3.12
- Docker installed
- AWS CLI configured
- Bedrock access enabled (Claude 3.5)

## Installation

```bash
sudo apt update
sudo apt install -y docker.io python3-venv awscli
git clone https://github.com/yourname/docker-agent-ai
cd docker-agent-ai
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
aws configure
