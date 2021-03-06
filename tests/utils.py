# encoding: utf-8
# Copyright (C) 2015 John Törnblom

import unittest
import xtuml.model
import rsl


class RSLTestCase(unittest.TestCase):

    def setUp(self):
        id_generator = xtuml.model.IntegerGenerator()
        self.metamodel = xtuml.model.MetaModel(id_generator)
        self.runtime = rsl.runtime.Runtime(self.metamodel)
        self.includes = ['./']
        
    def tearDown(self):
        del self.metamodel

    def eval_text(self, text, filename=''):
        ast = rsl.parse_text(text + '\n', filename)
        try:
            rsl.evaluate(self.runtime, ast, self.includes)
        except SystemExit as e:
            return e.code

def expect_exception(exception):
    def test_decorator(fn):
        def test_decorated(self, *args, **kwargs):
            self.assertRaises(exception, fn, self, *args, **kwargs)
        return test_decorated
    return test_decorator

def evaluate(f):
    return lambda self: f(self, self.eval_text(f.__doc__, f.__module__ + '.' + f.__name__))

