from dataclasses import dataclass
from typing import List


@dataclass
class NPVector:
    """A Vector returned by the Neuronpedia API."""

    label: str
    model_id: str
    source: str
    index: str
    values: List[float]
    hook_name: str
    default_steer_strength: float | None
    url: str | None = None

    def __eq__(self, other: "NPVector") -> bool:
        return (
            self.model_id == other.model_id
            and self.source == other.source
            and self.index == other.index
            and self.label == other.label
            and self.hook_name == other.hook_name
            and self.values == other.values
            and self.default_steer_strength == other.default_steer_strength
        )

    def delete(self):
        # import here to avoid circular import
        from neuronpedia.requests.vector_request import VectorRequest

        return VectorRequest().delete(self)
