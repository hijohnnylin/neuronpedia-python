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

    @classmethod
    def new(
        cls,
        label: str,
        model_id: str,
        layer_num: int,
        hook_type: str,
        vector: list[float],
        default_steer_strength: float | None = 10,
    ) -> "NPVector":
        # import here to avoid circular import
        from neuronpedia.requests.vector_request import VectorRequest

        np_vector = VectorRequest().new(
            label=label,
            model_id=model_id,
            layer_num=layer_num,
            hook_type=hook_type,
            vector=vector,
            default_steer_strength=default_steer_strength,
        )

        return np_vector
