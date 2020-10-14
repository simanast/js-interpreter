import unittest
from .test_utils import *


def runTest(path_to_folder: str):
    res = getTree(path_to_folder + '.js')
    exp = readTreeFromFile(path_to_folder + '.out')
    return exp, res


class MyTestCase(unittest.TestCase):

    def test_declarations_const(self):
        path = os.path.join(os.getcwd(), "test\\tests\\declarations\\const\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_declarations_let(self):
        path = os.path.join(os.getcwd(), "test\\tests\\declarations\\let\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_declarations_function(self):
        path = os.path.join(os.getcwd(), "test\\tests\\declarations\\let\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_expression_additive(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\additive\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_expression_assignment(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\assignment\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_expression_binary(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\binary\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_expression_binary_bitwise(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\binary-bitwise\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_expression_bitwise_shift(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\bitwise-shift\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_expression_binary_logical(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\binary-logical\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_expression_conditional(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\conditional\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_expression_equality(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\equality\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_expression_grouping(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\grouping\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_expression_multiplicative(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\multiplicative\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_expression_postfix(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\postfix\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_expression_primary_array(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\primary\\array\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)


    def test_expression_primary_literal(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\primary\\literal\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)


    def test_expression_primary_object(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\primary\\object\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)


    def test_expression_relational(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\relational\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_expression_unary(self):
        path = os.path.join(os.getcwd(), "test\\tests\\expression\\unary\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_statement_block(self):
        path = os.path.join(os.getcwd(), "test\\tests\\statement\\block\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_statement_break(self):
        path = os.path.join(os.getcwd(), "test\\tests\\statement\\break\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_statement_continue(self):
        path = os.path.join(os.getcwd(), "test\\tests\\statement\\continue\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_statement_empty(self):
        path = os.path.join(os.getcwd(), "test\\tests\\statement\\empty\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_statement_if(self):
        path = os.path.join(os.getcwd(), "test\\tests\\statement\\if\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_statement_iteration(self):
        path = os.path.join(os.getcwd(), "test\\tests\\statement\\iteration\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)

    def test_statement_return(self):
        path = os.path.join(os.getcwd(), "test\\tests\\statement\\return\\")
        filenames = getFilenames(path)
        for filename in filenames:
            exp, res = runTest(path + filename)
            self.assertEqual(exp, res)


if __name__ == '__main__':
    unittest.main()
