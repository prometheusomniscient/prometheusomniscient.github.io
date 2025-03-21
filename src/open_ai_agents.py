
from typing import Any, List, Optional
from base_model import BaseAgent
from agents import Agent, Runner, WebSearchTool
from agents.model_settings import ModelSettings




def get_agent_instance(name: str, model_type: Optional[str], instructions: Optional[str], tools: Optional[List[Any]]) -> Agent:
    if not tools:
        return  Agent(name=name, instructions=instructions,  model=model_type)
    return Agent(name=name, instructions=instructions,  model=model_type, tools=tools)




class BaseOpenAiAgent(BaseAgent):

    def __init__(self, model_type:str) -> None:
        super().__init__(ai_company='open_ai', model_type=model_type) 
        self.agent: Agent = None 



    def act(self, query: str) -> Any:
        return Runner.run_sync(self.agent, query)
    




class WebAgent(BaseOpenAiAgent):
    def __init__(self, model_type: str) -> None:
        super().__init__(model_type)  
        self.agent =  Agent(name="WebAgent",instructions="Search the internet for the given prompts.",tools=[WebSearchTool()],model_settings=ModelSettings(tool_choice="required"),)




    def act(self, query: str) -> Any:
        return Runner.run_sync(self.agent, query)
    



if __name__ == "__main__": 

    web = WebAgent(model_type="web agent")

    results = web.act("give me 10 real estate listings in the state of NY that have over 1,000,000 acres.")
    print(results)



