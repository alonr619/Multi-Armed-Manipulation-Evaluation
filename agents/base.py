from typing import Any

class BaseLLM:
    model_dict: dict[str, str] = {}
    client: Any = None

    @classmethod
    def get_model_dict(cls) -> dict[str, str]:
        return cls.model_dict
    
    @classmethod
    def get_client(cls) -> Any:
        return cls.client

    @classmethod
    def get_model_id(cls, model: str) -> str:
        return cls.model_dict[model]
    
    @classmethod
    def contains_model(cls, model: str) -> bool:
        return model in cls.model_dict
    
    @classmethod
    def query(cls, conversation: list[dict[str, str]], model: str) -> str:
        pass