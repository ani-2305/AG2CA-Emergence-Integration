# AutoGen CaptainAgent and Emergence AI Web Orchestrator Integration

This repository demonstrates how to integrate [AutoGen](https://github.com/microsoft/autogen) with [Emergence AI's Web Orchestrator](https://api.emergence.ai/). Originally designed for **AutoGen's CaptainAgent**, this implementation uses **AutoGen's AssistantAgent** for agent-based automation and **Emergence AI** for web automation workflows, providing similar functionality with enhanced reliability.

---

## Project Overview

- **`EmergenceWebOrchestratorAgent.py`**: Main Python file that:
  1. Extends AutoGen's `AssistantAgent` class
  2. Handles API communication with Emergence AI's web orchestrator
  3. Creates and polls Emergence AI web workflows
  4. Returns workflow results

- **`main.py`**: Entry point that:
  1. Creates the EmergenceWebOrchestratorAgent
  2. Sets up the AssistantAgent with function calling capabilities
  3. Creates a UserProxyAgent for handling user interactions
  4. Takes user input and initiates the conversation

- **`.env`**: Configuration file containing:
  - Emergence AI API key
  - OpenAI API settings
  - Model parameters

- **`requirements.txt`**: Python dependencies.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ag2ca-integration.git
cd ag2ca-integration
```

### 2. Create a Python Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

*(On Windows PowerShell: `.\.venv\Scripts\activate`)*

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- [AutoGen](https://github.com/microsoft/autogen)
- [Requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

### 4. Set Up Environment Variables

Create a `.env` file in the root directory with the following configuration:

```bash
# Emergence AI Configuration
EMERGENCE_API_KEY=your-emergence-key

# OpenAI Configuration
OPENAI_API_KEY=your-openai-key
OPENAI_MODEL=gpt-4o
OPENAI_TEMPERATURE=0.7
```

### 5. Run the Script

```bash
python main.py
```

When prompted, enter a **web automation prompt**—for instance:
```
What is the state of the VC space right now?
```

The script will:
1. Send your query to the Emergence Web Orchestrator
2. Poll for results
3. Display the formatted response
4. Automatically terminate the conversation

Example output:
```
[Emergence Agent] Created workflow: workflow-id
[Emergence Agent] Polling attempt 1...
[Emergence Agent] Polling attempt 2...
[Response with formatted information]
TERMINATE
```

### 6. Verify or Debug

- If you see `No Emergence API Key found in .env file`, check your `.env` file configuration
- If you see "Error creating Emergence workflow," verify your:
  - Internet connection
  - Emergence AI subscription status
  - API key validity

---

## File-by-File Summary

- **`EmergenceWebOrchestratorAgent.py`**  
  Defines a custom AutoGen agent that integrates with Emergence AI. Shows how to:
  1. Extend AutoGen's AssistantAgent class
  2. Create and poll Emergence web workflows
  3. Handle API communication and response processing

- **`main.py`**  
  Entry point that demonstrates how to:
  1. Set up the necessary agents (AssistantAgent, EmergenceWebOrchestratorAgent, UserProxyAgent)
  2. Configure function calling capabilities
  3. Handle user input and agent interactions

- **`.env`**  
  Configuration file containing Emergence AI API key and OpenAI settings.

- **`requirements.txt`**  
  Lists all Python dependencies needed for the project.

---

## Key Features

1. **AutoGen Integration**: Uses AutoGen's powerful agent framework for orchestrating conversations and tasks.
2. **Function Calling**: Leverages OpenAI's function calling capabilities for structured interactions.
3. **Custom Emergence Agent**: Implements a custom agent that interfaces with Emergence AI's web orchestrator.
4. **Web Automation**: Enables complex web automation tasks through natural language commands.
5. **Flexible Configuration**: Easy configuration of both OpenAI and Emergence AI settings.

---

## Contributing

Feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit pull requests

Please ensure you update tests and documentation for any new features.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Acknowledgments

- [AutoGen](https://github.com/microsoft/autogen) team for their excellent agent framework
- [Emergence AI](https://emergence.ai/) for their web automation platform 