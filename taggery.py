#!/usr/bin/python

# This script creates new filenames for music files based on tag information.
# It currently does this by copying the original file with a new name. The
# ability to then delete the original file (simulating an overwrite) will be
# added at a later date.

# @title:		taggery
# @author:		MisterShake2099
# @location:	The location of a folder containing audio file(s) to be
#				processed by the script.

# @mode: (to be implemented later)
#				The mode in which the script should run. Default to "copy".
#				replace:	New files with updated filenames will be written
#							and the base file will be deleted.
#				copy:		New files with updated filenames will be created.
#							Base files will be preserved.

import sys
import shutil

import mutagen.FLAC
import mutagen.ID3v2
import mutagen.OGG
import mutagen.APEv2
import mutagen.MP4
import mutagen.ASF

# accept two args: first a directory, second a mode
args = os.system(sys.argv[1], sys.argv[2])

def taggery(dir):

	# Store all appropriate fields from each audio file in 'location'.
	# Metadata order: track number, title, length, (album artist/artist),
	# album, notes.
	# Album Artist will be used for file naming when available, otherwise
	# Artist will be used.

	fields = []

	i = 0;

	for file in dir:
        if file is FLAC:
        	audio = FLAC("example.flac")
        if file is MP3:
        	audio = MP3("example.mp3")
        if file is MP4:
        	audio = MP4("example.mp4")


	# create copy of each file and use stored fields to name file

	for each in fields

	copyfile(src, dst)