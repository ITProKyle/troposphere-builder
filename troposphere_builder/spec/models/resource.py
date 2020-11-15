"""Data model for CloudFormation resource types.

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification-format.html#cfn-resource-specification-format-resourcetype

"""
# pylint: disable=no-self-argument,no-self-use
from copy import deepcopy
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, validator
from pydantic.fields import ModelField

from .enums import SpecPrimitiveItemType, SpecPrimitiveType
from .property import PropertySpec


class ResourceAttributeSpec(BaseModel):
    """Data model for resource.Attributes specification.

    Attributes:
        Name: Name of the attribute.
        ItemType: If the value of the Type field is List, indicates the type of
            list that the *Fn::GetAtt* function returns for the attribute if
            the list contains non-primitive types. The valid type is a name of
            a property.
        PrimitiveItemType: If the value of the Type field is List, indicates the
            type of list that the Fn::GetAtt function returns for the attribute
            if the list contains primitive types. For lists that contain
            non-primitive types, the ItemType property indicates the valid value
            type. The valid primitive types for lists are String, Long, Integer,
            Double, Boolean, or Timestamp.

            For example, if the type value is List and the primitive item type
            value is String, the Fn::GetAtt function returns a list of strings.
        PrimitiveType: For primitive return values, the type of primitive value
            that the *Fn::GetAtt* function returns for the attribute. A primitive
            type is a basic data type for resource property values. The valid
            primitive types are String, Long, Integer, Double, Boolean, Timestamp
            or Json.
        Type: For non-primitive return values, the type of value that the
            *Fn::GetAtt* function returns for the attribute. The valid types are
            a property name or List.

            A list is a comma-separated list of values. The value type for lists
            are indicated by the ItemType or PrimitiveItemType field.

    """

    Name: str
    PrimitiveItemType: Optional[SpecPrimitiveItemType] = None
    PrimitiveType: Optional[SpecPrimitiveType] = None
    Type: Optional[str] = None  # TODO create enum


class ResourceSpec(BaseModel):
    """Data model for resource specification.

    Attributes:
        Attributes: Resource attributes that you can use in an *Fn::GetAtt* function.
            For each attribute, this section provides the attribute name and the type
            of value that AWS CloudFormation returns.
        Documentation: A link to the AWS CloudFormation User Guide for
            information about the resource.
        Properties: Property specifications for the resource.
        TypeName: Resource type name.

    """

    Attributes: List[ResourceAttributeSpec]
    Documentation: str
    Properties: List[PropertySpec]
    TypeName: str

    @validator("Attributes", "Properties", pre=True)
    def _convert_dict_to_list(
        cls,  # noqa: N805
        v: Union[Dict[str, Any], List[Dict[str, Any]]],
        field: ModelField,
    ) -> List[Dict[str, Any]]:
        """Convert spec dict to list."""
        if isinstance(v, list):
            return v
        result = []
        for name, obj in deepcopy(v).items():
            if field.name == "Attributes":
                obj["Name"] = name
            else:
                obj["TypeName"] = name
            result.append(obj)
        return result
