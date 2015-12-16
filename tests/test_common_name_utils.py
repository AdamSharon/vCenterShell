﻿import unittest

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../vCenterShell/vCenterShell'))

from pycommon.common_name_utils import generate_unique_name

class test_common_name_utils(unittest.TestCase):
    
    def test_unique_name_generation(self):
        name_prefix = "some template name"
        unique1 = generate_unique_name(name_prefix)
        unique2 = generate_unique_name(name_prefix)
        self.assertNotEqual(unique1, unique2)

