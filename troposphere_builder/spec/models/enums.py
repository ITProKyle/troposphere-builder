"""Data model enums."""
from enum import Enum


class SpecPrimitiveItemType(str, Enum):
    """Primitive item types used in the CloudFormation spec."""

    BOOLEAN = "Boolean"
    DOUBLE = "Double"
    INTIGER = "Integer"
    LONG = "Long"
    STRING = "String"
    TIMESTAMP = "Timestamp"


class SpecPrimitiveType(str, Enum):
    """Primitive types used in the CloudFormation spec."""

    BOOLEAN = "Boolean"
    DOUBLE = "Double"
    INTIGER = "Integer"
    JSON = "Json"
    LONG = "Long"
    STRING = "String"
    TIMESTAMP = "Timestamp"


class SpecUpdateType(str, Enum):
    """Update types used in the CloudFormation spec."""

    CONDITIONAL = "Conditional"
    IMMUTABLE = "Immutable"
    MUTABLE = "Mutable"
