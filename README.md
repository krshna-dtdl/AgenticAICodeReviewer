# Code Review Agent Executor

This repository contains a toolset for reviewing Python code against PlantUML (PUML) designs. The solution integrates machine learning agents to assess code correctness, syntax validation, and design alignment through automated review and correction mechanisms.

## Table of Contents
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
.
├── main.py                      # Entry point for running the agent executor
├── prompts.py                   # Templates for prompting the agents
├── requirements.txt             # List of required Python packages
├── agent_executor/              # Contains the agent executor logic
│   └── agent.py                 # Factory for creating and configuring agent executors
├── design_comparison/           # Tools for comparing code with PUML designs
│   └── design_checker.py        # Design comparison and correction tool
├── tools/                        # Utility tools for code execution and content fetching
│   ├── code_executor.py         # Tool for executing Python code
│   └── url_fetcher.py           # Tool for fetching content from URLs
```

## Features
- Automated code review against PUML designs
- Syntax error detection and correction
- Execution of Python code snippets
- Fetching code and design content from external URLs
- Intelligent suggestions for aligning code with design patterns

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/code-review-agent-executor.git
   cd code-review-agent-executor
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the agent executor using:
   ```bash
   python main.py
   ```

2. The agent will:
   - Fetch Python code and PUML design from provided URLs.
   - Evaluate the code’s alignment with the design.
   - Detect and fix syntax errors or logical discrepancies.

3. The output will be printed to the console, including analysis and corrected code if any issues are found.

## Dependencies

The project requires the following packages:

- `langchain` - For building agents and managing prompts.
- `openai` - For using OpenAI language models.
- `requests` - For fetching content from URLs.
- `python-dotenv` - For managing environment variables.

Refer to the `requirements.txt` file for the complete list of dependencies.

## Customization

### Adjusting the Language Model

To change the language model used by the agent, modify the `AgentExecutorFactory` class in `agent_executor/agent.py`:

```python
self.llm = ChatOpenAI(model_name="your-preferred-model", temperature=1)
```

### Updating Prompt Templates

You can customize the review and comparison logic by editing the templates in `prompts.py`.

## Contributing

We welcome contributions to improve this project. If you have suggestions for enhancements or bug fixes, please fork the repository and submit a pull request.


