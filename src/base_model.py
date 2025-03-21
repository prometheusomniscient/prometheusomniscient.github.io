from abc import ABC, abstractmethod




class BaseAgent(ABC):


    def __init__(self, ai_company: str,   model_type : str, ) -> None:
        self.comp = ai_company
        self.model_type = model_type


    @abstractmethod
    def act(self) -> None:
        pass




class ManagerAgent(BaseAgent):


    def __init__(self, ai_company: str, model_type: str) -> None:
        super().__init__(ai_company, model_type)





"""
The open_ai_agents.py file defines classes and functions related to creating and using AI agents for specific tasks. Here's a summary:

Imports: The file imports necessary modules and classes from other parts of the project and type hints.

Function get_agent_instance: This function creates and returns an instance of the Agent class, optionally with tools.

Class BaseOpenAiAgent: This class inherits from BaseAgent and initializes an agent for OpenAI models. It includes a method act to run a query using the agent.

Class WebAgent: Inherits from BaseOpenAiAgent, initializes an agent specifically designed to search the internet using a WebSearchTool. It overrides the act method to run queries with this web search agent.

Main Execution: If the script is run as the main program, it creates an instance of WebAgent and uses it to search for real estate listings in NY with specific criteria, then prints the results.

This file is primarily concerned with setting up and using different types of AI agents for various tasks.
"""
