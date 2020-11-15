"""Data models associated with the CloudFormation spec."""
# pylint: disable=no-self-argument,no-self-use
from copy import deepcopy
from typing import Any, Dict, List, Union

from pydantic import BaseModel, validator

from .property import PropertySpec
from .resource import ResourceSpec


class Spec(BaseModel):
    """Data model for CloudFormation spec."""

    PropertyTypes: List[PropertySpec]
    ResourceSpecificationVersion: str
    ResourceTypes: List[ResourceSpec]

    @validator("PropertyTypes", "ResourceTypes", pre=True)
    def _convert_dict_to_list(
        cls, v: Union[Dict[str, Any], List[Dict[str, Any]]]  # noqa: N805
    ) -> List[Dict[str, Any]]:
        """Convert spec dict to list."""
        if isinstance(v, list):
            return v
        result = []
        for name, obj in deepcopy(v).items():
            obj["TypeName"] = name
            result.append(obj)
        return result
