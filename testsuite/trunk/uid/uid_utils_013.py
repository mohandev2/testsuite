#!/usr/bin/env python

from openhpi import *
import unittest

class TestSequence(unittest.TestCase):
    
    def runTest(self):
        ep = SaHpiEntityPathT()
               
        oh_init_ep(ep)
        
        self.assertEqual(oh_uid_initialize(),0)
        
        self.iid = oh_uid_from_entity_path(ep)
        
        self.assertEqual(not (self.iid), False)
         
        self.assertEqual(not (oh_entity_path_lookup(0, None)), False)
              
if __name__=='__main__':
    unittest.main()  
