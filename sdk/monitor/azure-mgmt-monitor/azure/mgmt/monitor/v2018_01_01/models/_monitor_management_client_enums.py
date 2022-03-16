# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class AggregationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """the aggregation type of the metric.
    """

    NONE = "None"
    AVERAGE = "Average"
    COUNT = "Count"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    TOTAL = "Total"

class MetricClass(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The class of the metric.
    """

    AVAILABILITY = "Availability"
    TRANSACTIONS = "Transactions"
    ERRORS = "Errors"
    LATENCY = "Latency"
    SATURATION = "Saturation"

class MetricUnit(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The unit of the metric.
    """

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    COUNT_PER_SECOND = "CountPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"
    PERCENT = "Percent"
    MILLI_SECONDS = "MilliSeconds"
    BYTE_SECONDS = "ByteSeconds"
    UNSPECIFIED = "Unspecified"
    CORES = "Cores"
    MILLI_CORES = "MilliCores"
    NANO_CORES = "NanoCores"
    BITS_PER_SECOND = "BitsPerSecond"

class ResultType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    DATA = "Data"
    METADATA = "Metadata"
