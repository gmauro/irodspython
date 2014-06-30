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

class testRodsFile(iRODSTestCase):

    def test_fileChmodInp_t(self):
        v1 = create_fileChmodInp_t()
        v2 = create_fileChmodInp_t()
        self.assertTrue(test_fileChmodInp_t(v1, v2))

    def test_fileChksumInp_t(self):
        v1 = create_fileChksumInp_t()
        v2 = create_fileChksumInp_t()
        self.assertTrue(test_fileChksumInp_t(v1, v2))

    def test_fileCloseInp_t(self):
        v1 = create_fileCloseInp_t()
        v2 = create_fileCloseInp_t()
        self.assertTrue(test_fileCloseInp_t(v1, v2))

    def test_fileClosedirInp_t(self):
        v1 = create_fileClosedirInp_t()
        v2 = create_fileClosedirInp_t()
        self.assertTrue(test_fileClosedirInp_t(v1, v2))

    def test_fileFstatInp_t(self):
        v1 = create_fileFstatInp_t()
        v2 = create_fileFstatInp_t()
        self.assertTrue(test_fileFstatInp_t(v1, v2))

    def test_fileFsyncInp_t(self):
        v1 = create_fileFsyncInp_t()
        v2 = create_fileFsyncInp_t()
        self.assertTrue(test_fileFsyncInp_t(v1, v2))

    def test_fileGetFsFreeSpaceInp_t(self):
        v1 = create_fileGetFsFreeSpaceInp_t()
        v2 = create_fileGetFsFreeSpaceInp_t()
        self.assertTrue(test_fileGetFsFreeSpaceInp_t(v1, v2))

    def test_fileGetFsFreeSpaceOut_t(self):
        v1 = create_fileGetFsFreeSpaceOut_t()
        v2 = create_fileGetFsFreeSpaceOut_t()
        self.assertTrue(test_fileGetFsFreeSpaceOut_t(v1, v2))

    def test_fileLseekInp_t(self):
        v1 = create_fileLseekInp_t()
        v2 = create_fileLseekInp_t()
        self.assertTrue(test_fileLseekInp_t(v1, v2))

    def test_fileLseekOut_t(self):
        v1 = create_fileLseekOut_t()
        v2 = create_fileLseekOut_t()
        self.assertTrue(test_fileLseekOut_t(v1, v2))

    def test_fileMkdirInp_t(self):
        v1 = create_fileMkdirInp_t()
        v2 = create_fileMkdirInp_t()
        self.assertTrue(test_fileMkdirInp_t(v1, v2))

    def test_fileOpenInp_t(self):
        v1 = create_fileOpenInp_t()
        v2 = create_fileOpenInp_t()
        self.assertTrue(test_fileOpenInp_t(v1, v2))

    def test_fileOpendirInp_t(self):
        v1 = create_fileOpendirInp_t()
        v2 = create_fileOpendirInp_t()
        self.assertTrue(test_fileOpendirInp_t(v1, v2))

    def test_fileReadInp_t(self):
        v1 = create_fileReadInp_t()
        v2 = create_fileReadInp_t()
        self.assertTrue(test_fileReadInp_t(v1, v2))

    def test_fileRenameInp_t(self):
        v1 = create_fileRenameInp_t()
        v2 = create_fileRenameInp_t()
        self.assertTrue(test_fileRenameInp_t(v1, v2))

    def test_fileRmdirInp_t(self):
        v1 = create_fileRmdirInp_t()
        v2 = create_fileRmdirInp_t()
        self.assertTrue(test_fileRmdirInp_t(v1, v2))

    def test_fileStageInp_t(self):
        v1 = create_fileStageInp_t()
        v2 = create_fileStageInp_t()
        self.assertTrue(test_fileStageInp_t(v1, v2))

    def test_fileStatInp_t(self):
        v1 = create_fileStatInp_t()
        v2 = create_fileStatInp_t()
        self.assertTrue(test_fileStatInp_t(v1, v2))

    def test_fileUnlinkInp_t(self):
        v1 = create_fileUnlinkInp_t()
        v2 = create_fileUnlinkInp_t()
        self.assertTrue(test_fileUnlinkInp_t(v1, v2))

    def test_fileWriteInp_t(self):
        v1 = create_fileWriteInp_t()
        v2 = create_fileWriteInp_t()
        self.assertTrue(test_fileWriteInp_t(v1, v2))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testRodsFile))
    
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())