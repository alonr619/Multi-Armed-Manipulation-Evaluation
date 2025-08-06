from typing import Dict, List

class BaseLLM:
    model_dict = {}
    client = None

    def __init__():
        pass

    @classmethod
    def get_model_dict(cls):
        return cls.model_dict
    
    @classmethod
    def get_client(cls):
        return cls.client

    @classmethod
    def get_model_id(cls, model: str):
        return cls.model_dict[model]
    
    @classmethod
    def contains_model(cls, model: str):
        return model in cls.model_dict
    
    @classmethod
    def query(cls, conversation: List[Dict[str, str]], model: str):
        pass