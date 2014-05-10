buka2jpg
========
This project aims to extract jpg from the downloaded buka file and view them on PC. buka2jpg is beta software and may change as buka format changed.

## System Requirements
Currently, this is a command-line program. You could use this on systems with python 2.x.

Linux
Mac OS X

##Current Status
Extract all files and create the corresponding folders based on chaporder.dat. If chaporder.dat does not exist, will extract all the .buka under the same directory. 

##SYNOPSIS
buka2jpg [OPTIONS]

##OPTIONS
    -f, --file
        Extract jpg from the specific file
    -h
        Print a usage message briefly summarizing these command-line options and the bug-reporting address, then exit.
    -v, --version
		Print the version number of buka2jpg to the standard output.

##Author
Written by Daniel Tai

##LICENSE
The MIT License (MIT)

Copyright (c) 2014 danielk1031

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

