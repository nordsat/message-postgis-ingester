"""Message postgis ingester."""
import json
import os

import numpy as np
import pytest
import yaml
from posttroll.message import Message
from posttroll.testing import patched_subscriber_recv

from message_postgis_ingester import (
    main,
    read_config
)

test_message = ("""pytroll://image/seviri_hrit file mraspaud@0c8caa669351 2023-05-22T10:59:20.391466 v1.01 """
                """application/json {"orig_platform_name": "MSG3", "service": "___", "start_time":"""
                """ "2023-05-22T10:45:00", "compression": "_", "platform_name": "Meteosat-10", "sensor": ["seviri"],"""
                """ "uri": "/mnt/output/20230522_1045_Meteosat-10_euro4_overview.tif", "uid":"""
                """ "20230522_1045_Meteosat-10_euro4_overview.tif", "product": "overview", "area": "euro4","""
                """ "productname": "overview", "areaname": "euro4", "format": "tif"}""")
