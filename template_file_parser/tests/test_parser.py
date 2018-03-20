import os
from unittest import TestCase
from template_file_parser import parse_file


class TestParser(TestCase):
    def test_unsafe(self):
        variables = {'a': 'hello', 'b': 'world'}
        in_file = os.path.join(os.path.dirname(__file__), 'test_files/in.txt')
        out_file = os.path.join(
            os.path.dirname(__file__), 'test_files/unsafe-res.txt')
        expected_file = out_file = os.path.join(
            os.path.dirname(__file__), 'test_files/unsafe-expected.txt')
        parse_file(in_file, out_file, variables)
        self.compare_files(expected_file, out_file)

    def test_safe(self):
        variables = {'a': 'hello', 'b': 'world'}
        in_file = os.path.join(os.path.dirname(__file__), 'test_files/in.txt')
        out_file = os.path.join(
            os.path.dirname(__file__), 'test_files/safe-res.txt')
        expected_file = out_file = os.path.join(
            os.path.dirname(__file__), 'test_files/safe-expected.txt')
        parse_file(in_file, out_file, variables, True)
        self.compare_files(expected_file, out_file)

    def compare_files(self, expected_file, got_file):
        with open(expected_file) as expected_fh, open(got_file) as got_fh:
            self.assertEqual(expected_fh.read().strip(), got_fh.read().strip())
