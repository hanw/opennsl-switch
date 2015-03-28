# The MIT License (MIT)
#
# Copyright (c) 2015 Han Wang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

#!/usr/bin/python
import sys
import antlr4
import argparse
import string

def parse_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", dest="verbose",
                        help="Turn on verbose logging")
    parser.add_argument("-f", "--file", dest="file", type=str,
                        help="Tell compiler which input file to use")
    return parser.parse_args()

def read_source_file(input_file=None):
    from CLexer import CLexer
    from CParser import CParser

    assert input_file is not None
    try:
        char_stream = antlr4.FileStream(input_file)
        lexer = CLexer(char_stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = CParser(tokens)
        print parser
    except RuntimeError as e:
        print e

def main(args):
    args = parse_options()
    source_file = args.file
    print source_file
    read_source_file(input_file=source_file)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
