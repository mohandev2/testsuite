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
 * This test verifies failure of oh_el_prepend with log info.OverflowFlag
 *
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
        
        el = oh_el()
        retc = None
        event = SaHpiEventT()
        data = []
        data.append("Test data one")
        data.append("Test data two")

        # test oh_el_prepend with event log info.OverflowFlag 
        el = oh_el_create(1)
        event.Source = 1
        event.EventType = SAHPI_ET_USER
        event.Timestamp = SAHPI_TIME_UNSPECIFIED
        event.Severity = SAHPI_DEBUG

        event.EventDataUnion.UserEvent.UserEventData.Data = data[0]
        retc = oh_el_prepend(el, event, None, None)
        if (retc != SA_OK):
            print "ERROR: oh_el_prepend failed."
            return 1
        
        event.EventDataUnion.UserEvent.UserEventData.Data = data[1]

        retc = oh_el_prepend(el, event, None, None)
        if (retc == SA_OK):
            print "ERROR: oh_el_prepend failed."
            return 1

        # close el 
        retc = oh_el_close(el)
        if (retc != SA_OK):
            print "ERROR: oh_el_close on el failed."
            return 1
        
        return 0

if __name__=='__main__':
        unittest.main()  
