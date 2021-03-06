# encoding: utf-8
# Copyright (C) 2015 John Törnblom

from utils import RSLTestCase
from utils import evaluate


class TestParseKeywords(RSLTestCase):

    @evaluate
    def testSimpleKeyword(self, rc):
        '''
        .assign s = "TEST:Hello world!"
        .exit "${s:TEST}"
        '''
        self.assertEqual("Hello world!", rc)

    @evaluate
    def testKeywordAsVariable(self, rc):
        '''
        .assign kw = "KEYWORD"
        .assign s = "KEYWORD:Hello!"
        .exit "${s:${kw}}"
        '''
        self.assertEqual("Hello!", rc)

    @evaluate
    def testKeywordMissmatch(self, rc):
        '''
        .assign s = "TEST:Hello world!"
        .exit "${s:test}"
        '''
        self.assertEqual("", rc)
        
    @evaluate
    def testKeywordWithSpaces(self, rc):
        '''
        .assign kw = "KEYWORD"
        .assign s = "KEYWORD: Hello!   "
        .exit "${s:${kw}}"
        '''
        self.assertEqual("Hello!", rc)
        