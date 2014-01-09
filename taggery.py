#!/usr/bin/python
#
# This script creates new filenames for music files based on tag information.
# It currently does this by copying the original file with a new name.
# The ability to then delete the original file (simulating an overwrite)
# will be added at a later date.
# The purpose of this renaming is to reduce filepath length for music files
# by naming them in a way that is organized as if folder trees were used AND
# to avoid a situation in which tags cannot be read thus rendering much of
# the metadata for a particular music file unusable.
#
# @title: taggery
# @author: MisterShake2099
# @param location:
#		The location of a folder containing audio files to be processed by the script
# @param mode: (to be implemented later)
#		The mode in which the script should run. Will default to "copy".
#			replace: new files with updated filenames will be written and the base file will be deleted
#			copy: new files with updated filenames will be created. Base files will be preserved.

def taggery(location):

	