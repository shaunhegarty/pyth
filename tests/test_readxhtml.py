
"""
Unit tests of the xhtml reader.
"""
from __future__ import absolute_import

import unittest

import pyth.document
from pyth.plugins.xhtml.reader import XHTMLReader


class TestReadXHTML(unittest.TestCase):

    def test_basic(self):
        """
        Try to read an empty xhtml document
        """
        xhtml = "<div></div>"
        doc = XHTMLReader.read(xhtml)
        self.assertTrue(isinstance(doc, pyth.document.Document))
        self.assertTrue(not doc.content)

    def test_paragraphs(self):
        """
        Try to read a simple xhtml document containing tree paragraphs
        """
        xhtml = "<div><p>p0</p><p>p1</p><p>p2</p></div>"
        doc = XHTMLReader.read(xhtml)
        self.assertTrue(len(doc.content) == 3)
        for i, p in enumerate(doc.content):
            self.assertTrue(isinstance(p, pyth.document.Paragraph))
            self.assertTrue(len(p.content) == 1)
            self.assertTrue(isinstance(p.content[0], pyth.document.Text))
            text = p.content[0]
            self.assertTrue(len(text.content) == 1)
            self.assertTrue(text.content[0] == 'p%d' % i)

    def test_bold(self):
        """
        Try to read a paragraph containing bold text
        """
        xhtml = "<div><p><b>bold</b></p></div>"
        doc = XHTMLReader.read(xhtml)
        text = doc.content[0].content[0]
        assert text['bold']

    def test_italic(self):
        """
        Try to read a paragraph containing italic text
        """
        xhtml = "<div><p><i>italic</i></p></div>"
        doc = XHTMLReader.read(xhtml)
        text = doc.content[0].content[0]
        assert text['italic']

    def test_sub(self):
        """
        Try to read a paragraph containing subscript
        """
        xhtml = "<div><p><sub>sub</sub></p></div>"
        doc = XHTMLReader.read(xhtml)
        text = doc.content[0].content[0]
        assert text['sub']

    def test_sup(self):
        """
        Try to read a paragraph containing supscript
        """
        xhtml = "<div><p><sup>super</sup></p></div>"
        doc = XHTMLReader.read(xhtml)
        text = doc.content[0].content[0]
        assert text['super']

    def test_url(self):
        """
        Try to read a paragraph containing an url
        """
        xhtml = '<div><p><a href="http://google.com">link</a></p></div>'
        doc = XHTMLReader.read(xhtml)
        text = doc.content[0].content[0]
        assert text['url'] == "http://google.com"


if __name__ == '__main__':
    unittest.main()
