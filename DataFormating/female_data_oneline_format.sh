#!/bin/bash

# this makes the text as 0 that is female
# run cat * > filename in the folder where the data is
# run the file
# when it is done run: sed -i 's/^[ \t]*//' filename from commandline

s/<Blog>//g
s/<\/Blog>//g
/<date>/d
s/<post>//g
s/<\/post>//g
s/\.\.\./\./g
s/\.\./\./g
s/\./\.\n/g
/^\s*$/d
s/\./\.,0/g

