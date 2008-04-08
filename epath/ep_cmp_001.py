#!/usr/bin/env python

"""
 (C) Copyright IBM Corp. 2008
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 file and program are licensed under a BSD style license.  See
 the Copying file included with the OpenHPI distribution for
 full licensing terms.
 
 Authors:
    Suntrupth S Yadav <suntrupth@in.ibm.com>
"""
# oh_cmp_ep: zero element entity path testcase.
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        ep1 = SaHpiEntityPathT()
        ep1.Entry[0].EntityType = SAHPI_ENT_ROOT
        ep1.Entry[0].EntityLocation = 0

        ep2 = SaHpiEntityPathT()
        ep2.Entry[0].EntityType = SAHPI_ENT_ROOT
        ep2.Entry[0].EntityLocation = 0

        self.assertEqual (not oh_cmp_ep(ep1, ep2),False)
    
if __name__=='__main__':
    unittest.main()
