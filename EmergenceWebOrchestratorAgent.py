# EmergenceWebOrchestratorAgent.py

import os
import time
import uuid
import requests
from dotenv import load_dotenv

from autogen import AssistantAgent

# Load environment variables from .env file
load_dotenv()

class EmergenceWebOrchestratorAgent(AssistantAgent):
    """
    A custom agent that calls Emergence AI's web orchestrator,
    creates a workflow, polls until complete, and outputs the result.
    """

    def __init__(self, name="emergence_web_agent", **kwargs):
        super().__init__(name=name, **kwargs)
        self.emergence_api_key = os.getenv("EMERGENCE_API_KEY")
        self.base_url = "https://api.emergence.ai/v0/orchestrators/em-orchestrator/workflows"
        
        if not self.emergence_api_key:
            print("WARNING: No EMERGENCE_API_KEY found in .env file. Please add it to your .env file.")

    def run(self, prompt: str) -> str:
        """Runs the Emergence web orchestrator with the given prompt."""
        if not self.emergence_api_key:
            return "No Emergence API Key configured. Please set EMERGENCE_API_KEY."

        headers = {
            "apikey": self.emergence_api_key,
            "Content-Type": "application/json",
            "Client-ID": str(uuid.uuid4())
        }

        # Step A: Create the workflow
        try:
            create_resp = requests.post(
                self.base_url,
                headers=headers,
                json={"prompt": prompt},
                timeout=30
            )
            create_resp.raise_for_status()

            resp_data = create_resp.json()
            workflow_id = resp_data["workflowId"]
            print(f"[Emergence Agent] Created workflow: {workflow_id}")
        except Exception as e:
            return f"Error creating Emergence workflow: {str(e)}"

        # Step B: Poll until success/fail
        poll_url = f"{self.base_url}/{workflow_id}"
        poll_count = 1

        while True:
            print(f"[Emergence Agent] Polling attempt {poll_count}...")
            poll_count += 1
            time.sleep(15)  # Wait 15s between polls

            try:
                poll_resp = requests.get(poll_url, headers=headers, timeout=30)
                poll_resp.raise_for_status()

                response_json = poll_resp.json()
                data_obj = response_json.get("data", {})
                status = data_obj.get("status", "UNKNOWN")

                if status == "SUCCESS":
                    # Return the final textual result from "output"
                    return data_obj.get("output", "No output provided by Emergence.")
                elif status in ("FAILED", "TIMEOUT"):
                    return f"Workflow ended with status {status}"

            except Exception as e:
                return f"Polling error: {str(e)}"
