# coding: utf-8

"""
    API Endpoints

    Deliver monetary rewards and incentives to employees, customers, survey participants, and more through the Tremendous API. For organizational tasks, like managing your organization and its members within Tremendous, please see the Tremendous Organizational API.

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
from tremendous.models.allow_email import AllowEmail
from tremendous.models.allow_ip import AllowIp
from tremendous.models.review_country import ReviewCountry
from tremendous.models.review_email import ReviewEmail
from tremendous.models.review_ip import ReviewIp
from tremendous.models.review_redeemed_rewards_amount import ReviewRedeemedRewardsAmount
from tremendous.models.review_redeemed_rewards_count import ReviewRedeemedRewardsCount
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

FRAUDRULEREQUESTCONFIG_ANY_OF_SCHEMAS = ["AllowEmail", "AllowIp", "ReviewCountry", "ReviewEmail", "ReviewIp", "ReviewRedeemedRewardsAmount", "ReviewRedeemedRewardsCount"]

class FraudRuleRequestConfig(BaseModel):
    """
    The configuration associated with the rule. The properties allowed depend on the type of rule.
    """

    # data type: ReviewCountry
    anyof_schema_1_validator: Optional[ReviewCountry] = None
    # data type: ReviewIp
    anyof_schema_2_validator: Optional[ReviewIp] = None
    # data type: ReviewEmail
    anyof_schema_3_validator: Optional[ReviewEmail] = None
    # data type: ReviewRedeemedRewardsCount
    anyof_schema_4_validator: Optional[ReviewRedeemedRewardsCount] = None
    # data type: ReviewRedeemedRewardsAmount
    anyof_schema_5_validator: Optional[ReviewRedeemedRewardsAmount] = None
    # data type: AllowIp
    anyof_schema_6_validator: Optional[AllowIp] = None
    # data type: AllowEmail
    anyof_schema_7_validator: Optional[AllowEmail] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[AllowEmail, AllowIp, ReviewCountry, ReviewEmail, ReviewIp, ReviewRedeemedRewardsAmount, ReviewRedeemedRewardsCount]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "AllowEmail", "AllowIp", "ReviewCountry", "ReviewEmail", "ReviewIp", "ReviewRedeemedRewardsAmount", "ReviewRedeemedRewardsCount" }

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
        # validate data type: ReviewCountry
        if not isinstance(v, ReviewCountry):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReviewCountry`")
        else:
            return v

        # validate data type: ReviewIp
        if not isinstance(v, ReviewIp):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReviewIp`")
        else:
            return v

        # validate data type: ReviewEmail
        if not isinstance(v, ReviewEmail):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReviewEmail`")
        else:
            return v

        # validate data type: ReviewRedeemedRewardsCount
        if not isinstance(v, ReviewRedeemedRewardsCount):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReviewRedeemedRewardsCount`")
        else:
            return v

        # validate data type: ReviewRedeemedRewardsAmount
        if not isinstance(v, ReviewRedeemedRewardsAmount):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReviewRedeemedRewardsAmount`")
        else:
            return v

        # validate data type: AllowIp
        if not isinstance(v, AllowIp):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AllowIp`")
        else:
            return v

        # validate data type: AllowEmail
        if not isinstance(v, AllowEmail):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AllowEmail`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in FraudRuleRequestConfig with anyOf schemas: AllowEmail, AllowIp, ReviewCountry, ReviewEmail, ReviewIp, ReviewRedeemedRewardsAmount, ReviewRedeemedRewardsCount. Details: " + ", ".join(error_messages))
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
        # anyof_schema_1_validator: Optional[ReviewCountry] = None
        try:
            instance.actual_instance = ReviewCountry.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[ReviewIp] = None
        try:
            instance.actual_instance = ReviewIp.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[ReviewEmail] = None
        try:
            instance.actual_instance = ReviewEmail.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[ReviewRedeemedRewardsCount] = None
        try:
            instance.actual_instance = ReviewRedeemedRewardsCount.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[ReviewRedeemedRewardsAmount] = None
        try:
            instance.actual_instance = ReviewRedeemedRewardsAmount.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_6_validator: Optional[AllowIp] = None
        try:
            instance.actual_instance = AllowIp.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_7_validator: Optional[AllowEmail] = None
        try:
            instance.actual_instance = AllowEmail.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into FraudRuleRequestConfig with anyOf schemas: AllowEmail, AllowIp, ReviewCountry, ReviewEmail, ReviewIp, ReviewRedeemedRewardsAmount, ReviewRedeemedRewardsCount. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], AllowEmail, AllowIp, ReviewCountry, ReviewEmail, ReviewIp, ReviewRedeemedRewardsAmount, ReviewRedeemedRewardsCount]]:
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


