import os
import unittest
from pyth.plugins.xhtml.reader import XHTMLReader
from pyth.plugins.rtf15.writer import Rtf15Writer

class TestRtfWithImage(unittest.TestCase):

    def test_inline_png(self):
        sample_with_image = os.path.join(os.path.abspath(os.path.dirname(__file__)), "html", "sample-with-image.html")
        with open(sample_with_image, 'rb') as rtf:
            source = XHTMLReader.read(rtf)
            doc = Rtf15Writer.write(source).getvalue()
            self.assertIn('pngblip', doc)
            self.assertIn('picwgoal750\\', doc)
            self.assertIn('pichgoal750\\', doc)


if __name__ == '__main__':
    unittest.main()
