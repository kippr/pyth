import unittest
import os.path
import glob

import pyth.document
from pyth.plugins.rtf15.reader import Rtf15Reader

class TestRtfMeta(type):
    def __new__(meta, name, bases, dict):
        fileDir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "rtfs")
        files = glob.glob(os.path.join(fileDir, "*.rtf"))

        def gen_file_test(path, name):
            def test(self):
                # Just make sure they don't crash, for now
                Rtf15Reader.read(open(path, "rb"))
            test.__name__ = "test_%s" % name
            return test

        for path in files:
            name = os.path.splitext(os.path.basename(path))[0]
            dict["test_%s" % name] = gen_file_test(path, name)
            print path, name

        return type.__new__(meta, name, bases, dict)


class TestRtfFile(unittest.TestCase):
    __metaclass__ = TestRtfMeta
    pass


class TestRtfWithImage(unittest.TestCase):

    def test_inline_png(self):
        sample_with_image = os.path.join(os.path.abspath(os.path.dirname(__file__)), "rtfs", "sample-with-image.rtf")
        with open(sample_with_image, 'rb') as rtf:
                doc = Rtf15Reader.read(rtf)
                image = next(node.content[0] for node in doc.content if isinstance(node.content[0], pyth.document.Image))
                expected = {'pngblip': True, 'picw': '20714', 'picwgoal': '750', 'pich': '12143',
                            'pichgoal': '750', 'picscaley': '100', 'picscalex': '100'}
                self.assertEquals(expected, image.properties)


if __name__ == '__main__':
    unittest.main()
