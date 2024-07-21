import unittest
from ccwc import ccwc
from io import StringIO
import sys

class TestCCWC(unittest.TestCase):
    def test_count_bytes(self):
        self.assertEqual(ccwc.count_bytes('ccwc/test.txt'), 342190)

    def test_count_lines(self):
        self.assertEqual(ccwc.count_lines('ccwc/test.txt'), 7145)

    def test_count_words(self): 
        self.assertEqual(ccwc.count_words('ccwc/test.txt'), 58164)

    def test_count_chars(self):
        self.assertEqual(ccwc.count_chars('ccwc/test.txt'), 339292)

    def test_main_output_bytes(self):
        saved_stdout = sys.stdout

        try:
            out = StringIO()
            sys.stdout = out
            ccwc.main(['ccwc.py', '-c', 'ccwc/test.txt'])
            output = out.getvalue().strip()
            self.assertEqual(output, '342190 ccwc/test.txt')
        finally:
            sys.stdout = saved_stdout

    def test_main_output_lines(self):
        saved_stdout = sys.stdout

        try:
            out = StringIO()
            sys.stdout = out
            ccwc.main(['ccwc.py', '-l', 'ccwc/test.txt'])
            output = out.getvalue().strip()
            self.assertEqual(output, '7145 ccwc/test.txt')
        finally:
            sys.stdout = saved_stdout

    def test_main_output_words(self):
        saved_stdout = sys.stdout

        try: 
            out = StringIO()
            sys.stdout = out
            ccwc.main(['ccwc.py', '-w', 'ccwc/test.txt'])
            output = out.getvalue().strip()
            self.assertEqual(output, '58164 ccwc/test.txt')
        finally:
            sys.stdout = saved_stdout

    def test_main_output_chars(self):
        saved_stdout = sys.stdout

        try:
            out = StringIO()
            sys.stdout = out
            ccwc.main(['ccwc.py', '-m', 'ccwc/test.txt'])
            output = out.getvalue().strip()
            self.assertEqual(output, '339292 ccwc/test.txt')
        finally:
            sys.stdout = saved_stdout

    def test_main_output_all(self): 
        saved_stdout = sys.stdout

        try: 
            out = StringIO()
            sys.stdout = out
            ccwc.main(['ccwc.py', 'ccwc/test.txt'])
            output = out.getvalue().strip()
            self.assertEqual(output, '7145 58164 342190 ccwc/test.txt')
        finally:
            sys.stdout = saved_stdout

if __name__ == '__main__':
    unittest.main()
