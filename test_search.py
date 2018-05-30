import os
import unittest
import search

# concerns: 
#  + danger: link to an ancestor file could cause infinite recursion

class TestSearch(unittest.TestCase):

    def test_FunctionReturnsData(self):
        currentDir = os.getcwd()
        keyword = ''
        self.assertIsNotNone(search.getCurrentPathList(currentDir, keyword))

    def test_FunctionReturnsADictionary(self):
        currentDir = os.getcwd()
        keyword = ''
        self.assertEqual(type(search.getCurrentPathList(currentDir, keyword, {})), dict)

    def test_ReturnsSingleEntryDictionaryIfFilePathIsSent(self):
        currentDir = os.getcwd() + '/search.py'
        keyword = ''
        self.assertEqual(search.getCurrentPathList(currentDir, keyword, {}), { currentDir: 0 })

    def test_RecursesThroughSubFoldersAndAddsToDictionary(self):
        currentDir = os.getcwd() +'/testDir'
        keyword = ''
        self.assertEqual(search.getCurrentPathList(currentDir, keyword, {}), { currentDir: 1, currentDir+'/testSubDir': 2 })


    