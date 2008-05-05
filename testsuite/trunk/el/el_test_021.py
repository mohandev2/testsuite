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
    Jayashree Padmanabhan <jayshree@in.ibm.com>
"""

import unittest
from openhpi import *


class TestSequence(unittest.TestCase):
       
    """
    runTest : EL test
 *
 * This test verifies failure of oh_el_prepend when res != None
 *
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
        
        el = oh_el()
        retc = None
        event = SaHpiEventT()
        res1 = SaHpiRptEntryT()
        data = []
        data.append("Test data one")
        data.append("Test data two")
        data.append("Test data three")
        data.append("Test data four")
        data.append("Test data five")
        data.append("Test data six")
        data.append("Test data seven")
        data.append("Test data eight")
        data.append("Test data nine")	
        data.append("Test data ten")

        # test oh_el_prepend with res != None
        el = oh_el_create (30)
        event.Source = 1
        event.EventType = SAHPI_ET_USER
        event.Timestamp = SAHPI_TIME_UNSPECIFIED
        event.Severity = SAHPI_DEBUG
    
        res1.EntryId = 1
        res1.ResourceId = 1
        res1.ResourceSeverity = SAHPI_CRITICAL
        res1.ResourceCapabilities = 1

        for x in range (0,10):
            event.EventDataUnion.UserEvent.UserEventData.Data = data[x]		
            xretc = oh_el_prepend(el, event, None, res1)
            self.assertEqual (retc != SA_OK,True)
            
            x = x+1

        # close el 
        retc = oh_el_close(el)
        self.assertEqual (retc != SA_OK,False)
    
if __name__=='__main__':
        unittest.main()  
