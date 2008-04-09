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

# oh_set_ep_location: Entity path that has 4 elements testcase. 
import unittest
from openhpi import *

class TestSequence(unittest.TestCase):

    def runTest(self):
        
        ep = SaHpiEntityPathT()
        ep.Entry[0].EntityType = SAHPI_ENT_PROCESSOR
        ep.Entry[0].EntityLocation = 111
        ep.Entry[0].EntityType = SAHPI_ENT_DISK_BAY
        ep.Entry[0].EntityLocation = 2222
        ep.Entry[0].EntityType = SAHPI_ENT_BATTERY
        ep.Entry[0].EntityLocation = 33333
        ep.Entry[0].EntityType = SAHPI_ENT_IO_SUBBOARD
        ep.Entry[0].EntityLocation = 444444
        ep.Entry[0].EntityType = 0
       
        #SaHpiEntityLocationT
        x = 10101010

        err = oh_set_ep_location(ep, SAHPI_ENT_IO_SUBBOARD, x)
        self.assertEqual  (err!=None,True)
        
        self.assertEqual  (ep.Entry[3].EntityLocation != x,True) 
        
        self.assertEqual (ep.Entry[3].EntityType != SAHPI_ENT_IO_SUBBOARD,True) 
    
        self.assertEqual (ep.Entry[0].EntityLocation != 111,True)
    
        self.assertEqual (ep.Entry[0].EntityType != SAHPI_ENT_PROCESSOR,True)
    
        self.assertEqual (ep.Entry[1].EntityLocation != 2222,True)
    
        self.assertEqual (ep.Entry[1].EntityType != SAHPI_ENT_DISK_BAY,True)
    
        self.assertEqual (ep.Entry[2].EntityLocation != 33333,True)
    
        self.assertEqual (ep.Entry[2].EntityType != SAHPI_ENT_BATTERY,True)
    
if __name__=='__main__':
    unittest.main()
