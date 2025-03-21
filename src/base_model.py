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







    