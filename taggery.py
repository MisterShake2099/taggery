#!/usr/bin/python

# This script creates new filenames for music files based on tag information.
# It currently does this by copying the original file with a new name. The
# ability to then delete the original file (simulating an overwrite) will be
# added at a later date.

# @title: taggery
# @author: MisterShake2099

# Command line arguments:
# @src: a relative or absolute filepath containing source audio files.
# @dst: a relative or absolute filepath to put processed audio files.
# @mode: an optional argument specifying which mode to use.

import argparse

import mutagen.FLAC
import mutagen.ID3v2
import mutagen.OGG
import mutagen.APEv2
import mutagen.MP4
import mutagen.ASF

parser = argparse.ArgumentParser()
parser.add_argument("src", help="filepath to source directory")
parser.add_argument("dst", help="filepath to destination directory")
parser.add_argument("mode", help="list how to invoke mode options here")
args = parser.parse_args()

print(args.src)
print(args.dst)
print(args.mode)

fields = args.src

def taggery(dir):

    # Store all appropriate fields from each audio file in 'location'.
    # Metadata order: track number, title, length, (album artist/artist),
    # album, notes.
    # Album Artist will be used for file naming when available, otherwise
    # Artist will be used.

    for file in fields:
        if file is FLAC:
            audio = FLAC("example.flac")
        if file is MP3:
            audio = MP3("example.mp3")
        if file is MP4:
            audio = MP4("example.mp4")

    # create copy of each file and use stored fields to name file

    copyfile(args.src, args.dst)
