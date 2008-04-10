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

""" oh_set_ep_location: Entity path has 4 elements, victim element 
   in the middle. Only victim element's instance number changed """
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        
        ep = SaHpiEntityPathT()
        ep.Entry[0].EntityType = SAHPI_ENT_FAN
        ep.Entry[0].EntityLocation = 11099
        ep.Entry[0].EntityType = SAHPI_ENT_BATTERY
        ep.Entry[0].EntityLocation = 2002
        ep.Entry[0].EntityType = SAHPI_ENT_RACK
        ep.Entry[0].EntityLocation = 37373
        ep.Entry[0].EntityType = SAHPI_ENT_DISK_BAY
        ep.Entry[0].EntityLocation = 440044
        ep.Entry[0].EntityType = 0
        
        #SaHpiEntityLocationT 
        x = 123456

        err = oh_set_ep_location( ep, SAHPI_ENT_RACK, x)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual (ep.Entry[2].EntityLocation != x,True)
        
        self.assertEqual (ep.Entry[2].EntityType != SAHPI_ENT_RACK,True)
        
        self.assertEqual (ep.Entry[0].EntityLocation != 11099,True)
        
        self.assertEqual (ep.Entry[0].EntityType != SAHPI_ENT_FAN,True)
        
        self.assertEqual (ep.Entry[1].EntityLocation != 2002,True)
        
        self.assertEqual (ep.Entry[1].EntityType != SAHPI_ENT_BATTERY,True)
        
        self.assertEqual (ep.Entry[3].EntityLocation != 440044,True)
        
        self.assertEqual (ep.Entry[3].EntityType != SAHPI_ENT_DISK_BAY,True)
        
if __name__=='__main__':
    unittest.main()