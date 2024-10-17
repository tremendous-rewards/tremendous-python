# coding: utf-8

"""
    API Endpoints

    Deliver monetary rewards and incentives to employees, customers, survey participants, and more through the Tremendous API. For organizational tasks, like managing your organization and it's members within Tremendous, please see the Tremendous Organizational API.

    The version of the OpenAPI document: 2
    Contact: developers@tremendous.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from tremendous.models.fraud_config_allow_email import FraudConfigAllowEmail
from tremendous.models.fraud_config_country import FraudConfigCountry
from tremendous.models.fraud_config_ip import FraudConfigIP
from tremendous.models.fraud_config_redeemed_rewards_amount import FraudConfigRedeemedRewardsAmount
from tremendous.models.fraud_config_redeemed_rewards_count import FraudConfigRedeemedRewardsCount
from tremendous.models.fraud_config_review_email import FraudConfigReviewEmail
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

FRAUDRULEREQUESTCONFIG_ANY_OF_SCHEMAS = ["FraudConfigAllowEmail", "FraudConfigCountry", "FraudConfigIP", "FraudConfigRedeemedRewardsAmount", "FraudConfigRedeemedRewardsCount", "FraudConfigReviewEmail"]

class FraudRuleRequestConfig(BaseModel):
    """
    The configuration associated with the rule. The properties allowed depend on the type of rule.
    """

    # data type: FraudConfigCountry
    anyof_schema_1_validator: Optional[FraudConfigCountry] = None
    # data type: FraudConfigIP
    anyof_schema_2_validator: Optional[FraudConfigIP] = None
    # data type: FraudConfigReviewEmail
    anyof_schema_3_validator: Optional[FraudConfigReviewEmail] = None
    # data type: FraudConfigRedeemedRewardsCount
    anyof_schema_4_validator: Optional[FraudConfigRedeemedRewardsCount] = None
    # data type: FraudConfigRedeemedRewardsAmount
    anyof_schema_5_validator: Optional[FraudConfigRedeemedRewardsAmount] = None
    # data type: FraudConfigIP
    anyof_schema_6_validator: Optional[FraudConfigIP] = None
    # data type: FraudConfigAllowEmail
    anyof_schema_7_validator: Optional[FraudConfigAllowEmail] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[FraudConfigAllowEmail, FraudConfigCountry, FraudConfigIP, FraudConfigRedeemedRewardsAmount, FraudConfigRedeemedRewardsCount, FraudConfigReviewEmail]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "FraudConfigAllowEmail", "FraudConfigCountry", "FraudConfigIP", "FraudConfigRedeemedRewardsAmount", "FraudConfigRedeemedRewardsCount", "FraudConfigReviewEmail" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = FraudRuleRequestConfig.model_construct()
        error_messages = []
        # validate data type: FraudConfigCountry
        if not isinstance(v, FraudConfigCountry):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FraudConfigCountry`")
        else:
            return v

        # validate data type: FraudConfigIP
        if not isinstance(v, FraudConfigIP):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FraudConfigIP`")
        else:
            return v

        # validate data type: FraudConfigReviewEmail
        if not isinstance(v, FraudConfigReviewEmail):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FraudConfigReviewEmail`")
        else:
            return v

        # validate data type: FraudConfigRedeemedRewardsCount
        if not isinstance(v, FraudConfigRedeemedRewardsCount):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FraudConfigRedeemedRewardsCount`")
        else:
            return v

        # validate data type: FraudConfigRedeemedRewardsAmount
        if not isinstance(v, FraudConfigRedeemedRewardsAmount):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FraudConfigRedeemedRewardsAmount`")
        else:
            return v

        # validate data type: FraudConfigIP
        if not isinstance(v, FraudConfigIP):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FraudConfigIP`")
        else:
            return v

        # validate data type: FraudConfigAllowEmail
        if not isinstance(v, FraudConfigAllowEmail):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FraudConfigAllowEmail`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in FraudRuleRequestConfig with anyOf schemas: FraudConfigAllowEmail, FraudConfigCountry, FraudConfigIP, FraudConfigRedeemedRewardsAmount, FraudConfigRedeemedRewardsCount, FraudConfigReviewEmail. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[FraudConfigCountry] = None
        try:
            instance.actual_instance = FraudConfigCountry.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[FraudConfigIP] = None
        try:
            instance.actual_instance = FraudConfigIP.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[FraudConfigReviewEmail] = None
        try:
            instance.actual_instance = FraudConfigReviewEmail.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[FraudConfigRedeemedRewardsCount] = None
        try:
            instance.actual_instance = FraudConfigRedeemedRewardsCount.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[FraudConfigRedeemedRewardsAmount] = None
        try:
            instance.actual_instance = FraudConfigRedeemedRewardsAmount.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_6_validator: Optional[FraudConfigIP] = None
        try:
            instance.actual_instance = FraudConfigIP.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_7_validator: Optional[FraudConfigAllowEmail] = None
        try:
            instance.actual_instance = FraudConfigAllowEmail.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into FraudRuleRequestConfig with anyOf schemas: FraudConfigAllowEmail, FraudConfigCountry, FraudConfigIP, FraudConfigRedeemedRewardsAmount, FraudConfigRedeemedRewardsCount, FraudConfigReviewEmail. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], FraudConfigAllowEmail, FraudConfigCountry, FraudConfigIP, FraudConfigRedeemedRewardsAmount, FraudConfigRedeemedRewardsCount, FraudConfigReviewEmail]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


