# Copyright (c) 2013, University of Liverpool
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
# Author       : Jerome Fuselier
#

import unittest
from common import *
from irods import *

class testRodsQuery(iRODSTestCase):

    def test_generalUpdateInp_t(self):
        v1 = create_generalUpdateInp_t()
        v2 = create_generalUpdateInp_t()
        self.assertTrue(test_generalUpdateInp_t(v1, v2))

    def test_genQueryInp_t(self):
        v1 = create_genQueryInp_t()
        v2 = create_genQueryInp_t()
        self.assertTrue(test_genQueryInp_t(v1, v2))
         
    def test_genQueryOut_t(self):
        v1 = create_genQueryOut_t()
        v2 = create_genQueryOut_t()
        self.assertTrue(test_genQueryOut_t(v1, v2))
   
    def test_simpleQueryInp_t(self):
        v1 = create_simpleQueryInp_t()
        v2 = create_simpleQueryInp_t()
        self.assertTrue(test_simpleQueryInp_t(v1, v2))
   
    def test_simpleQueryOut_t(self):
        v1 = create_simpleQueryOut_t()
        v2 = create_simpleQueryOut_t()
        self.assertTrue(test_simpleQueryOut_t(v1, v2))
   
    def test_sqlResult_t(self):
        v1 = create_sqlResult_t()
        v2 = create_sqlResult_t()
        self.assertTrue(test_sqlResult_t(v1, v2))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testRodsQuery))
    
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
