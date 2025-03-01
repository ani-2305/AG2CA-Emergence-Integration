import os
from dotenv import load_dotenv
from autogen import UserProxyAgent, AssistantAgent
from EmergenceWebOrchestratorAgent import EmergenceWebOrchestratorAgent

# Load environment variables
load_dotenv()

def get_config_list():
    """Get OpenAI configuration list."""
    config_list = [{
        "model": os.getenv("OPENAI_MODEL", "gpt-4"),
        "api_key": os.getenv("OPENAI_API_KEY"),
        "temperature": float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
    }]
    return config_list

def main():
    # Load the configuration
    config_list = get_config_list()
    
    emergence_agent = EmergenceWebOrchestratorAgent(name="emergence_web_agent")

    # Create a wrapper function that properly handles the arguments
    def run_emergence_query(query: str) -> str:
        """Run a query through the Emergence Web Orchestrator."""
        return emergence_agent.run(query)

    # Define the function schema
    function_map = {
        "run_emergence_query": {
            "name": "run_emergence_query",
            "description": "Run a query through the Emergence Web Orchestrator to get real-time information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The query to send to the Emergence Web Orchestrator"
                    }
                },
                "required": ["query"]
            }
        }
    }

    emergence_ca_system_message = """You are an AI assistant tasked with answering questions using the Emergence Web Orchestrator.
    You have access to a function named 'run_emergence_query' that takes a query string as input.
    For any question or task, you should use this function to get the most up-to-date and accurate information.
    
    When using run_emergence_query, prefer to use the user's exact query text when possible, only rephrase if necessary to get better results.
    Always use the function before providing an answer.
    Do not ask for user input aside from asking for the user query.
    Only output your response to the user query.
    After providing your response, end with 'TERMINATE' on a new line to signal the end of the conversation."""

    # Create the Assistant Agent with function calling capabilities
    assistant = AssistantAgent(
        name="assistant",
        system_message=emergence_ca_system_message,
        llm_config={
            "config_list": config_list,
            "functions": [function_map["run_emergence_query"]]
        }
    )

    # Create the UserProxyAgent with function execution capability
    user_proxy = UserProxyAgent(
        name="user_proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=2,  # Reduced to prevent loops
        code_execution_config={"use_docker": False},
        function_map={
            "run_emergence_query": run_emergence_query  # Use the wrapper function
        }
    )

    # Get user input for the prompt
    user_prompt = input("Enter your prompt: ")

    print("\nAsking Assistant to handle the prompt using Emergence's orchestrator...\n")

    # Initiate the chat
    user_proxy.initiate_chat(
        assistant,
        message=user_prompt
    )

if __name__ == "__main__":
    main()