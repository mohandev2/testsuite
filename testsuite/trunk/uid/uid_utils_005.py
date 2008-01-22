#!/usr/bin/env python

from openhpi import *
import unittest

class TestSequence(unittest.TestCase):
    iid = [0,1,2,3,4,5,6,7,8,9,10]
    
    def test(self):
        
        ep = SaHpiEntityPathT()
        rep = SaHpiEntityPathT()
        self.assertEqual(oh_uid_initialize(),0)
        
        oh_init_ep(ep)
        
        for i in range (0, 10):
            ep.Entry[0].EntityLocation = i
            self.iid[i] = oh_uid_from_entity_path(ep)
                   
        self.assertEqual(oh_uid_remove(self.iid[8]), 0)
        self.assertEqual(oh_uid_remove(self.iid[3]), 0)
        
        self.assertEqual(not (oh_entity_path_lookup(self.iid[8], rep)), False)
        
        self.assertEqual(not (oh_entity_path_lookup(self.iid[3], rep)), False)
        
if __name__=='__main__':
    unittest.main()      
