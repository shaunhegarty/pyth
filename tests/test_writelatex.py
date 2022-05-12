"""
unit tests of the latex writer
"""
from __future__ import absolute_import, unicode_literals

import unittest
import six

from pyth.plugins.latex.writer import LatexWriter
from pyth.plugins.python.reader import PythonReader, P, T, BOLD, ITALIC


class TestWriteLatex(unittest.TestCase):

    def test_basic(self):
        """
        Try to create an empty latex document
        """
        doc = PythonReader.read([])
        latex = LatexWriter.write(doc).getvalue()

    def test_paragraph(self):
        """
        Try a single paragraph document
        """
        doc = PythonReader.read(P["the text"])
        latex = LatexWriter.write(doc).getvalue()
        assert six.ensure_binary("the text") in latex

    def test_bold(self):
        doc = PythonReader.read([P[T(BOLD)["bold text"]]])
        latex = LatexWriter.write(doc).getvalue()
        assert six.ensure_binary(r"\textbf{bold text}") in latex, latex

    def test_italic(self):
        doc = PythonReader.read([P[T(ITALIC)["italic text"]]])
        latex = LatexWriter.write(doc).getvalue()
        assert six.ensure_binary(r"\emph{italic text}") in latex, latex

    def test_metadata(self):
        """
        assert that the document metadata are added into the latex file
        """
        doc = PythonReader.read([])
        doc["author"] = "The Author"
        doc["subject"] = "The Subject"
        doc["title"] = "The Title"

        latex = LatexWriter.write(doc).getvalue()
        assert six.ensure_binary("pdfauthor={The Author}") in latex, latex
        assert six.ensure_binary("pdfsubject={The Subject}") in latex, latex
        assert six.ensure_binary("pdftitle={The Title}") in latex, latex
