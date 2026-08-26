from abc import ABC, abstractmethod


class EmbeddingModelInterface(ABC):

    @abstractmethod
    def embed(self, input_text: str):
        """Generate an embedding for the input text."""
        raise NotImplementedError