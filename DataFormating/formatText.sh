#!/bin/bash

# Create one file
#cat * > datafile.txt

# Delete date line
/<date>/d

# Change <post> to "
s/<post>/\"/g

# Change </post> to ",
s/<\/post>/\",/g

# Change <Blog> to [
s/<Blog>/[/g

# Change </Blog> to ]
s/<\/Blog>/]/g

# TODO: Fix this
# Remove empty lines
#:a;N;$!ba;s/\n/ /g

# Remove last ,
s/\",]/\"]/g
