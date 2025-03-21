import json
from typing import Any, List, Optional
from base_model import BaseAgent
from agents import Agent, Runner, WebSearchTool
from agents.model_settings import ModelSettings
import re
import pandas as pd




def get_agent_instance(name: str, model_type: Optional[str], instructions: Optional[str], tools: Optional[List[Any]]=None) -> Agent:
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
    


class ParseAgent(BaseOpenAiAgent):
    def __init__(self, model_type) -> None:
        super().__init__(model_type) 
        self.agent = get_agent_instance(name ="Parser", model_type="gpt-3.5-turbo", instructions="You will be given a string of real estate listings. I want you to pasre the given string "
        "into a json style strin like this: [{}, {} ...]. For each listing make sure you include the price, acreage, and location")

    @staticmethod
    def format_json_string(text: str) -> str:
        return re.sub(r"^```json\s*|\s*```$", "", text.strip(), flags=re.DOTALL)


    def act(self, string_data: str) -> str:
        result = Runner.run_sync(self.agent,string_data )
        result = self.format_json_string(result.final_output)
        return json.loads(result)



if __name__ == "__main__": 

    web = WebAgent(model_type="web agent")
    parse = ParseAgent(model_type="parser")
    results = web.act("give me 10 real estate listings in the state of NY that have over 1,000,000 acres.")
    parsed = parse.act(results.final_output)
    df_parsed = pd.DataFrame(parsed)
    df_parsed.to_csv('company/project1/prometheusomniscient.github.io/output_data/real_estate1.csv')



